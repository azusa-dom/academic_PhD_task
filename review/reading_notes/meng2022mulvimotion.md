# meng2022mulvimotion：阶段03阅读记录

作者授权的AI辅助工作稿。实际深度：SELECTED_FULLTEXT。

来源：https://pmc.ncbi.nlm.nih.gov/articles/PMC7613225/
版本：Publisher record: IEEE Transactions on Medical Imaging; volume 41; issue 8; pages/article 1961-1974; issued [[2022, 8]]
已读：Methods§III hybridnet/shape；§IV-A数据与split。

原图／表像素：未检查，除非下列具体记录另作说明。未运行研究代码或下载受试者数据。

## 当前稿件用途与证据

### S03-68-01 / body.tex:156

稿件：`580 UK Biobank subjects split into 450 for training, 50 for validation and 80 for testing`

来源定位：§IV-A dataset and training。

证据：580、450/50/80核实；multi-view SAX2CH4CH；sparse2Dedges弱shape监督，无3DmotionGT。

判断：SUPPORTED；当前窄主张与已读取来源相符；不外推材料真值或临床干预获益。

### S03-68-02 / supplement.tex:310

稿件：`Hybrid 2D/3D network`

来源定位：§III。

证据：FeatureNet2D+MotionNet3D，training形状正则，inference直接motion；正确。

判断：SUPPORTED；当前窄主张与已读取来源相符；不外推材料真值或临床干预获益。

## 边界与访问
本次阅读足以支撑所列窄主张；未声称全文及全部补充已读。

访问请求及失败详见sources/retrieval_log.csv；本地文件：sources/stage03/meng2022mulvimotion_crossref.json; sources/stage03/meng2022mulvimotion_epmc.json; sources/stage03/meng2022mulvimotion_full.xml; sources/stage03/meng2022mulvimotion_full.txt