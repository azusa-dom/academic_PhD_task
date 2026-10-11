# cine-CMR v10 审查摘要

本轮只读审查已覆盖主文36页、补充20页、全部科学图表与图注，并对决定性主张核查原始来源。没有改稿、改图或开展实验。全文报告及证据表在 `/mnt/iusers01/fatpou01/bmh01/f12147zh/codex-slurm/csf3_v10_readonly_review_20261011_012543/review/`。

文章值得保留的主线是：把cine图像线索、估计对应、strain定义和验证终点分开，承认特定whole-slice/global/segment Ecc的正面证据，同时不把它扩展为focal位置、范围和时间的完整验证。StrainNet两类测试、MRXCAT切片平均误差以及重建研究的端点边界，在现稿中大体解释准确。

优先处理两项已确认主要问题：

- **A01：训练与验证混淆。** DLSS以配准4D-flow速度训练，读者壁运动评分用于测试；aligned strain先学形变，后做LGE分类。当前段落/S3把整个流程写成下游标签监督，需按模块拆清。
- **A02：证据地图的读深/分类/计数不一致。** 摘要未提及不能升级为全文未报告；当前14个material加1个focal，与lane合计15不一致。需要统一定义并保留unknown。

三项局部修复：**A03** FT–tagging的全球径向ICC上限应为0.63，0.81属于FT–FT；**A04** REGAIN跨方案LoA应与同法scan–rescan precision区分；**A05** Figure4不能凭SD重叠推断病例间无排序。

仍待材料确认：**B01** 当前citation/读深映射和历史筛选记录如何支持现稿两个具体缺失性结论；**B02** Jahromi的3.5%等效性界值是否有预先指定依据。后者数值和给定界值内等效本身有原文支持。三项可选建议涉及投影损失定义、实际插入尺寸的小字和章节衔接，不是科学错误。

独立计数：主文引用93个不同key，补充81个，并集94个；不是94项纳入研究。核查表39行包含已确认、部分支持和未核查状态，未声称94篇全文审计。输入校验结论见[最终校验](/mnt/iusers01/fatpou01/bmh01/f12147zh/codex-slurm/csf3_v10_readonly_review_20261011_012543/audit/input_integrity_after.json)；无输入修改。审查完成不等于论文通过。

建议阅读顺序：[完整报告](/mnt/iusers01/fatpou01/bmh01/f12147zh/codex-slurm/csf3_v10_readonly_review_20261011_012543/review/REVIEW_REPORT_ZH.md) → [意见表](/mnt/iusers01/fatpou01/bmh01/f12147zh/codex-slurm/csf3_v10_readonly_review_20261011_012543/review/FINDINGS.csv) → [主张证据核查](/mnt/iusers01/fatpou01/bmh01/f12147zh/codex-slurm/csf3_v10_readonly_review_20261011_012543/review/CLAIM_EVIDENCE_AUDIT.csv) → [覆盖与访问限制](/mnt/iusers01/fatpou01/bmh01/f12147zh/codex-slurm/csf3_v10_readonly_review_20261011_012543/review/READING_AND_COVERAGE.md)。运行状态见[REVIEW_STATUS.json](/mnt/iusers01/fatpou01/bmh01/f12147zh/codex-slurm/csf3_v10_readonly_review_20261011_012543/review/REVIEW_STATUS.json)。
