#!/usr/bin/env bash
set -euo pipefail

project_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
output_root="${1:-${project_root}/build/release}"

if [[ -e "${output_root}" ]]; then
  echo "Please choose a new build directory: ${output_root}" >&2
  exit 2
fi

mkdir -p "${output_root}/main" "${output_root}/supplement"
output_root="$(cd "${output_root}" && pwd)"
cd "${project_root}"

python3 scripts/static_qa.py

build_one() {
  local source="$1"
  local target_dir="$2"
  local job="${source%.tex}"
  pdflatex -interaction=nonstopmode -halt-on-error -file-line-error \
    -output-directory="${target_dir}" "${source}"
  (
    cd "${target_dir}"
    BIBINPUTS="${project_root}:" BSTINPUTS="${project_root}:" bibtex "${job}"
  )
  pdflatex -interaction=nonstopmode -halt-on-error -file-line-error \
    -output-directory="${target_dir}" "${source}"
  pdflatex -interaction=nonstopmode -halt-on-error -file-line-error \
    -output-directory="${target_dir}" "${source}"
}

build_one main.tex "${output_root}/main"
build_one supplement.tex "${output_root}/supplement"

cp "${output_root}/main/main.pdf" "${output_root}/v81_main.pdf"
cp "${output_root}/supplement/supplement.pdf" "${output_root}/v81_supplement.pdf"

echo "Built ${output_root}/v81_main.pdf"
echo "Built ${output_root}/v81_supplement.pdf"
