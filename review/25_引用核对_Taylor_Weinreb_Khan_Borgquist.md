# 引用逐句核对：Taylor 2016、Weinreb 2021、Khan 2012、Borgquist 2022（2026-10-14）

用途：只核对稿子里引用这几篇的句子是否被原文支持，不做通读拆解。方法按 `zoya-paperhelper` 的阅读范围登记与来源标签（[原文事实] / [作者推断] / [读者推断] / [未报告]）。被核对的稿件句子取自作者在对话中的引述；本仓库各分支的 `manuscript/` 中都没有这几句，也没有这四篇的引用键，因此没有对照稿件上下文。

## 阅读范围

| 文献 | 实际读到的 | 读深 |
|---|---|---|
| Taylor 2016, Heart Rhythm 13(2):481–9, [DOI](https://doi.org/10.1016/j.hrthm.2015.10.024)，PMID 26498258 | 作者提供的出版版 PDF，共 9 页，逐页看页面图像，含 Table 1–4、Fig. 1–3、参考文献。无补充材料 | 全文 |
| Weinreb 2021, Radiology 298(1):28–35, [DOI](https://doi.org/10.1148/radiol.2020202903) | 同文联合发表于 Kidney Medicine 2021;3(1):142 起（末页未在 XML 中给出；[DOI](https://doi.org/10.1016/j.xkme.2020.10.001)，PMC7873723），经 Europe PMC JATS XML 读全文，含 Table 1–3 | 全文（联合发表版本；未逐字比对 Radiology 版） |
| Khan 2012 (TARGET), JACC 59(17):1509–18, [DOI](https://doi.org/10.1016/j.jacc.2011.12.030)，PMID 22405632 | PubMed 摘要；Borgquist 2022 Table 4 中的 TARGET 行 | 仅摘要 |
| Borgquist 2022, Heart Rhythm O2 3(4):377–384, [DOI](https://doi.org/10.1016/j.hroo.2022.05.003)，PMC9463689 | 全文（Europe PMC XML），含 Table 4 | 全文 |

## Taylor 2016：全文核对后，两句话都成立，但有三处要写准

作者提供了出版版 PDF（9 页），逐页看了页面图像，包括 Table 1–4、Fig. 1–3 和参考文献。下面的页码是期刊页码。

**第 1 点（激动的测量方法）。成立。** 软件是 TomTec（Tomtec Imaging Systems, Munich），对象是 basal、mid、apical 三层短轴（p483 左栏）。图像来自 1.5 T GE Signa 上的 SSFP cine：TR 3.2 ms，TE 1.7 ms，层厚 7 mm、层间隔 3 mm，每个心动周期 25 个时相，平均时间分辨率 40 ms（p482–483）[原文事实]。作者选周向应变而不用径向应变，理由是它与 CMR tagging 做过验证、重复性更好；tagging 只出现在引用的前作里，本研究没有采集 tagging 或 DENSE [原文事实，p483]。所以"read from feature-tracking time to peak circumferential strain on cine CMR"准确。

"最晚"的判定方法：每段取收缩期周向应变峰值出现的时间，用占 RR 间期的百分比表示；在可分析节段中取峰值最晚的节段作为 LMA [原文事实，p483 右栏；Fig. 1A 示例只标出一个 LMA 节段]。判定前有两道筛选：

- 只考虑 11 个游离壁节段；
- 峰值周向应变高于 0 或在 0 到 −6.3% 之间的节段视为疤痕，先排除，不参与 LMA 判定 [原文事实，p483]。作者说 −6.3% 这个截断是为了偏向疤痕的特异性，敏感性交给 LGE。

也就是说，时相的读取本身没有阈值，但读取前有一道应变幅度门槛。

**第 2 点（疤痕的排除）。LGE 只记"有/无"，没有透壁度阈值。** 观察者 R.J.T. 用 CVI42 在 16 节段上目测判读，每段记为 present 或 absent（p483 左栏）[原文事实]。全文没有出现 >50% 或其他透壁度标准 [未报告：Methods、Results、Discussion 已查]。透壁或心内膜下 LGE 只用来把病因分为缺血性（p482）。对比剂是 gadolinium-DTPA 0.1 mmol/kg [原文事实]，按 Weinreb 2021 的分组属于 group I；这与本稿论证无关，只作记录。

**concordant 的定义比摘要写的宽：** "(1) subtended a nonscarred segment and (2) subtended LMA *or the adjacent segment*"（p483 右栏）[原文事实]。所以 concordant 是"无疤痕 + LMA 或其相邻节段"，不是严格的"最晚激动节段"。稿子如果写成"lead over the latest-activated, scar-free segment"，应改成"over or adjacent to the latest-activated segment"，或者不展开细节、只说"concordant with late activation and absence of scar"。

**第 3 点（效应大小）。concordance 独立预测 LVRR，但调整的协变量很少；临床终点实际是 HR，被误标成 aOR。**

LVRR 方面（Table 3，逻辑回归）：
- 单变量：concordant 的 OR 为 6.62（95% CI 2.61–16.79）；LMA 或相邻节段 3.27（1.29–8.30）；单独"无疤痕"2.60（0.86–8.29，P = .09，未达显著）。
- 多变量：Model 3 中 concordant 的 OR 为 6.28（2.45–16.08，P < .001），只与年龄一起进入模型。Model 2 中无疤痕 4.85（1.24–18.94），LMA 或相邻节段 7.01（1.96–25.10）[原文事实]。
- 进入多变量模型的规则是单变量 P < .10（p485）。所以除年龄外，QRS 时限、病因、LVEF 都没有进入 LVRR 模型 [原文事实]。但 Table 1 中两组的 QRS 时限（155.3 vs 143.0 ms，P = .02）和缺血病因（45% vs 67%，P = .04）是不平衡的 [原文事实]。因此"独立预测"只是相对年龄而言 [读者推断]。
- 导线恰好落在 LMA 节段本身（而不是相邻节段）的 20 人中，18 人（90%）出现 LVRR（p486）[原文事实]。

临床终点方面（Table 4，Cox 回归）：随访中位 4.4 年，共 28 例心脏死亡（concordant 组 8 例，nonconcordant 组 20 例），心衰住院 3 例和 10 例（p486）[原文事实]。
- Model 2 中 concordant 对心脏死亡的 HR 为 0.27（0.12–0.62），对心脏死亡或心衰住院为 0.26（0.12–0.58）。
- Model 1 中"无疤痕"分别为 0.24（0.11–0.52）和 0.24（0.12–0.49）。
- 两个模型都只调整了年龄和 LVEF [原文事实]。
- 单独的"LMA 或相邻节段"对两个终点都没有预测作用：HR 0.82（0.33–2.02，P = .66）和 1.19（0.57–2.51，P = .64）[原文事实]。

Table 4 的表头和统计方法一节都写的是 Cox 比例风险模型和 HR，但摘要和正文 p486 把同一组数字写成"adjusted odds ratio [aOR]"。这是论文自身的标注错误 [原文事实：两处标注不一致]。稿子如果引用这些数字，应写 HR，并注明出自 Table 4。

**第 4 点（局限与可重复性）。FT 时相的可重复性没有报告。** 作者自述的局限包括：单中心、样本量中等、观察性设计，不能证明 LGE/FT 引导优于透视定位；CMR 是多年后回顾分析的（作者认为这相当于对 FT 结果设盲）；没有收集 QRS 形态数据（p488 Study limitations）[原文事实]。全文没有任何关于 LMA 时相或疤痕判读的观察者内或观察者间重复性数据 [未报告：Methods、Results、Limitations 已查]。文中唯一涉及"reproducibility"的地方，是选择周向应变的理由，引用了前作中的应变幅度重复性（引文 8、23，p483）。PubMed 标的 MeSH 词"Reproducibility of Results"大概来自这里 [读者推断]。所以稿子里应保持"read from"，不要写"accurately"或"reproducibly measured"。

**与稿子论证相关的另外两点：**

- 时相是在平均 40 ms 的时间分辨率下读取的（p483）。节段间的激动时间差本来就不大，Borgquist 2022 的讨论也强调了这一点。这可以作为 §4"时相空缺"的一个具体例子 [读者推断]。
- 作者的结论是"it is scar rather than LMA that primarily relates to clinical outcomes"（p487），以及"The assessment of myocardial strain does not add value in predicting cardiac mortality or HF hospitalizations over and above the assessment of myocardial scar"（p488 Clinical implications）[作者推断]。

**对稿子两句话的判断：**

1. "late activation was read from feature-tracking time to peak circumferential strain on cine CMR"——全文支持，措辞可以不改。
2. "最晚激动 + 无疤痕"的导线位置与 CRT 反应相关——支持，但要写准三处：
   - "concordant"包括相邻节段；
   - 激动时相（LMA）只与 LVRR 相关，与死亡和住院无关，硬终点主要由"无疤痕"解释；
   - 这是回顾性、单中心、n = 89 的研究，多变量模型只调整了年龄（或年龄加 LVEF）。
   若稿子用它说明"时相信息有临床意义"，应限定为"associated with LV reverse remodelling"。

## Weinreb 2021：稿子那句话成立，但要改成具体主体和条件，附带的论证要收窄

**第 1 点（group II 的定义与清单）。** Table 1 列出的 group II 共五个产品：gadobenate dimeglumine（MultiHance，线性离子型）、gadoteridol（ProHance）、gadobutrol（Gadavist/Gadovist）、gadoterate meglumine（Dotarem、Clariscan） [原文事实，Table 1]。group II 不等于"大环类"：gadobenate 是线性的，但被归入 group II，理由是"the evidence supporting a very low risk of NSF is actually greater for gadobenate than it is for the macrocyclic GBCM"（Is the Risk of NSF the Same for All GBCM? 一节） [原文事实]。group III 只有 gadoxetate（Eovist/Primovist） [原文事实]。

你所在机构用于 CMR 的对比剂我无法从这里确认，需要你核实。英国常用的 gadobutrol 和 gadoterate 都在 group II 之列。gadobenate 在欧盟/英国的适应证受监管限制，Weinreb 的分组是 ACR（美国）分类，不涉及欧盟监管状态 [读者推断]。

**第 2 点（风险数字的来源）。** 这组数字全部来自两篇二次研究。0/4931 和总体 95% CI 上限 0.07% 来自 Woolen 等 2019/2020 年的系统综述与 meta 分析（JAMA Intern Med 2020;180(2)，正文引文 23），对象是"4,931 group II GBCM administrations in patients with stage 4 or 5 CKD"。分期数字来自 Shankar & Davenport 2020（Radiology 297(3):741–747，引文 24）的亚分析：CKD 5D 为 0/1849，上限 0.2%；未透析 CKD 5 为 0/732，上限 0.5%；两者合并 0/2581，上限 0.1% [原文事实]。这些数据全部是 group II。

各原始研究的随访时长，Weinreb 没有报告 [未报告：全文已查]。这一点有分量，因为同一篇文章写道，NSF 从暴露到发病"ranges from the same day to approximately 10 years (median, 42 days)" [原文事实，NSF and GBCM Exposure 一节]。随访不足会低估风险，要知道随访多长需要读 Woolen 2020。还有两处措辞要注意。摘要写"4931 administrations"，正文同一处又写"zero cases in 4,931 patients"，给药次数与人数混用 [原文事实，读者注意到的不一致]。文章也明确说 group II 并非零病例："In a review of 405 patients diagnosed with NSF, group II GBCM exposures were reported in 23 patients; however, only two were unconfounded"，引文 21 是两例 gadobutrol 相关病例 [原文事实]。

**第 3 点（共识实际建议了什么）。** Table 2 第 4 条："Group II GBCM should not be withheld or delayed if harm would result from not proceeding with an indicated contrast-enhanced MRI." 第 7 条："The risk of NSF is very low for a standard dose (0.1 mmol/kg) of group II GBCM, even in patients with eGFR <30 mL/min per 1.73 m2 or AKI." 第 5 条：group II 用药前的肾功能筛查是可选的 [原文事实，Table 2]。所以对 eGFR <30 或透析患者，共识的立场是"不要因为 NSF 扣下或推迟必要的检查"，而不是"仍应避免"。但同一篇文章保留了三个限定：

- **剂量。** 结论只针对标准剂量 0.1 mmol/kg："the risk associated with greater doses or intra-arterial administration has not been assessed"。文中还特意说大剂量用法已基本废弃，"except in some instances of cardiac MRI" [原文事实，Is There an Association between NSF and the Dose of GBCM? 一节]。这一点和 CMR 直接相关：若稿子讨论的 CMR 方案用了超过 0.1 mmol/kg 的剂量，这篇的低风险结论就不能直接套用 [读者推断]。
- **"共识"的主体。** 这是 ACR–NKF（美国）的共识。文中写明 ESUR "advises 'caution' when administering group II GBCM to patients with eGFR less than 30"；Table 3 写明 KDIGO 2013 认为 eGFR <15 时"GBCM should be avoided … unless there is no alternative" [原文事实]。稿子里的"current consensus"建议改成"the ACR–NKF consensus"，或注明欧洲指南更保守。
- **知情告知。** 对已知 AKI 或 CKD 4–5 期的患者仍应告知 NSF 的潜在风险 [原文事实，eGFR threshold 一节]。

**另外三种情形是否被讨论：**

- **妊娠：** 全文未出现 [未报告：全文已查]。
- **钆过敏：** 只在引言里作为临床决策的考虑因素之一提到（"the risk of an allergic-like reaction"），没有分析 [原文事实]。
- **反复给药：** 只从 NSF 角度讨论了。Table 2 第 11 条说紧急情况下不应因 NSF 推迟后续剂量，非紧急时可间隔 24 小时以上或安排透析；正文承认"The risk of multiple closely spaced doses has not been evaluated in patients with eGFR less than 30" [原文事实]。
- **累积沉积（钆滞留）：** 被明确排除在外，原文为"Conditions purported to be associated with gadolinium retention … are not addressed in this document" [原文事实，引言]。

**对稿子的判断。** "current consensus regards the risk of NSF from group II agents as very low even in advanced kidney disease"这句成立，但建议改成"ACR–NKF consensus statements regard the risk … at a standard dose of 0.1 mmol/kg as very low …"，这样主体和剂量条件都对。用它削弱"不能打对比剂"的论证时，它只覆盖肾功能/NSF 这一种情形：妊娠和过敏它没涉及，累积沉积它明确不讨论，反复给药只覆盖 NSF 风险。按你预设的规则，§1 里"钆禁忌"这类空缺确实应缩成一句，并改写为：肾功能已基本不构成限制（在 ACR–NKF 框架内、标准剂量下），剩下的是妊娠、过敏和反复给药/钆滞留，而这几种情形不由这篇文献支撑。剂量限定是否需要在稿子里提，取决于该段讨论的 CMR 方案剂量，这个需要你判断。

## Khan 2012（TARGET）：摘要层面确认"无疤痕"是超声应变幅度，不是 LGE

摘要写道："220 patients … underwent baseline echocardiographic speckle-tracking 2-dimensional radial strain imaging"，干预组的导线放在"the latest site of peak contraction with an amplitude of >10% to signify freedom from scar" [原文事实，摘要]。所以 TARGET 的激动时相和"无疤痕"都来自超声斑点追踪径向应变，没有使用 CMR 或 LGE。主要终点（6 个月 LVESV 下降 ≥15%）响应率 70% vs 55%（p = 0.031）[原文事实，摘要]；Borgquist 2022 Table 4 中的 TARGET 行与之一致。全文未读。

## Borgquist 2022：两项试验的激动时相都来自超声；只有一项在有条件时用 CMR 判定疤痕

这是 STARTER 与 CRT Clinic 两项 RCT 的患者水平合并分析（n = 289，中位随访 6.3 年）。Methods 原文："Both studies used GE Echopac … for analysis of radial strain. Speckle tracking–based strain analyses were performed using short-axis views of the mid and basal segments"。疤痕的判定两项试验不同：STARTER 用超声，标准为"thin-walled segments (≤5 mm) with hyperacoustic appearance"；CRT Clinic 用"cardiac magnetic resonance imaging (CMR) showing accumulation of gadolinium contrast, or (in the absence of CMR) by peak radial strain ≤9.5%" [原文事实，Methods]。结果方面，干预组心衰住院更少（30% vs 42%，P = .035），全因死亡差异不显著（28% vs 38%，P = .13） [原文事实，摘要 Results]。

因此，如果稿子里"CRT 三项证据"是指 Taylor、TARGET 和 Borgquist，那么后两项的激动时相都来自超声，只有 Taylor 用的是 cine CMR FT。CMR 在这两项里最多只出现在 CRT Clinic 的疤痕判定中，而且是"有 CMR 时"才用。稿子应注明这一点。

还有一句与你 §4 的论证直接相关："Echocardiography-based strain … is the only modality that so far has been prospectively validated for CRT regarding segmental strain. CMR-based strain, however, allows for better reproducibility" [作者推断，Discussion "Identifying the latest mechanically activated segment" 一节]。这支持"CMR 时相信息在 CRT 中缺乏前瞻性验证"的说法。但它是作者在讨论部分的判断，引用时应写成"Borgquist et al. noted that …"，而不是当作他们研究的结果。

## 待办

1. ~~取得 Taylor 2016 全文 PDF~~：已完成（2026-10-14）。
2. 确认机构用于 CMR 的对比剂品种和剂量（是否 0.1 mmol/kg）。
3. 若稿子要用随访时长论证 NSF 风险，需要另读 Woolen 2020（JAMA Intern Med）。
4. 把稿子当前版本放进仓库，我好对照原句和上下文做最终改写建议。

信息来源：According to PubMed / PubMed Central；全文经 Europe PMC。
