# Reference and claim-support verification

## Scope and result

- The v9 manuscripts cite 51 unique keys.
- references.bib was reduced to those 51 actually cited entries; the 98-entry inherited/expanded source library is preserved as qa/source_library_v9_full.bib.
- The citation-management validator parsed all 51 entries: 51 valid, zero errors, zero duplicates, four warnings.
- Warnings were reviewed rather than mechanically “fixed”: Fourier-Net+ and the 2026 adjacent review were online publications without verified volume/page fields at the inspected date; the Tsuneta article code contains a literal hyphen and is not a page range.
- BibTeX compilation produced only cited references. No unresolved citation was present in the final compile log.

## High-consequence metadata and claim checks

| Key | Metadata/source check | Claim-support check | Status |
|---|---|---|---|
| wang2023strainnet | DOI 10.1148/ryct.220196; PMC full text | Development/test split, contour source, EPE and cine ICCs checked as separate evaluations | AI_source_checked; human_review_pending |
| wehner2018 | DOI 10.1186/s12968-018-0485-4; PMC full text | 88 participants/186 pairs; slice-specific bias/CoV; dyssynchrony checked | AI_source_checked; human_review_pending |
| cao2018 | DOI 10.1186/s12968-018-0448-9; PMC full text | Recruitment/exclusions, one-slice scale, ICC/bias/limits and radial disagreement checked | AI_source_checked; human_review_pending |
| militaru2021 | DOI 10.1186/s12968-021-00742-3; PMC full text | Four population groups, 16-segment Lagrangian strain and global ICC ranges checked | AI_source_checked; human_review_pending |
| kihlberg2020clinical | DOI 10.1186/s12968-020-00684-2; PMC full text | LGE threshold, 34/116 subset, AUC and sensitivity values checked | AI_source_checked; human_review_pending |
| bell2025strain8 | DOI 10.1093/ehjimp/qyaf144; full text | Same-day design, eight protocols, CoV definitions and segmental pattern checked | AI_source_checked; human_review_pending |
| jahromi2026densecine | DOI 10.1007/s10237-026-02120-3; PubMed/publisher | Phantom, 40 healthy volunteers and component/layer conclusions checked at abstract/publisher depth | AI_source_checked; human_review_pending |
| zhou2018straus | DOI 10.1109/TMI.2017.2708159; full paper | Three templates x six states, modalities, meshes and engineering strain checked | AI_source_checked; human_review_pending |
| stanforddata | DOI 10.25740/xt223hz2438; DataCite plus Stanford lab page | 51-versus-55 scope discrepancy, acquisition dates, sequences and ODbL metadata checked | AI_source_checked; subject files not inspected; human_review_pending |
| tobongomez2013cmac | DOI 10.1016/j.media.2013.03.008; PubMed/full record | 15 volunteers, dynamic phantom, 12 landmarks and interobserver error checked | AI_source_checked; human_review_pending |
| wissmann2014mrxcat | DOI 10.1186/s12968-014-0063-3; PubMed/PMC | Generator and reconstruction-simulation role checked | AI_source_checked; human_review_pending |
| mrxcat2023 | DOI 10.1186/s12968-023-00934-z; PMC/ETH | Healthy/infarct/DCM/HCM generator and known simulated function checked | AI_source_checked; human_review_pending |

## Atomicity rule applied

Composite sentences were split when sources supported different clauses. Dataset size, sequence availability, usable pairing, derived-algorithm test size and independence are never treated as the same fact. Repetition, anatomy overlap, tissue discrimination and outcome association are not cited as direct dense-motion accuracy. Specific claims that could not be checked were narrowed, labelled not reported/not file-verified, or omitted.
