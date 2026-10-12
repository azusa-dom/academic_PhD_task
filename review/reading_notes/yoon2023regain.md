# REGAIN：采集、重建与下游分析的联合比较

[原文](https://pmc.ncbi.nlm.nih.gov/articles/PMC10315558/) DOI10.1148/radiol.222878，2023;307(5):e222878。已读全部相关Methods/Results/Discussion、图注；原Fig4像素已看。附录与补表未读；网页与本地HTML身份一致。

单中心3T Siemens；2018–2021回顾性1616患者训练，仅无视觉伪影图像，低分辨率输入由删外侧相位编码构造。2021–2022前瞻181人（126患者55健康），并非外部中心。屏气组130（94+36），实时组100（61+39），49重叠；与应变分析恰同为49并不证明两组逐人相同。应变子组来自有长轴的49人，cvi42 5.11.1，人工可修正轮廓。

Methods Model Evaluation明确独立采集常规GRAPPA与REGAIN cine，非同一k-space只换算法。Fig4原图n49、三方向均值取整0，GRS LoA−7至6、GCS−2至3、GLS−3至3，单位是绝对应变百分点；稿件数字正确，%宜改percentage points，避免相对误差。正文与Fig4吻合。此为全局FT的一致性，不能隔离采集变异、重建与估计器误差；不是局灶保存验证。

全部Results仅全局应变/容积/质量；没有局灶异常恢复端点。单中心、vendor/场强固定、半自动轮廓是作者明示限制。无新实验或代码复算。


## 阶段04自查

1616/181/130=94+36/49分母分别有据；独立GRAPPA采集可核。再次看Fig4A，GRS/GCS/GLS LoA依次−7至6、−2至3、−3至3，改单位为百分点，数值不改。

实际回查位置：Methods Model Evaluation / Image Interpretation; Results Breath-hold; Fig4A。证据文件与散列见 stage04_self_check.csv；此记录不提高既有全文阅读等级。
