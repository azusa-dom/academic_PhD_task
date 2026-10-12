# 中心引文独立核对（修订前定向复核）

日期：2026-10-11。状态：完成首批八项及追加四项中心来源核对；这是定向 fresh-context 引文/证据核查，不是全参考文献或整篇科学认证。作者批准仍待完成，未投稿。本核查只写本报告和配套 CSV，没有修改正文、图件或任务配置。

方法：先读当前 working/manuscript/body.tex、supplement.tex 中相关段落/表行及 references.bib 八条记录，再检索原始来源。不读既有审稿判断，不将历史 VERIFIED 标志当作证据。已读 AGENTS.md 与 skills/paper-writer/references/verification-ladder.md；使用独立上下文来源核查一级机制。每篇采用题名、作者/主题/年、核心关键词三类查询，随后定位原文方法、结果与表图。检索仅为这些证据缺口，不构成新系统检索，不改变原稿历史搜索日期或流程。

主要结论：最有后果的问题是把“运动估计器如何训练”与“下游如何验证”混为一谈（DLSS、aligned strain），以及 Jahromi 等效结论的时间端点、单位和预设性。StrainNet 的 ICC 数字正确，补充节段一致性界限可使正面结果与局限同时成立。MRXCAT 的四个模拟病例及共享 ACDC 背景必须明示。MyoNet 的 tagged-MRI/SinMod 监督和 Tsuneta 的人体结果应予保留。

## SRC01 · masutani2023dlss

**判定：** OVERCLAIM: training/evaluation conflated; AUC tied to threshold

**原文定位：** [Algorithm Development and Training Data; Neural Network Architecture; Abstract Results; Fig. 1](https://pubs.rsna.org/doi/10.1148/ryct.220202)。

**建议英文表述：**

> DLSS used a modified 3D U-Net trained on coregistered 4D-flow myocardial velocities from 223 examinations in 219 patients. In a separate coronary-disease cohort (53 patients, 846 segments), its radial-strain score yielded an AUC of 0.90 against four-reader consensus. At a 30% peak radial strain threshold, sensitivity, specificity and accuracy were 86%, 85% and 86%.

**边界及处理：** Do not classify velocity network as reader-label supervised. AUC spans thresholds. Primary abstract and Key Points differ in ordering of sensitivity/specificity: use Abstract Results and detailed Results, not ambiguous Key Points.

**实际阅读深度：** Publisher full-text relevant sections freshly retrieved; PMC direct access captcha。作者状态：author approval pending。

## SRC02 · koehler2025alignedstrain

**判定：** OVERCLAIM: pipeline supervision collapsed into LGE target

**原文定位：** [Materials and Methods: Study Datasets; DL Pipeline; Fig. 3; Detecting LGE+ Patients](https://pubs.rsna.org/doi/10.1148/ryai.240303)。

**建议英文表述：**

> Aligned strain combines cardiac key-frame detection, segmentation and deformable registration to derive phase-specific strain. Its registration model uses image similarity, mask agreement and smoothness losses; LGE-derived labels are used in the subsequent patient-level fibrosis classifier. The study used development and later internal-test datasets of 57 and 82 boys or men with DMD at one centre.

**边界及处理：** LGE is not displacement truth. Main binary endpoint is patients with at least one LGE+ segment; segment-wise exploratory association is separate. Do not describe same-centre temporal test as external-site validation.

**实际阅读深度：** Publisher full-text relevant methods/results freshly retrieved。作者状态：author approval pending。

## SRC03 · wang2023strainnet

**判定：** VERIFIED with missing uncertainty; source-internal global LoA discrepancy

**原文定位：** [Intramyocardial Displacement; Comparison of StrainNet, FT, and DENSE; Table 2 image visually inspected](https://pubs.rsna.org/doi/10.1148/ryct.220196)。

**建议英文表述：**

> For cine-contour end-systolic circumferential strain in 59 test participants, StrainNet versus feature tracking achieved ICCs of 0.87 versus 0.72 globally and 0.75 versus 0.48 segmentally against DENSE. Segmental StrainNet–DENSE bias was −0.55 percentage points, with 95% limits of agreement from −9.16 to 8.07 points. The 0.75±0.35-mm displacement EPE instead used DENSE-magnitude contours.

**边界及处理：** Global Table 2 −0.51±5.15 pp implies [−5.66,4.64], but Results text gives [−5.74,4.72]. Do not silently combine. Segmental table/text agree to rounding. ICC is not Pearson r (global r=.88/.79).

**实际阅读深度：** Publisher text, local primary-text snapshot, and actual Table 2 raster inspected。作者状态：author approval pending; global LoA source discrepancy flagged。

## SRC04 · jahromi2026densecine

**判定：** OVERCLAIM: prespecification; incomplete endpoint/unit

**原文定位：** [Statistical Analysis; §3.2.1; Table 1 caption; Table 2](https://link.springer.com/article/10.1007/s10237-026-02120-3)。

**建议英文表述：**

> In 40 healthy volunteers contributing two slices each, the one-slice cine and two-slice DENSE models met a TOST equivalence criterion for peak-systolic endocardial circumferential strain within a chosen margin of ±3.5 percentage points; the mean cine-minus-DENSE difference was −2.7 points. Other components and the epicardial layer showed larger discrepancies.

**边界及处理：** The source says selected/chosen margin, not prospective prespecification. Endpoint is slice-level peak systolic, not entire-curve equivalence. Eighty slice observations are clustered in 40 people. Do not interpret pp as relative-percent error.

**实际阅读深度：** Publisher full-text relevant sections freshly retrieved and local source snapshot reread。作者状态：author approval pending。

## SRC05 · mrxcat2023

**判定：** OVERCLAIM: radial abolition; SD-overlap inference; independence scope

**原文定位：** [Methods: DeepStrain application and tissue-property definition; Results: Cardiac functional model / DeepStrain analysis; Fig. 14 caption and image](https://pmc.ncbi.nlm.nih.gov/articles/PMC10116689/)。

**建议英文表述：**

> In the simulated infarct, remote/scar peak radial strain was 0.95/0.30, circumferential strain −0.18/0.01 and longitudinal strain −0.18/−0.17. Radial thickening was reduced, circumferential shortening was absent, and longitudinal shortening was similar. Reported DeepStrain errors were averaged over three mid-ventricular short-axis slices, not isolated scar voxels. The evaluation was by another research group, but DeepStrain and the image-texture model both used ACDC.

**边界及处理：** Reported Ecc error .02±.04; Err −.24±.21 overall, infarct −.20±.21. Source calls infarct lowest performance despite aggregate signed means not establishing ranking; report attributed wording or omit ranking. SD overlap is not equivalence. Fig.14 shows boxplots, not plotted per-case error SD bars. No explicit between-case inferential test identified in inspected main article; bounded statement only.

**实际阅读深度：** Local primary full-text snapshot sections reread; original Fig. 14 raster visually inspected; current publisher/PMC search identity confirmed。作者状态：author approval pending。

## SRC06 · militaru2021

**判定：** COMPARATOR_AMBIGUITY

**原文定位：** [Abstract Results; Global strain comparison; Fig. 5; Statistical analysis](https://pmc.ncbi.nlm.nih.gov/articles/PMC8117295/)。

**建议英文表述：**

> In 61 participants, global longitudinal and circumferential ICCs against tagging ranged from 0.92 to 0.94 and from 0.88 to 0.91, respectively. The 0.10–0.81 global radial ICC range describes agreement among feature-tracking vendors, not the feature-tracking–tagging comparison.

**边界及处理：** Keep vendor comparison distinct from tagging. The abstract/body give slightly different regional LS ranges, so avoid unnecessary new regional numbers without exact location.

**实际阅读深度：** Fresh primary full-text search response and local snapshot identification。作者状态：author approval pending。

## SRC07 · an2026myonet

**判定：** INSUFFICIENT_METHOD_DESCRIPTION

**原文定位：** [§2.1 Image Acquisition and Preprocessing; §2.2 MyoNet / Fig. 2; §2.4 Experimental Setup; Table 2](https://pmc.ncbi.nlm.nih.gov/articles/PMC13024448/)。

**建议英文表述：**

> MyoNet maps manually segmented binary cine sequences to in-plane displacement using a U-Net-like network with alternating spatial and temporal convolution kernels. In 22 Dahl salt-sensitive rats contributing 64 short-axis slices, training targets were x- and y-displacements extracted from tagged images with SinMod. Reported circumferential and radial strain ICCs were 0.973 and 0.975.

**边界及处理：** Explicit tagged-MRI reference preserves positive material-sensitive evidence. Not raw-intensity cine input, not 22 held-out tests; scan-level 80/10/10 split. Do not conflate MyoNet with residual ResMyoNet. ICC numbers agree abstract/table; Pearson radial differs abstract/table and should not be added.

**实际阅读深度：** Fresh PMC full HTML fetched with read-only network command after browser captcha/MDPI rate-limit; exact relevant sections read。作者状态：author approval pending。

## SRC08 · tsuneta2025dlr

**判定：** VERIFIED; retain in-vivo positive evidence

**原文定位：** [CMR protocols; Strain evaluation; Results: Strain analysis; Fig. 4; Table 6; Discussion](https://pmc.ncbi.nlm.nih.gov/articles/PMC12772260/)。

**建议英文表述：**

> In ten healthy volunteers at 3 T, model-based reconstruction reduced the SD of global circumferential strain differences from the fully sampled reference relative to compressed sensing: 3.0 to 1.7 percentage points at R=6 and 4.5 to 2.3 points at R=8. Circumferential bias persisted, and radial-strain precision did not improve.

**边界及处理：** This is real volunteer evidence, not a phantom test. Different raw-data acquisitions at R=1/2/4/6/8; DLR/CS reconstructed accelerated raw data. Global per-volunteer endpoint; precision here is SD of differences to full sampling, not scan–rescan precision or material accuracy.

**实际阅读深度：** Fresh PMC full HTML fetched with read-only network command after browser/J-STAGE failures; relevant methods/results read。作者状态：author approval pending。

## 原始来源内部不一致，不能假装已消除

1. **StrainNet global LoA**：实际打开并目视 Table 2 图片，global StrainNet 一行是 −0.51 ± 5.15；正文给 −5.74 至 4.72。前者展开为 −5.66 至 4.64。不能混用二者生成一个看似精确的新数值。节段界限 −9.16 至 8.07 与表格 −0.55 ± 8.61 仅有舍入差异，适合正文保留。ICC 在表格与正文一致；global Pearson r 另为 .88/.79，不能替换 ICC。
2. **MRXCAT case ordering**：原文将 infarct 称为最低表现，但给出的 infarct 径向 signed mean error −0.20 与总体 −0.24 不能单独推出排序。原 Fig.14 是真实/估计 strain 的箱线图，星号/圆点是箱线图离群值语境，未见足以视作显著性标记的说明；不要自行给这些标记发明检验。图注宜直接限制为三个中室短轴切片的报告值，不以 SD 重叠作“无差异”理由。
3. **MyoNet Pearson radial**：abstract 的 .953 与 Table 2 的 .975 不同；本次不建议新增该指标。所需 ICC .973/.975 一致，不受此问题影响。

## 访问与阅读记录

实际读取的本地源内容：review/source_snapshots/strainnet.txt、strainnet.html；jahromi.txt；mrxcat.txt 与 mrxcat_Fig14.jpg；militaru.txt（识别及相关来源定位）；dlss.txt（没有可用正文，转出版社）；review/citation_audit_retrieval/an2026myonet.json、an2026myonet_official.json、tsuneta2025dlr.json（仅原始 metadata/abstract payload，不采纳其中核查结论）。正文读取为上述八篇有关段落、表行、图注；未声称逐字读完三份 manuscript 文件或全参考文献。

新鲜网页读取：RSNA 的 DLSS、aligned strain、StrainNet 方法与结果；Springer Jahromi 方法、结果及表题；PMC Militaru primary full-text search response；MDPI/PMC MyoNet、J-STAGE/PMC Tsuneta。普通浏览器访问 PMC 多次返回 CAPTCHA，MDPI 首次返回 429，J-STAGE PDF 超时/HTML不可访问。沙箱内 Python DNS 失败；随后经自动批准的只读网络命令取得 MyoNet、Tsuneta PMC 完整 HTML，在内存中提取并阅读相关章节。StrainNet Table 2 同样以只读网络获取真实 JPEG 并实际目视。未将访问失败当作来源不存在。

两张实际目视图：StrainNet Table 2 原始表格；MRXCAT Fig.14 原始结果图。未在本子任务中渲染/目视最终稿 PDF，不对最终版排版提供确认。MRXCAT 数值与 ACDC 来源范围根据本地原文快照重新读取，并以新鲜官方检索确认来源身份；未重新下载其全文。

## 实际检索词（代表三种形式，全部在本次执行）

- DLSS：完整题名；`"Deep Learning Synthetic Strain" Masutani 2023`；`synthetic strain cine myocardial wall motion velocity`。
- aligned strain：完整题名；`"Deep Learning-Based Aligned Strain" Koehler 2025`；`aligned strain myocardial fibrosis key frames`。
- StrainNet：完整题名；`"StrainNet" myocardial strain DENSE Wang 2023`；`StrainNet circumferential strain DENSE limits agreement`。
- Jahromi：完整题名；`Jahromi Perotti automated cardiac strain 2026 DENSE Cine`；`automated short axis DENSE cine strain one slice two slice`。
- MRXCAT2.0：完整题名；`MRXCAT2.0 Buoso Joyce 2023 phantom ACDC`；`cardiac numerical phantom shape learning tissue texture MRXCAT`。
- Militaru：完整题名；`Militaru Panovsky strain 2021 tagging ICC`；`feature tracking multivendor 3T regional strain comparison`。
- MyoNet：完整题名；`"MyoNet" "2026" An`；`myocardial strain cine MyoNet sine wave rat U-net`。
- Tsuneta：完整题名；`Tsuneta Aono deep learning reconstruction strain 2025 volunteers precision`；`model based deep learning reconstruction cine cardiac precision strain compressed sensing healthy volunteers`。

其他追加定位检索包括 DOI/PMCID、SinMod、0.973/0.975、GCS/GRS、3.5 和 ACDC。宽泛查询有噪声返回；结论仅采用原始文章和出版者/PMC来源，没有用聚合网站支持机制或数字。此列表记录新的定向核查，不补写或认证历史文献搜索。

## 待最终稿复核

请主编辑修订后重查正文、主表、附表和图内标签是否一致，尤其 DLSS 的阈值与 AUC，Jahromi 的 peak-systolic / percentage points / chosen margin，Militaru 的 vendor-to-vendor comparator，以及 Fig.4 的 reduced radial thickening。作者批准、版权/AI声明与投稿状态仍须单列待办。本报告提供可落实的修订依据，不代表作者声明已经核准。

## 追加四篇的定向复核

主编辑追加要求后，继续直接核对当前段落与来源；未使用既有审稿推理。

### SRC09 · buoso2025tagging3d

判定：UNDERREPRESENTED_VALIDATION。来源：[原始文章](https://pmc.ncbi.nlm.nih.gov/articles/PMC12049999/)，定位：§2.2 In-vivo data acquisition and processing; Abstract Results; Fig.9/10; Results porcine validation。

> Buoso and colleagues trained separate short-axis and long-axis displacement networks on synthetic 3D tagged images and evaluated them on an external human landmark dataset and 23 in-vivo porcine datasets. Human displacement deviations had medians of 0.72, 0.81 and 1.12 mm in the x, y and z directions; porcine peak-systolic strain was compared with manual cine annotations. These results concern analysis of tagged acquisitions.

范围：Human IQR 1.17/1.64/4.17 mm respectively; do not call manual cine annotation dense material truth. Synthetic training is not synthetic-only validation. Do not interpret 23 datasets as 23 unique animals without checking the earlier study.

阅读深度：Fresh PubMed abstract/figure captions and fresh PMC full HTML relevant sections via read-only network command。作者批准待完成。

### SRC10 · portal2025semisup

判定：VERIFIED_CONFIG_NUMBERS; EPE_REFERENCE_NEEDS_NAMING。来源：[原始文章](https://doi.org/10.1016/J.COMPBIOMED.2025.110739)，定位：Abstract; dataset/reference-contour description; §4.4 implementation details; §5 configuration comparisons。

> Portal and colleagues report EPEs of 1.02 mm for the base configuration, 0.95 mm with end-diastolic distance-map weighting and 0.91 mm with full supervision, versus 1.19 mm for retrained RAFT. Evaluation contour points were initialized manually and propagated using conventional feature tracking; these points were not training targets.

范围：271-patient multicentre/multivendor in-house dataset. Full supervision refers to segmentation supervision, not dense motion truth. Do not promote .95 or .91 to all configurations; point-tracking agreement does not establish intramyocardial material accuracy.

阅读深度：Fresh publisher abstract plus publisher full-text sections returned by indexed DOI retrieval; direct browser DOI open failed。作者批准待完成。

### SRC11 · cao2018

判定：SCOPE_CORRECTION。来源：[原始文章](https://pmc.ncbi.nlm.nih.gov/articles/PMC5907464/)，定位：Abstract Methods; Image analysis; Results whole-cohort paragraph; Table 3。

> Cao and colleagues reported an ICC of 0.778 for DENSE versus tagging peak circumferential strain measured in a matched mid-ventricular short-axis plane. This is a whole-cohort comparison of slice-level peak strain, not an AHA-segmental ICC or whole-LV three-dimensional validation.

范围：Suggested compact Figure1 label: mid-slice peak Ecc, DENSE vs tagging, ICC .778. If axis wording implies regional ICC, revise the label/legend. Ell came from 4-chamber plane; Ecc/Err from one SAX plane.

阅读深度：Local primary full-text snapshot relevant methods/results reread; fresh three-form primary retrieval。作者批准待完成。

### SRC12 · kihlberg2020clinical

判定：TEMPORAL_ENDPOINT_CORRECTION。来源：[原始文章](https://pmc.ncbi.nlm.nih.gov/articles/PMC7720468/)，定位：Fig.6 caption; Results segment-level ROC paragraph; CMR acquisition description。

> At end systole, segmental circumferential strain discriminated LGE transmurality above 50% with AUCs of 0.87 for DENSE, 0.83 for tagging and 0.66 for feature tracking. This analysis comprised 1856 segments in 116 patients, including 84 qualifying scar segments in 34 patients.

范围：Change supplement peak systolic to end-systolic for quoted ROC endpoint. Patient-level GCS ROC has different AUCs (.78/.69/.69); do not mix them. Primary abstract versus Results significance p-values differ; no need to introduce those p-values.

阅读深度：Local primary full-text methods/results/Fig.6 caption reread; fresh title/author/keyword primary retrieval。作者批准待完成。

追加检索记录：Buoso 完整题名、`Buoso Stoeck Kozerke 2025 tagging synthetic human porcine`、`synthetic trained 3D tagging networks in vivo validation`；Portal 完整题名、`Portal Dietenbeck 2025 distance maps memory myocardial EPE`、`semi supervised cardiac videos distance maps memory networks tracking`；Cao 完整题名、`Cao Ngai 2018 DENSE feature tracking tagging strain comparison`、`DENSE feature tracking tagging circumferential strain comparison 0.778`；Kihlberg 完整题名、`Kihlberg Gupta 2020 strain torsion suspected coronary artery disease`、`strain torsion DENSE tagging scar transmurality end systole`。Cao 和 Kihlberg 的本地原始全文快照补读到方法、结果和目标图表说明；Buoso 本次取回 PMC 全文并读相应章节；Portal 限于出版者搜索索引返回的相应全文段落及摘要，不宣称全部附录已读。

进一步处理要点：Buoso 的验证不能写成“只有 synthetic images”；Portal 原先 abstract-level 的保守提示可据本次实际全文段落改为具体 reference contour-tracking 描述，新增阅读应进入独立检索补记；Cao 的 .778 应明确 mid-slice peak Ecc；Kihlberg 主表已见 end-systolic，但补充表仍有 peak systolic，应同步。
