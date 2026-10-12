# Integrated PDF, figure, table and reference QA

## Final artefacts inspected

- Main manuscript: `delivery/main_v10_skill_revised_20261011.pdf`, 35 A4 pages, 812,743 bytes.
- Supplement: `delivery/supplement_v10_skill_revised_20261011.pdf`, 20 A4 pages, 477,552 bytes.
- Both PDFs were produced from a clean extraction of `delivery/manuscript_source.zip`, not copied from an earlier working build.

## Build and reference checks

- The source archive passed `unzip -t` with no compressed-data errors.
- Clean rebuild used `scripts/build_manuscript.sh`: static QA, pdfLaTeX, BibTeX and three post-BibTeX pdfLaTeX passes for each document.
- Static QA result: 3 TeX files and 2 manuscript CSV files checked; 94 active citation keys, 94 BibTeX records, 90 DOI-bearing entries and no missing cited key, duplicate key, duplicate DOI, missing file reference or malformed environment.
- Final `main.log` and `supplement.log` contain no `Warning`, undefined citation/reference, overfull/underfull box, duplicate destination, fatal error or build error.
- `pdffonts` showed every listed font embedded and subsetted (`yes yes yes`); no non-embedded font row was found.
- `pdftotext` succeeded for both PDFs. Searches found the corrected “external-to-developers”, “no between-case inferential test” and selected `±3.5`-percentage-point wording, and found no `??` marker.

## Page-level visual inspection

All 35 main pages and all 20 supplementary pages were rendered at 90 dpi and inspected as contact sheets for blank pages, orientation, clipping, displaced floats, broken glyphs and gross overflow. Higher-resolution 144–180 dpi inspection covered:

- Main pages 1, 5, 7, 9, 14, 16, 18–19, 21, 23, 25, 27–28 and 35.
- Supplement pages 1, 3–6, 8–13 and 20.

The inspected set covers the title/abstract, every numbered main and supplementary figure, all main tables, the full long-table sequence S1–S3, declarations, beginning/end of both reference lists and representative dense-text pages. No clipping, collision, truncated rule, missing panel, blank overflow page or rotated page was found.

## Figure checks

| Figure | Final main/supplement page | Checks |
|---|---:|---|
| Figure 1 | Main 5 | Panel order, equations, reported values, legend and caption visible; no clipping. |
| Figure 2 | Main 7 | Mapping labels, stretch range/mean and analytic/non-empirical boundary agree with text. |
| Figure 3 | Main 14 | 48-entry classification, evidence counts and corpus-bound caption agree with Table S3/data; dense labels remain legible at 176 mm. |
| Figure 4 | Main 16 | Remote/scar values, case-average errors, EF values and “no between-case test” statement agree with source data and revised text; no scar-level recovery is claimed. |
| Figure 5 | Main 23 | Validation-target claims, three proposed stages and equal-mean regional example agree with the proposed-programme text. |
| Figure S1 | Supplement 3 | Engineering/Green–Lagrange conversion, layer/axis, timing and aggregation examples consistent. |
| Figure S2 | Supplement 4 | Attribute-specific error and Jacobian examples visible and described as schematics. |
| Figure S3 | Supplement 5 | Training- versus inference-time controls and held-out contract consistent. |

The source PDFs are 190 mm wide with a recorded minimum native text size of about 7.06 pt. Final placement is 176 mm, giving an estimated minimum of about 6.54 pt, compared with about 5.94 pt at the baseline ~160-mm placement. Readability improved and was checked on rendered pages; this measurement is not a claim of JCMR production compliance. Figure 3 remains intrinsically dense and should be reviewed by the author at 100% display/print size.

The supplied muted sage/olive/terracotta palette and white background were preserved. No generative image model or stylistic redesign was used. PDF, SVG, Python sources and data for Figures 3–4 are included in `manuscript_source/figures/editable_sources/`.

## Table checks

- Main Table 1 (page 9), Table 2 (pages 18–19), Table 3 (around pages 19–20) and Table 4 (page 25) were inspected for column boundaries, row continuation and unit/endpoint labels.
- Supplementary pre-specification and study-example tables and Tables S1–S3 (pages 6–13) were inspected across every continued page.
- The duplicate PDF destination warning caused by resetting the supplementary long-table counter was removed by assigning unique hyperlink anchors.
- Dense table text is small but within the page and readable on enlargement. It is an author-review layout, not a journal typeset proof.

## Limitations of QA

- Visual QA establishes rendering integrity and internal consistency, not scientific truth, legal rights, accessibility certification or journal acceptance.
- No physical press proof, colour-vision user study or journal production template was available.
- Current live JCMR upload fields and AI-assisted-artwork policy could not be certified from this host and remain an author check.
