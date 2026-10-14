# v10 figure sources (copied 2026-10-14)

Copied from `azusa-dom/claude` `figures/cine-cmr-review-v10/` and `design-templates/house-style/agarwood-scifig/`
at the commit in `SOURCE_COMMIT.txt`. These are the sources of the figures now in `../integrated/`.
`../integrated_sources/` holds an earlier version and is no longer the source of record.

Rendering the unmodified `src/fig5_validation_programme.py` here reproduced the manuscript's Figure 4 SVG
byte for byte before the change below.

Changes made in this repository:

- 2026-10-14: Figures 4 and 5 were renumbered. `src/fig4_validation_targets.py` is derived from
  `src/fig5_validation_programme.py`; panel b now shows three questions answered by complementary
  (not sequential) evidence instead of the Stage 1-3 programme table. Panels a and c are unchanged.
  It writes `out/Figure_4_validation_targets_programme.*`, copied to `../integrated/`.

Build one figure: `PW=/opt/node-tools/node_modules/playwright python3 src/fig4_validation_targets.py`
(needs Node with Playwright/Chromium, Pillow, and Liberation Sans/Serif fonts).
Other scripts still use their pre-renumbering output names.
