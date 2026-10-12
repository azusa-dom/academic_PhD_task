# fu2026cinema：阶段03阅读记录

作者授权的AI辅助工作稿。实际深度：SELECTED_FULLTEXT。

来源：https://pmc.ncbi.nlm.nih.gov/articles/PMC13396196/
版本：Publisher record: Communications Medicine; volume 6; issue 1; pages/article 408; issued [[2026, 5, 13]]
已读：Final XML Introduction Par9; Methods Par11,15,17,21–24; Table1任务清单及相关Results。

原图／表像素：未检查，除非下列具体记录另作说明。未运行研究代码或下载受试者数据。

## 当前稿件用途与证据

### S03-73-01 / body.tex:158

稿件：`15 million cine images from 74,916 studies`

来源定位：Methods Par11/21; Introduction Par9。

证据：超过15M images，74,916 studies，UKB首次及重复成像均入；不得改写为74,916独立患者。

判断：SUPPORTED；当前窄主张与已读取来源相符；不外推材料真值或临床干预获益。

### S03-73-02 / body.tex:158

稿件：`The retrieved task descriptions do not include dense motion estimation`

来源定位：Methods downstream tasks, Table1。

证据：完整任务表包含分割、landmarks、EF、MAPSE/GLS、疾病和survival；无dense deformation任务。GLS是ED/ES心室长度变化，非稠密材料跟踪。

判断：SUPPORTED_WITH_QUALIFICATION；限定为所报任务；勿扩大为完全没有运动相关功能量。

### S03-73-03 / supplement.tex:330

稿件：`diagnosis, prognostication across independent datasets`

来源定位：Table1; Methods Par17/24。

证据：CineMA有生存预测；并非两个模型均做prognostication；UKB下游同来源且包含重复visit。

判断：SUPPORTED_WITH_QUALIFICATION；合并行容易把任务／独立性套给两篇，建议分列。

建议：CineMA: segmentation, landmark-derived function, diagnosis and exploratory survival prediction; CMR-FM: classification, segmentation, landmark localisation and pathology detection. Neither task list reports dense motion estimation.

## 边界与访问
本次阅读足以支撑所列窄主张；未声称全文及全部补充已读。

访问请求及失败详见sources/retrieval_log.csv；本地文件：sources/stage03/fu2026cinema_crossref.json; sources/stage03/fu2026cinema_epmc.json; sources/stage03/fu2026cinema_full.xml; sources/stage03/fu2026cinema_full.txt