# ye2021deeptag：阶段03阅读记录

作者授权的AI辅助工作稿。实际深度：SELECTED_FULLTEXT。

来源：https://doi.org/10.1109/CVPR46437.2021.00718
版本：Publisher record: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR); volume ; issue ; pages/article 7257-7267; issued [[2021, 6]]
已读：CVF paper §3 composition/globalLagrangianloss；§4.1/4.2 data/landmarks；ResultsTable1。

原图／表像素：未检查，除非下列具体记录另作说明。未运行研究代码或下载受试者数据。

## 当前稿件用途与证据

### S03-77-01 / body.tex:170

稿件：`differentiable composition layer to recover the Lagrangian field`

来源定位：§3 Eqs9–12。

证据：相邻tMRI双向微分同胚motion可微composition到referenceframe；确非普通cine。

判断：SUPPORTED；当前窄主张与已读取来源相符；不外推材料真值或临床干预获益。

### S03-77-02 / supplement.tex:346

稿件：`Clinical tagging dataset; landmark tracking accuracy and efficiency`

来源定位：§4.1–4.2。

证据：230seq split140/30/60来自不同subjects；两clinicalexperts标注每seq8–32landmarks，用RMSdistance；不是dense已知strain。

判断：SUPPORTED；当前窄主张与已读取来源相符；不外推材料真值或临床干预获益。

## 边界与访问
本次阅读足以支撑所列窄主张；未声称全文及全部补充已读。

访问请求及失败详见sources/retrieval_log.csv；本地文件：sources/stage03/ye2021deeptag_crossref.json; sources/stage03/ye2021deeptag_epmc.json; sources/stage03/ye2021deeptag_cvf.pdf; sources/stage03/ye2021deeptag_cvf.txt