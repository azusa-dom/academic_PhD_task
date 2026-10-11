# Integrated editable figures — 11 October 2026

This derivative retains the newest user-supplied agarwood figure layouts, including the table-based Figure 5 and parallel-flow Figure S3. The original ZIP and job outputs remain unchanged outside this directory. The active sources are the nine Python scripts listed below; historical poster and Typst alternatives are not part of this build.

- fig1_two_track_journal.py → Figure 1
- fig2_counterexample.py → Figure 2
- fig3_timeline.py → Figure 3
- fig4_attributes.py → Figure 4
- fig5_validation_programme.py → Figure 5
- figS1_strain_definitions.py → S1
- figS2_error_attributes.py → S2
- figS3_training_inference.py → S3
- graphical_abstract.py → graphical abstract

The manuscript inserts main and supplementary figures at 190 mm. Ordinary labels are source-audited at approximately 7.06 pt or larger; mathematical subscripts are smaller (approximately 6.19–6.73 pt). The graphical abstract is a separate 260 × 100 mm artifact. Do not shrink these assets and retain the same font-size claim.

Figure 3 has 49 plotted entries, not 49 independent experiments or a field-wide denominator. The selected endpoint categories count 20 mask/landmark/registration/inter-method, 8 downstream labels, 16 known-field or DENSE/tagging strain comparisons, 1 prescribed-scar evaluation reporting whole-slice errors, 3 unverified endpoints and 1 other-task entry. A study may report several endpoints; colours are not a validation ranking. Source-specific rationale, reading depth and final S3 source lines are in data/table_s3_methods.csv.

Figure 1 uses global radial FT–tagging ICC 0.10–0.63; 0.81 belongs to an FT–FT comparison. Figure 4 retains source values but does not infer equivalence from SD overlap or scar recovery from slice-average error. Figure 5 is a proposed programme of complementary tests, and its original bottom clipping is repaired. The graphical abstract intentionally contains no evidence-prevalence counts.

To edit, change the relevant Python script or data CSV and run that script with Python 3, Pillow and pypdf installed. The renderer needs Node.js plus Playwright/Chromium; PW can point to the Playwright module and CHROME to the executable. Font measurement uses Liberation Sans on Linux or Arial on macOS (SCIFIG_FONT_DIR may override the directory). The supplied SVGs retain editable text; PDFs embed fonts. No font files are redistributed. Prebuilt PDFs are sufficient to compile the manuscript without rebuilding figures.

Actual final captions are mirrored in captions_and_alt_text.md. The manuscript declarations describe AI assistance and numerical redraw provenance. These diagrams are not new experimental evidence.
