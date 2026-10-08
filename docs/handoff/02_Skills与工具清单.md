# Skills 与工具清单

整理依据是实际项目日志和可读的本地 skill 文件。以下“实际应用”指执行日志记录了对应操作及产物，本次没有重跑这些研究任务。“可用”仅表示本地有文件；“已打包”不证明执行过。

## 当前综述的核心 skills：v9 有执行记录

这 10 个 skills 采用 v9 任务的项目快照，具体执行证据保存在交接包 `evidence/V9_SKILL_EXECUTION_LOG.md`。快照可能与 `/Users/hydra/.codex/skills/` 中较新的版本不同，不静默替换。

| Skill | 工作职责 | v9 日志中的实际产物 |
|---|---|---|
| `medical-imaging-review` | 医学影像综述路线、范围、出处与项目状态 | narrative 路线、上下文、原子主张台账和审计 |
| `literature-review` | 问题驱动检索与跨论文综合 | 检索时间线、按估计量/尺度/参考组织的综合 |
| `citation-management` | DOI/PMID/元数据和 BibTeX 检查 | 文献核查与引用验证；保留 98 条源库、使用 51 条活跃引用 |
| `scientific-critical-thinking` | 估计量、参考、统计单位、替代解释 | 主张来源台账和数据集/队列关联记录 |
| `peer-review` | 内部科学评阅与回应 | 评阅回应表；属于同一流程内部评阅 |
| `scholar-evaluation` | 定性评价贡献和证据充分性 | 定性评估，不提供接收概率或研究者排名 |
| `academic-writing` | 论证重组、反向提纲和正文修订 | 章节、表格和结论重写 |
| `scientific-writing` | 数值一致性、声明、证据及构建追溯 | 作者待办、AI 声明、QA 与图件哈希记录 |
| `writing-assistant` | 连续段落、术语统一和语言精修 | 英文终校与术语修订，保留证据限定词 |
| `venue-templates` | 目标期刊格式和官方要求核查 | 有日期的 JCMR 要求记录和投稿准备材料 |

## 选题、写作与图件工具箱

下列目录也随包附带。它们是供本人迁移的原始本地副本，是否执行、是否适合当前任务、是否缺依赖应另行判断。

| Skill | 用途 | 使用状态或选择条件 |
|---|---|---|
| `literature-search` | 关键词、筛选边界、阅读清单和检索记录 | 2026-10-07 研究方向交接记录明确使用 |
| `academic-deep-research` | 跨论文证据矩阵、争议与机会图 | 同一交接记录明确使用 |
| `deep-research` | Supervisor-Skills 的综述级研究流程 | 本地工具箱；与上一项不是同一个 skill，按具体任务选择 |
| `idea-evaluator` | 候选问题、可行性与最近邻差异评估 | 本地工具箱；医学意义与验证资源优先于泛化评分 |
| `paper-writer` | 根据已核实材料起草正文 | 本地工具箱；不生成未发生的方法和结果 |
| `paper-polish` | 忠实润色、去模板表达 | Claude v8 二轮任务有项目快照；本包采用仓库当前副本 |
| `pre-submission-reviewer` | 稿件逻辑、写作和投稿前检查 | 同上；不能替代作者、编辑或正式同行评审 |
| `vibe-research-workflow` | coding / figure / writing 阶段分工 | 工作流指导工具；不据此宣称 AI 提高了特定倍数效率 |
| `drawio-reconstruction` | 可编辑图件重建、导出和审计 | 六图与 v8.2 有应用记录；本包采用当前仓库副本，未保证与旧任务完全同版 |
| `medical-ai-figure-workflow` | 我的医学与 AI 图件规划、预览、修订和交付规则 | 本地个人工作包；当前可读，不将可用性当历史执行证明 |
| `scientific-figure-suite` | 图件路由、面板、箭头、图注、审计和包装 | 六图任务有项目副本；本包采用当前安装副本 |
| `scientific-visualization` | 有真实数据依据的定量图与导出审查 | 本地可用；仅在需要数值绘图时选择 |
| `scientific-slides` | 科研汇报、PPT/Beamer | 2026-10-07 分享包存在；不能据此断言日常使用或依赖已安装 |
| `pptx-posters` | 可编辑科研 PowerPoint 海报 | 分享包存在；有独立固定依赖及人工检查要求 |

## 可发现但未随核心包复制的工具

`nature-figure`、`matplotlib`、`seaborn`、`scientific-schematics`、`scientific-brainstorming`、`experimental-design`、`hypothesis-generation`、`pydicom`、`matlab`、`pdf`、`docx`、`pptx`、`image-to-ppt` 等在当前技能目录中可发现。这里列出它们用于后续按需查找，不声称全部用于现有项目。优先获取原始发行包及其许可证，不将整个技能库都导入。

当前 `pydicom` skill 示例要求的版本与旧 DENSE 项目实际使用的 2.4.4 不同；当前 PPT 海报 skill 的 Pillow/lxml 固定要求也与旧绘图环境不同。技能版本更新不能自动改变已有科研环境。

Codex 插件提供的 documents、presentations、spreadsheets、Pages、Sites、Figma、CUA，以及本次会话里的 web 和 imagegen，是平台工具或连接器。它们不是仅靠复制 `SKILL.md` 就能迁移的普通 Python 包。Claude 需要自己的连接器、MCP、CLI、浏览器或生成服务，并重新确认访问是否可用。

`imagegen` 适用于获授权的概念视觉或图片编辑；不能生成伪装成真实患者的 MRI，也不属于 v9 纯文本修订流程。`CLI-Anything` 是 CLI 桥接/工程工具，ScholarWeave 有相关原型实现；其他仓库被克隆不等于已安装并用于科研。See-through 与 LivePortrait 属于旁支。

## 使用路由

| 当前任务 | 主要 skill | 必要时补充 |
|---|---|---|
| 寻找候选课题 | `literature-search` → `academic-deep-research` | `idea-evaluator`、`scientific-critical-thinking` |
| 修改 cine-CMR 叙述综述 | `medical-imaging-review` | `literature-review`、`citation-management`、`scientific-writing` |
| 检查某个论断的证据 | `scientific-critical-thinking` | `citation-management`、`peer-review` |
| 起草有证据的段落 | `academic-writing` 或 `paper-writer` | `scientific-writing` |
| 精修已有文字 | `writing-assistant` 或 `paper-polish` | 保留原稿与修改说明 |
| 制作或修改医学示意图 | `medical-ai-figure-workflow` | `scientific-figure-suite`、`drawio-reconstruction` |
| 绘制真实数据的数值图 | `scientific-visualization` | 实际 plotting backend 和对应环境 |
| 内部审查与投稿准备 | `peer-review` | `pre-submission-reviewer`、`venue-templates` |
| 制作科研汇报或海报 | `scientific-slides` / `pptx-posters` | 独立 presentation 环境与实际渲染检查 |

这些是根据已存在工作整理的建议路由，不能误称每个项目都逐项执行过。按任务阅读必要部分并记录实际使用，不要求每次调用全部 skills。

## 迁移限制

原文件保留其 frontmatter、references、scripts、assets 和许可证文件。部分 skill 含 Codex 路径示例、项目内 `.codex/scientific-figure-memory` 记录或外部 API/工具依赖。项目内记录目录只是存储约定；不要把它误认成 Claude 已有的系统能力。按实际安装位置解析 `SKILL_DIR`，不要将旧 Mac 的绝对路径当跨机器入口。

Supervisor-Skills 的部分参考材料提及仓库 `handbook/`，本核心包没有复制整套 handbook；需要时回到原仓库阅读。不同 skill 的许可证声明可能与仓库级声明不同，本包保留原声明并在 provenance 中记录，未作统一许可或公开再分发结论。本包供本人在自己的 Claude 环境迁移使用。
