#!/usr/bin/env python3
"""Static portability and consistency checks for the submission source."""

from __future__ import annotations

import csv
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEX_FILES = [
    ROOT / "main.tex",
    ROOT / "body.tex",
    ROOT / "supplement.tex",
]
BIB_FILE = ROOT / "references.bib"


def strip_comments(text: str) -> str:
    return "\n".join(re.sub(r"(?<!\\)%.*$", "", line) for line in text.splitlines())


def balanced_braces(path: Path, text: str) -> list[str]:
    errors: list[str] = []
    depth = 0
    for line_no, line in enumerate(text.splitlines(), 1):
        for char in line:
            if char == "{":
                depth += 1
            elif char == "}":
                depth -= 1
                if depth < 0:
                    errors.append(f"{path.name}:{line_no}: closing brace without opener")
                    depth = 0
    if depth:
        errors.append(f"{path.name}: {depth} unmatched opening brace(s)")
    return errors


def environment_stack(path: Path, text: str) -> list[str]:
    errors: list[str] = []
    stack: list[tuple[str, int]] = []
    pattern = re.compile(r"\\(begin|end)\{([^}]+)\}")
    for line_no, line in enumerate(text.splitlines(), 1):
        for kind, env in pattern.findall(line):
            if kind == "begin":
                stack.append((env, line_no))
            elif not stack:
                errors.append(f"{path.name}:{line_no}: end{{{env}}} without begin")
            else:
                opened, opened_line = stack.pop()
                if opened != env:
                    errors.append(
                        f"{path.name}:{line_no}: end{{{env}}} closes begin{{{opened}}} from line {opened_line}"
                    )
    errors.extend(f"{path.name}:{line_no}: unclosed begin{{{env}}}" for env, line_no in stack)
    return errors


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    tex = ""
    for path in TEX_FILES:
        if not path.exists():
            errors.append(f"Missing TeX input: {path.relative_to(ROOT)}")
            continue
        cleaned = strip_comments(path.read_text(encoding="utf-8"))
        tex += "\n" + cleaned
        errors.extend(balanced_braces(path, cleaned))
        errors.extend(environment_stack(path, cleaned))

    bib = BIB_FILE.read_text(encoding="utf-8")
    errors.extend(balanced_braces(BIB_FILE, strip_comments(bib)))
    bib_keys = re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,", bib)
    cited_keys: list[str] = []
    cite_pattern = re.compile(r"\\cite\w*(?:\s*\[[^]]*\]){0,2}\s*\{([^}]+)\}")
    for match in cite_pattern.finditer(tex):
        cited_keys.extend(key.strip() for key in match.group(1).split(","))

    duplicate_keys = sorted(key for key, count in Counter(bib_keys).items() if count > 1)
    missing_keys = sorted(set(cited_keys) - set(bib_keys))
    unused_keys = sorted(set(bib_keys) - set(cited_keys))
    if duplicate_keys:
        errors.append(f"Duplicate BibTeX keys: {', '.join(duplicate_keys)}")
    if missing_keys:
        errors.append(f"Undefined citation keys: {', '.join(missing_keys)}")
    if unused_keys:
        warnings.append(
            f"Unused bibliography entries retained from the auditable source library: {len(unused_keys)}"
        )

    labels = re.findall(r"\\label\{([^}]+)\}", tex)
    references = re.findall(r"\\(?:eqref|ref|cref|Cref|autoref)\{([^}]+)\}", tex)
    duplicate_labels = sorted(key for key, count in Counter(labels).items() if count > 1)
    dangling_references = sorted(set(references) - set(labels))
    unreferenced_objects = sorted(
        key for key in set(labels) - set(references) if key.startswith(("fig:", "tab:"))
    )
    if duplicate_labels:
        errors.append(f"Duplicate LaTeX labels: {', '.join(duplicate_labels)}")
    if dangling_references:
        errors.append(f"Undefined LaTeX references: {', '.join(dangling_references)}")
    if unreferenced_objects:
        errors.append(f"Unreferenced figure/table labels: {', '.join(unreferenced_objects)}")

    dois = [doi.lower().strip() for doi in re.findall(r"\bdoi\s*=\s*\{([^}]+)\}", bib, re.I)]
    duplicate_dois = sorted(doi for doi, count in Counter(dois).items() if count > 1)
    if duplicate_dois:
        errors.append(f"Duplicate DOI values: {', '.join(duplicate_dois)}")

    for graphic in re.findall(r"\\includegraphics(?:\[[^]]*\])?\{([^}]+)\}", tex):
        candidates = [ROOT / graphic, ROOT / "figures" / graphic]
        if not any(path.exists() for path in candidates):
            errors.append(f"Missing graphic: {graphic}")
    for input_name in re.findall(r"\\input\{([^}]+)\}", tex):
        path = ROOT / input_name
        if path.suffix == "":
            path = path.with_suffix(".tex")
        if not path.exists():
            errors.append(f"Missing input: {input_name}")

    csv_roots = ["research", "audit", "search", "supplementary", "independent-review", "figures/source_data"]
    csv_paths = sorted({path for name in csv_roots for path in (ROOT / name).rglob("*.csv")})
    for path in csv_paths:
        with path.open(newline="", encoding="utf-8") as handle:
            rows = list(csv.reader(handle))
        if not rows:
            errors.append(f"Empty CSV: {path.relative_to(ROOT)}")
            continue
        width = len(rows[0])
        bad = [index for index, row in enumerate(rows[1:], 2) if len(row) != width]
        if bad:
            errors.append(f"Malformed CSV rows in {path.relative_to(ROOT)}: {bad[:10]}")

    if "\\begin{landscape}" in tex and "\\usepackage{pdflscape}" not in tex:
        errors.append("landscape environment used without pdflscape")
    if "\\bibliography{references}" not in tex:
        errors.append("main bibliography declaration not found")

    if re.search(r"\band others\b", bib, re.I):
        errors.append("Bibliography contains prohibited 'and others' author placeholders")

    portable_violations: list[str] = []
    for path in (ROOT / "scripts").glob("*.py"):
        if path.resolve() == Path(__file__).resolve():
            continue
        source = path.read_text(encoding="utf-8")
        if ".agents/skills" in source or str(ROOT) in source:
            portable_violations.append(str(path.relative_to(ROOT)))
    if portable_violations:
        errors.append(f"Nonportable local-skill/project imports: {', '.join(portable_violations)}")

    if re.search(r"\b(systematic review|systematic literature review)\b", tex, re.I) and "not a systematic review" not in tex:
        warnings.append("Check that the review is not inadvertently labelled systematic")

    print(f"TeX files checked: {len(TEX_FILES)}; CSV files checked: {len(csv_paths)}")
    print(
        f"Citation keys: {len(set(cited_keys))}; BibTeX entries: {len(bib_keys)}; "
        f"DOI entries: {len(dois)}; labels/references: {len(labels)}/{len(references)}"
    )
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        return 1
    print(
        "PASS: braces, environments, labels, citations, bibliography uniqueness, "
        "file references, CSV shape and portability"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
