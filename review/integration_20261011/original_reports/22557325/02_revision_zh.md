# Cine-CMR 全文修订说明

日期：2026-10-11。任务：作者审阅准备，非投稿。唯一基线为 `inputs/cine-cmr-review-v10-120fa02-agarwood-figures/`；现稿位于 `working/manuscript/`。独立稿件Git起点为 `09d5429fcb896b133651c96782acd9731da47c10`。输入与原始图件保持不变，全部科学编辑在工作副本完成。

## 修订后的核心论证

本文仍是关于常规cine能否支持区域/局灶功能测量的批判性叙述综述。没有改成算法论文、系统综述或已完成的benchmark。最终论证是：有用的区域测量已有实证支持，但每项结论必须绑定采集、输入、估计器、群体、空间尺度、应变定义、时间点、参照及容差；轮廓、材料运动、重复性、组织关联和临床预测回答不同问题。已检配对研究的特定周向应变终点有正面支持，不能因此推广到所有方向、病变属性或软件互换。

全文先修科学与逻辑，再调整组织与语言。主文方法段保留feature tracking、registration、有限元/物理约束、学习监督和不同表示的具体机制。临床动机、预测/瘢痕关联和重建研究的成功结果得到保留。摘要、Plain English summary、综合讨论和结论与此一致，不再以泛化的“验证不足”代替方法解释。

## 关键科学改正

1. **Figure 4 / MRXCAT2.0。** 保留0.95→0.30等原始数值，径向改为明显降低且仍有残余；周向接近零，纵向基本不变。区分规定的组织应变与估计误差。0.02±0.04、−0.24±0.21和infarct −0.20±0.21是三个中室短轴切片的汇总，all包含infarct。删除由SD重叠或未报告检验推出等效/无差异的逻辑，不据单个径向数字建立所有指标的统一排序。已读结果未直接量化scar内幅度、边界/位置、范围和峰时误差。另明确SNR30、去除心肌纹理、TextNet与DeepStrain共享ACDC图像域；独立评价团队不等于独立数据域，共享来源也不自动证明泄漏。
2. **Figure 1与配对证据。** Militaru的LS/CS范围为FT–tagging，RS范围为FT厂商间比较；Cao的0.778是中室切片peak Ecc而非AHA节段ICC，Ell来自四腔面；Kihlberg ROC为end-systolic segmental Ecc、LGE>50% transmurality。Bello是302例PH中的RV预后模型、内部校正C-index及manual-variable模型比较。概念牛眼图segment11与曲线对应已修正，所有计算读数明确为示意。
3. **StrainNet与Jahromi。** StrainNet区分243/62人内部划分、670/190 sections、59个cine应变测试，以及DENSE-contour输入下0.75±0.35mm EPE；保留cine–DENSE ICC改进，同时加入LoA和外部验证限制。源文global LoA正文与Table2略有不一致，S1公开列出，未静默调和。Jahromi结论限于40健康受试者、两个中室层面的peak median systolic endocardial Ecc；chosen ±3.5pp margin不写成预设，slice聚类处理未明不补造。
4. **监督、参考与正面结果。** DLSS的4D-flow速度监督、commercial-software分割标签和53例/846节段四读者临床评估分开；AUC0.90不绑定30%工作点。Aligned strain的图像/掩膜/平滑运动损失与下游LGE患者分类分开，57/82为同中心时间留出。MyoNet保留binary cine masks、tagging/SinMod监督和大鼠范围。Portal正确配对1.02/0.95/0.91/1.19mm，新增传统FT传播评估点的参照定义。Buoso保留人体landmark和猪cine标注比较，不能称仅synthetic验证。Tsuneta的比较差值离散程度不冒充scan–rescan精密度。
5. **推理框架。** 式3限定为registration示例；共同mask的解析反例证明mask不足以唯一确定内部对应，不证明所有cine必然无法恢复运动。输入、表示、估计与参照误差允许耦合。投影试验需说明范数、边界、采样及应变导数；训练损失权重变化通常需匹配重训，不能只在测试时改变未暴露的参数。
6. **资源与独立性。** STRAUS的18虚拟例来自3模板×6状态；Stanford的51/55是同一资源的版本化描述，Jahromi明确资源关联但未核对个体文件。CMAC稀疏landmark、MRXCAT生成器和重建资源不被称为通用dense motion truth。未下载患者文件，也未新增实验。

## 搜索、覆盖和证据记录

历史18组查询、每query 100上限及281 returned counts保留为现存记录。253去重、21保留、232排除以及citation-expansion停止规则缺乏原始导出/逐条决策，正文和补充方法都明确不能重构。September截止与October追加分开，Oct8叙述/Oct9台账差异保留。本次10月11日核验是追加查证，不冒充历史检索复现。

`meaning_changes.csv`记录176条意义、来源披露及相关图版更改，含原文、修订、理由、证据和作者状态。`issue_resolution.csv`对27项审计问题逐项给出行动及余留事项。`claim_evidence.csv`保留163条审计/继承行并追加12条新核验；旧verdict保留为历史，当前状态见revision列。`coverage.csv`保留371条覆盖记录并新增修订行动/深度字段。`current_citation_claim_map.csv`将94个当前citekeys定位到具体段落/表图，并保留实际阅读深度。135条历史claim通过当前key或相同DOI别名对齐，10条未对应当前引用的历史记录仍保留，不当作当前支持证据。

fresh-context来源代理完成12项重点核验及修订后回读。其报告记录可访问全文的相关章节、摘要、metadata和失败访问；并非全部94条逐篇全文新核验，更不是独立人工临床评审。最终回读发现的Cao尺度、DLSS分割来源、STCMT/FE摘要级否定断言与Figure3注释问题均已落实。具体查询和访问限制见dated addendum及独立报告。

## 图表与排版

原agarwood资产保持原样。当前PDF使用 `figures/revision/` 衍生图，可编辑Python/SVG/CSV位于 `figures/revision_sources/`。没有新医学图像或生成式图像。原来的190mm图缩入160/166mm正文导致小字进一步缩小；现采用190mm宽专页居中插图，正文边距不变，并调整图1列内文字、底部留白及S3图底部。最终普通图中文字最低约7.06pt，数学上下标约6.20–6.74pt；这是最终PDF抽取尺寸，不是名义源字号。专页带来留白，保留为作者审阅版的可读性取舍；最终期刊排版需另按确定要求处理。

Figure3的48项为选择性、异质方法/比较/评价记录，不是独立队列数或全领域分母。当前图类为21 mask/registration、8 label、15 material、1 prescribed-scar evaluation、2未核验、1其他任务；material加focal共16。GA删除错误14/48。图内类别不作验证强度排名，未知不作“无验证”。所有图注、摘要图、S1–S3和声明与此同步。

## 仍需作者或外部信息的事项

历史筛选原始记录；StrainNet源文global LoA内部差异；未全文核验的非中心细节；作者/机构/通信地址、贡献、利益冲突、基金、致谢及历史AI使用；数值重绘/程序图的权利与期刊政策解释。JCMR官方Guide仍403，不能确认当前Review格式/GA要求。本文保留必要声明占位，不推定作者确认。没有发送信件、投稿或启动新的调度任务。

编译、页面、字体、输入校验和交付包检查见 `REVISION_QA_REPORT.md`；最终状态见 `FINAL_REVISION_STATUS.md`。脚本成功只证明对应技术检查，不认证科学或临床有效性。
