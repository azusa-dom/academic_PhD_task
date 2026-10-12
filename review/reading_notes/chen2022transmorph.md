# chen2022transmorph：阶段03阅读记录

作者授权的AI辅助工作稿。实际深度：SELECTED_FULLTEXT。

来源：https://pmc.ncbi.nlm.nih.gov/articles/PMC9999483/
版本：Publisher record: Medical Image Analysis; volume 82; issue ; pages/article 102615; issued [[2022, 11]]
已读：PMC author manuscript §3.2.2/3.4/3.4.1；§4.1 dataset；§5uncertainty相关段。

原图／表像素：未检查，除非下列具体记录另作说明。未运行研究代码或下载受试者数据。

## 当前稿件用途与证据

### S03-64-01 / body.tex:148

稿件：`hybrid Transformer--convolutional architecture`

来源定位：Abstract; §3。

证据：hybridencoder/convdecoder, diffeo/Bayesvariant，brain和phantomCT；正确。

判断：SUPPORTED；当前窄主张与已读取来源相符；不外推材料真值或临床干预获益。

### S03-64-02 / supplement.tex:295

稿件：`uncertainty calibration`

来源定位：§3.4.1 and uncertainty results。

证据：主要明确appearanceuncertainty校准；不是任意displacementerror或regionalstrainerror被校准。

判断：SUPPORTED_WITH_QUALIFICATION；建议补appearance限定，保持非cardiacpathology证据边界。

建议：Brain MRI and phantom-to-CT registration; topology preservation and appearance-uncertainty calibration.

## 边界与访问
本次阅读足以支撑所列窄主张；未声称全文及全部补充已读。

访问请求及失败详见sources/retrieval_log.csv；本地文件：sources/stage03/chen2022transmorph_crossref.json; sources/stage03/chen2022transmorph_epmc.json; sources/stage03/generalreg_methods_web.json; sources/stage03/generalreg_web.json