# Cine-CMR 唯一基线科学与结构审计

审计日期：2026-10-11。状态：**审计完成，未改稿**。这是作者侧科学审阅，不是独立临床专家认证、系统综述认证或投稿批准。共 27 项：MAJOR 12、MODERATE 13、MINOR 2，未确认需要推翻整个综述的CRITICAL缺陷。严重性依对论证、证据及可读性的影响判定，未按词频或标点升级。

最先需要修正的是：图1比较对象错误；DLSS/aligned strain监督链混淆；图3/GA计数及未读即未报告的编码；历史检索与缺口结论不匹配。图4原始数值可以保留，但统计解释、径向描述和独立性须同步澄清。全文的核心问题仍成立：不同验证目标支持不同层次的区域功能论断。

## 1. 对象、实际工作与证据边界

唯一基线为 `/mnt/iusers01/fatpou01/bmh01/f12147zh/codex-slurm/cine-review-astra-20261011/inputs/cine-cmr-review-v10-120fa02-agarwood-figures`，原ZIP SHA-256为 `a17cb575bca448c3fc6d1b71f2980e64263bec595d2278cb29bb35a0fbad14b8`。输入252文件和工作稿249文件均按开始时清单逐一复核，内容无变化。独立审计Git在`review/.git`，起始revision `3f5b6d10cee3e481f8a5cb086ea897a6a4c58e16`。本报告引用的TeX行号为本次未修改源码行号，不是PDF行号。

已完整阅读main.tex、body.tex、supplement.tex、references.bib、全部caption、4个主表、3个编号补表和2个补充note表；读取135条claim、40行方法矩阵、17条旧atomic ledger、10行cohort linkage、94行历史metadata、134条registry、18条query log、23条near-neighbour及140个存档Markdown笔记/报告。笔记里的全文路径缺失时，只计为读到笔记，不能计为读过论文。全部9个独立图件已目检；56页PDF已渲染并看过全部contact sheets，另放大检查主文p5/8/15/17/19、补充p8/12；其他图以独立图件视图审查。contact overview不是每页逐字目检。

本次新取并阅读关键段落的原始论文包括MRXCAT2.0、Militaru、Cao、Kihlberg、Wehner、StrainNet、Jahromi、Strain-8、REGAIN、Bello、Mukherjee和STRAUS；STRAUS为作者站PDF，另读Stanford/DataCite、STRAUS和CMAC官方页。独立引用审计另读DLSS、aligned strain、MyoNet、Tsuneta相关全文段及近期方法摘要。具体读到何处见claim_evidence.csv，不声称全部94篇全文或全部补充材料已逐字审核。

独立引用表覆盖94条：87个Crossref DOI记录、6个官方记录已取得，1个MRXCAT代码仓库受反机器人页阻挡。三种Crossref查询实际282次中276次限流，之后串行DOI重试取得身份记录。子审计58项详细论断标NOT_FULLY_AUDITED，root另补查其中部分核心来源；这不等于58条引用错误，也不能把它们称为全文已验证。原文访问失败、身份不匹配、未观察到某结果、和原文直接矛盾严格分开。

交叉阅读发现的“没有报道”不能自动作为原文遗漏：本审计将这种不确定性本身列为可关闭问题。完整审计指完成所给稿件/图表/记录的检查和中心论断查证，不是宣称每篇来源的每个细节均已认证。

## 2. 应保留的、有证据支持的优点

1. **主问题与文章类型一致。** 引言把global、regional与focal分开，§4以验证目标组织证据，适合critical narrative review；不需要转成算法论文或完成benchmark。
2. **图2反例成立在所声明的范围内。** 相同轮廓可有不同角向对应；它没有将解析曲线冒充数据。应保留“只证明mask不足”的限制。
3. **StrainNet拆分实验的写法基本准确。** 305/243/62、670/190、59cine及DENSE-input EPE没有混为同一个测试；新增LoA和内部拆分语境即可，不应删掉正面结果。
4. **临床与技术验证已经分开。** Kihlberg scar discrimination、Bello outcome、scan–rescan precision未被整体当作材料运动真值。局部标签错误修正后，这条论证可保留。
5. **资源描述重视分母和适用范围。** STRAUS的3模板/18合成病例、Stanford的51/55、CMAC稀疏点与MRXCAT generator的区分有价值；新查证总体支持这些边界。
6. **方法覆盖不只有限制。** 文本讨论multi-view、mesh、temporal、supervision和physics的实际结构；§6验证计划明确未来性质，S3图区分训练与推理控制。应在修订中保持。
7. **源码和图件可维护。** 未改TeX可重编译，无未定义引用；当前图件可编辑，未发现必须因栅格格式而否决的医学图像问题。

## 3. 实质性替代解释

- 弱径向一致性可能同时来自边界/partial volume、应变定义、参考DENSE或tagging误差、数据域与估计器；不能把全部差异归因于cine信息不足或regularisation。
- MRXCAT不同分量平均误差不同，是特定生成域的结果；同一源文将心肌纹理移除，且TextNet与DeepStrain共享ACDC来源，这些条件影响外推，但不构成已证实的泄漏。
- 高ICC可伴随较大个体LoA；有用预后信号可伴随运动偏差。两者不互相否定。
- 表S3在局灶列大量NR也可能反映原论文目标不同和综述阅读深度不足；不能全部当成研究失败。
- 图2角向例子不施加所有生理约束。额外图像线索/物理约束可能减少其歧义；它证明轮廓不足，而非cine永远不可辨识。
- STRAUS/Mukherjee确有已知运动和区域病理/敏感性设计；这支持研究建议具有先例，但不自动证明已完成本综述要求的固定估计器、graded focal attribute恢复。

## 4. 逐项问题与关闭条件

MAJOR：改变核心科学解释、缺口依据或关键证据可读性。MODERATE：影响具体研究/终点/设计/声明的准确性。MINOR：不改变中心结论的结构或书目维护。所有问题当前均OPEN_AUDIT_ONLY；建议不是已经完成的修改。

### AUD-001 [MAJOR] 图1把厂商间ICC标成对tagging的一致性

**准确位置**：`body.tex:36`；关联：Figure 1b; body.tex:234; supplement.tex:199; fig1_two_track_journal.py。

> vendor range of cine feature-tracking ICC against tagging

**证据**：本次读Militaru原文Global LV Strain及摘要：LS 0.92–0.94、CS 0.88–0.91确为各FT对tagging；RS 0.10–0.81是FT厂商间范围。原文另报cvi42对tagging 0.63、Segment对tagging 0.48。图1把三行置于同一cine FT vs tagging标题下。（CE-003）

**影响**：比较对象错误，改变读者对径向参照一致性的理解；不是小数或排版问题。

**建议修正**：分开FT–FT与FT–tagging，或去掉无法统一比较对象的RS范围；表2和S1明确intervendor。

**验收条件**：图源、PDF、图注、表2/S1及证据台账每一ICC均写明双方，且与原始结果对应。

**替代解释/保留项**：径向方法差异大的总体结论仍获支持，不应据此否定全部FT。

### AUD-002 [MAJOR] 图4以SD重叠推断不排序的统计逻辑不成立

**准确位置**：`body.tex:202`；关联：body.tex:197; Figure 4b; captions_and_alt_text.md。

> per-case standard deviations overlap, so no case ordering is implied

**证据**：MRXCAT全文及本次目检原始Figure 14：原图为不同指标的箱线图，未展示正式病例间检验；总体径向误差−0.24±0.21与梗死−0.20±0.21不是两个独立组。原文称梗死最低表现但该单一数值不能支撑径向误差排名。图件已改成No between-case test was reported，正文/TeX图注未同步。（CE-001; CE-002）

**影响**：重叠SD既不证明无差异也不证明等效；无显著性检验也不禁止描述性比较。

**建议修正**：保留原始数值，说明来源叙述与单一汇总数字不足以建立统一排名；删除SD重叠的推论；描述不同指标有不同表现。

**验收条件**：全文和图内不再以SD重叠或未检验推出相同/等效；明确Figure14三层中室SAx均值及无scar-level误差。

**替代解释/保留项**：原图确实显示梗死Dice较差，但位移误差并非同一排序；不得把某指标的低表现推广到全部指标。

### AUD-003 [MODERATE] 图4径向“largely abolished”与残余幅度不匹配

**准确位置**：`body.tex:195`；关联：body.tex:195,202; Figure 4a; editable captions。

> radial and circumferential strain are largely abolished

**证据**：原始峰值径向0.95→0.30，即下降约68.4%、保留约31.6%；周向−0.18→0.01才接近零；纵向−0.18→−0.17。当前图内及独立caption draft已用markedly reduced，TeX仍用abolished。（CE-001）

**影响**：把明显下降写成近乎消失，掩盖分量差别，且多版本互相冲突。

**建议修正**：分别写径向明显降低、周向接近零、纵向近似保持；数值单位/应变定义依原文，不强行改作Green–Lagrange。

**验收条件**：正文、图注、图源、摘要相关概括及alt text一致；保留所有原始值，计算百分比若采用需明确为本次算术而非原论文统计。

**替代解释/保留项**：“largely”可能指大幅减少，但图4强调属性差别，精确分开表述更合适。

### AUD-004 [MAJOR] DLSS监督来源错分，AUC被错误绑定到阈值

**准确位置**：`supplement.tex:343`；关联：body.tex:174; Figure 1b; Figure 3; Table S3:343。

> Cine; supervised on radiologist wall-motion reference

**证据**：独立核验读DLSS全文方法/结果：训练参照为配准的4D-flow心肌速度及分割（223 examinations/219 patients）；53人846节段的四读者共识为临床评价参照。AUC=0.90描述ROC，30%峰值径向应变阈值对应敏感度86%、特异度85%、准确率86%。（CE-011）

**影响**：混淆学习目标与评价目标，破坏§3.6分类；AUC不属于一个固定阈值。

**建议修正**：分别列训练输入/监督与推理输入/评价；拆开AUC与阈值操作点，更新分类数据。

**验收条件**：body174、S3、图1数字上下文及图3分类同步；不再称DLSS由读者标签训练。

**替代解释/保留项**：其临床评价仍不能证明稠密材料运动准确；这个合理边界不能作为误写训练机制的理由。

### AUD-005 [MAJOR] Aligned strain运动学习与下游LGE分类被混合

**准确位置**：`supplement.tex:347`；关联：body.tex:174; Table S3:347; Figure 3。

> Cine; supervised, LGE-defined fibrosis reference

**证据**：独立核验原文DL Pipeline/Figure3：关键时相检测、分割、SSIM+smoothness+Dice形变估计、LGE定义的患者分类是不同环节。57人开发、82人同中心时间留出；主要分类判定患者是否含≥1个LGE阳性节段。（CE-012）

**影响**：把LGE写为运动场监督，且“detect fibrotic myocardium”易被解读为瘢痕空间定位；相对百分比缺比较对象。

**建议修正**：按流水线解释真实损失与分类标签；明确患者级终点、同中心留出、balanced accuracy及比较对象。

**验收条件**：正文/S3不再暗示LGE监督运动或验证scar boundary；139=57+82保持；相对改进有分母或改绝对值。

**替代解释/保留项**：组织标签为有价值的下游验证，不能因其非运动真值而贬为无效研究。

### AUD-006 [MAJOR] 图3/图形摘要材料敏感计数及总体分母不自洽

**准确位置**：`body.tex:183`；关联：body.tex:178,183; Figure 3a/b; Graphical abstract; table_s3_methods.csv。

> appear in 14 of 48 entries

**证据**：CSV计数22 mask+8 label+14 material+1 focal+3 NR=48；各泳道material-sensitive计数相加为15，因focal也有known-motion参照。标题14/48却未限定为nonfocal。48混有一般配准起源、tagging对照方法、foundation models和同一方法独立评价，且合并/拆分单位不同。（CE-018）

**影响**：“多数方法缺少材料验证”的量化印象可能被分类和选择单位驱动；图形摘要重复传播。

**建议修正**：定义entry单位与包含范围；将cine方法、相关方法和独立评价分层；材料敏感总数含focal或明确互斥定义；逐行重审后重算。

**验收条件**：S3行到48点的映射可追踪；所有泳道、柱图、图例、主文、GA总数一致；不把选择性叙述样本当领域普查比例。

**替代解释/保留项**：时间线作为所选文献地图很有用，问题在统计解释，不必删掉方法史。

### AUD-007 [MAJOR] 未读/未核验被写成原研究未报告

**准确位置**：`supplement.tex:245`；关联：body.tex:178; Table3 caption body253; TableS3; Figure3 legend。

> NR means the source does not state the item

**证据**：TableS3含metadata-only INR、abstract-level多行，无法断言全文未报告。Table3把not inspected定义为study did not evaluate，另有Gao abstract-depth行；图3将INR/low-rank/CMR foundation列成validation data not reported。CMR foundation实际上报告其他任务验证。（CE-018; CE-025）

**影响**：将访问限制变为文献缺陷，系统性削弱先前研究并强化缺口。

**建议修正**：区分not assessed by this review、not reported in inspected abstract、not a target of study、confirmed absent in full text；无全文者不作否定性编码。

**验收条件**：每个NR/absence cell有访问深度和可定位依据；图3不以metadata-only判定无验证。

**替代解释/保留项**：摘要不含某终点可以记录，但不能作为原研究不存在该实验的证据。

### AUD-008 [MAJOR] 历史筛选数量与停止规则缺少可复查原始记录

**准确位置**：`body.tex:23`；关联：§1.1; supplement:37–51; supplementary/historical/search-record.md; main.tex:88。

> The query strings, hit counts and screening record are given in the Supplementary Methods.

**证据**：18条查询日志确实存在，返回数求和281；历史253唯一、21保留、232排除、9Sept补2条是继承断言。所指search/gap_2026-09-01/screening.csv、原始导出、两个检索/筛选脚本及independent-review包在本基线缺失。citation-expansion逐轮记录也不在包中。（CE-023）

**影响**：不可复现去重与纳入决策；“record given”和“reproducible export”超出实际交付证据。

**建议修正**：保留日期与历史身份，准确列已存/缺失文件；作者若能恢复原始记录再核对，不能用本次检索冒充历史重建。

**验收条件**：历史计数标为reported/inherited且出处清楚；恢复则逐记录重算；不恢复则删除可复现/完整screening可用的强断言。

**替代解释/保留项**：叙述综述不必伪装系统综述，也不机械要求双人筛选；要求是如实描述实际程序。

### AUD-009 [MODERATE] 截止日期与10月核查/新增来源需拆开

**准确位置**：`body.tex:21`；关联：supplement.tex:37–51; source registry; crossref_verification_20261009.csv; references.bib。

> The third step, completed on 8 October 2026

**证据**：结构化搜索1Sept cutoff，3Sept执行，9Sept同cutoff补充；稿件第三步8Oct完成，但台账及source notes标9Oct。Jahromi 15Sept、IG-BiReg 5Oct等可来自定向补充，不能归入1Sept集合；10月实际查询/纳入日志不完整。（CE-023）

**影响**：读者无法知道当前94条来源何时以何种路径纳入，阅读深度声明也可能引用旧状态。

**建议修正**：分历史有界检索、10月定向更新、本次11Oct审计三条时间线；不擅自更改旧执行日期。

**验收条件**：每条post-cutoff来源有加入路径、记录依据/未知标志；本次新增检索单独addendum，无假定筛选人数。

**替代解释/保留项**：出版截止与访问日期不同本身不是错误；问题是更新集合没有交代。

### AUD-010 [MAJOR] 复杂联合设计未检出不能证明较简单设计未检出

**准确位置**：`body.tex:206`；关联：body.tex:206; historical bounded conclusion; near-neighbour NN21。

> did not identify a study that varied abnormality size, severity or transmurality

**证据**：历史检索结论同时要求prescribed abnormality、acquisition/prior perturbations、预设estimand、regional distortion和selective performance；现文只要求变大小/严重度/透壁度且固定估计器。没有交集证据不推出没有其中子集。NN21甚至继承了size/amplitude等yes标记。本次读Mukherjee原文发现实际敏感性为分辨率/噪声，孤立梗死是未来扩展，未据此证明反例。（CE-019; CE-023）

**影响**：中心研究缺口比已执行搜索能证明的范围更宽；“only one”受选择性覆盖影响。

**建议修正**：重审near-neighbour各列，以实际操作性标准限定未检出结论；把one写成所读集合中identified example，避免领域唯一性。

**验收条件**：每个必要条件有paper-level判定依据；任何否定性结论绑定实际查询、cap、日期、读源范围；无法证实则改为研究优先项。

**替代解释/保留项**：现有证据仍表明需要属性特异的局灶验证；无需靠绝对新颖性来成立。

### AUD-011 [MAJOR] 式3不宜声称覆盖几乎所有估计器

**准确位置**：`body.tex:118`；关联：body.tex:126; Figure1a; Table1。

> Almost every estimator reviewed below can be written as, or interpreted through, the objective

**证据**：式3只有image similarity+regularisation；StrainNet采用轮廓到位移的DENSE监督，DLSS采用4D-flow监督，结果预测具有不同标签损失。Table1已写label loss，和§3.1的全覆盖描述不一致。（CE-009; CE-011; CE-012）

**影响**：把训练监督、推理求解和图像匹配统一成错误的数学目标，削弱方法解释。

**建议修正**：将式3明确为配准类说明例；区分监督风险、先验/表示与推理映射；保留forward/backward约定说明。

**验收条件**：举例涵盖配准、监督轮廓模型、物理约束和下游分类，不强加同一优化式。

**替代解释/保留项**：可保留“信息加假设”的共同抽象，但不能将抽象相似写成相同损失函数。

### AUD-012 [MODERATE] 三种失败归因需允许耦合，投影误差需定义

**准确位置**：`body.tex:130`；关联：body.tex:130,309–319; Figure1a each testable alone; Figure5。

> the limitation was the estimation process

**证据**：固定图像调整alpha的成功提示正则/估计贡献，但不能排除信息欠定；投影已知位移的结果依投影范数、边界、分辨率和应变导数而异。文中只给重采样一项条件性解释。（CE-020）

**影响**：把诊断性试验写成排他因果归因；可能使推荐验证程序产生过强结论。

**建议修正**：把if-then改为有控制条件的支持性归因，明确位移/应变空间、投影和可同时存在的因素；保持训练alpha要重训的S3说明。

**验收条件**：不写成功调整alpha即排除其他因素；投影指标与最终estimand匹配；计划仍是计划。

**替代解释/保留项**：这种分解作为组织工具有价值；图2仅证明轮廓不唯一，不能证明全部cine信息都无法辨识。

### AUD-013 [MAJOR] Jahromi等效性的预设性和统计单位表述过强

**准确位置**：`body.tex:216`；关联：body.tex:216,244; supplement.tex:207; cohort linkage。

> within a prespecified margin of 3.5

**证据**：本次原文统计/结果：chosen/selected 3.5 percentage points；未找到注册/方案证明prespecified。40健康人两中室切片，主要比较是slice-wise peak median systolic endocardial Ecc；差值−2.7pp且差异检验显著，可同时通过TOST。重复切片的聚类处理不能由现有描述确定。S1仍写numerical limits NR in inspected abstract。（CE-010）

**影响**：强化了等效性研究设计，并使整层健康者结果可能被误读为区域材料运动等效。

**建议修正**：去掉未经证实的预设性；写±3.5pp、具体estimand及均差，保留健康/中室/模型限制；说明聚类处理未明；统一S1访问深度。

**验收条件**：原文、主文、S1、ledger数值与单位相同；不把不显著/TOST变成临床可互换或focal等效。

**替代解释/保留项**：DENSE模型亦有误差，某方向差异不必全部归为cine偏差；不能无证据声称有数据泄漏。

### AUD-014 [MODERATE] 图1概念牛眼图的异常节段标签错位

**准确位置**：`figures/editable_sources/src/fig1_two_track_journal.py:111`；关联：Figure1a; body.tex:36; segment numbering loop str(7+i)。

> segs = [-0.18, -0.19, -0.17, -0.08, -0.20, -0.18]

**证据**：源码依序标7–12，最弱−0.08位于第四个即10；图中却写seg11 reduced，后一站seg11曲线为另一个概念构造。五个曲线读数是计算示意值，并非研究观测。（CE-021）

**影响**：测量链同一节段的视觉追踪不一致，即使是概念图也会误导。

**建议修正**：对齐数组索引、牛眼编号、异常色块、seg11曲线与caption；所有示意数值保持conceptual/computed标签。

**验收条件**：视觉检查异常块确为11；读数由对应曲线计算可重现；不用概念数值充作外部证据。

**替代解释/保留项**：不要求牛眼所有数值等于任一时相，但同一异常节段身份必须一致。

### AUD-015 [MAJOR] 最终PDF图件字号低于源文件声明的可读尺度

**准确位置**：`body.tex:35`；关联：全部5主图和3补图；main p5/6/15/17/24; supplement p3/4/5。

> \includegraphics[width=\textwidth]{Figure_1_two_track_evidence_map.pdf}

**证据**：主文A4减两侧25mm=160mm；图源宽190mm，缩放0.8421。PDF提取实际最小字：F1约5.44pt，F2约5.21pt，F3–5约5.95pt；补充版心166mm，S1约5.88pt、S2/S3约6.17pt。独立图与插图页面均已目检。（CE-022）

**影响**：核心证据、标签和比较对象在完整页面难读；源图190mm字号审计通过不能证明正文可读。

**建议修正**：在现有agarwood风格下做160mm/166mm可编辑导出版，减少面板内长句、增加字号/拆面板，必要时独立图页；不任意改变全稿边距。

**验收条件**：最终插入PDF按实际缩放测字体并目检；建议普通标签≥7pt、次级数学下标≥6pt作为本任务QA目标，非本次已认证的JCMR硬性规则；无裁切/重叠。

**替代解释/保留项**：画面是可编辑矢量，保留原资产可用性很高；栅格医学影像本身不是缺陷。

### AUD-016 [MODERATE] StrainNet正面证据应同时呈现绝对一致性和验证范围

**准确位置**：`body.tex:170`；关联：body.tex:170; Table2:238; TableS1:203; Figure1b。

> ICCs were 0.87 versus 0.72

**证据**：原文支持ICC改善、243/62人、670/190sections、59人cine子集和DENSE输入EPE0.75±0.35mm。cine Ecc的LoA：global −5.74至4.72pp，segment −9.16至8.07pp。研究按受试者内部拆分，源文明确缺少外部数据验证；cine mask有预处理/分辨率匹配。（CE-009）

**影响**：仅突出ICC不足以评估临床可容忍误差，且“独立test”易与外部验证混淆。

**建议修正**：保留数字与已正确分开的DENSE/cine实验，增加关键LoA、内部留出与输入处理；不要要求新实验。

**验收条件**：高ICC与绝对误差并列、59不算另一独立cohort、不把DENSE EPE移到cine；临床容差未验证须明示。

**替代解释/保留项**：这是重要的支持性结果；较宽LoA不推翻学习改善一致性的事实。

### AUD-017 [MODERATE] Bello结果缺少右室/PH及内部校正语境

**准确位置**：`body.tex:174`；关联：Figure1b; supplement.tex:333。

> a human benchmark of 0.59 in 302 patients

**证据**：原文302名incident pulmonary hypertension，右室运动表征预测生存；0.75/0.59为bootstrap optimism-corrected C，比较对象是人工测得容积/功能变量模型，不是医生直接预测的读者试验。（CE-008）

**影响**：容易将RV/PH外推为LV局灶准确性，或把human benchmark理解为临床读者胜负。

**建议修正**：写明PH/RV、内部bootstrap和常规人工容积指标模型；保持预测性能与效用区分。

**验收条件**：图1、正文和S3统一人群/心室/终点/验证方式；不声称外部效用或LV瘢痕恢复。

**替代解释/保留项**：结果确有较高预后区分能力，不能因其不是运动真值而淡化其实际贡献。

### AUD-018 [MODERATE] Kihlberg所引用ROC终点为end-systolic

**准确位置**：`supplement.tex:201`；关联：TableS1:201; Figure1b; body.tex:236,285。

> strain and torsion; peak systolic

**证据**：原文Figure6及结果将所引AUC0.87/0.83/0.66、80%特异度时82/71/35%敏感度对应end-systolic segmental circumferential strain与>50%透壁LGE。116人中34人有符合阈值瘢痕。（CE-007）

**影响**：peak/end-systolic是本综述强调的estimand差别，表内不能混写。

**建议修正**：把被引用ROC的具体方向和时相明确到cell/图注；不把所有strain/torsion合成同一指标。

**验收条件**：S1、表2、图1和claim ledger对同一数字均用同一终点；LGE仍是组织参照。

**替代解释/保留项**：数值转录正确，错误在终点标签。

### AUD-019 [MODERATE] MyoNet应说明二值分割输入与tagging-derived监督

**准确位置**：`supplement.tex:349`；关联：body.tex:172; TableS3:349。

> Cine (rat model); supervised against sine-wave-modelling reference

**证据**：独立核验全文Figures1–2/Table2：cine分割形成binary spatiotemporal images，位移监督由配对tagging的SinMod获得；不是泛指灰度cine直接预测。ICC0.973/0.975和大鼠放射损伤范围获支持。（CE-013）

**影响**：真实输入的约束丢失，使与StrainNet/直接图像模型的比较失真。

**建议修正**：补输入处理及tagging来源，保持rodent非human限定。

**验收条件**：输入、监督、推理及评价目标分列；不给未读实验添加人类泛化。

**替代解释/保留项**：源研究可支持架构路线，不能凭animal数据声明临床准确。

### AUD-020 [MODERATE] Portal距离图配置与EPE数值混配

**准确位置**：`supplement.tex:313`；关联：body.tex:152; TableS3:313。

> EPE 1.02~mm versus 1.19~mm

**证据**：本次独立读原始摘要：基础半监督1.02mm vs RAFT1.19mm；加入ED distance map后0.95mm，完全监督0.91mm。当前cell把distance weighting和1.02连成同一配置。（CE-014）

**影响**：无法判断改进来自何种设置，也遗漏研究实际成功。

**建议修正**：将配置逐项配对；若正文精简只保留最终加权设置，应同时说明参照与abstract-level限制。

**验收条件**：摘要能逐项回查数值配置；无全文不得新增baseline公平性或focal评价结论。

**替代解释/保留项**：参考位移的具体生成仍需全文核验，摘要可证数字配对但不能证明生物运动真值。

### AUD-021 [MODERATE] Buoso三维tagging的在体验证被漏掉

**准确位置**：`supplement.tex:337`；关联：TableS3:337; Figure3 tagging comparator class。

> Synthetic 3D tagged images with analytic signal model (abstract level)

**证据**：新读原始摘要除合成实验，还报告external in-vivo human及porcine与人工tracking比较；当前“Reported data and validation”只列synthetic。（CE-015）

**影响**：方法证据显得比原研究薄弱，违反平衡覆盖。

**建议修正**：加入已报告的在体验证及人工参照，仍标tagging comparator、abstract-depth。

**验收条件**：S3和分类理由包含正面在体结果，不把它误记为routine-cine验证。

**替代解释/保留项**：人工追踪仍有误差且不是独立物理标记；两点可同时陈述。

### AUD-022 [MODERATE] 研究独立性应按开发者、数据和评价队列拆开

**准确位置**：`body.tex:195`；关联：body.tex:195; Figure3/4/abstract; COHORT_DATASET_LINKAGE.csv。

> which is independent of the DeepStrain developers

**证据**：MRXCAT原文明确TextNet与DeepStrain均用ACDC；开发团队不同不等于外观域/训练资料完全独立。Jahromi全文又明确健康数据属于Stanford repository的一部分，而继承linkage表仍说exact repository linkage not asserted。STRAUS18来自3templates；CMAC15为多论文重复使用基准。（CE-001; CE-010; CE-016; CE-017）

**影响**：可能累加相关数据为独立验证，或漏报已可确认的资源关联。

**建议修正**：保留外部团队评价的事实，加数据域共享；按资源/人/切片/任务分母登记；Jahromi更新资源级关联，subject级对应仍未文件核验。

**验收条件**：四种独立性分别表述；不凭ACDC共享指控泄漏，也不凭资源描述声称完整配对人数。

**替代解释/保留项**：Stanford 51healthy/55total不是矛盾数据集，应保留页面范围差别。

### AUD-023 [MAJOR] 当前94文献与135条历史claim ledger未充分对齐

**准确位置**：`body.tex:23`；关联：evidence/codex_claim_ledger_135.csv; method matrix; source_registry; S3。

> The evidence ledger states the depth for every cited source

**证据**：135条旧claim共69个citekey，75full_text/56abstract/4official；历史69与现行94集合不同，存在key别名。多数source_locator为缺失sources文件的line1，evidence_excerpt是标记过的释义而非原文定位。独立本次身份检查不等于每条细节核验。（CE-025）

**影响**：精细阅读声明缺可追踪证据；将历史AI_checked当新鲜全文核验会造成假保证。

**建议修正**：创建现行引用—论断—原文段/表/图的映射，区分本次primary、继承、metadata-only和access failure；核心否定论断优先补读或收窄。

**验收条件**：每个强数值/机制/absence论断有相称深度和精确定位；所有94身份行保留，无法核验的详细cell明确suspended。

**替代解释/保留项**：原台账主动标paraphrased和human_pending是优点，应保留而非伪装直接引文。

### AUD-024 [MODERATE] AI/来源声明与数值重绘、现行包不完全一致

**准确位置**：`main.tex:103`；关联：main.tex:103,106; submission_materials; editable README/FIGURE_CONTRACT。

> no patient image, published figure or experimental result is reproduced

**证据**：图1/4重绘已发表结果数值，未复制第三方图像；“no experimental result reproduced”易否认数值来源。main106仅点名MRXCAT和S3，却图1还有Militaru/Cao/StrainNet/REGAIN/Kihlberg/Bello/DLSS。旧compliance仍51refs/3figures/10supp pages/drawio，与当前94refs/5main+3supp/20pages/SVG不符。Figure contract还说F1 Typst，实际journal版Python。（CE-026）

**影响**：作者无法据同一组声明确认实际来源、工具和交付物；历史版本断言可能被误当当前认证。

**建议修正**：分原创示意、解析计算、已发表数字重绘；逐图列来源；将旧状态文件明确归档，未来最终声明只反映现包。

**验收条件**：图1每组来源和工具可定位；权利/AI/作者签署保留pending；不得代填资助、COI、同意或作者身份。

**替代解释/保留项**：程序重绘不同于复制论文版式/患者图像，旧Kaggle/Wehner影像许可问题不能自动套到当前纯示意图。

### AUD-025 [MINOR] 少量书目信息和时间线年份需要维护

**准确位置**：`references.bib:343`；关联：Fourier-Net+ entry; S3 Morales comparison year; Figure3 year。

> pages = {1--15}

**证据**：本次Crossref正式页为37(10):5712–5726；Morales comparison 2023卷期与2022online可同时成立，需统一时间线口径。94条未发现可据证据判为不存在；MRXCAT repo被反机器人页面阻挡。（CE-027）

**影响**：可检索性/时间线一致性问题，不影响主要数值结论。

**建议修正**：采用当前正式卷期；注明online-first口径；保留技术key。

**验收条件**：只修改有原始元数据支持的字段；不把Crossref不全当题名/作者造假。

**替代解释/保留项**：Smiseth长题、Goetze2026、Tsuneta article code有支持，不要过度修正。

### AUD-026 [MINOR] 结构性重复与表图密度削弱综合论证

**准确位置**：`body.tex:189`；关联：§2/§4/§5/§6/§7/§8/§9; all captions; Table2/3/S1。

> No single study can answer every layer of the measurement chain

**证据**：全读后可见reference cannot establish alone、matching estimands、global not regional在多个结尾重述；§4已有实证，§5/7/8/9部分返回同一一般限制。主文36页、S1/主表密集；图1caption占大量页面。（CE-028）

**影响**：读者需反复读边界却较难提取方法机制与研究之间的解释关系。

**建议修正**：以§2定义、§3机制、§4实证、§5矛盾解释、§6建议为主线；S1容纳细节，主表呈现有区分度的结论；删除重复需逐条保留唯一证据。

**验收条件**：无固定缩短比例；技术细节与临床动机不丢；每段有新的证据/机制/推论；不强行六段引言或算法模块。

**替代解释/保留项**：核心框架清楚、非拼贴；这是精简与连接的改进，非推翻现有结构。

### AUD-027 [MODERATE] 候选期刊与图形摘要政策尚未得到可用的当前确认

**准确位置**：`main.tex:106`；关联：submission_materials/JCMR compliance; graphical abstract; author checklist。

> confirm the journal's current policy on AI-assisted programmatic artwork

**证据**：11Oct官方JCMR Guide for Authors请求403；Elsevier现行官方AI页面可读，区分解释图、数据图与primary research images，并对graphical abstract另有dedicated/professional illustration tools要求。程序SVG由AI辅助生成如何适用，不能自行认证。（CE-026）

**影响**：旧指南引文和“符合”断言不能替代当前栏目/图形摘要政策核实。

**建议修正**：记录官方URL、访问日期、失败状态与具体未决问题；作者侧确认稿不需等待投稿流程，更不得代发询问信。

**验收条件**：最终作者审阅状态单独列journal/rights pending，未认证字数/图数/摘要格式；无投稿或通信。

**替代解释/保留项**：AI-assisted code与直接生成图像应区分，但不能凭此宣布自动豁免。

## 5. 图1数值逐组核对与图4结论

图1所有已发表数值组均已核对：MRXCAT三组误差及EF/Dice/位移见CE-001；Militaru三方向ICC见CE-003（RS比较对象错误）；Cao .778见CE-004；StrainNet四个ICC见CE-009；REGAIN三个LoA和49人见CE-005；Strain8的20×8见CE-006；Kihlberg三个AUC、三个敏感度、80%特异度、116/34和50%LGE阈值见CE-007；Bello .75/.59/302见CE-008；DLSS .90/53/846/4readers/30%见CE-011。0.5是判别指标随机基准示意，非观察研究数据。图1a五个数由曲线计算，见CE-021。原文的数值和解释不能打一个统一的VERIFIED标签。

图4原始Figure14已实际打开：它不能消除源文“worst”与单一径向汇总数字的歧义，也没有提供瘢痕属性恢复的统计。可保留源值，不能从箱线/SD重叠推出等效；不能把case/slice均值提升为scar定位、范围或幅度误差。图内“未检验所以不排序”也应写得更精确。

## 6. 构建、视觉和未完成边界

未修改源码通过现有pdflatex+BibTeX脚本，在review/qa/baseline_build隔离输出主文36页、补充20页；未安装共享软件。最终log无undefined citation/reference、Overfull、Warning或Error，全部页面有可提取文本，字体嵌入清单在qa/audit_checks.json。static_qa只核查3TeX和2个其扫描路径内CSV，不能证明它覆盖全部evidence CSV或科学论断。全部输入与工作稿开始/结束SHA-256一致。

图像检查范围如§1；重要限制是最终字号偏小，未修图、未改稿、未重跑图源渲染链。未下载原始患者数据，未运行新合成/临床验证或训练。数学readout复算仅核对现有解析图。没有完成作者确认、版权/期刊解释或投稿。审计表和后续蓝图已完成，存在的来源/历史程序缺口已作为发现交付，不被隐藏为“验证通过”。

## 7. 文件索引

- issues.csv：27个稳定问题ID、精确引句、证据、影响、修正与验收。
- claim_evidence.csv：28个本次中心证据单元+135个明确标记的继承claim。
- coverage.csv：章节、表图、caption、原始记录、94个当前来源及中心论断的覆盖/深度。
- revision_blueprint.md：按依赖排序的修订方案；本轮不执行。
- SKILL_EXECUTION_LOG.md：实际读取的技能文件与适用/覆盖规则。
- independent_citation_audit_zh.md/.csv：独立引用核验及访问限制。
- retrieval_addendum_20261011.md：本次定向查询，绝不回填历史检索。
- QA_REPORT.md、FINAL_AUDIT_STATUS.md、SHA256SUMS：可恢复交接。

关键外部依据：[MRXCAT2.0](https://pmc.ncbi.nlm.nih.gov/articles/PMC10116689/)、[Militaru](https://doi.org/10.1186/s12968-021-00742-3)、[StrainNet](https://pmc.ncbi.nlm.nih.gov/articles/PMC10316292/)、[Jahromi](https://doi.org/10.1007/s10237-026-02120-3)、[DLSS](https://pubs.rsna.org/doi/10.1148/ryct.220202)、[Aligned strain](https://pmc.ncbi.nlm.nih.gov/articles/PMC12127955/)。其他逐项URL在claim_evidence.csv。
