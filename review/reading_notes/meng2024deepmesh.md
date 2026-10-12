# meng2024deepmesh：阶段03阅读记录

作者授权的AI辅助工作稿。实际深度：SELECTED_FULLTEXT。

来源：https://pmc.ncbi.nlm.nih.gov/articles/PMC7615801/
版本：Publisher record: IEEE Transactions on Medical Imaging; volume 43; issue 4; pages/article 1489-1500; issued [[2024, 4]]
已读：Methods§III template/mesh/motion/rasterizer P14–32；Introduction功能定义。

原图／表像素：未检查，除非下列具体记录另作说明。未运行研究代码或下载受试者数据。

## 当前稿件用途与证据

### S03-69-01 / body.tex:156

稿件：`maintaining temporal vertex correspondence and common template indexing`

来源定位：MethodsP14–32。

证据：固定templatevertex/faces保证计算索引；不是证明组织材料跨时空对应；正文限制合理。

判断：SUPPORTED；当前窄主张与已读取来源相符；不外推材料真值或临床干预获益。

### S03-69-02 / supplement.tex:312

稿件：`unsupervised via differentiable rasteriser`

来源定位：MethodsP31–32。

证据：rasterizer将3Dmesh变2Dsoftcontours并与groundtruth2Dseg比较，监督由shape提供。

判断：PARTIALLY_SUPPORTED；不使用motionGT不等于无标注；与MulViMotion表格术语应一致。

建议：SAX and LAX cine; no motion-field labels, with weak supervision from 2D segmentations through a differentiable rasteriser.

## 边界与访问
本次阅读足以支撑所列窄主张；未声称全文及全部补充已读。

访问请求及失败详见sources/retrieval_log.csv；本地文件：sources/stage03/meng2024deepmesh_crossref.json; sources/stage03/meng2024deepmesh_epmc.json; sources/stage03/meng2024deepmesh_full.xml; sources/stage03/meng2024deepmesh_full.txt

## 阶段04自查

2D参考分割经rasterizer作形状监督明确。无3D运动标签与无任何监督不是同一命题；补表改弱监督。

实际回查位置：Methods III-C P31–35; Training P39。证据文件与散列见 stage04_self_check.csv；此记录不提高既有全文阅读等级。
