# 最终修订者定向复核

日期：2026-10-11。模型：GPT-6 Astra，High；依据 `runs/22557325/selected_model.txt` 及 launcher 配置。本报告不是新的独立审稿；独立报告 `03_independent_review_zh.md` 与其冻结副本保持不变。

独立审稿的17项科学内容修正和3处书目字段修正已落实。访问、历史记录和源内差异不能通过改写消失，分别保留。当前处置以 `issue_resolution.csv` 的 IV-001–028 以及 `finalizer_targeted_recheck.csv` 为准；较早报告和状态文件保留其原始日期/阶段，不代表最终状态。

本轮新检索是有界补查，不是系统检索或重跑9月流程。共3个搜索字符串、9个直接URL请求，完整响应保存在权威项目 `review/finalizer/web_retrieval_1.json` 至 `3.json`（不在交付包重复分发网页正文）。查询为 `"10.1109/TMI.2015.2478117" "47"`、`"Fully automated myocardial strain estimation" "40"`、`"10.1088/1361-6560/aeb060"`。直接请求包含MPN、Chen、WarpPINN-fibers、Fourier-Net、Zheng、Tuyisenge、Puyol-Anton机构记录、IG-BiReg DOI和JCMR官方作者指南。Chen即时页面出现浏览器挑战，使用同日保存的正确原文；IG-BiReg DOI和作者指南访问失败，未用失败证明来源不存在或推导政策。

修改后的含义逐项与以下原始内容对照，而非照抄审稿结论：

| 来源 | 实際读取范围 | 本轮保留的边界 |
|---|---|---|
| MPN | 同日原文 §§4.1–4.2、Table4；新arXiv页面 | 另一模型生成并施加的已知运动，非独立生理真值 |
| Chen | 同日原文Methods、Results、tagging比较相关段落 | tagging比较不含nD+t/pTVreg；模拟/跟踪比较另列 |
| WarpPINN-fibers | 原文 §§2.6–2.7、limitation及新arXiv页面 | 人体没有参考应变曲线；landmark改善不等于strain accuracy |
| Fourier-Net | 原文表示方法和讨论；新arXiv页面 | scaling-and-squaring后不再严格带限 |
| Fourier-Net+ | 既有已发表摘要记录；较早预印本的适用范围 | 2026实验未读最终表，正文明确摘要归属 |
| Zheng | 原文Table1、§4.3/Table4；新arXiv页面 | 九特征含shape/volume/EF和motion；95%为CV |
| Vigneault / Puyol-Anton | 前者同日原文dataset/segmentation段；后者新机构摘要 | 42+21与40+40分别归属；后者比较cvi42 |
| Tuyisenge | 新PubMed原始摘要 | 47患者、三层、ICC>0.8、clinical scores仅按摘要陈述 |
| Grob / Bello | 同日正确原文Methods人群段 | 19参与者非19患者；Bello是Group4 CTEPH |
| Buss / He | 同日保存的原始摘要（Europe PMC记录） | 全局/患者级LVEF恢复与节段来源预后分开；不认证完整统计模型 |
| Qin2018 / MulViMotion | 原文experimental setup划分及评价段 | 总队列和测试队列分开 |
| Liu | 已保存出版商摘要/索引正文片段 | 2D+t known-motion；3D+t仅临床mask；不认证完整实验表 |
| FOAL / Metz | FOAL原文摘要/online optimisation文字；Metz保存的PubMed原始摘要 | 0.4s是在线优化；3%为CTA平均偏差 |
| DeepMesh / Rendell | 原文temporal correspondence及low-rank image-stack段 | 模板索引不是材料同源；低秩对象为对齐图像 |
| REGAIN | 原文采集/strain子集描述和既有独立核查 | 跨采集/重建加分析的一致性，非重扫精密度 |
| 书目字段 | 同日Crossref/DataCite/出版商记录 | 未核实网页日期改n.d.；不改变SegMorph作者归属 |

这些是相关段落的定向阅读，不是上述全文逐页精读，更不是94篇原始研究重新阅读全文。旧独立引用检查及296行覆盖表保留；其范围不能自动转移为本轮阅读范围。未读取患者文件，未做新临床或合成验证实验。

保守语言润色覆盖 `main.tex`、`body.tex`、`supplement.tex` 的现有文本，修复连接、冗余短语与引文间距；完整词表扫描保存在 `finalizer/style_scan.csv`，纯措辞变化见 `pure_language_edits.json`。技术术语和有界结论未因词频被机械替换。科学含义变化累计记录在 `meaning_changes.csv`；本轮新增53条（含图源、访问边界和AI过程说明），全部待作者审阅。

最终PDF正文39页、补充23页；技术和视觉范围见 `FINAL_QA_REPORT.md`。构建、源文对照和图像目检均不构成科学批准。
