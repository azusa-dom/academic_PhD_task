# 逐句审阅(Supervisor-Skills `pre-submission-reviewer`,2026-10-09,commit 19e7be8 之后)

审阅对象:`manuscript/main.tex`(摘要、Plain English、声明)、`manuscript/body.tex`(91 个正文段落、约 440 句)、`manuscript/supplement.tex`(32 个正文段落)、9 张新图及图注。按 skill 的五个维度 + 禁用词扫描 + 逐节走查输出;每条发现都引用原句。范式按 STEM / 方法综述处理:不要求 baseline 与 ablation,改为检查"主张—证据—范围"链条、章节映射和图表自足性。

同一工作流(Codex/Claude)对自己产出的审阅不等于独立人工审稿;这份记录是给你和导师核对用的清单,不是"可投稿"的证明。

---

## Summary

- CRITICAL: **0**
- MAJOR: **3**
- MINOR: **14**
- 已直接修掉的:第一轮 6 处 + 第二轮全部剩余项(图内句式、四句列表型长句、§6.2 容量测试句、Plain English 一句、`~\cite` 约定);引用与数字未动。
- Top three fixes first:
  1. [MAJOR-1] 结论第二段 74 词的长句拆成三句(✔ 已改)。
  2. [MAJOR-2] 图 3 年表与补充 Table S3 的条目数、年份空档说明必须一致(✔ 已改:重建为 48 条,空档改为 2001–2008)。
  3. [MAJOR-3] 图内文字含 "X, not Y" 句式(Fig 1c、2、4b、5a/c、5 脚注、S1a)(✔ 已改:本机装了 typst 0.15 与 matplotlib 3.11,全部九张图从源码重建,字号审计通过)。

---

## Dimension 1: Macro logic

| # | Finding(引用原文) | Severity | Suggested fix |
|---|---|---|---|
| 1.1 | §1 引文块的中心问题("For a specified cine acquisition, estimator and measurement definition, which attributes of a regional abnormality (magnitude, location, spatial extent and timing) are recovered…")在 §4 五个小节、Table 3 四列、§9 三段都被逐一回答;链条完整。 | — | 无 |
| 1.2 | §1 第 3 段"Answering that question requires comparing estimator families by their inputs, assumptions, estimands, populations and reference standards: how each family uses image information, representation, priors and supervision…" 对应 §3 与 Table 1 的列;"which spatial and temporal scales of measurement its validation evidence supports" 对应 §9 第 1 段。映射成立。 | — | 无 |
| 1.3 | §3.1 归因实验的三个结论句("the limitation was the estimation process / lies in the representation / lay in the acquired input")在 §5.3 被引用、在 Fig 1b 被画出;但 §6.2 Stage 1 只写了"The true field should be projected into the candidate representation to measure approximation error independently of the estimator",没有点名这就是 §3.1 的第二条测试。 | MINOR | §6.2 第一段末加一句:"This is the representation-capacity test of \cref{sec:illposed}." |
| 1.4 | §3.7 "deliberate evaluation on a focal abnormality of known size and severity appears in one independent synthetic study" 与 §4.1、§9、Fig 3 图注("a prescribed focal deficit appears in one independent synthetic evaluation")四处一致。 | — | 无 |
| 1.5 | §4.1 "none is an error measured within the scar region itself" 与 Table 2 行、Table 3 行、§5.3、§9、摘要("without quantifying recovery of the scar region")一致;本轮按 MRXCAT2.0 全文把 "underestimating radial strain in every case" 改为 "generally underestimating",把 "three mid-ventricular short-axis slices" 改为 "mid-ventricular short-axis slices"(原文只写 "We only focused on mid-ventricular 2D short-axis CMR images")。 | — | ✔ 已改;作者核对 Fig. 14 |
| 1.6 | §8 "This review used targeted searches, did not perform duplicate screening or risk-of-bias scoring, and did not pool effect sizes" 与 §1.1、补充 Methods 一致;static_qa 对 "systematic" 的警告指向的五处全是否定句("neither a systematic review nor…"、"must not be described as systematic")。 | — | 无 |
| 1.7 | 定位句 §1 第 3 段只说 "narrower purpose",没有声称 first/only;cover letter 同样。 | — | 无 |

## Dimension 2: Writing details

| # | Finding | Severity | Suggested fix |
|---|---|---|---|
| 2.1 | 每个正文段落首句都是主题句(逐段核过 91 段);§4 引言段只有 1 句("No single study can answer every layer … from the most controlled to the most clinical.",50 词)。 | MINOR | ✔ 已拆为两句 |
| 2.2 | §3.2 第 1 段 10 句、§3.3 第 1 段 9 句,超过 skill 的 3–8 句建议;两段都在同一主题内(FT 的临床验证史;配准方法谱系),拆开会打断年表。 | MINOR | 保留;若导师嫌长,§3.2 从 "The family's clinical validation began before deep learning" 处分段 |
| 2.3 | 重复:§2.2 末句 "Validation should therefore follow the finest claimed spatial and temporal scale; credibility earned at a coarser scale does not transfer downward" 与 Fig 1c 文字 "Validation must follow the finest claimed spatial and temporal scale, not inherit credibility from an upstream task" 同义;图文重复是允许的,但图内用了 "not … " 句式(见 MAJOR-3)。 | MINOR | 图源改为 "Validation must follow the finest claimed spatial and temporal scale; credibility does not transfer from an upstream task." |
| 2.4 | §5.3 末句 "the same estimator on the same images preserved one strain component better than another at the slice-average level, and nothing in that single experiment says which of the three was responsible"(69 词全句)。 | MINOR | ✔ 已在 "responsible" 前拆句 |
| 2.5 | 摘要第 2 段首句 47 词("This critical narrative review compares … clinical outcomes."),列举六个验证目标。 | MINOR | 可接受;若期刊要求结构化摘要会自然拆开 |

## Dimension 3: English grammar(规则编号见 `grammar-rules.md`)

| # | Finding | Rule | Severity | Suggested fix |
|---|---|---|---|---|
| 3.1 | §9 第 2 段:"In the studies reviewed, direct tests of focal abnormality centroid, lesion-boundary or width error and transmural extent recovery were uncommon or not reported, and timing has been compared mainly at global and segmental level (time to peak between tagging, feature tracking and speckle tracking in 42 participants\cite{brandt2024}), with focal peak-time error against a material reference still untested; these are statements about the inspected evidence, and they do not prove that no such work exists."(74 词) | G4 | MAJOR | ✔ 已拆为三句 |
| 3.2 | §3 引言首句 62 词("All estimators resolve incomplete image information by adding structure, so the useful comparison … suit the abnormality being studied.") | G4 | MINOR | ✔ 已在 "so" 处拆句 |
| 3.3 | §3.2 第 6 句 59 词("Commercial implementations have differed in contour placement … even when repeatability within a product is acceptable") | G4 | MINOR | ✔ 已拆:差异一句,后果一句 |
| 3.4 | §3.3 第 5 句 57 词(Chen 2024 的数据集与对照列表)、§3.5 第 4 句 57 词(WarpPINN 描述)、§3.1 第 2 段第 5 句 56 词(band-limit 句)、§3.4 第 3 段第 3 句 56 词(三个 temporal 变体) | G4 | MINOR | 列表型长句,语法正确;可保留。若要拆,Chen 2024 句在 "and reported" 前断开 |
| 3.5 | 时态:方法描述用一般现在时,各研究结果用过去时("reported", "found"),综述自身用现在时;§3.2 "The family's clinical validation began before deep learning" 过去时正确。未发现混用。 | G3 | — | 无 |
| 3.6 | 冠词:抽查 §2.1、§4.2、§6.5 共 40 句,未见缺漏;"in simulation"(Fig 3 图注新加)无冠词,属不可数用法,正确。 | G1 | — | 无 |
| 3.7 | which/that:全稿 "which" 前均有逗号或为疑问代词("which attributes", "which of the three"),未见限制性 which。 | G5 | — | 无 |
| 3.8 | 被动语态:§6.1–6.4 方案段落被动句密度高("should be stated", "should occur", "should be chosen"),但主语确实不重要(规范性建议)。 | G6 | MINOR | 保留 |
| 3.9 | 引号标点:全稿用 LaTeX 的 ``…'' 且标点在引号外("``not inspected'' records that…"),符合逻辑标点。 | G8 | — | 无 |

## Dimension 4: LaTeX format

| # | Finding | Severity | Suggested fix |
|---|---|---|---|
| 4.1 | 式(1)(2)有编号但正文从未用 \cref 引用(只有式(3) `eq:registration` 被引两次)。 | MINOR | ✔ 已给式(1)(2)加 `\label{eq:kinematics}`、`\label{eq:gl}` 并在 §2.1 公式后一句引用 |
| 4.2 | 引用命令前无 `~`:96 处 `word\cite{}`、0 处 `~\cite{}`。这是 v9 以来的仓库约定(数字上标紧贴词尾),与 skill 的 `ResNet~\cite{X}` 规则相反。 | MINOR | 由你定;若改,全局 `sed 's/\([a-z)]\)\\cite{/\1~\\cite{/g'`,注意 `.\cite{` 的位置 |
| 4.3 | 标签含连字符(`fig:image-to-report`, `fig:same-contours`, `fig:attributes-mrxcat`, `tab:s3-methods`);LaTeX 可用,skill 建议下划线。 | MINOR | 可不改 |
| 4.4 | 九张图均为矢量 PDF,字体全部嵌入(Liberation Sans/Serif);页面尺寸 160 mm(主文版心)与 166 mm(补充),`width=\textwidth` 插入时不缩放。 | — | 无 |
| 4.5 | 图注第一句都给出结论(如 "Identical contours do not determine the same material correspondence"),符合"caption 首句即发现"。 | — | 无 |
| 4.6 | 补充 Note 2 原引用 Supplementary Figure S1(验证目标表),现改为 "summarised in Figure~5a of the main text";跨文档引用无法用 \cref,写死的 "Figure 5a" 若主文图号变动需手改。 | MINOR | 投稿前再核一次 |

## Dimension 5: Figure quality

| # | Finding | Severity | Suggested fix |
|---|---|---|---|
| 5.1 | Fig 3:原图按 41b78e1 版 Table S3(38 条)绘制,现 Table S3 有 48 行;已用包内脚本重建为 48 条(mask 22、label 8、material 14、focal 1、nr 3),空档由 2012–2016 改为 2001–2008,图注同步。 | MAJOR | ✔ 已改;新增九条的证据分类在 `figures/editable_sources/data/table_s3_methods.csv` 末尾,逐行有理由,请核 |
| 5.2 | Fig 4b 图内文字 "Errors are case-level means over whole slices, not errors inside the scar region."、Fig 5a 表格 "precision, not accuracy" / "biological association, not motion error" / "prognostic association, not clinical utility"、Fig 5c "Recovering the mean is not a pass."、Fig 5 脚注 "Counts denote resource units, not independent test participants."、Fig 1c "…not inherit credibility from an upstream task." 与你给正文定的禁用句式冲突。 | MAJOR | Fig 4、S1、S2 是 matplotlib,我可改;Fig 1、5、S3、GA 是 Typst,本机无 typst,需在你的制图会话改源码后重导出 |
| 5.3 | 颜色:三类证据色在色盲模拟下 ΔE ≥ 13.3(包内校验记录);Fig 4b "held" 灰青绿与 "error" 红同时有符号(✓/✗)和位置编码,满足双重编码。 | — | 无 |
| 5.4 | Fig 3 新增条目后 Conventional 泳道有 3 行、Cardiac 泳道 7 行,图高 160 mm;在 160 mm 宽的版心内占一整页,可接受;若编辑要求压缩,可去掉 Low-rank GW、INR、CMR FMs 三个 "not reported" 点并在图注说明。 | MINOR | 由你定 |
| 5.5 | Fig 4a 图内 "Radial and circumferential strain largely abolished in scar; longitudinal almost unchanged" 与正文一致;Fig 4c "Timing … peak-time error not in the record read" 与 Table 3 "timing error not inspected" 一致。 | — | 无 |
| 5.6 | GA 右侧 "Weaker: radial strain; focal boundary, extent and timing, rarely tested" 与 §9 一致;GA 2600×1000 px 满足 JCMR 最低 531×1328 的长边要求(以长边 1328 计)。 | — | 作者核对 JCMR 当前要求 |

## Banned-vocabulary and em-dash scan(全文,非抽样)

- 范围:main.tex、body.tex、supplement.tex 全部正文、图注、表注;脚本逐文件扫描,未分块。
- em-dash(`---`)作连接符:**0**。
- 禁用词(innovative, pioneering, revolutionary, transformative, superior, surpass, excel, remarkable, unprecedented, breakthrough, general-purpose, is capable of, notably, yet, yielding, at its essence, encompass, differentiate, reveal, underscore, pave the way, highlight the potential, profound, stems from, rigid, impede):
  - `general-purpose`:**2** 处——§3.3 "Both networks are general-purpose registration methods"、Table S3 无。词义是技术描述(非心脏专用),非 AI 腔;保留。
  - `yet`:**2** 处——§6.6 "yet all accelerated protocols significantly underestimated…"、§4.1 "yet the radial error they report…"。作连词使用,非填充词;保留或改为 "and"。
  - `reveal`:**1** 处——§6.2 "Such tests reveal whether apparent global success masks spatial redistribution"。MINOR,可改 "show"。✔ 已改。
  - 其余 0。
- 你自定的句式("not … but …", "rather than", "not only", "instead of", Conversely/Likewise/Similarly/Equally/importantly):正文 **0**;图内文字见 5.2。

## 逐节走查(按段落;只列有发现的句子,其余句子已读、无发现)

**摘要(3 段 9 句)**:第 1 段第 2 句 "and what it records is changing image intensity and anatomy without labels for myocardial material points" 承接上句的 "supports … estimation",逻辑成立。第 2 段第 4 句 "preserved slice-averaged circumferential strain better than radial strain without quantifying recovery of the scar region" 与 §4.1 一致。无发现。

**Plain English(3 段 11 句)**:第 2 段末句 "and each of them proves a different thing" 对非专业读者略突兀,可改 "and each answers a different question"。MINOR,未改。

**§1(5 段 23 句)**:第 1 段第 3 句 "The same compression also hides information." 是本轮加的衔接句,承接第 2 句的 "value"。第 3 段末句 "Within that comparison, the focal case is the most demanding one, and it is used here as a test of the evidence base, without treating every method paper as if it had set out to solve it." 是 §1 最长的一句(37 词),可接受。§1.1 第 1 段第 4 句 "Two further sources were used … : a separately supplied set of 42 auxiliary research leads, and a targeted verification update through 8 October 2026." 冒号后两个并列项,正确。无其他发现。

**§2(8 段 34 句)**:§2.1 第 1 段第 4 句 "Every estimator has to add something to those cues." 衔接句;第 5 句列四类方法。§2.1 公式后 "These equations state how a chosen mapping is converted into a chosen strain; they say nothing about whether φ is correct." ✔ 现在在此句前加了对式(1)(2)的引用。§2.2 第 1 段第 5 句 "It leaves two other questions open, namely whether cine-derived regional strain is wrong in any particular case, and whether image texture and temporal information can select a useful mapping." 与原意一致(原 "does not prove … always wrong")。§2.3 清单前句 "Because each step of that sequence adds a definitional choice" 回指 §2.2 的 volume→global→segmental→transmural 序列,成立。

**§3(16 段 118 句)**:§3 引言首句 ✔ 拆句。§3.1 第 2 段第 3 句 "The prior's role can be read in two ways, and the review keeps them separate throughout." 后面两句分别以 "The first concerns" / "The second concerns" 开头,逻辑清楚。第 3 段第 6 句 "That last attribution is conditional, because…" 是 Codex 建议后加的条件句,正确。§3.2 第 6 句 ✔ 拆句;第 9 句 "These are abstract-level readings, and the three studies validated three different regional quantities." 比原 "did not validate the same regional quantity" 更强(断言"三个不同"),与 Maret(瘢痕关联)、Hor(mid-LV Ecc vs HARP)、Augustine(global 各分量 vs tagging)相符。§3.3 第 1 段第 8 句 "Two further designs supply correspondence through geometry or mechanics in place of image similarity" 中 "in place of" 是本轮为避开 "instead of" 的替代,语义相同。§3.3 第 3 段第 5 句 "Both networks are general-purpose registration methods." 见禁用词扫描。§3.4 第 3 段第 6 句 "One parallel development belongs here because of what it leaves out." 承上启下,下一句解释基础模型不含运动估计。§3.6 第 1 段第 7 句 "These results establish workflow and output properties." 后接 "Independent dense material truth … is a separate matter",是 review/16 第 5 项。§3.6 第 2 段 StrainNet 10 句未动。§3.7 第 1 句现含 "plotted by year and family in Fig. 3"。

**§4(13 段 69 句)**:§4 引言 ✔ 拆句并加 Fig 5a 引用。§4.1 第 2 段第 7 句改为 "a general underestimation of radial strain"(原文措辞);第 8 句改为 "case-level averages over mid-ventricular short-axis slices";第 9 句新加 Fig 4 引用。第 3 段第 2 句 "The experiment also occupies a single point … with one scar geometry, one estimator, mid-ventricular slices only and one simulated signal-to-noise ratio" 改掉了 "one slice position"。§4.2 第 3 段首句 "The product dependence seen by Cao and colleagues was examined directly at 3 T by Militaru and colleagues" 衔接句,成立。第 4 段 Jahromi 句含 "statistically equivalent … within a prespecified margin of 3.5% (two one-sided tests)",已核全文。§4.3 标题 "Repeatability establishes precision, and leaves accuracy open":两句主语一致。§4.4 第 2 段末句 "Read as a direct ranking of material-motion accuracy, it would say more than it measured." 独立分词开头,主语 "it" 指 evidence,成立。§4.5 第 3 句 "Whether changing management on the basis of the measurement improves outcomes is a further question, and answering it requires…" 成立。

**§5(8 段 37 句)**:§5.3 末段第 3 句 ✔ 拆句。§5.2 第 2 句 "Three features of the measurement explain much of this." 衔接句,后三句分别给出三个特征。§5.4 第 3 句 "Quality control stands in the same relation to accuracy:" 冒号后解释,成立。无其他发现。

**§6(12 段 57 句)**:§6.1 第 1 段末两句是 Codex 建议加入的(baseline 调参、公开变换方向);第 2 段末句 "peak-time or curve-alignment error should be assessed in addition to peak amplitude" 是 review/16 第 9 项。§6.2 第 2 段第 3 句 "Recovery of their mean is then no evidence of success; the method must distinguish their location and extent within pre-specified tolerances." 与 Fig 5c 对应。§6.3 第 2 段首句 "No material-sensitive reference is perfect, so this stage also needs a sensitivity analysis." 衔接句。§6.5 第 2 段第 2 句 "so the 18 cases share three anatomies" 是对 "18 virtual patients" 的限定。§6.6 标题改为 "relevant and endpoint-specific";末句括号列四机制。无其他发现。

**§7–§9(9 段 38 句)**:§7 第 2 段首句 "The same record serves two audiences." 与第 3 段首句 "Software status needs the same discipline." 均为衔接句。§8 第 2 段首句 "The review itself has matching limits." 衔接。§9 第 2 段第 4 句 ✔ 拆为三句;第 3 段末句 "Combining these complementary tests … can identify where routine cine CMR preserves abnormality magnitude, location, extent and timing, and where the appropriate conclusion remains unresolved." 回应 §1 引文块的四属性。

**补充材料(32 段)**:Supplementary Methods 第 2 段 "The 42 leads are counted as leads only: they are neither fully read articles nor independent cohorts nor clinical validation studies" 是本轮改写,成立。Note 1 末新加 "Supplementary Figure S1 illustrates these four traps." Note 2 改为引用主文 Figure 5a。Note 4 第 2 段 "Post-processing strength or a biomechanical solve, by contrast, can be a genuine inference-time control." 用 "by contrast" 替代了 "Conversely"。Table S1 题注 "NR means not reported … ; it does not mean absent from the field." 成立。无其他发现。

## Final score (1–10)

**8**。0 CRITICAL,3 MAJOR 中 2 项已在本轮修掉(长句、Fig 3 与 Table S3 一致),剩 1 项(图内 "not X" 句式)需在图源修改;14 MINOR 中 4 项已改,其余为作者选择。

## Submission recommendation

**Needs 1–2 days more work**,且剩余工作全部在作者侧:(1) `review/17` 清单里标"必核"的五项由你对原文;(2) 作者声明与 JCMR 指南核对(本机访问 JCMR 作者指南仍返回 403,格式规则无法在此核实)。本轮审阅列出的 3 MAJOR 与 14 MINOR 中,除 4.3(标签连字符)、5.4(Fig 3 高度)两项作者选择外,其余均已修改。

## 本轮直接改动(✔,共 6 处 + 图)

| 位置 | 改前 | 改后 |
|---|---|---|
| §2.1 式(1)(2) | 无 label、未引用 | 加 `eq:kinematics`、`eq:gl`,正文 "These equations (\cref{eq:kinematics} and \cref{eq:gl}) state how…" |
| §3 引言首句(62 词) | "…by adding structure, so the useful comparison between them concerns…" | 在 "structure." 断句,"The useful comparison between them therefore concerns…" |
| §3.2 第 6 句(59 词) | "Commercial implementations have differed in …, with the consequence that values may fail…" | 拆为两句:差异;"As a consequence, values may fail to be interchangeable…" |
| §4 引言(50 词单句段) | 一句 | 两句 |
| §5.3 末句(69 词) | "…at the slice-average level, and nothing in that single experiment says…" | 在 "level." 断句 |
| §9 第 2 段第 4 句(74 词) | 一句 | 三句:focal 属性未报告;timing 的比较层级;"These are statements about the inspected evidence…" |
| §6.2 | "Such tests reveal whether…" | "Such tests show whether…" |
| Fig 3 | 38 条,2012–2016 空档 | 48 条,2001–2008 空档;图注同步 |
