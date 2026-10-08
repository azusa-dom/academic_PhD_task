# 合并与审查方案(v8.1 + v9 → v10 工作稿)

日期:2026-10-09。工作稿位于 `manuscript/`,基线输入保留在 `manuscript/baseline_inputs/`。

## 基线选择

- **v9 为正文基线**。理由:v9 已逐条纠正 v8.1 的数字(StrainNet 243/62 拆分、Wehner 88/186、Cao 87、Militaru 61 等),表格改为可交叉属性矩阵,51 条活动引用全部可解析、零重复,主文 23 页。
- **从 v8.1 回收的内容**(v9 删掉但对"算法方向的方法综述"必要):
  1. §3 方法谱系 1999–2026:FFD → groupwise B-spline → VoxelMorph/TransMorph/Fourier-Net → 心脏专用(Qin 2018 … STCMT 2026)→ 物理/力学约束 → DENSE 监督与端到端。v9 §3 只剩 6 行原型表和十来个方法名。回收后同时回答导师"几几年出了什么文章"。
  2. §3.1 "欠定问题与先验在做什么":配准目标函数式、表示容量/估计过程/输入信息三因素归因实验。v9 §5.3 保留了三个问题但丢了归因实验的操作逻辑。
  3. v8.1 §5.1 "针对预设局灶异常的测试":DeepStrain 在 MRXCAT2.0 四例(正常/DCM/HCM/梗死)上的具体结果(Dice 0.82、位移 1.0±0.9 mm、Ecc 误差 0.02±0.04、Err −0.24±0.21、梗死例 −0.20±0.21)及"worst"排序不能定量引用的限定;Yeon 2001 sonomicrometry 作为设计先例;"检索范围内未发现系统改变异常大小/严重度/跨壁度的研究"的空白陈述。这是全文中心问题的唯一直接证据,v9 的 Table 2 只剩一句"Exposes image/functional reference"。
  4. 对应的 31 条参考文献(v8.1 第二轮已对 Crossref/arXiv/DataCite 核实)。
- **不回收**:v8.1 重复的通用警示段落;v8.1 §4–§7 的长版本(v9 已用纠正后的数字重建);FDA K232661 与 DeepStrain 仓库引用(v9 补充材料 Note 6 已明确不审计此类记录);v8.1 的 StrainNet 段落(其 305 人写法有误,以 v9 为准)。
- **图件不动**:沿用 v9 六张图(字节一致)。图像版权问题(v8.1 OPEN_ISSUES A1–A3)不在本轮范围,仍属作者事项。

## 章节与 skill 对应

| 章 | 处理 | 主要审查视角 |
|---|---|---|
| 摘要 / Plain English | 微调一句(纳入预设局灶测试结论) | scientific-writing(摘要与结论一致性) |
| §1 问题界定与范围 | 沿用 v9,审查 | medical-imaging-review(范围、检索声明)、citation-management |
| §2 从图像到区域测量 | 沿用 v9,审查 | scientific-critical-thinking(反例的推断边界) |
| §3 估计器家族 | **合并重写** | academic-deep-research(方法演进矩阵)、citation-management |
| §4 验证文献 | **回收 §4.1 局灶测试**,其余沿用 | scientific-critical-thinking(评估协议、单位、参照不确定度) |
| §5 矛盾结果的调和 | 沿用,补一处交叉引用 | scientific-critical-thinking |
| §6 验证方案与资源 | 沿用,审查 | medical-imaging-review |
| §7 报告实践、§8 局限、§9 结论 | 沿用,结论补一句 | scientific-writing、peer-review |
| 补充材料 | 新增 Table S3(按年份的方法表,合并 v8.1 Tables 3+4) | academic-deep-research |
| 全稿 | 编译、引用完整性、术语一致、润色 | writing-assistant、pre-submission-reviewer |

## 交付方式

每章一个 `review/NN_*.md`:改动后的正文(仅变更的部分贴全文,未变更的部分给文件行号)+ 修改表(位置 / 改动 / 理由 / 来源)。每章完成即 commit 并推送。
