# Supervisor-Skills 实际执行记录

日期：2026-10-11。执行范围：只审计，不改稿。权威顺序：本轮用户audit-only指令及AGENTS.md任务合同高于技能默认写作/评分/自动化要求。

## 已实际读取的文件

以下均为本项目本地文件，路径相对项目根；不是仅根据技能名称宣称使用。

| 文件 | 应用 |
|---|---|
| AGENTS.md | 唯一基线、输入不作指令、五项聚焦审计、无新实验/任务/投稿、真实阅读深度、报告中文 |
| skills/pre-submission-reviewer/SKILL.md | 科学/结构/语言/TeX/图质量逐项审阅，精确引句及严重性；本次主技能 |
| skills/pre-submission-reviewer/references/logic-and-structure.md | 检查论证链、研究问题/证据/结论、相关工作平衡 |
| skills/pre-submission-reviewer/references/section-guides.md | 审计摘要、引言、方法叙述、讨论/结论的功能；不机械套算法论文 |
| skills/pre-submission-reviewer/references/latex-rules.md | 标签引用、表图、编译和最终版面 |
| skills/pre-submission-reviewer/references/grammar-rules.md | 语言/语义一致性检查；没有为标点制造科学缺陷 |
| skills/pre-submission-reviewer/references/forbidden-patterns.md | 全文候选词/破折号扫描，结果qa/style_scan.csv；保留technical nonrigid等词，不按词频升级 |
| skills/paper-writer/SKILL.md | 应用证据纪律与验证阶梯，不调用起草流程 |
| skills/paper-writer/references/evidence-discipline.md | 区分已报告结果、推理、未证实和计划；缺证据不填充 |
| skills/paper-writer/references/verification-ladder.md | 独立fresh-context引用核验；来源身份与论断支持分列 |
| skills/paper-writer/references/verification-checklist.md | 正面结果、基线、引用、验证范围与缺口的核对 |
| skills/paper-polish/SKILL.md | 阅读其科学意义保护规则；本轮只识别后续编辑风险，未润色稿件 |
| skills/paper-polish/references/section-conventions.md | 结构/衔接和相同语义的语言改进候选 |
| skills/paper-polish/references/ai-tone-guardrails.md | 克制论断、具体转承，避免套话；未自动词替换 |

另读取`/mnt/iusers01/fatpou01/bmh01/f12147zh/codex-slurm/OBSIDIAN_EXPORT_POLICY.md`用于交接镜像。没有CSF3数据库/Slurm失败，不触发历史修复手册或数据库操作。

## 执行方式与覆盖规则

1. 已读取唯一基线四个TeX/Bib文件、全部图表及提供的证据/搜索记录。coverage.csv记录章节/文件/图表/94当前来源，claim_evidence.csv分本次28个中心证据单元与135条继承claim。
2. 依verification-ladder的独立引用复核要求，启动一个fresh-context子代理`citation_verifier`。它读取AGENTS.md、verification-ladder和四个基线文件，不把历史ledger当证据。并行的是只读来源核验；没有两个任务改同一稿件，也未提交scheduler任务。未将AI子审计称作独立人工reviewer。
3. 子代理实际执行282个Crossref查询（276限流），随后串行DOI重试；94条身份行全部记录。对DLSS、aligned strain、MyoNet、Tsuneta读相关全文，对近期论文读相关摘要。详细身份、深度、失败和未决见独立CSV及报告。主代理另查中心论文、图1数值、MRXCAT原始图14、STRAUS/Stanford等，实际检索另记dated addendum。
4. 未使用deep-research技能；本次检索是围绕既有中心论断的定向核验，不是扩展新survey。没有调用原始实验、训练或新基准验证。
5. 先检查build_manuscript.sh/static_qa.py再运行；编译输出隔离在review/qa/baseline_build。逐幅图像目检、全部页面contact总览、重要页放大及新构建重点页检查已完成，具体范围见QA_REPORT.md。

## 与任务合同冲突的默认规则如何处理

- 不应用“六段引言”“固定参考数量”“算法模块/消融/真实案例”等原始算法论文模板。
- 不把光栅医学图像当缺陷；当前实际图主要是可编辑程序图，以内容、最终尺寸、字号和科学准确性评估。
- 不执行按em-dash或单词出现次数自动MAJOR评级；全量扫描只保留候选，严重性按后果。
- 不给投稿评分或Ready认证；作者、权利、期刊和submission状态各自独立。
- 不因能取得全文而声称读完或论断正确；不会把metadata身份匹配等同结果核验。
- 不采用evidence-discipline中可能把计划写成“preliminary results”的默认建议；本任务计划始终保持未来性质。
- 不执行paper-polish的改稿步骤，本轮用户明确要求no rewrite。修订建议进入blueprint，未改工作稿。

## 产出与验证

27个问题，每个有原文精确子串、实际源码行号、严重性、证据、影响、建议与验收条件。写出时脚本确认引句存在于该文件。输入/工作稿SHA-256未变。图/表统计和机械QA与科学审计状态分开。所有问题保持OPEN_AUDIT_ONLY，不伪称解决。

## 第二阶段：已授权全文修订（2026-10-11）

本节补充而不覆盖前述 audit-only 历史。用户现明确授权执行全文修订，故旧日志的“不改稿”仅描述第一阶段。实际重新阅读三项 SKILL.md 及 logic-and-structure、section-guides、latex-rules、grammar-rules、evidence-discipline、verification-ladder、verification-checklist、section-conventions、ai-tone-guardrails 引用文件；阅读 01_audit_zh.md、revision_blueprint.md、issues、claim_evidence、coverage、独立引用审计及现有全稿/补充材料。应用顺序为科学/逻辑、组织和跨节一致性、图表、语言。

- reviewer：对27项稳定ID逐项落实；不作评分或投稿认证。
- writer：保留方法输入、表示、先验、监督及正面结果；补充有具体原始来源的限定和新增方法细节；依验证阶梯启动 fresh-context `revision_source_check`，完成12项核心来源核验及回读。其两份报告保留独立AI性质，不称人工评审，不等同全94条全文认证。
- polish：重写摘要/结论，减少重复泛化限制，保留临床动机；176条意义/披露/相关版面变更记录与作者待审状态分开。没有按任意压缩比例或标点数量编辑。
- 未调用 deep-research：只是对既有论断的有界定向核验。没有新增实验、数据下载、scheduler任务、通信或投稿。
- 实际检查脚本后编译；原图的Python3.12 f-string与当前3.9不兼容，仅修衍生图源。查阅 CSF3 故障恢复手册的 LaTeX/工具链有关段落；未运行数据库修复或更改共享环境。librsvg/fitz为现有工具；保留失败日志。
- 权威顺序仍为本轮用户授权和AGENTS合同优先。既有技能中作者确认默认门槛不阻止已授权、可审阅的证据改稿；真正缺失声明与权利信息仍保持pending。


## 2026-10-11 独立核验阶段（fresh context）

先读修订稿、补充材料、书目、图与原始证据；冻结独立报告后才读issues.csv和issue_resolution.csv。未读写作者其余总结作为论断依据。未改稿。

已读取并实际应用：
- AGENTS.md：输入/操作边界、读源纪律、保存和镜像要求。
- skills/pre-submission-reviewer/SKILL.md；references/logic-and-structure.md：按论证后果审查，不使用分数提交认证，不以标点/词表或光栅格式定科学严重度。
- skills/paper-writer/SKILL.md；references/verification-ladder.md、evidence-discipline.md、verification-checklist.md：新上下文独立核查、三查询身份核查、获取与阅读深度分离、失败访问和证据缺失分离。该verification-ladder明确要求可用时fresh verifier，故分派三个独立证据核查；无多数票证据。
- skills/paper-polish/SKILL.md：先科学意义后语言；本阶段仅审查和建议，不润色写回。
- 早期批量打开pre-submission-reviewer的latex-rules、forbidden-patterns、section-guides等时输出有截断；不将这些文件列为逐字全读，不据未见内容认证。

实际产物：03_independent_review_zh.md、verification_findings.csv、independent_citation_checks.csv、verification_coverage.csv。逐源/逐页范围、原始取证和冻结记录在independent_verification。

## 2026-10-11 Finalizer：独立审查后修订及最终润色

读取并应用三个项目技能：skills/pre-submission-reviewer/SKILL.md、skills/paper-writer/SKILL.md、skills/paper-polish/SKILL.md。相关引用实际读取：reviewer 的 logic-and-structure、grammar-rules、latex-rules；writer 的 verification-ladder、verification-checklist、evidence-discipline；polish 的 section-conventions、ai-tone-guardrails。早期批量输出截断的内容不作为全读认证。按科学意义、跨图表一致性、语言的顺序执行。未启动新独立审查；本轮定向回查均为同上下文 finalizer 检查，既有独立报告不被覆盖。

按28条IV意见落实，保留27条AUD历史与当前状态；新增53条意义变更、8处纯语言润色。图注便利副本从最终TeX同步，未引入额外主张。没有执行词表机械定级、固定篇幅、原始算法/实验模板、额外实验或scheduler任务。未调用deep-research，检索仅围绕现有论断。构建、静态QA、全部62页联系表和重点图表放大检查的范围见最终QA报告。
