# 与 Codex 合并稿的对比,以及本稿的论证逻辑

日期:2026-10-09。比较对象:Codex 的 `Cine_CMR_methods_review_author_draft`(manuscript.md,主文约 6,161 词,10 章,4 表,3 图,69 条引用,md→docx/pdf)与本仓库 `manuscript/`(body.tex 约 9,750 词,9 章,4 主表 + 3 补充表,6 图,84 条引用,LaTeX)。审查视角:peer-review(论证结构与证据边界)、scientific-critical-thinking(具体主张是否被原文支持)、citation-management(引用与阅读深度)。

## 一、差距从哪里来

两份稿子起点相同(v8.1 + v9),差距主要不是写作水平,而是三个层面的选择不同。

**第一,对"这篇综述是什么"的回答不同。** Codex 把稿子重新定义为算法方法综述:题目改成 *Algorithms for myocardial motion and strain estimation from cine CMR: methods, measurement and validation*,摘要开头就讲算法如何建立对应关系,第 4 章是"方法发展与分类"(六个抽取维度:输入几何、形变表示、训练目标、时间参数化、先验、验证目标),第 8 章是"研究优先项"。本稿保留了 v9 的定位——*From routine cine CMR to regional myocardial dysfunction*,一篇围绕"区域/局灶异常能否被恢复"这个测量问题的批判性叙述综述——只是在 §3 里把方法谱系补回来。换句话说,Codex 写的是"方法综述,用测量逻辑约束";本稿写的是"测量问题综述,用方法谱系支撑"。导师如果要的是前者,Codex 的框架更贴近;如果要的是 v9 已经和导师讨论过的那条主线,本稿更贴近。这是作者要做的选择,不是哪一版"写得更好"。

**第二,核查深度不同。** Codex 为 69 条引用每条建了 source note,32 条有本地全文,135 条主张台账,并且在合并时重新读了若干关键原文,改出了四处实质修正(见第二节)。本稿的核查是:书目元数据全部联网核对(Crossref/arXiv/DataCite,0 错误),但正文事实沿用 v8.1/v9 已有的 claim ledger,没有重读全文。因此本稿在"数字是否正确"上依赖前两轮的记录,Codex 在这一点上更扎实。

**第三,产出形态不同。** Codex 交付 Word/PDF 可编辑稿,引用用工作用 numeric CSL;本稿交付 LaTeX 源码,沿用 v9 的 jcmr-review.bst 与编译/静态检查链。Codex 的包里有逐篇 source_notes、方法演化矩阵 CSV、检索日志;本稿的包里有逐章修改表、合并方案、图件重设计方案。两者互补,不冲突。

篇幅上 Codex 更紧(6.2k vs 9.7k 词),因为它把方法谱系压成一张"时期—代表工作—问题变化—解释边界"的表(Table 1)加一节分类讨论,本稿则按家族逐个方法写并把 36 行明细放进补充 Table S3。

## 二、Codex 做对而本稿原来做错或做弱的地方(已采纳或标记)

| 项 | Codex 的发现 | 本稿原状 | 处理 |
|---|---|---|---|
| MRXCAT2.0 的 DeepStrain 误差 | 0.02±0.04 / −0.24±0.21 是跨病例、跨切片的均值,不是瘢痕区内的恢复误差;"局灶梗死按该误差恢复"的写法已取消 | §4.1 写了"across all cases, including the infarcted case"并在 §5.3/§9/摘要把它说成"保住了周向分量",读者会以为瘢痕区周向应变被准确恢复 | **已改**:§4.1 两段、Table 2、Table 3、§5.3、§9、摘要共七处改为"case-averaged / slice-averaged … does not quantify recovery of the scar region" |
| 时序证据 | Brandt 2024 比较了 tagging 与 FT 的 global/segmental time to peak(ICC 0.56–0.82,无显著偏倚),"时序从未被研究"不成立 | §9 把 peak-time error 与质心/边界/范围并列为"uncommon or not reported" | **已改**:§4.2 加一句 Brandt 结果(本轮按 PubMed 摘要核实:42 人,17 子痫前期史、3 健康、22 LBBB),§9 改为"timing has been compared mainly at global and segmental level … rather than as focal peak-time error" |
| Fourier-Net+ | 正式版摘要含 3D cardiac MRI 评估(Dice、Hausdorff、容积、EF);v8.1 的"无心脏评估"归类错误 | v9 已经写对("its reported cardiac evaluation includes registration, geometric and functional measures"),本稿合并时保留了 v9 的句子,但又从 v8.1 带回"both are general-purpose registration networks … benchmarks"的表述,同一段内略有张力 | 当前文字仍一致(先说通用基准、再说心脏评估不证明区域应变),**不改**;作者可按口味删掉前半句 |
| Jahromi 2026 | 等效性检验的具体界值 ±3.5 percentage points、均值差 −2.7 points(Codex 读了全文) | 本稿只有定性表述 | **未加**:PubMed 摘要不含这两个数,本轮没有全文;列为作者核对后可补的项 |
| Motion Pyramid Networks 的 EPE | EPE 实验的运动场由另一个训练模型生成再合成图像,不是独立材料参照 | Table S3 只写"multiple metrics",没有引用 EPE,不受影响 | 无需改 |
| StrainNet 三个分母 | 305 / 243+62 / 59 拆开 | v9 已拆开,本稿保留 | 一致 |

## 三、本稿不打算跟 Codex 走的地方(及理由)

1. **保留 v9 的题目与中心问题。** v9 的 23 页稿、摘要、Plain English summary、结论都围绕"magnitude / location / extent / timing 四属性能否恢复"组织;这条线在 v9 的中文报告里是作者审阅过的主线。改成"算法综述"要重写摘要、§1、§9,属于作者决定。
2. **保留逐方法的 §3 与补充 Table S3,而不是 Codex 的时期表。** 导师的问题是"几几年出了什么",按方法逐条、带验证证据列出比按时期概括更直接;代价是篇幅。
3. **保留 LaTeX 与 v9 的 QA 链。** v9 在 CSF3 上的构建、哈希、静态检查都基于这套源码,换成 md→docx 会丢掉这些可追溯性。

## 四、本稿的论证逻辑(逐章一句话)

- **§1** 区域功能是独立于 EF 的测量问题;预后关联证明"值得测",不证明"测得准";中心问题是四属性在给定采集/估计器/定义下能否在容差内恢复。
- **§2** cine 只提供边界、强度和时间线索,不提供材料点标签;同一轮廓可以对应不同的材料映射(解析反例);应变是映射的导数,其数值取决于完整的估计量定义。
- **§3** 所有估计器都在解同一个欠定问题(式 3),差别在于加了什么结构;表示容量、估计过程、输入信息是三个可分别检验的失败点;1999–2026 的方法按家族展开,年表在 S3;读完记录得到三个模式——模态证据是 mask/landmark 一致、材料敏感参照几乎只在健康/混合人群、病理列基本空白。
- **§4** 证据按验证目标而非算法年代组织:已知运动证明容量与技术误差(唯一的预设局灶测试是 DeepStrain/MRXCAT2.0,结果是分量特异的切片均值);配对 DENSE/tagging 证明匹配定义下的一致性(周向强于径向);重复性证明精度不证明准确;LGE 证明组织关联不证明运动误差;结局是下游证据。
- **§5** 看似矛盾的结果在拆开估计量后可以并存:全局一致与区域不一致并存;径向应变是定义敏感的压力测试;正则化既能稳定也能偏置,三个问题要分开问;不确定性图不等于校准误差。
- **§6** 一个可辩护的区域主张需要先定测量合同,再按"已知运动 → 配对材料敏感 → 组织/决策"三阶段递进;STRAUS、Stanford、CMAC、MRXCAT 各自只能回答链上一段;重建改变输入,结论限定于终点。
- **§7–§8** 报告要把采集、估计器、估计量、统计单位、验证目标、失败策略写在一处;本综述是定向检索、无双人筛选、不合并效应量。
- **§9** 支持最强的是匹配定义下的整切面/全局/AHA 节段周向应变;径向与更局部的主张支持变弱;唯一的预设局灶测试给出分量特异、切片均值的结果;"信息不足/平滑/低维偏置"仍是假设,除非实验分离三因素。

这条逻辑的骨架是 v9 的,Codex 的骨架是"方法—机制—验证—优先项"。两者都自洽;区别在于把"方法"还是"测量问题"放在第一位。

## 五、建议

把 Codex 的三样东西并进本仓库而不是二选一:`source_notes/`(逐篇阅读深度记录)、`extraction/method_evidence_matrix.csv`(40 条方法矩阵,比本稿 S3 多"baseline 协议、数据划分、未检查细节"三列)、`claim_ledger.csv`(135 条)。然后由你和导师决定题目与第一章走哪条线;其余章节两版的事实层已经基本对齐。
