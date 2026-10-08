# 结果报告（v8 漏斗式批判性综述）

**日期**：2026-10-08 · **作业状态**：**未全部完成**——批处理作业在第 9 阶段（投稿材料包）开始前触及用量上限并停止。
**必须分清**：下面写的"完成"只表示**作业跑完了这一步、产物存在、机器检查通过**；不等于科学正确、不等于人工审阅通过、更不等于可以直接投稿。

---

## 一、已经做出来的东西

| 交付物 | 状态 | 说明 |
|---|---|---|
| `manuscript_v8/`（`main.tex`、`body.tex`、`references.bib`、`supplement.tex`、`jcmr-review.bst`、6 个矢量图 PDF） | 完成 | 全文改写完毕 |
| `manuscript_v8/v8_main.pdf` | 完成 | **50 页**，正文 11,163 词，零 LaTeX 警告、零错误 |
| `manuscript_v8/v8_supplement.pdf` | 完成 | 2 页：检索记录、训练期 vs 推理期对照图 S1、条件可恢复性的报告格式 |
| `manuscript_v8/scripts/build_v8.sh` | 完成 | 可复现编译（tectonic 或 pdfLaTeX+BibTeX） |
| `manuscript_v8/scripts/static_qa_v8.py` | 完成 | 引用/标签完整性、图表顺序、缩写首次展开、英式拼写、单位格式；出错即非零退出 |
| `manuscript_v8/figure_alt_text.md` | 完成 | 6 条 alt text，按要求与图注分开 |
| `figures_v8/` | 完成 | v8 drawio（只改 1 处）、6 页 PDF+PNG、`figure_change_log.md`、contact sheet |
| `REVISION_MAP.md`、`CHANGELOG.md` | 完成 | 原稿行号 → v8 章节；结构/删除/新增/移除文献 |
| `qa/new_references_verification.csv` | 完成 | 47 条新文献逐条核实 + 3 条图像出处 |
| `qa/claim_audit.csv` | 完成 | 66 条新增定量/比较陈述，注明来源位置与阅读深度 |
| `qa/additional_verification_20261008.md` | 完成 | 本轮补做的内容核实与**三处被纠正的说法** |
| `qa/internal_peer_review.md`、`qa/response_to_internal_review.md` | 完成 | 两种审稿人身份，17 条意见，逐条处理 |
| `qa/funnel_logic_review.md`、`qa/final_proofread.md`、`qa/word_count.md` | 完成 | 漏斗逻辑、终校、字数 |
| `OPEN_ISSUES.md` | 完成 | 分 A（阻塞项）/B（指南未核实项）/C（科学待办）/D（篇幅） |
| `delivery_manifest.json`、`review_v8_delivery.zip` | 完成 | 54 个交付物的哈希；**27/27 输入哈希全部一致，输入未被改动** |

### 关键改写决策

1. **题目**：*Recovering regional myocardial dysfunction from routine cine CMR: methods, validation evidence and open questions*。理由：同时点出临床对象、模态限制和"方法→验证→空白"三段式，且不把标题写成疑问句。
2. **中心问题**作为独立引文块放在 §1，§7.3 明确回答。原稿的 conditional recoverability 从全文主轴降为 §6.1 的一个紧凑定义。
3. **§3 基本重写**（3,266 词，占 29%），覆盖 1999–2026 年各方法家族，并新增 35 行 × 2 的对比表：**Table 3 写"做什么"，Table 4 写"怎么验证的、有没有在病理/局灶异常上评估过"**。查不到的格一律写 `not reported`（共 19 格），不猜。
4. **§5 是漏斗收窄处**，分四类证据写，并且**刻意反驳自己最强的那条证据**（见下）。
5. **守住了五条禁区**：不预设"现有方法会抹平异常"；不把几何指标写成"算法必然失败"；不把 LGE/AUC/预后当运动准确性；不混淆 k-space 频率与运动场频率；不写"平滑位移 = 不能表示局部应变"（§3.1、§6.3 明确反驳）。逐条检查记录在 `qa/funnel_logic_review.md` 第 3 节。

### 本轮纠正的事实错误（重要）

- **MRXCAT2.0 评估 DeepStrain 的那段**：原稿和你的工作笔记都写"径向应变低估、梗死病例最严重"。我把 MRXCAT2.0 **全文**读了（Europe PMC PMC10116689）。论文正文确实这样说，**但它自己报的数字不支持这个排序**：总体径向误差 −0.24±0.21，梗死病例 −0.20±0.21（绝对值更小）。v8 两者都写，并明确说"不能当成定量排序引用"。
- **Emidec 数据集**：只有延迟强化图像，**没有 cine**。原先的表格行写错了，已改。
- **CMRxRecon2024**：摘要正文取不到，所以 v8 **不写**受试者数和划分，并在表下加了说明。
- **`bell2026inr`**：无法核实其采集方式（原稿说是 tagging MRI），已改成"记录中无摘要，故不描述"，表格该行全部 `not reported`。

---

## 二、没有通过 / 没有做的检查（如实列出）

### 完全没做的交付物
1. **`submission_package/` 整个目录没有建**：cover letter、推荐审稿人、pre-submission enquiry、JCMR 合规清单、**Graphical abstract**、作者确认清单、`DELIVERY_STATUS.json` 都不存在。作业在这一步触及用量上限。
   - 其中 **Graphical abstract 是 JCMR 明文要求的强制项**（`qa/jcmr_guidelines_notes.md`），没有它不能投稿。
2. **`作者理解指南.zh-CN.md` 没有写**。这是你明确要求的"不只要好看的文本，还要懂背后的知识"那一份，优先级在任务书里排最后，所以被牺牲掉了。

### 没有通过或无法核实的检查
3. **图像版权（阻塞）**：Figure 2 的 "Wehner 2015" 对应两篇候选论文，无法确定是哪一篇哪一幅；Kaggle DSB case 233 的再发布权未查；**Figure 1 a/c 面板里的真实 cine 图像根本没有任何出处标注**。三项都写进 `OPEN_ISSUES.md` A1–A3，原图注一字未改，没有编造来源。
4. **JCMR 指南有 6 项读不到**（`UNVERIFIED-1`…`-6`）：官方缩写表下载不到；Review 摘要是否必须结构化及字数上限不明；推荐审稿人政策不明；预印本政策、cover letter、ORCID、行号、双倍行距、是否盲审不明；是否需要 demographics/Limitations 不明；APC 与许可不明。
5. **篇幅比例有两处没达标**：§7 占 4.8%（任务书写 5–8%），§4 占 16.4%、§5 占 16.5%（任务书写约 15%）。我没有为了凑比例加水或删证据。
6. **没有独立双人筛选**，全文所有"未检索到…"的说法都只在本次记录的检索范围内成立——这一点在 §1.1、§3.3、§5.1、§6.3 和 §7.2 都原地写明了。
7. **内部同行评审不是独立评审**：是同一条流水线换两种身份自评，`qa/internal_peer_review.md` 开头已声明。
8. **阅读深度**：112 条文献里只有 MRXCAT2.0、Militaru（Detailed Results/Fig.5/Fig.7）、Jahromi（Eqs.1–6/Results）、Goetze（Table 2）是全文或指定段落读的，其余是摘要级。所有定量陈述的阅读深度逐条记在 `qa/claim_audit.csv`。**书目核实 ≠ 全文核实**。
9. **图件是否"与正文一致"以你本人目视确认为准**。我做了机器检查（页数、尺寸、非空）和逐页看图，但这不等于你的最终认可。

### 通过了的检查
- 编译：主文件与补充材料最后一遍 pdfLaTeX **零警告零错误**。
- 引用：112 条 bib 条目，112 条被引用，0 条缺失、0 条多余。
- 图表：5 图 9 表 1 公式全部被正文引用，且首次引用顺序与编号顺序一致（修了 1 处）。
- 缩写：首次出现均有全称（修了 3 处）。
- 拼写：全文英式，无美式变体。
- 终校中发现并修掉 5 处缺陷，记录在 `qa/final_proofread.md`。
- 输入完整性：27/27 哈希一致。

---

## 三、接着做什么（按优先级）

1. 建 `submission_package/`：先做 **Graphical abstract**（由 Figure 1 的概念链简化，仍然只改 drawio），再写 cover letter、推荐审稿人（4–6 位，标注"作者须自行核实"，不编邮箱）、pre-submission enquiry、合规清单、`DELIVERY_STATUS.json`（人工审批类字段不得填 passed）。
2. 写 `作者理解指南.zh-CN.md`。
3. 解决 `OPEN_ISSUES.md` A1–A3 的图像版权。
4. 发 review proposal 给 jcmroffice@scmr.org（本流水线没有也不会联系任何人）。
5. 下载官方缩写表并对齐（`UNVERIFIED-1`）。

所有产物都已 git 提交，从任一提交处都可以续跑。
