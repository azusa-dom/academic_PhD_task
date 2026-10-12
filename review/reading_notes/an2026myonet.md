# an2026myonet：阶段03阅读记录

作者授权的AI辅助工作稿。实际深度：SELECTED_FULLTEXT。

来源：https://pmc.ncbi.nlm.nih.gov/articles/PMC13024448/
版本：Publisher record: Bioengineering; volume 13; issue 3; pages/article 310; issued [[2026, 3, 7]]
已读：Methods§2.1/2.2/2.6/2.7; Results§3.1/3.3及XML Table2；Discussion限制。

原图／表像素：未检查，除非下列具体记录另作说明。未运行研究代码或下载受试者数据。

## 当前稿件用途与证据

### S03-79-01 / body.tex:174

稿件：`Cine segmentations are converted to binary spatiotemporal inputs`

来源定位：§2.1/2.2。

证据：22 Dahl SS rats、64 SAX slices、20frames；manualcine masks，SinMod(InTag)displacement监督。

判断：SUPPORTED；当前窄主张与已读取来源相符；不外推材料真值或临床干预获益。

### S03-79-02 / body.tex:174

稿件：`0.973 and 0.975`

来源定位：Table2。

证据：MyoNet ICC Ecc .973 Err .975；ResMyoNet两项.955；参照SinMod分析，不是独立材料真值。

判断：SUPPORTED；当前窄主张与已读取来源相符；不外推材料真值或临床干预获益。

### S03-79-03 / supplement.tex:360

稿件：`Preclinical tagging-reference agreement; not human cine validation`

来源定位：§2.1; Discussion limitations。

证据：动物实验、binaryinput、标注参照三者均稿件正确；不采纳原论文“优于tagging”的未经独立真值证明推论。

判断：SUPPORTED；当前窄主张与已读取来源相符；不外推材料真值或临床干预获益。

## 边界与访问
本次阅读足以支撑所列窄主张；未声称全文及全部补充已读。

访问请求及失败详见sources/retrieval_log.csv；本地文件：sources/stage03/an2026myonet_crossref.json; sources/stage03/an2026myonet_epmc.json; sources/stage03/an2026myonet_full.xml; sources/stage03/an2026myonet_full.txt