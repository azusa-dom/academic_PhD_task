# balakrishnan2019voxelmorph：阶段03阅读记录

作者授权的AI辅助工作稿。实际深度：SELECTED_FULLTEXT。

来源：https://pubmed.ncbi.nlm.nih.gov/30716034/
版本：Publisher record: IEEE Transactions on Medical Imaging; volume 38; issue 8; pages/article 1788-1800; issued [[2019, 8]]
已读：arXiv v3 §IVMethods/IV-C1/IV-C2；Discussion；发表摘要。

原图／表像素：未检查，除非下列具体记录另作说明。未运行研究代码或下载受试者数据。

## 当前稿件用途与证据

### S03-63-01 / body.tex:148

稿件：`image-matching and smoothness objective`

来源定位：§IV-C Eqs4–7。

证据：MSE或localCC+diffusiongradientregularization；训练集amortized优化，testsingleforward。

判断：SUPPORTED；当前窄主张与已读取来源相符；不外推材料真值或临床干预获益。

### S03-63-02 / supplement.tex:293

稿件：`optional auxiliary segmentations`

来源定位：§IV-C2 Eq10。

证据：segDice作为可选训练信息，不能笼统把所有variant无监督化。

判断：SUPPORTED；当前窄主张与已读取来源相符；不外推材料真值或临床干预获益。

## 边界与访问
Author arXiv v3 TMI-linked manuscript; selected full methods, not all supplements.

访问请求及失败详见sources/retrieval_log.csv；本地文件：sources/stage03/balakrishnan2019voxelmorph_crossref.json; sources/stage03/balakrishnan2019voxelmorph_epmc.json; sources/stage03/voxelmorph_loss_web.json; sources/stage03/generalreg_web.json