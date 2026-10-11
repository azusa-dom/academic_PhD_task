# cine-CMR v10 只读科学审查报告

## 审查范围与版本

本轮审查的是批判性叙述综述 **From routine cine CMR to regional myocardial dysfunction: Fidelity, validation and interpretation of motion and strain estimates**，按JCMR临床与技术读者评价科学内容。没有将其套作原始研究或系统综述，没有要求PRISMA、双人筛选、消融或新实验，也不输出分数、录用等级或录用概率。

阅读基准为当前包的主文PDF（36页）及补充PDF（20页），当前manuscript源文件只用于定位和解释。主文各节、摘要、结论、声明和参考文献，以及补充Methods、Notes1–8、全部图表及图注均已读。全部5幅主图、3幅补充图、主表1–4、补充表S1–S3及Note5/8的表格已目视当前PDF渲染；另查看graphical abstract。没有重新编译或修改任何输入。

本轮重新提取PDF文本并对关键意见所在段落、数字和图注核对当前源文件，未在这些定位处发现主文PDF与当前源文件实质性不一致；这不是对全部源码与PDF的字节级等价认证。Figure4的图内文字与图注解释不一致列为A05，属于当前稿内部不一致，不是两个版本混用。

输入基准SHA-256：主文 `a9e9013044586e781d67c25b4d6a5f51942b5ddcf67121dcdc38100ad525e1fb`；补充 `119a0b69824403d1686912e7d341c5ec55952ebf1b2a1d05329d2dd3a33b3a83`。独立引用解析结果为主文93个不同key、补充81个、并集94个；补充独有`osman2000harp`，无未定义key。**94是实际引用并集，不是纳入研究数。** Figure3的48个entry、历史筛选的23条记录/22项研究及135个claim–source pair属于不同分母。

工作目录为 `/mnt/iusers01/fatpou01/bmh01/f12147zh/codex-slurm/csf3_v10_readonly_review_20261011_012543`；起始Git revision为 `26e47f323814e80ba9acaebc8671df4d2f5f6e54`，Slurm Job 22557312，在node911计算节点完成。启动器请求模型为gpt-6-astra、reasoning为high；本报告不把请求配置冒充独立取得的实际模型响应元数据。用户指定的五份技能说明已完整阅读并按“仅审查、无评分、非正式ARA”调整，详见[reading_log](/mnt/iusers01/fatpou01/bmh01/f12147zh/codex-slurm/csf3_v10_readonly_review_20261011_012543/audit/reading_log.md)。

## 作者实际问题、论点与证据基础

作者问的不是“cine能不能测strain”这个二元问题，而是在固定采集、输入、估计器及measurement definition后，异常的幅度、位置、范围和时间属性能够在多大证据边界内被恢复。文章把测量链拆成图像中的边界/强度线索、估计的材料对应、位移和导数所定义的strain，最后才是空间/时间聚合及临床解释。这个复述来自摘要和§1–2，而不是预先接受任务中的定位。

其主要论点有三层。第一，形状重叠和体积可以可靠，并不因此唯一确定内部材料点运动；同一掩膜的解析反例证明的是不唯一性，不是任何具体cine算法失败。第二，方法间差异必须结合输入、representation、prior、监督及完整estimand解释，不能把每个低于预期的局部结果都归因于cine信息不足或平滑。第三，known-motion、tagging/DENSE、scan–rescan、LGE、reader labels和outcomes检验的是不同对象；证据必须与主张尺度相匹配。

证据基础包括选定方法谱系、跨模态/跨产品比较、模拟与临床相关研究、重复性研究和数据资源。Table1提供方法比较轴，Tables2–3负责将验证端点映射回幅度、位置、范围和时间。当前稿明确承认：配对定义下的whole-slice/global/某些segment Ecc有正面支持，DENSE监督可改善segmental agreement，产品和方向间仍有差异。文章没有一概否定FT，也没有把缺乏focal边界误差报告写成cine必然无法表达该边界。

作者自己的贡献主要是概念整理与验证建议：区分capacity、estimation、input sufficiency，提出measurement contract和分阶段验证，把误差、参照不确定性、failure policy与临床用途连接起来。Figures2/5及补充解析示意不是新实验；所提容差和流程不是已验证临床标准、获监管认可规范或完成的benchmark。

## 值得保留的实质内容

**定义匹配做得具体。** §2与Supplementary Note1不仅说“不同软件不可互换”，还交代参考构型、strain度量、方向、层次、维度、求导和平滑、空间聚合以及peak与平均的顺序。这些因素确实决定比较对象，能帮助临床读者避免把定义差异认作算法错误。

**StrainNet的两项测试被正确拆开。** 当前稿将DENSE-magnitude contour下的位移EPE与普通cine contour下的ES Ecc比较区分，保留243/62及59人的正确分母。相关原文核查支持这一解释；不能把0.75mm宣传为普通cine像素位移误差，也不能因此抹去节段Ecc的正面结果。[StrainNet正式原文](https://pubs.rsna.org/doi/10.1148/ryct.220196)

**对验证参照的边界总体公平。** 正文将LGE判别、重复性和outcome association分别解释，并承认DENSE/tagging也受采集、分割、平滑和配准影响。Kihlberg的高透壁LGE判别与Militaru的跨产品应变比较可以并存，不能把两项结果硬拼成普遍优劣排名。对当前稿而言，这些正面结果不需要被反复加上“并未证明所有focal属性”才能具有价值。[Kihlberg原文](https://doi.org/10.1186/s12968-020-00684-2)

**MRXCAT2.0的关键外推边界正确。** 原始Fig14汇总中段SAX切片结果，当前稿没有把case/slice-average error误写成scar内误差；没有用该单一实验确定平滑、低维表示或训练域是失败原因。Figure4的局部统计措辞仍需A05修正，但不应因此否定整个实例。[MRXCAT2.0原文](https://doi.org/10.1186/s12968-023-00934-z)

**重建章节包含真实端点，而非泛论AI伪影。** REGAIN与CineVN的全球/切片应变比较，以及DENT的图像域端点，被用来说明重建与测量需联合评价。CineVN保留了残余偏差、患者缺乏传统参照和分割失败排除等限制；本轮相关原文核查支持这些限定。[CineVN原文](https://onlinelibrary.wiley.com/doi/full/10.1002/mrm.30260)

**数据规模的单位意识应保留。** 稿件区分模拟实例、共享模板、受试者、切片、像素和配对可用性，也没有把Stanford库总人数当作已处理的cine–DENSE真值对。本轮官方DataCite核查支持55=51健康+4主动脉瓣狭窄及元数据更新日期，但未检查受试者压缩包。[官方元数据](https://api.datacite.org/dois/10.25740/xt223hz2438)

## A 已确认的问题

已确认5项，其中A01、A02为major，A03–A05为minor。没有提出critical意见。这里的严重程度表示对本文论证的影响，不是稿件等级。

### A01｜将训练监督、运动模块和下游验证对象分开

**证据状态：confirmed；严重程度：major。** 直接影响按监督与验证对象组织的方法谱系，涉及两项核心实例；不是对原研究性能的否定。

**定位与检查范围。** 主文p13–14，§3.6，行418–427；p8–9，式(3)及行189–198；补充p13，Table S3的DL synthetic strain与DL aligned strain行。源文件：`/mnt/iusers01/fatpou01/bmh01/f12147zh/codex-slurm/csf3_v10_readonly_review_20261011_012543/inputs/cine-cmr-review-v10-120fa02-agarwood-figures/manuscript/body.tex:174（关联118–126）；/mnt/iusers01/fatpou01/bmh01/f12147zh/codex-slurm/csf3_v10_readonly_review_20261011_012543/inputs/cine-cmr-review-v10-120fa02-agarwood-figures/manuscript/supplement.tex:343、347`。短原文/缺失项：“supervised on a downstream label in place of motion”；S3：“supervised on radiologist wall-motion reference”；“supervised, LGE-defined fibrosis reference”。

**问题与依据。** 原始来源内容支持错误；训练目标与测试终点混淆。 Masutani 2023，DOI 10.1148/ryct.220202，正式PDF p2 Algorithm Development and Training Data、p3独立CAD测试：DLSS使用配准4D-flow心肌速度训练，读者共识用于独立评价。[原始来源](https://pubs.rsna.org/doi/10.1148/ryct.220202) 。Koehler 2025，DOI 10.1148/ryai.240303，正式全文Methods、Figs2–3：DeformReg使用图像相似性、掩膜与光滑性损失，LGE分类发生于后续ML模块。[原始来源](https://pubs.rsna.org/doi/10.1148/ryai.240303) 。本轮读取正式全文相关方法/图注/结果，非仅摘要；2026-10-11访问。

**对中心论证的影响。** 读者会误判cine网络获得了什么额外信息，也会把临床分类证据误当成整个运动流程的训练方式。修正后，下游AUC仍支持壁运动判别，仍不直接给出运动场误差。

**最小可行修复。** 分别记录训练输入、训练监督、运动模块损失、测试参照。将DLSS移到速度参照监督的相应讨论，保留读者AUC作为临床终点；将aligned strain拆成运动估计和后续分类阶段。检查式(3)“same objective covers…learning-based”适用范围：图像配准损失不能直接替代StrainNet/DLSS的参照标签损失。AUC0.90与30%操作阈值分开陈述，AUC不是某一阈值上的指标。无需新增实验。

**额外材料及反证条件。** 确立本意见不需要额外材料；若进一步比较监督质量，可读DLSS Appendix S1及aligned Appendix S1，但不据此假设独立测试具备材料真值。 正文写“evaluated against”本身正确，但段首和段末将整组定义为下游监督，S3又明确写成训练标签，不能由这个局部正确表述抵消。只有原文另有读者/LGE直接监督运动模块的证据才可能改变具体分类；已读方法并不如此。

### A02｜证据地图把未充分读取与未报告混在一起，材料参照计数也不一致

**证据状态：confirmed；严重程度：major。** 作为“published evaluation record”的定量综合，阅读深度、类别定义和计数的不一致会影响中心缺口判断；单独算术差异仅属minor。

**定位与检查范围。** 主文p14，§3.7，行428–439；p15 Figure3及图注；p20 Table3图注及Gao行；补充p2 Reading depth、p10 TableS3图注。源文件：`/mnt/iusers01/fatpou01/bmh01/f12147zh/codex-slurm/csf3_v10_readonly_review_20261011_012543/inputs/cine-cmr-review-v10-120fa02-agarwood-figures/manuscript/body.tex:178、183、253、262；/mnt/iusers01/fatpou01/bmh01/f12147zh/codex-slurm/csf3_v10_readonly_review_20261011_012543/inputs/cine-cmr-review-v10-120fa02-agarwood-figures/manuscript/supplement.tex:49、245；/mnt/iusers01/fatpou01/bmh01/f12147zh/codex-slurm/csf3_v10_readonly_review_20261011_012543/inputs/cine-cmr-review-v10-120fa02-agarwood-figures/manuscript/figures/editable_sources/data/table_s3_methods.csv`。短原文/缺失项：“strongest validation evidence each cited source reports”；“NR means the source does not state the item”；“14 of 48 entries”；Table3把“not inspected”定义为原研究未评价。

**问题与依据。** 证据状态编码与综合分母/类别不一致；并非已证明相关原研究实际上做过缺失实验。 当前PDF和可编辑CSV独立核对：48行分为mask22、label8、material14、focal1、NR3；各lane的material-sensitive计数含focal，合计15，而图标题/图注为14。材料参照包含known-motion的文字定义也应涵盖focal一行。DeepStrain/DeepTag的tagging-landmark验证被归mask，说明“参照是否材料敏感”与“空间密度/终点”被单轴折叠。当前补充Methods明确多数S3项只读摘要/元数据，但图注和NR定义升级为源文未报告。证据均为当前稿及本轮计数，无外部缺失性断言。

**对中心论证的影响。** 地图可用于描述所提取的证据，不能在读取不全的条目上确认整篇论文不存在某终点。14/48也不能与lane数字同时成立，更不能解释为48项独立临床研究的患病人群证据比例。

**最小可行修复。** 保留unknown/not assessed at available depth；对承担“only/mostly/not reported”推论的条目检查相关全文，否则限定为已检索部分。明确材料参照类型和终点密度是两轴，并说明为何合并/拆分entry。若保持当前分类，说明14不含focal；若总数包括known motion，则统一为15。同步图、图注、正文、graphical abstract；不要求为全部方法补做原始实验或把综述改成系统综述。

**额外材料及反证条件。** 统一计数不需外部资料；确认每项缺失终点需要该项全文/补充。完整读深映射见B01。 图注承认abstract/metadata、正文也说不是能力判断，这是重要限定，应保留；但不足以使“未读到”成为“source does not state”。若作者将NR严格改为在所读材料中未见，并统一类别，本意见大部分即可消除。

### A03｜全球径向ICC上限0.81来自FT软件之间，而非FT对tagging

**证据状态：confirmed；严重程度：minor。** 比较对象抄录不准确，抬高径向FT–tagging范围上限；不改变方向/产品依赖的总体结论。

**定位与检查范围。** 主文p5 Figure1“cine FT vs tagging, global”RS；p19 Table2 Militaru行；补充p8 TableS1 Militaru行。源文件：`/mnt/iusers01/fatpou01/bmh01/f12147zh/codex-slurm/csf3_v10_readonly_review_20261011_012543/inputs/cine-cmr-review-v10-120fa02-agarwood-figures/manuscript/body.tex:234；/mnt/iusers01/fatpou01/bmh01/f12147zh/codex-slurm/csf3_v10_readonly_review_20261011_012543/inputs/cine-cmr-review-v10-120fa02-agarwood-figures/manuscript/supplement.tex:199；Figure1图内文字对应当前插入PDF`。短原文/缺失项：“global RS ICC across vendors 0.10–0.81”及Figure1的FT vs tagging标题。

**问题与依据。** 定量结果的比较对象混用。 Militaru 2021，[原始来源](https://doi.org/10.1186/s12968-021-00742-3)，原始PDF p7 Global strain comparison，p11 Fig5c：cvi42–tagging .63，Segment–tagging .48，Tomtec–tagging .10；.81为cvi42–Segment。本轮取得全文并目视Fig5c，渲染audit/rendered/source_militaru_p11.png；访问2026-10-11。

**对中心论证的影响。** 读者会把跨产品相互一致性误读为对独立参照的一致性。

**最小可行修复。** FT–tagging用0.10–0.63，或逐产品列出；若保留0.81，应另列为FT–FT，并同步三处。无需重分析原始数据。

**额外材料及反证条件。** 不需要。 Table2单独“across vendors”可能包含FT–FT，但该行比较器写Tagging，图1标题明确vs tagging；不能靠这一歧义维持原数值。原文摘要的0.10–0.81本来就包含不同配对。

### A04｜Figure1将REGAIN跨方案一致性放进precision栏

**证据状态：confirmed；严重程度：minor。** 发生于中心导航图的证据类别，正文已正确限定，因此修复局部即可。

**定位与检查范围。** 主文p5 Figure1“Precision at the tested scale”；对照p26，§6.6，行711–722；补充Note7 p6–7。源文件：`/mnt/iusers01/fatpou01/bmh01/f12147zh/codex-slurm/csf3_v10_readonly_review_20261011_012543/inputs/cine-cmr-review-v10-120fa02-agarwood-figures/manuscript/body.tex:36（Figure1图注）、399（§6.6）；Figure1图内文字`。短原文/缺失项：precision栏中的“REGAIN vs GRAPPA”及49人LoA。

**问题与依据。** 测量重复性与跨采集/重建方案一致性的分类混用。 Yoon 2023，[原始来源](https://pubs.rsna.org/doi/10.1148/radiol.222878) ，Methods Model Evaluation / Image Interpretation，Results及Fig4：同一人分别采集GRAPPA与REGAIN，49人有全球应变分析，原文LoA为RS−7到6、CS−2到3、LS−3到3个百分点。正式全文相关方法、结果及Fig4图注已读；2026-10-11。

**对中心论证的影响。** 该LoA包含两种方案及重复采集的差异，不能隔离同一方法scan–rescan方差；与Strain-8同栏会使导航图损失正文已建立的区分。

**最小可行修复。** 将该实例标作跨方案agreement，或清楚区分同法repeatability与跨法agreement；保留原数值及正文reconstruction-plus-analysis解释。

**额外材料及反证条件。** 不需要；没有必要要求REGAIN补做scan–rescan来保留现有结果。 两方案确实是在同一人上重复采集，但同时改变方法不能单独证明任一方法精密度。正文§6.6正确，说明这是图内分类问题，不是全篇误解。

### A05｜Figure4图注不能用SD重叠推断不存在病例排序

**证据状态：confirmed；严重程度：minor。** 统计解释不严谨，但稿件不做病例排序的保守结论本身合理。

**定位与检查范围。** 主文p16，§4.1，行471–474；p17 Figure4图注；对照同图面板(b)的“No between-case test”文字。源文件：`/mnt/iusers01/fatpou01/bmh01/f12147zh/codex-slurm/csf3_v10_readonly_review_20261011_012543/inputs/cine-cmr-review-v10-120fa02-agarwood-figures/manuscript/body.tex:197、202`。短原文/缺失项：“per-case standard deviations overlap, so no case ordering is implied”。

**问题与依据。** 描述性离散度与正式组间比较混淆。 当前PDF图内/图注独立目视；MRXCAT2.0原文 [原始来源](https://doi.org/10.1186/s12968-023-00934-z) ，Results/DeepStrain evaluation及Fig14（原始PDF p8结果、p16 Fig14），已读相关全文。−.20与−.24是infarct病例与含该病例的总体摘要，并非两个独立组。SD不是均值不确定性的CI，也不能由其重叠排除差异。统计判断为本轮方法学分析；访问2026-10-11。

**对中心论证的影响。** 目前的限定容易被读成已做过无差异检验，削弱稿件对参考误差和统计边界的要求。

**最小可行修复。** 统一图内文字、图注与正文，以缺少可比较的病例级检验和聚合口径差异为理由，不以SD重叠推出排序结论。保留“不能据此量化病例优劣”的判断。无需新实验。

**额外材料及反证条件。** 若作者坚持病例排序，需要每例同口径原始端点、样本单位和比较方法；仅移除SD推理不需要额外数据。 面板(b)已有“No between-case test was reported”的较好限定，说明作者本意并非统计无差异；该解释不能使SD因果连接成立，但使本问题限于局部。

## B 需要原文或记录才能确认的问题

以下不是已认定的科学错误。B01是审查材料与主张可追溯性问题；B02只针对预先指定这个时间性断言。

### B01｜当前主张与历史检索/读深记录之间缺少可复核的完整映射

**证据状态：needs_verification；严重程度：major。** 影响“未发现某种设计”和“每条来源已说明读深”的可核查性；现有材料不足以判断这些声明真伪。

**定位与检查范围。** 主文p3，§1.1，行96–120；p10，§3.3缺失性表述；p17行489–492；补充Methods p1–2。源文件：`/mnt/iusers01/fatpou01/bmh01/f12147zh/codex-slurm/csf3_v10_readonly_review_20261011_012543/inputs/cine-cmr-review-v10-120fa02-agarwood-figures/manuscript/body.tex:21、23、148、206；/mnt/iusers01/fatpou01/bmh01/f12147zh/codex-slurm/csf3_v10_readonly_review_20261011_012543/inputs/cine-cmr-review-v10-120fa02-agarwood-figures/manuscript/supplement.tex:43、45、49；/mnt/iusers01/fatpou01/bmh01/f12147zh/codex-slurm/csf3_v10_readonly_review_20261011_012543/inputs/cine-cmr-review-v10-120fa02-agarwood-figures/manuscript/supplementary/historical/search-record.md`。短原文/缺失项：“The evidence ledger states the depth for every cited source”；253 unique /232 excluded；当前未发现固定估计器而改变异常大小/严重度设计。

**问题与依据。** 审查可及材料限制和检索结论的逻辑范围待核实，不指控作者未读或未检索。 本轮核算18查询的数据库命中数41/244/508与返回数281；矩阵23记录含MulViMotion两版本。135对ledger的75full/56abstract/4official与其自身一致，但69个key按DOI只映射当前94条中的61条；另有17行v9更新及其他notes，尚不能凭缺失key推断未阅读。历史记录引用的search/gap_2026-09-01/screening.csv及筛选脚本不在当前包中可定位文件清单。旧结论是异常+采集/prior扰动+contract+retention+selective等完整合取；“没有满足全部条件”并不自动证明当前较窄子条件的集合为空。已读现稿后才检查这些历史文件。

**对中心论证的影响。** 作者已经限制数据库、日期、cap和单人筛选，不能据此批评“非系统综述”。问题是读者目前不能从历史合取结论独立推出当前两项具体absence，也不能逐项确认读深账。

**最小可行修复。** 提供一个当前citation key/DOI–主张–来源定位–读深的映射及可用筛选结果，说明哪次核查按当前两个条件重筛。可以只提供决定性候选的核查记录，并进一步限定措辞；无需重做系统检索、双人筛选或补实验。

**额外材料及反证条件。** 当前版本读深主索引；去重候选/筛选决策表或其公开定位；对Fourier类cine验证及异常size/severity固定估计器两个具体问题的候选核对记录。 若在未纳入本ZIP的现有记录中已完成这些映射和较窄条件重筛，本意见即可关闭；若仅证明旧完整合取为空，则仍未解决逻辑缺口。未声称已有反例或全领域不存在此设计。

### B02｜Jahromi研究的3.5%界值是否预先指定尚无原文证据

**证据状态：needs_verification；严重程度：minor。** 等效性数值和方向有全文支持，待核实的是是否预先指定margin，不能把没有报告预注册写成事后选择。

**定位与检查范围。** 主文p18，§4.2，行522–527；补充p8 TableS1 Jahromi行。源文件：`/mnt/iusers01/fatpou01/bmh01/f12147zh/codex-slurm/csf3_v10_readonly_review_20261011_012543/inputs/cine-cmr-review-v10-120fa02-agarwood-figures/manuscript/body.tex:216；/mnt/iusers01/fatpou01/bmh01/f12147zh/codex-slurm/csf3_v10_readonly_review_20261011_012543/inputs/cine-cmr-review-v10-120fa02-agarwood-figures/manuscript/supplement.tex:207`。短原文/缺失项：“within a prespecified margin of 3.5%”；S1仍称“numerical limits NR in inspected abstract”。

**问题与依据。** 时间性修饰词证据不足；正文与补充读深状态不同步。 Jahromi 2026，[原始来源](https://doi.org/10.1007/s10237-026-02120-3) ，原始PDF p7 §2.5、p13–14 §3.2：结果写selected/chosen margin，3.5%下TOST成立，平均差−2.7个百分点；所读方法没有提供该margin预先制定的时点/依据。本轮读取相关全文，不由摘要推断。

**对中心论证的影响。** 读者可能把研究内选定的等效性界值当作预先论证或临床容差；不影响“特定健康中段心内膜Ecc在给定界值内等效”的事实。

**最小可行修复。** 核实协议/原始补充；若不能证实预先指定，删除该时间性修饰，只保留研究采用的界值。同步S1读深及可得数字，说明这是该研究的等效性条件，非通用临床阈值。

**额外材料及反证条件。** 只有保留prespecified才需时间戳协议、统计计划或作者明确原始说明；不要求新实验或作者向期刊询问。 存在尚未提供的预先计划会使该疑虑不成立；原文未说prespecified并不能证明post hoc。现稿其他位置已承认临床阈值不能通用，应保留。

## C 可选表达与结构建议

这些建议不计作已确认科学错误，也不要求作者按本轮建议开展实验。

### C01｜给表示空间投影检验补上目标误差的定义

**证据状态：optional；严重程度：suggestion。** 有助于把合理研究建议变成可执行检验；不把未开展未来实验当作综述缺陷。

**定位与检查范围。** 主文p9，§3.1，行208–219；p23，§6.2，行637–644。源文件：`/mnt/iusers01/fatpou01/bmh01/f12147zh/codex-slurm/csf3_v10_readonly_review_20261011_012543/inputs/cine-cmr-review-v10-120fa02-agarwood-figures/manuscript/body.tex:130、337`。短原文/缺失项：“projected directly onto the estimator’s function space…limitation lies in the representation”。

**问题与依据。** 未来验证建议的操作性与充分条件。 本轮解析检查audit/analytical_checks.md：位移L2投影最优与某个应变导数/幅度属性的最优不同；一次投影结果不佳不足以排除整个空间中其他参数匹配某指定属性。无需外部经验数据。

**对中心论证的影响。** 把capacity、estimation、input分开很有价值，明确投影损失可防止实际执行时再次错误归因。

**最小可行修复。** 说明投影的变量、范数、约束和判定属性；报告目标属性误差，并说明如何保证最佳近似或只给出下界/诊断性结果。匹配全部字段或仅一个属性应区别。

**额外材料及反证条件。** 不需要新资料；作者可给操作定义而非开展试验。 若作者所说projection本已定义为目标属性上的全局最佳近似，意见可关闭；现稿未给这一条件。更细采集同时改变离散化/训练域的限制正文已写，不再重复要求。

### C02｜在实际插入尺寸下改善主图小字阅读

**证据状态：optional；严重程度：suggestion。** 无明显遮挡或科学数值读不出的证据；目视发现的是整页阅读负担。

**定位与检查范围。** 主文p5 Figure1、p6 Figure2、p15 Figure3、p17 Figure4、p24 Figure5。源文件：`/mnt/iusers01/fatpou01/bmh01/f12147zh/codex-slurm/csf3_v10_readonly_review_20261011_012543/inputs/cine-cmr-review-v10-120fa02-agarwood-figures/manuscript/body.tex:35、61、182、201、353；对应插入的figure PDF`。短原文/缺失项：检查范围：全部主图/补充图及各面板、符号、图注，在当前PDF页中144dpi渲染。

**问题与依据。** 可选视觉易读性建议，不冒充实验或排版致命错误。 audit/rendered/和render_manifest.json；实际主文PDF文字对象有约5.4–7.1pt图内标签，Figure3密集条目与Fig1说明需放大。目视未发现明显裁切/遮挡，Tables1–4/S1–S3及补充图可辨。没有仅凭190mm源画布就判定失败。

**对中心论证的影响。** JCMR临床读者需频繁放大以核对核心证据；不改变科学结论。

**最小可行修复。** 作者后续可减少图内重复解释、增大最小标签、用图注承接长句，并重新检查实际版心尺寸；本轮不改图。

**额外材料及反证条件。** 若采用新的期刊版面，需在最终尺寸查看；当前判断不依赖未核查的期刊字体政策。 放大屏幕可读且未见遮挡，故不列major；若最终排版扩大图件，问题可自然消失。

### C03｜加强方法谱系与已验证端点的对应，减少重复限定

**证据状态：optional；严重程度：suggestion。** 改进临床与技术读者的比较路线，不改变叙述综述类型，也不要求压缩到ML会议篇幅。

**定位与检查范围。** 主文§3 p8–15、§4–5 p16–22、§6–7 p23–27；尤其p13行385的superlative。源文件：`/mnt/iusers01/fatpou01/bmh01/f12147zh/codex-slurm/csf3_v10_readonly_review_20261011_012543/inputs/cine-cmr-review-v10-120fa02-agarwood-figures/manuscript/body.tex:168、178、287–323、325–349`。短原文/缺失项：“most completely documented end-to-end cine workflow”；多个章节重复不证明focal accuracy。

**问题与依据。** 结构与证据措辞建议。 当前全文比较：§3前半主要沿方法/年份组织，Table1已有比较轴；§4和Tables2–3完成实质综合；§5–7复述部分参照边界。“most completely documented”缺少文档完整性比较标准，本轮不将其判断为事实错误。

**对中心论证的影响。** 提高读者找到“哪个输入/先验改变了哪个已测试端点”的效率，同时让已支持的正面结论更醒目。

**最小可行修复。** 各方法家族收束到现有六个比较轴及一个验证实例，避免补充表重新叙述一遍；保留global/segment Ecc、scar discrimination和precision的各自价值。对文档完整性最高级用明确比较范围/标准，或撤去无必要的排序。

**额外材料及反证条件。** 无需额外实验；若坚持superlative，需要可检查的候选范围和文档完整性标准。 现稿已通过§3.7、§4和Table1搭桥，不能称整篇只是逐篇罗列。若篇幅允许保留重复作为不同读者入口，本建议可不采纳。

## 章节贡献评估

| 当前章节 | 对中心问题的贡献 | 本轮判断与需保留的边界 |
|---|---|---|
| 摘要、Plain English summary、§1 | 把问题从方法性能改为异常属性的可测量范围 | 主旨与正文一致。摘要“the one independent test”应随正文限定在所检索/读取文献内，依B01落实可追溯性；不是已证明存在反例。 |
| §1.1与Supplementary Methods | 说明叙述检索来源、cap、读深和停止规则 | 已充分声明非系统综述及单人筛选；B01针对当前映射和absence条件，不要求换文章类型。 |
| §2与Notes1–3 | 区分观测、对应和应变，防止estimand混用 | 是全篇最稳固的理论基础。解析反例已明确不是实验；不应要求它证明真实cine普遍失败。 |
| §3.1–3.5及Table1 | 将输入、表示、先验与损失联系起来 | 具备比较框架；式(3)的普适性应随A01校准。C01补足投影判别的操作条件。 |
| §3.6–3.7及Figure3/S3 | 解释监督方式并提炼评估谱系 | A01、A02是主要修复处。修正训练目标不会自动改变一项论文的最强测试端点；两轴需分别处理。 |
| §4及Tables2–3 | 按验证对象而非时间线综合来源 | 有实际比较，不是简单逐篇罗列。A03与A05为局部数值/推理修复；S3/表3的未知编码受A02约束。 |
| §5 | 将矛盾拆回测量定义、capacity/estimation/input及QC | 逻辑有价值，已对采样改变带来的混杂作限定。QC不等于accuracy、uncertainty需校准，均不宜删除。 |
| §6.1–6.4、Figure5、Note5 | 提供可操作验证和报告路线 | 属于作者建议，无证据表明被当作已验证规范；不要求综述本身执行这些实验。 |
| §6.5及Table4/S2 | 解释数据资源如何补足不同验证阶段 | 单位、共享模板、配准与参照处理边界合理。尚未独立复核全部资源数字/许可，见核查表。 |
| §6.6及Note7 | 把重建条件接入下游应变测量 | 本轮核查支持大部分主要端点叙述；Figure1的precision归类需A04修正。Tsuneta残余径向结果仍在本轮未确认清单。 |
| §7、Notes6/8 | 把论证转为阅读研究与报告结果的实际条目 | 与目标临床/技术读者相关。没有必要扩展成软件法规市场调查；本轮不认证任何产品或声明。 |
| 局限、结论 | 明确已支持、未确定和未来检验的分界 | 总体与证据相称。无需用更强保守语气否定whole-slice/global/segment Ecc、临床分类或重复性的已有用途。 |

MRXCAT2.0还有一个适合在现有局限中具体化的输入条件：原文Methods的Tissue properties definition说明最终去除了LV心肌纹理。若讨论input sufficiency，这比笼统提及生成器image-formation model更有解释力；但没有实验能由此单独确定本文所引径向偏差的成因，不将其列为已确认因果遗漏。

## 按影响排序的处理建议

1. 先修正A01的训练监督/下游测试混淆，检查Table1、式(3)、§3.6及S3是否使用一致的概念。不得因为训练使用材料参照就直接宣称独立测试已验证材料运动。
2. 处理A02和B01的证据状态与追溯链：明确48个entry的构成、unknown类别、材料参照计数及现有缺口判断所依赖的候选记录。可以限定结论，不必为保留综述补做所有原研究的实验。
3. 同步A03–A05的图表与正文。它们都有小范围修复路径；修复前后不必推翻现有正面综合。
4. 对B02核实“prespecified”；拿不到证明时撤去这一修饰即可。未核实不等于认定作者事后设阈值。
5. 有余力再考虑C01–C03。优先让已支持的终点与研究建议更加直接、可查，避免继续堆叠方法名或一般性谨慎语句。

## 审查局限与证据状态

本轮形成39行主张核查记录，其中包含内部解析/检索声明核查及明确未核查项，不能当作39篇全部全文研究，更不能宣称对94条参考文献全部完成全文审计。主要意见依赖的外部事实均定位到原始论文方法、结果或图注；每条的访问深度在CSV与覆盖报告中单独记录。取得PDF也不等于读完所有页：例如Chen2024仅核了有限部分，未用于“该论文没有某实验”的已确认指控。

网络访问有实际限制：PMC直接页出现browser check，RSNA PDF直接下载403，部分PubMed请求429/空内容、Nature跳转失败、EuropePMC XML失败。可用的出版社HTML、官方PDF和原始论文索引正文已用于补足关键核查，失败记录也保留；没有绕过访问限制或安装工具。网页索引正文只支持实际显示的段落，不认证未返回的补充材料。未完整读取的临床结局论文、部分近期方法/资源、Tsuneta径向附图及检索筛选文件不构成已确认错误。

没有重新运行估计器、重建图件、验证原始病例数据、审计训练泄漏或复现统计分析。所有关于参照误差、队列复用和阈值差异的意见均限制在已读信息内；不能把“未报告”写成“未做”。本轮也没有独立认证作者身份、资金、利益冲突、授权、最新期刊合规或实际使用模型。

当前输入完整性及交付物验证以`audit/input_integrity_after.json`和`audit/deliverable_validation.json`为机器记录。主文和补充均未修改。`complete_with_declared_limits`表示本轮约定审查及有限性声明完成，**不表示论文通过或达到投稿/接收标准**。启动器负责把人类可读成果复制到本任务独立Obsidian staging目录；项目内副本为权威来源，本轮未验证Mac/iCloud目的地。
