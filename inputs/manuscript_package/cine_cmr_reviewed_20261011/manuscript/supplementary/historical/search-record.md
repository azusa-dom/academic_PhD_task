# Bounded gap-search record

## Scope

- Evidence date cap: 1 September 2026.
- Retrieval date: 3 September 2026.
- Databases: PubMed, Europe PMC and OpenAlex, through their official APIs.
- Query families: regional post-MI cine strain; known-motion/digital phantom;
  prior/regularisation perturbation; conditional recoverability;
  failure-aware/selective prediction; regional localisation/spillover/attenuation.
- Exact database-specific strings, reported hit counts, retrieved counts, caps,
  date cap and retrieval date: `gap-search-query-log.csv`.

## Counts and caps

Across the 18 query/database combinations, the APIs reported 41 PubMed, 244
Europe PMC and 508 OpenAlex hits. The reproducible export contains 281 returned
rows and 253 unique records after deduplication. Twenty-one were retained as
near-neighbours and 232 were excluded at title and available abstract/metadata
screening. Two further records were added by the documented 9 September 2026
top-up check below; they are reported separately from these denominators. No record met the complete joint-design conjunction.

## Top-up check, 9 September 2026

A targeted top-up check was run on 9 September 2026 with the same 1 September
2026 publication cutoff. Two cine-only tissue-inference studies were identified
that the six 3 September query families had not returned:

- Righetti F, Rubiu G, Penso M, Moccia S, Carerj ML, Pepi M, Pontone G, Caiani EG.
  *Deep learning approaches for the detection of scar presence from cine cardiac
  magnetic resonance adding derived parametric images.* Med Biol Eng Comput
  2025;63(1):59-73. DOI 10.1007/s11517-024-03175-z. PMID 39105884.
  Published online 6 August 2024. Retained as NN22.
- Yang G, Chen J, Sheng X, Yang S, Zhuang X, Raman B, Li L, Grau V.
  *Contrast-Free Myocardial Scar Segmentation in Cine MRI using Motion and
  Texture Fusion.* arXiv:2501.05241, January 2025. Retained as NN23.

Both DOIs and the PMID were checked against the 253 deduplicated candidates in
`search/gap_2026-09-01/screening.csv`; neither is present, so these are
additions rather than reclassified exclusions. The 3 September denominators
(281 rows, 253 unique records, 21 retained, 232 excluded) are unchanged. With
the top-up the component matrix holds 23 near-neighbour records representing 22
distinct studies.

This top-up is a directed check prompted by a known coverage gap. It is not a
repeat of the six query families, does not re-establish exhaustiveness within
the recorded boundary, and was screened in the same single AI-assisted stream.
Independent human duplicate screening of NN22 and NN23 is outstanding.

## Caps

Each request was capped at 100 results to keep this targeted narrative-review
gap audit bounded and reproducible. The cap affected the broad regional post-MI
query in Europe PMC (239 hits) and OpenAlex (473 hits); it did not affect the
other 16 query/database combinations. This cap limits the absence statement.

## Deduplication

The search script normalised DOI and PMID fields and merged records by DOI,
PMID/OpenAlex identifier and normalised title. Source database and query-family
memberships were retained. The exact reusable implementation is
`scripts/run_bounded_gap_search.py`; the screen is in
`scripts/screen_bounded_gap_search.py`.

## Screening

The recorded screen was completed in one AI-assisted review stream from title
and available abstract/metadata, with primary/full sources checked where a
record was used for a manuscript claim. Inclusion as a near-neighbour required
contribution to at least one component of the design; inclusion did not imply
that the study met the full conjunction. The per-record decision and reason are
in `search/gap_2026-09-01/screening.csv`. The complete 23-row component matrix
is `near-neighbour-matrix.csv` (NN01-NN21 from 3 September 2026, NN22-NN23
from the 9 September 2026 top-up check).

The source set did not separately label any of the 232 exclusions as a
full-text final-stage exclusion. They must not be redescribed as such. A real
independent human reviewer has not yet returned decisions. The blinded review
pack in `independent-review/` defines the limited second-review step; the
manuscript does not report dual screening or a disagreement count.

## Citation expansion and manual supplementation

The broader narrative review used backward and forward citation expansion from
the core DeepStrain, multivendor, DENSE-comparison, deformation-standardisation,
SCMR and current review papers. Official regulator, guideline, product,
repository and dataset records were added manually because bibliographic
databases index them incompletely. Expansion stopped when an additional round
changed no method family, comparison axis or principal conclusion. This is a
thematic stopping rule for the narrative review, not proof of exhaustive
retrieval.

## Bounded conclusion

Within this database, query, cap and date boundary, no study was identified
that jointly implemented the prescribed regional abnormality, acquisition and
controllable-prior perturbations, one predeclared estimand contract, regional
retention/distortion outcomes and failure-aware selective-performance
assessment. This does not imply that the individual components have not been
studied or that a qualifying study cannot exist outside the recorded boundary.
