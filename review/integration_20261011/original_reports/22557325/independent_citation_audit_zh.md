# 独立参考文献与引用匹配审计

日期：2026-10-11。性质：独立审计，不修改稿件、不认证投稿就绪。

审计对象仅为唯一基线 `inputs/cine-cmr-review-v10-120fa02-agarwood-figures/manuscript/` 中 `main.tex`、`body.tex`、`supplement.tex`、`references.bib`。未用历史 source notes、证据台账或历史 VERIFIED 标签作判断。操作规则读取 `AGENTS.md` 与 `skills/paper-writer/references/verification-ladder.md`；应用其独立来源核验、访问深度分层、访问失败不等于不存在等规则。主任务另行负责 MRXCAT2.0、Figure 1 临床数字、Jahromi、STRAUS 和 Stanford 的详核；本文件不将其他审核者的结论算作本审核者的独立发现。

## 范围与状态

- 共 94 条文献，每条在 `independent_citation_audit.csv` 中有一行，含基线行号、全部引用位置、实际检索链接、日期、访问深度、身份状态和未决状态。
- 87 条取得 Crossref DOI 记录并比较身份；6 条取得官方网页、arXiv 或 DataCite 记录；1 条 MRXCAT2.0 仓库只返回反机器人页面，标记 INCONCLUSIVE。没有条目被判为 NOT_FOUND。
- 对每条文献实际尝试三个 Crossref 查询形式：完整标题、第一作者加关键词和年份、核心关键词。282 次查询中仅 6 次返回 200，其余 276 次返回 429；随后降低速率，串行重试 DOI 并取得 87 条 DOI 记录。不能把这种状态写成“三种检索形式均成功交叉核验”。Crossref 不注册 DataCite/arXiv DOI，404 不能作为文献不存在的依据。
- Europe PMC 实际返回 76 条索引记录；取得摘要不等于已经逐句核对摘要。本审计重点阅读 2025–2026 条目的可用摘要，以及若干较早关键论文摘要。完整稿件引用层面的全面全文复核尚未完成；CSV 的 58 条 NOT_FULLY_AUDITED 明确保留该边界，并列为作者后续审阅项。
- DLSS、aligned strain、MyoNet 与 Tsuneta DLR 阅读到与问题有关的全文方法、结果或图注；不是四篇的每页、全部补充材料均已审阅。没有下载原始患者数据，没有重新运行分析，也未在本子任务中检查图像渲染。

机器检索原始记录与脚本位于 `review/citation_audit_retrieval/`。身份匹配并不代表细节论断 VERIFIED；CSV 使用分开的 `identity_status`、`metadata_status` 和 `claim_status`，避免合并成一个过强的“通过”标签。

## 需要优先处理的引用问题

1. **DLSS 训练监督与评价参照混淆（MAJOR）。** `body.tex:174` 的段落总述和 `supplement.tex:343` 把 DLSS 归为专家壁运动标签监督。实际网络由配准的 4D-flow 心肌速度与分割数据训练，专家共识用于独立临床评价。这会改变方法分类与其信息来源解释，应调整段落归类及 S3。该研究的 ROC AUC 为 0.90，不能写成“在 30% 阈值下 AUC 0.90”；30% 峰值径向应变阈值对应敏感度 86%、特异度 85%、准确率 86%。[原始论文方法与结果](https://pubs.rsna.org/doi/10.1148/ryct.220202)

2. **Aligned strain 不应被压缩为 LGE 监督的运动网络（MAJOR）。** `body.tex:174`、`supplement.tex:347` 应区分自监督关键时相检测、监督分割、SSIM／平滑／Dice 引导的形变估计、以及以 LGE 定义患者标签的下游分类。主要分类终点为患者是否含至少一个 LGE 阳性节段，不是瘢痕边界定位。DMD82 是同中心较晚时间段的内部留出数据。建议用具体绝对性能及比较对象替代含义不够明确的“+40%／+17%”，并说明 balanced accuracy。原稿“组织参照不是运动真值”的原则可以保留，但监督链必须准确。[原始论文 DL Pipeline、Figure 3 与分类结果](https://pmc.ncbi.nlm.nih.gov/articles/PMC12127955/)

3. **MyoNet 的真实输入需要补全（MODERATE）。** `body.tex:172`、`supplement.tex:349` 的“cine”过于笼统：输入是由 cine 分割得到的二值时空图像，监督位移来自配对 tagging 的 SinMod 分析。大鼠放射损伤背景及 ICC 0.973／0.975 得到支持，但不能引申为人体性能。此处是输入与参照描述精度问题，不是数字虚构。[原文 Figures 1–2、Table 2](https://pmc.ncbi.nlm.nih.gov/articles/PMC13024448/)

4. **Portal 的配置和数值应配对（MODERATE）。** `body.tex:152`、`supplement.tex:313` 将距离图加权设计与 EPE 1.02 mm 连在一起。摘要先给出 1.02 mm 对 RAFT 1.19 mm，再明确加入舒张末期距离图将误差改善到 0.95 mm，完全监督为 0.91 mm。应拆分配置或给出最终加权配置的数值。完整参照生成方式仍需全文确认。[原文摘要](https://doi.org/10.1016/j.compbiomed.2025.110739)

5. **Buoso 三维 tagging 的正面验证被漏列（MODERATE，覆盖平衡）。** `supplement.tex:337` 仅写合成图像评价，摘要还报告外部人体与猪在体评价，参照为人工追踪。应补充，而继续明确这是 tagging、不是 routine cine。遗漏可能使方法记录显得比原始研究更薄弱。[原文摘要](https://doi.org/10.1016/j.jocmr.2025.101869)

6. **合并 foundation-model 行的任务归属需准确（MINOR）。** `supplement.tex:317` 将两个模型和任务列表合并；CineMA 明确包含 prognostication，Jacob 的九项任务列表是序列／视图分类、四类分割、landmark 和两类病理检测。不要让联合列暗示两个模型都验证了每一种任务。摘要列出的任务中没有 dense-motion task，只能在此范围内写缺失。[Jacob 原文](https://doi.org/10.1016/j.jocmr.2025.101967)

## 元数据与未决事项

- **Fourier-Net+ 页码已更新。** `references.bib:339` 仍为 early-access 1–15；本次 Crossref 为 volume 37、issue 10、5712–5726。建议采用当前正式卷期页，同时保留在线日期（若需要）。[注册元数据](https://api.crossref.org/works/10.1109/TNNLS.2026.3688245)
- **Morales comparison 年份需统一口径。** Bibliography 的 2023、57(5):1507–1515 与索引一致，S3 写“2022 comparison”可对应在线先行日期，但时间线与表格应统一或标明 online-first；文献 key 中的 2022 无需重命名。
- **CardioMorphNet 作者字段分割不同。** Crossref 为 given=`Reza Akbari`、family=`Movahed`；BibTeX 为 given=`Reza`、family=`Akbari Movahed`。是同一显示姓名，不是捏造作者；按作者／出版社偏好确认姓氏分割。
- **不要误改 Smiseth、Goetze、He、Tsuneta。** Smiseth 的完整副标题获 Europe PMC 支持，Crossref 仅短标题；Goetze 在线 2025／卷期 2026 并不冲突；He 的正式页码获 Europe PMC 支持，Crossref 不完整；Tsuneta 的 24:2024-0202 获原始 PDF 支持，不能根据 Crossref 的 n/a 擅自删除。Tsuneta 径向低估也确实出现在补充 Figure 4，不能因摘要未提及就判作无依据。[Tsuneta 原文](https://pmc.ncbi.nlm.nih.gov/articles/PMC12772260/)
- **MRXCAT2.0 仓库暂挂。** HTTP 200 实际内容为反机器人页面，不能据此确认创建日期或文件可用性。保留“访问未完成”，不判不存在，也不擅自移除相关研究。[仓库入口](https://gitlab.ethz.ch/ibt-cmr-public/mrxcat-2.0)

本次审计没有证明 94 条文献的所有细节论断都正确，也没有重建或认证历史检索、筛选和全文阅读流程。上述错误应通过逐处修改和重新核对关闭；其余细节未审项在 CSV 明确暂挂供作者处理。工作树中的稿件与输入均未因本子任务而更改。
