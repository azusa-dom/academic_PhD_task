# Where the build scripts are

This folder holds the editable SVG of every figure, the data tables behind
Figures 3 and 4, the font-size audit and contact sheet, the figure contract,
captions and the README of the figure package. The Python generators
(`src/*.py`), the house style (`design-templates/house-style/agarwood-scifig`),
the Chromium renderer (`style/render_outputs.cjs`) and `build.sh` were not
copied into the manuscript repository; they live in the figure repository
`azusa-dom/claude`, branch `claude/agarwood-style-remaining-figures-3t4uv0`,
folder `figures/cine-cmr-review-v10` (commit 28096d5, "Use the two-track
evidence map as Figure 1"). Run `./build.sh` there to regenerate `out/`.
The README in this folder describes that layout.
