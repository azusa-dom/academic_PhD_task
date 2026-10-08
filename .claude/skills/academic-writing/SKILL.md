---
name: academic-writing
description: Draft structured academic manuscripts from research inputs (notes, results, references, outlines) and produce publication-ready first drafts. Use when the user asks to write or expand abstracts, introductions, methods, results, discussions, full papers, theses, or grant-style academic prose.
---

# Academic Writing

## Workflow
1. Collect core inputs before drafting:
- research question and contribution
- target venue or style constraints
- available evidence (figures, tables, citations, experiments)
- draft scope (section-only or full manuscript)

2. Build a section plan in IMRaD order unless the user specifies another structure:
- Title and abstract
- Introduction (problem, gap, contribution)
- Methods (reproducible procedure)
- Results (objective findings tied to evidence)
- Discussion (interpretation, limits, implications)

3. Draft with claim-evidence discipline:
- state one main claim per paragraph
- attach evidence or citation support to each claim
- avoid inventing numeric values or references

4. Produce outputs in two layers when useful:
- Layer A: concise outline with bullet claims
- Layer B: full prose draft for direct editing

5. Hand off to `writing-assistant` for polishing, style tightening, and journal-tone optimization.

## Output Requirements
- Keep terminology consistent across sections.
- Use explicit transitions between paragraphs.
- Flag missing evidence with `[Evidence Needed]` instead of fabricating details.
- If citation metadata is incomplete, use placeholder keys like `[Author, Year]` and list unresolved items.

## References
- Use [references/paper-draft-template.md](references/paper-draft-template.md) for a reusable draft scaffold.
