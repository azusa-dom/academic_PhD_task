# 已应用与建议的修改

## 已应用(影响科学含义)

| 位置(基线行) | 改前 | 改后 |
|---|---|---|
| body §4.2 (218) | In 42 participants, Brandt … moderate-to-good agreement … a focal peak-time error endpoint was not established by the abstract inspected here | Among 42 enrolled participants, 30 contributed to the circumferential tagging–feature-tracking comparison, in which Brandt and colleagues found ICCs of 0.82 for global and 0.74 for septal and lateral time to peak strain … the study did not establish lesion-scale timing accuracy, and ICCs of this size do not establish individual interchangeability |
| body §3.3 (146) | Two further designs supply correspondence through geometry or mechanics without an image-similarity term | …through geometry or mechanics |
| body §3.3 (146) | They reported reduced late-diastolic drift and better correlation … than optical flow, pairwise registration and GLR. Comparisons with nD+t B-splines and pTVreg concerned simulation and in-vivo tracking endpoints | Both groupwise metrics reduced late-diastolic drift relative to Farneback optical flow and pairwise registration, and the locally low-rank version correlated better with tagging for radial strain in several segments than those two methods and than the global low-rank version. nD+t B-splines and pTVreg were compared on simulated tracking and strain errors and on public-data contour tracking; they were absent from the patient tagging comparison |
| body §3.4 (156) | without an intensity-based similarity loss | without a warped-image intensity-similarity term (its variational objective retains an image-reconstruction loss) |
| body §3.4 (158) | IG-BiReg … could not be verified from an accessible primary source | IG-BiReg combines a bidirectional residual fusion network with global constraints in mean-intensity and principal-component feature spaces; its published abstract reports mask and contour agreement on ACDC and M&Ms, and material-strain validation was not verified |
| body §3.6 (172) | circumferential Green–Lagrange strain | circumferential Lagrangian strain, derived from the estimated displacement (the exact tensor implementation sits in a technical appendix that was not accessible) |
| body §4.2 (216) | agreement in peak circumferential strain and similar regional patterns … while cine radial strain was overestimated | broadly similar end-systolic regional circumferential strain … while cine radial strain was overestimated, particularly in healthy and non-infarcted myocardium |
| body Table 2 (238) | global RS ICC 0.10–0.63 versus tagging and 0.10–0.81 between FT products | global RS ICC 0.10–0.63 versus tagging (0.63, 0.48 and 0.10 by product); between FT products 0.81 for one pair and 0.10–0.19 for the pairs involving the third product (abstract range 0.10–0.81) |
| body Table 3 Gao (266) | Similar regional patterns reported at abstract depth / Peak values; timing error not established here | Six-region patterns compared with DENSE; LGE-based infarct and transmurality discrimination evaluated / Regional peaks identified at end systole; full-cycle curves compared; focal time-to-peak error not established |
| body Table 3 Wehner (268) | only mid-slice Ecc was judged acceptable by the study | mid-slice Ecc showed the best agreement …, and longitudinal strain was described as borderline acceptable |
| body Table 3 MRXCAT (276) | Peak values; timing error not established here | Three mid-ventricular slices averaged; the temporal aggregation of the reported strain summaries was not established from the report; timing error not established |
| body §4.3 (285) | found the same kind of variation across scanners and post-processing | found relatively good inter-scanner agreement for global longitudinal and circumferential strain, lower agreement for global radial strain and larger software-related differences |
| body §6 (297) | across disease cohorts | in disease cohorts and in a population-based cohort |
| body §7 (371) / Table 4 (392) | median inter-observer variability of 0.84 mm | median inter-observer distances of 0.77 mm in the phantom and 0.84 mm in the volunteers |
| body Table 4 (396, 398) | Repository cited by the paper; live contents not verified / with disease labels | Repository linked by the paper and the developers' software page; live code and example contents not verified / spanning disease groups; per-case disease information withheld for training and validation |
| body §7.2 (405) | −7% to 6% … ; On individual mid-ventricular slices, CineVN … overestimated peak circumferential strain | −7 to 6 percentage points … ; For slice-level peak radial and circumferential strain, CineVN … overestimated (gave less negative) peak circumferential strain |
| body §7.2 (407) | DENT was developed from 5840 patients across nine centres | developed and evaluated with retrospective cine from 5840 patients across nine centres, with the data of six centres reserved for external testing |
| supplement (56, 163, 208, 216, 218, 223, 268, 290, 295, 299, 312, 320, 328, 330, 335, 339, 356) | 见 claim_reaudit.csv | 见 claim_reaudit.csv |
| Table S3 数据 + Figure 3 | IG-BiReg 证据类别 nr | mask(摘要级);图已重绘 |

## 已应用(书目与格式)

- references.bib:CineVN 在线日期 26 August 2024;MCM 说明改为"Listed in the MICCAI 2025 Reconstruction and Motion Estimation in Medical Imaging workshop programme"。
- 补充方法:94-reference set → 92。
- 五处 "whereas" 改为 while/and 或分号,以符合作者句式规则。
- 九张表列宽占满版心。

## 建议但未应用(待作者决定)

- STRAUS 3 × 6 与 engineering strain:确认后保留,否则改为 "STRAUS provides 18 virtual cases with simulated electromechanical motion; the number of independent source anatomies and the strain convention require full-method verification"。
- Morales 2021:若希望平衡呈现,可在 §3.6 加 "The original study also evaluated 10 synthetic motion datasets and compared global end-systolic strain with a tagging-based reference in 15 healthy participants; these endpoints do not establish dense regional accuracy in disease."
