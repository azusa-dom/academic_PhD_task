# 阶段03：其余来源与92条书目身份审计

本阶段已为阅读计划中余下 **71 个 Tier 2/3 key** 建立有边界的阅读与主张记录，并检查其在当前正文、补充材料中的 **149 处显式引用**。结合前两阶段，92 个 key 均有记录，250 处显式引用均有对应覆盖表；没有 NOT_READ。此处“完成”指审计和限制已登记，不表示92篇全文均已读，也不表示所有主张均获支持。本文为作者授权的 AI 辅助工作稿，不是独立人类同行评审。

本阶段实际深度为：33 个 SELECTED_FULLTEXT、37 个 ABSTRACT、1 个 METADATA_ONLY。累计为53、38、1。SELECTED_FULLTEXT包括明确注明版本的作者稿、官方技术说明和部分出版商正文片段，不等于完整期刊全文或补充材料阅读。新增155条原子记录：119条支持、20条需限定、6条部分支持、10条未核实。累计315条，其中12条 NOT_VERIFIED；前阶段的 StrainNet 应变实现和 MRXCAT2.0 补充材料限制没有被本阶段自动解除。

权威明细是[逐条主张台账](claim_citation_audit.csv)、[阅读登记](source_reading_register.csv)、[本阶段引用位置覆盖](stage03_occurrence_coverage.csv)及每篇[阅读笔记目录](reading_notes/)。正文摘录保持英文；建议均留在 review/，未改动论文、图、原始书目或 Zotero。

## 优先处理的发现

| 当前位置 / 来源 | 核对结果与影响 | 作者可采用的处理 |
|---|---|---|
| body:158；supplement:328，IG-BiReg | 出版商存入Crossref的完整摘要现已可读，原稿“仅题名／未访问科学内容”的状态过时。双向残差融合和均值强度／PCA特征空间约束可核；ACDC/M&Ms指标是mask及轮廓一致性。完整监督与方法仍受限。 | 更新至摘要级机制描述；不能把题名中的implicit直接归为坐标式INR。见S03-89。 |
| body:156；supplement:320，CardioMorphNet | 作者v2的Eq.6/11仍有VAE图像重建MSE；所省略的是形变后图像与固定图像之间的配准强度相似性项。表中“without an intensity loss”过宽。 | 改为“without a warped-image similarity term; VAE image-reconstruction loss retained”。最终摘要与v2均有UKB及M&Ms，不用仅UKB的v1替代。 |
| supplement:312，DeepMesh | 无稠密运动标签，但rasterizer用2D分割进行形状监督。称“unsupervised via differentiable rasteriser”容易误解为不使用标注。 | 写明“no motion-field labels, with weak supervision from 2D segmentations”。固定顶点索引不证明材料同源性，正文已有的限制合理。 |
| body:158；supplement:330，两篇基础模型 | 15M cine images / 74,916 **studies**与36M images / 27,524 **subjects**均有正式Methods支持。CineMA包含UKB首次及重复成像；CMR-FM是多序列，不只是cine。 | 保留分母，分列任务。生存预测属于CineMA；CMR-FM的9任务没有该项，且其部分下游样本来自预训练来源，不能统称全部独立外部验证。 |
| body:297，Chadalavada | 45,700人的UKB一般人群队列被并入“across disease cohorts”，队列属性表述不准。 | 改成“across disease cohorts and a population-based cohort”。关联结果不需要因此删除。 |
| body:398；supplement:248，CMRxRecon2025 | 官方Data页列tagging采集，但未建立稠密运动真值；Tasks说明训练／验证逐例疾病信息不公开。“with disease labels”无充分支持。 | 区分疾病覆盖、公开标签、tagging采集和运动标签。保留配对数量未核的限制；不能声称2025不含tagging。 |
| body:371；表4/S2，CMAC | 0.84 mm获官方README原像素支持，但它是按规则排除landmark后、对所有时点计算的人体观察者间变异中位数。SSFP跨模态误差因时间错位仅在ES和final frame评价。 | 补充筛选和时相范围；不把0.84当算法误差下限、材料真值准确度或所有原始点的无条件变异。 |
| body:367；表4/S2；图5，STRAUS | 官方页和论文摘要支持18 virtual cases、90 sequences、2700 volumes及图像／mesh类型。本次未读到足以确认三模板×六状态、全部病理名称及engineering-strain定义的原始Methods。 | 这些细节保留NOT_VERIFIED，不能继承清单的“已核”。图5中的3×6同样应暂缓认证。 |
| body:146，Laplace/变分同化 | 几何／收缩模型及摘要所列阳性结果有据，但“without an image-similarity term”需要完整目标函数。出版商与合法替代访问未取得足够全文。 | 删除这项否定性限定，或待完整Methods核对；不能判为已证实错误，也不能保留为已核事实。 |

CMAC的[官方说明](https://www.cardiacatlas.org/motion-tracking-2011-challenge/)与[CMRxRecon2025任务页](https://cmrxrecon.github.io/2025/Tasks.html)是资源边界的直接证据。IG-BiReg摘要的出版身份为[2026年10月5日在线论文](https://doi.org/10.1088/1361-6560/aeb060)。详细替换句与重复位置见[targeted_corrections.md](targeted_corrections.md)，不要求重写本篇叙述性综述。

## 物理、INR、FE及验证参照

Fourier-Net正式AAAI论文明确说微分同胚版本经scaling-and-squaring后，最终形变不再带限。因此“基础表示带宽”不等于最终位移频谱或局部应变恢复能力，稿件保留该区别是正确的。Fourier-Net+正式2026摘要支持五数据集及3D心脏几何／功能指标；补表“shortened contracting path”未由本次取得的正式Methods核实，另列NOT_VERIFIED。早期预印本不能无条件代替最新正式版本。

WarpPINN的近不可压缩Jacobian项包含在neo-Hookean正则中，AD和Fourier features属于表示与求导实现，不是应变准确性的独立证明。WarpPINN-fibers作者稿明确讨论人体应变参照不足；其纤维角度／权重敏感性实验也不是病灶大小／严重度扫描。两文所读版本均已注明，未声称与期刊最终稿逐字一致。Qin的生物力学先验由模拟形变训练VAE，其中模拟与分割形态关联；“物理先验”不构成独立材料测量。

Liu的2026 FE论文摘要确实分别限定2D+t与3D+t：前者有模拟已知运动／应变及公开／临床数据，后者只有临床mask评价。不能把2D已知真值证据平移为3D材料准确性。STCMT的病种组间区分、ApparentFlow的95%/94%分类准确率、Portal的轮廓EPE、MPN施加模型生成形变后的EPE，都需要保留各自参照。MPN的§4.1/4.2及Portal出版商§4.1/4.2片段已实际读到，支持稿件将其与独立生理真值分开的处理。

MyoNet原文Table2确认ICC .973/.975，属于大鼠、cine二值分割输入、SinMod标注MRI分析参照。Buoso的3D tagging网络则使用tagging推理，外部人体为人工landmark，猪应变参照来自cine手工分析；其不同方向应变的计算也并非统一的一套张量分量。两者不能直接扩展为人类普通cine的稠密材料准确性。

## 2025/2026版本和书目

92条均检查了可访问的主记录：86条使用出版商存入Crossref的论文记录，另5条为官方资源／DataCite／arXiv记录；MRXCAT2.0仓库只确认原论文及ETH官方页面的链接身份，GitLab实时内容和revision仍未核实。该计数是身份核对，不是全文阅读计数。

[书目更正表](bibliography_corrections.csv)现有92行；[字段核对表](stage03_bibliography_field_check.csv)保留题名、作者、年份、卷期页、DOI和venue核对及例外。没有把旧citation key、DOI中的早年数字、online-first日期与卷年差异误当错误。

确定建议改动只有两项：保留前阶段CineVN在线日期26 August 2024的更正；MCM的workshop名称应为 **Reconstruction and Motion Estimation in Medical Imaging**，官方MICCAI日程确认列入该报告，但不能据日程保证实际报告已经发生。MCM继续引用已验证的arXiv作者版本，未编造正式章节DOI。可直接审阅[统一补丁](bibliography_proposed.patch)或[两条完整BibTeX建议](proposed_bibliography_patch.bib)，均不自动应用。

FOAL与DeepTag存在IEEE DOI记录和CVF开源PDF的页码差异；当前输入匹配IEEE记录，故不机械替换成CVF页码。Puntmann的Crossref展开了团体成员，PMC原始byline支持现有10作者加团体写法。Smiseth完整题名由PubMed支持；He的2002–2017由PubMed卷期确认；Tsuneta的mp.2024-0202是J-STAGE文章号。IG-BiReg、Monfared当前没有可确认的卷页，不补猜测值。

CardioMorphNet、WarpPINN-fibers、FE、Fourier-Net+、STCMT、latent ODE、CineMA、MyoNet及2026综述均已核正式身份。内容深度另列：例如CardioMorphNet读的是2026-06-08作者v2，而WarpPINN-fibers读的是2025作者版本；这种差别在阅读表中可见。

## 资源、跨文档与未核实项

Stanford当前官方repository与DataCite身份可核。lab页面的51 healthy与repository的55（51 healthy、4 aortic stenosis）不是同一版本口径；cine全LV、DENSE对应位置和三个mid-LV tagging切片不能写成所有模态全心室等覆盖。本次未下载受试者ZIP，因此有效配对数、排除后分析人数和与已有研究是否重叠仍不得从总人数推断。[资源笔记](reading_notes/stanforddata.md)保留版本9及ODbL信息。

已检查摘要、结论、方法表S3、资源表、图注文件、Figure3原始CSV和SVG文字。图3是选择性方法／评价地图，不能用其条目数推全领域缺失比例。“direct tests ... remain sparse”属于本叙述性综述范围的综合判断，不是本轮复现的系统检索结论。图中material类别还混合模拟已知运动和有误差的材料敏感参照，现有图注的类别非等级说明应保留。

[跨文档核对](stage03_cross_document_check.md)列出同步事项；[图3定位与阅读深度建议表](stage03_figure3_proposed_updates.csv)只供作者审阅，未改输入。原图表中的历史reading_depth不作为本次独立证据。

[未核实清单](stage03_unresolved.md)逐项列出本阶段10条显式NOT_VERIFIED及其他阅读限制。不存在未读key，但仍存在未读的方法细节、补充材料和局灶终点。尤其不能将“未取得／未在所读部分核实”改成“论文没有”。

## 保存、验证与继续位置

原始压缩包及解包manifest的哈希用于保持唯一稿件基线。项目.git是只读保护目录，无法记录有效起始revision；没有另建项目或线程，未提交新Slurm作业。原job22636451、run目录、stdout/stderr及最终消息路径保存在progress.json。前两阶段快照及本阶段prompt都保留。

[结构与完整性检查](validation_stage03.json)验证记录数量、确切源行摘录、文件哈希、覆盖数及输入未变；它不证明科学结论正确。最终继续点是上述未核实主张的原文取得／版本核对与作者决定是否采纳建议，不需要重做已完成的71-key审计。

根据本项目“只在项目内工作”的明确限制，阅读镜像暂存于delivery/obsidian-stage03；没有写外部Obsidian导出目录或声称Mac/iCloud已同步。
