# zoya-paperhelper

一个用于 Claude Code / Claude Agent Skills 的单篇论文精读 skill：**重走作者的研究路线，并找出问题。**

它把读一篇论文拆成三层，外加一轮自我反驳：

1. **重走研究路线**：先写下作者的结论，再按"已有认识 → 缺口 → 假设 → 设计 → 数据 → 方法 → 评价 → 结果 → 结论"重建路线，标出作者真正做选择的**决策分叉**（替代做法是什么、换了结果会怎么变），以及相邻两步接不上的**路线断点**。
2. **核对证据**：为每条核心结论建主张–证据台账（支撑图表、成立条件、未被证明的部分），每句话标注 [原文事实] / [作者推断] / [读者推断] / [未报告]；用十个探针（关键支点、构念一致性、参考标准、统计单位、泄漏、多重比较、混杂、外部有效性、效应量、数字内部一致性）找问题，并按致命 / 限定 / 次要分级。
3. **自我反驳**：替作者辩护，删掉论文已经回应或只是偏好之争的批评。
4. **下一步**：可借鉴的、要避开的、引用时怎么写才不超出证据、还没被回答的问题及最小实验。

不同研究类型用不同的尺子（`references/study_type_rulers.md`）；心脏影像运动/应变论文另有领域检查（`references/cardiac_motion_strain.md`）。

## 安装

把整个 `zoya-paperhelper/` 目录复制到项目的 `.claude/skills/` 或用户级 `~/.claude/skills/` 下即可。

## 用法示例

- "精读这篇，帮我重走作者的思路并找问题：<PDF 或 DOI>"
- "这篇 StrainNet 的结论能信到什么程度？"
- "Deconstruct this paper and tell me what I can borrow for my own strain project."

## 示例与测试

`examples/wehner2018_example.md` 是对一篇开放获取的 cine FT–DENSE 一致性研究的完整示例输出；`evals/iteration-1_summary.md` 记录了与不加载 skill 的基线对比。

## 状态与局限

v0.1.0 草稿。输出是 AI 辅助的单人精读，不等于独立同行评审；关键数字在使用前应对照原文核实。致谢与许可见 `NOTICE.md`。
