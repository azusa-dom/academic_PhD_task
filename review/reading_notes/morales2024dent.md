# DENT：有外部图像插值测试，未验证材料运动

[PMC期刊全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC11211941/)，DOI10.1148/ryct.230177，2024;6(3):e230177。已读Abstract、全部Materials/Methods与Results、Discussion/limitations、主图及视频图注；实看Table1和Fig1像素。未看附录/补图，未播放视频。

5840患者跨9中心是整个回顾性开发和测试资源，不是全部训练数据。前三中心5292分3177/1059/1056 train/val/internaltest，其余6中心548external。图1/表1确认；摘要4:1不能替代此划分。前瞻总76=57临床+19健康；B组61=49临床+12健康（组成见摘要）比两次独立采集25/50fps，C组42实时，非可直接相加的互斥组。

输入4相邻图像，预测多个形变和blending mask生成中间相位，用图像L1监督和验证PSNR选模型。A组移除真实相位再插值，RMSE为图像误差；B组因独立屏气和心率差只读者偏好比较；C组有降帧回填RMSE及50/100fps主观评价，没有真正100fps参照。不能把图像非劣效等同应变非劣效。

原文明确把strain列为未来用途，limitations明确未评价预测形变向量准确性、未评价高帧率临床价值。完整Methods/Results的终点清单为图像RMSE和读者评价，不包括应变或病灶恢复。无幻觉伪影的观察不是系统局灶保持验证；mask可能模糊亦是作者机制推测。文中读者偏好存在小内部错字：摘要/Key Points实际采集15/122，Results写14/122；后者加84+23只121，非劣效解释一句把−.10写作CI下界亦与前句−.01不一致。稿件未引这些数，本审计不猜改来源或新增入稿。总体方法层级表述可保留，最好明确5840包含测试人群。


补充正文措辞复查：supplement.tex:163用improved概括前瞻读者结果略宽；B为非劣效，C为描述性偏好趋势，建议分别表述。新增DENT-06。


## 阶段04自查

5840包含训练/测试，548外部测试明确；读者比较B为非劣效、C描述性偏好，不能统称显著改善；变形向量未验证是原文明示。

实际回查位置：Study Sample; Model Evaluation B/C; Results B; Discussion limitations。证据文件与散列见 stage04_self_check.csv；此记录不提高既有全文阅读等级。
