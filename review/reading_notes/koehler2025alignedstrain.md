# Aligned strain：患者纤维化分类与时间留出

[PMC原文](https://pmc.ncbi.nlm.nih.gov/articles/PMC12127955/)，DOI10.1148/ryai.240303，2025;7(3):e240303。读完整Methods、Results、Discussion及图注；未看原图/表像素、附录，故SELECTED_FULLTEXT。

单中心139男性DMD，57例2018–2019开发、82例2020–2023内部时间留出；无影像质量排除用于DL，不等于FT亦全部可用（正文说FT共14失败，测试集10）。DMD57四折+超过2000模型选择，后固定管线测试DMD82；“reproducibility”在此为后续数据泛化，不是scan–rescan。

KeyFrameDet五相，Seg2D分割，DeformReg估计ED2K/K2K位移；Fig3图注明确SSIM、smoothness、Dice损失，无LGE监督位移。LGE临床报告分段标签用于分组及下游分类；不能说整项研究仅患者层面——确有分段/时相关联与mixed-effects分析。最终分类目标是至少一段LGE阳性的患者；Discussion明确139人二分类不反映纤维化量/段级组织量。

论文用分段应变特征改进患者判别；保留EF、轻度纤维化假阴性与疾病依赖的局限。既不是瘢痕空间边界误差，也不直接证明材料轨迹或减少造影剂策略有临床获益。稿件目前对这几层的区分准确。摘要与Results的年龄不同，稿件未引，不据此修改无关内容。


## 阶段04自查

57开发/82同中心后续时间测试、无LGE形变监督及患者至少一段阳性的分类目标均支持。研究也有区域/相位与混合模型分析，不能批为全部实验仅患者层面。

实际回查位置：Study datasets; Fig2/3 captions; Experiments; Discussion。证据文件与散列见 stage04_self_check.csv；此记录不提高既有全文阅读等级。
