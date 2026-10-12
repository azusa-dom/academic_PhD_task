# arratia2023warppinn：阶段03阅读记录

作者授权的AI辅助工作稿。实际深度：SELECTED_FULLTEXT。

来源：https://pubmed.ncbi.nlm.nih.gov/37598608/
版本：Publisher record: Medical Image Analysis; volume 89; issue ; pages/article 102925; issued [[2023, 10]]
已读：arXiv Methods§2.3 loss/FFM；abstract synthetic and15healthy benchmark；实验/限制相关段。

原图／表像素：未检查，除非下列具体记录另作说明。未运行研究代码或下载受试者数据。

## 当前稿件用途与证据

### S03-76-01 / body.tex:164

稿件：`hyperelastic regulariser and a Jacobian penalty`

来源定位：§2.3 Eqs2–3。

证据：dataintensity+neoHookean TrC-3-2logJ+lambda(J-1)^2；Jac项属于hyperelasticregularizer，不应当两个独立physicsprovenance。

判断：SUPPORTED；当前窄主张与已读取来源相符；不外推材料真值或临床干预获益。

### S03-76-02 / body.tex:164

稿件：`Strain follows by automatic differentiation`

来源定位：Abstract/§2。

证据：连续neuraldeformation、AD、Fourierfeatures；synthetic和15healthyCMAC正确。

判断：SUPPORTED；当前窄主张与已读取来源相符；不外推材料真值或临床干预获益。

### S03-76-03 / supplement.tex:335

稿件：`focal abnormality not evaluated`

来源定位：Read scope: selected Methods and benchmark description。

证据：本次尚未逐项读所有syntheticResults/supplement，不能排除focal定义；healthyhumanbenchmark确定。

判断：NOT_VERIFIED；将无条件否定改为阅读界限；物理约束并不证明strain准确。

建议：Healthy-volunteer benchmark; a prescribed focal-abnormality experiment was not verified in the accessed sections.

## 边界与访问
本次阅读足以支撑所列窄主张；未声称全文及全部补充已读。

访问请求及失败详见sources/retrieval_log.csv；本地文件：sources/stage03/arratia2023warppinn_crossref.json; sources/stage03/arratia2023warppinn_epmc.json; sources/stage03/arratia2023warppinn_arxiv.pdf; sources/stage03/arratia2023warppinn_arxiv.txt

## 阶段04自查

所访问版本有模拟及15健康benchmark；既有局部阅读不足以否定所有focal实验，保留NOT_VERIFIED，不作论文缺失指控。

实际回查位置：Author abstract/Methods selected sections。证据文件与散列见 stage04_self_check.csv；此记录不提高既有全文阅读等级。
