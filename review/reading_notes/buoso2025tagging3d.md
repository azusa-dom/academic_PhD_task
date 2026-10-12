# buoso2025tagging3d：阶段03阅读记录

作者授权的AI辅助工作稿。实际深度：SELECTED_FULLTEXT。

来源：https://pmc.ncbi.nlm.nih.gov/articles/PMC12049999/
版本：Publisher record: Journal of Cardiovascular Magnetic Resonance; volume 27; issue 1; pages/article 101869; issued [[2025]]
已读：Methods§2 synthetic generation/in-vivo/strain evaluation；Results external landmark与porcine；Fig1/9 captions。

原图／表像素：未检查，除非下列具体记录另作说明。未运行研究代码或下载受试者数据。

## 当前稿件用途与证据

### S03-83-01 / body.tex:170

稿件：`external human landmark comparison and porcine strain comparisons with manual cine annotations`

来源定位：Methods p0065,p0080,p0100;Results p0120。

证据：3Dtagging输入，CMAC外部人工landmarks；23porcinedatasets cine手工SegmentCMR参照。不是cine推理网络。

判断：SUPPORTED；当前窄主张与已读取来源相符；不外推材料真值或临床干预获益。

### S03-83-02 / supplement.tex:348

稿件：`manual reference has its own uncertainty`

来源定位：Methods p0080/0100。

证据：circumferential取midwall径变化、longitudinal取skeletonlength，radial用GL投影；参照是几何／人工估计量，勿全归为统一GL材料strain。

判断：SUPPORTED_WITH_QUALIFICATION；当前概述正确，若补写tensor公式须区分方向与实现。

## 边界与访问
本次阅读足以支撑所列窄主张；未声称全文及全部补充已读。

访问请求及失败详见sources/retrieval_log.csv；本地文件：sources/stage03/buoso2025tagging3d_crossref.json; sources/stage03/buoso2025tagging3d_epmc.json; sources/stage03/buoso2025tagging3d_full.xml; sources/stage03/buoso2025tagging3d_full.txt