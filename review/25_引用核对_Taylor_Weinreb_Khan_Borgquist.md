# 引用逐句核对：Taylor 2016、Weinreb 2021、Khan 2012、Borgquist 2022（2026-10-14）

用途：只核对稿子里引用这几篇的句子是否被原文支持，不做通读拆解。方法按 `zoya-paperhelper` 的阅读范围登记与来源标签（[原文事实] / [作者推断] / [读者推断] / [未报告]）。被核对的稿件句子取自作者在对话中的引述；本仓库各分支的 `manuscript/` 中都没有这几句，也没有这四篇的引用键，因此没有对照稿件上下文。

## 阅读范围

| 文献 | 实际读到的 | 读深 |
|---|---|---|
| Taylor 2016, Heart Rhythm 13(2):481–9, [DOI](https://doi.org/10.1016/j.hrthm.2015.10.024)，PMID 26498258 | PubMed 摘要与 MeSH 词。无 PMC 全文；Aston 机构库只有摘要页；出版社页面拒绝自动访问 | **仅摘要**。方法、多变量表、局限均未读 |
| Weinreb 2021, Radiology 298(1):28–35, [DOI](https://doi.org/10.1148/radiol.2020202903) | 同文联合发表于 Kidney Medicine 2021;3(1):142 起（末页未在 XML 中给出；[DOI](https://doi.org/10.1016/j.xkme.2020.10.001)，PMC7873723），经 Europe PMC JATS XML 读全文，含 Table 1–3 | 全文（联合发表版本；未逐字比对 Radiology 版） |
| Khan 2012 (TARGET), JACC 59(17):1509–18, [DOI](https://doi.org/10.1016/j.jacc.2011.12.030)，PMID 22405632 | PubMed 摘要；Borgquist 2022 Table 4 中的 TARGET 行 | 仅摘要 |
| Borgquist 2022, Heart Rhythm O2 3(4):377–384, [DOI](https://doi.org/10.1016/j.hroo.2022.05.003)，PMC9463689 | 全文（Europe PMC XML），含 Table 4 | 全文 |

## Taylor 2016：只能核到摘要层面，四点中有三点需要全文

**第 1 点（激动的测量方法）。** 摘要写的是"Feature-tracking and late gadolinium enhancement images were analyzed retrospectively"，并在括号里把 LMA 定义为"time to peak systolic circumferential strain" [原文事实，摘要 Methods]。标题写明"feature-tracking … cardiovascular magnetic resonance study"，MeSH 标了"Magnetic Resonance Imaging, Cine"。摘要里没有出现 tagging 或 DENSE。因此"read from feature-tracking time to peak circumferential strain on cine CMR"在摘要层面成立。用的是哪个软件、哪几层短轴、"最晚"是按节段排序取最晚还是设了阈值，摘要都没写 [未报告：仅读摘要]。

**第 2 点（疤痕的排除）。** 摘要定义 concordant 为"no scar and LMA"，nonconcordant 为"scar and/or no LMA" [原文事实]。所以 concordant 确实要求两个条件同时满足。LGE 透壁度阈值摘要没给 [未报告：仅读摘要]。

**第 3 点（效应大小）。** 摘要给出：LVRR 在 concordant 组为 68%，nonconcordant 组为 24%（P < .001），n = 89。中位随访 4.4 年（范围 0.1–8.7 年）。concordance 对心脏死亡的 aOR 为 0.27（95% CI 0.12–0.62），对心脏死亡或心衰住院的 aOR 为 0.26（0.12–0.58）。"no scar" 对心脏死亡的 aOR 为 0.24（0.11–0.52），对心脏死亡或心衰住院为 0.24（0.12–0.49） [原文事实，摘要 Results]。

需要注意：摘要报告的是 **adjusted odds ratio，不是 HR**。随访跨度长达 8.7 年，却用比值比而不是时间–事件模型，这一点要看全文的统计方法才能判断 [读者推断]。另外，摘要的结论把两种成分分开说："LVRR was primarily related to LMA, whereas events were primarily related to scar" [作者推断，摘要 Conclusion]。也就是说，与硬终点相关的主要是"无疤痕"，不是激动时相。稿子如果用这篇支撑"时相信息有临床价值"，可依托的是 LVRR，而不是死亡或住院。

**第 4 点（局限与可重复性）。** 摘要自述是回顾性研究、n = 89。PubMed 给这篇标了 MeSH 词"Reproducibility of Results"，提示正文里很可能有某种可重复性分析。但它测的是什么（时相、应变幅值，还是轮廓），在摘要里无法确认 [读者推断]。在拿到全文之前，稿子里这句应保持现在的措辞，只说"read from"，不要写成"accurately measured"或"reproducibly measured"。

**还需要全文才能完成的核对：** Methods 中的 FT 软件、短轴层数与 LMA 判定规则；LGE 透壁度阈值；多变量模型纳入了哪些协变量，concordance 是否独立预测 LVRR；Limitations 里关于 FT 时相可重复性的表述。请从曼大图书馆下载 PDF 放进仓库，或直接贴相关段落，我再补完这一节。

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

1. 取得 Taylor 2016 全文 PDF，补完第 1、2、4 点和多变量结果。
2. 确认机构用于 CMR 的对比剂品种和剂量（是否 0.1 mmol/kg）。
3. 若稿子要用随访时长论证 NSF 风险，需要另读 Woolen 2020（JAMA Intern Med）。
4. 把稿子当前版本放进仓库，我好对照原句和上下文做最终改写建议。

信息来源：According to PubMed / PubMed Central；全文经 Europe PMC。
