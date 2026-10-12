# zhou2018straus：阶段03阅读记录

作者授权的AI辅助工作稿。实际深度：ABSTRACT。

来源：https://pubmed.ncbi.nlm.nih.gov/28574344/
版本：Publisher record: IEEE Transactions on Medical Imaging; volume 37; issue 3; pages/article 741-754; issued [[2018, 3]]
已读：正式摘要和Crossref；官方dataset全文另见strausdata；IEEE/HAL全文访问失败。

原图／表像素：未检查，除非下列具体记录另作说明。未运行研究代码或下载受试者数据。

## 当前稿件用途与证据

### S03-41-01 / body.tex:367

稿件：`18 \emph{virtual patients}`

来源定位：Published abstract and official resource。

证据：E/M healthy/pathologicalmotion、18virtual、90seq/2700volumes与多模态。

判断：SUPPORTED；当前窄主张与已读取来源相符；不外推材料真值或临床干预获益。

### S03-41-02 / body.tex:367

稿件：`three volunteer-derived multimodal templates`

来源定位：Access boundary。

证据：摘要和已读官方页不足以确认3×6构成及五种病理全名；IEEE空页、HAL反爬、CREATIS仅摘要。

判断：NOT_VERIFIED；不继承前模型／清单3×6断言；需要原论文Methods或作者合法AAM。

建议：STRAUS provides 18 virtual cases with simulated electromechanical motion; the number of independent source anatomies and the detailed state construction require full-method verification.

### S03-41-03 / body.tex:367

稿件：`the paper used engineering strain`

来源定位：Access boundary。

证据：已访问摘要/官方页未给strain公式；IEEE/HAL尝试未取全文。

判断：NOT_VERIFIED；不能把mesh参考自动解释为engineeringstrain；表S2同样暂缓。

建议：The framewise meshes support reference deformation calculations; the strain convention must be verified from the original methods.

## 边界与访问
IEEE full text empty; HALdocument challenge; CREATIS bibliographic page only; title/DOI searches located thesis but no full original Methods inspected.

访问请求及失败详见sources/retrieval_log.csv；本地文件：sources/stage03/zhou2018straus_crossref.json; sources/stage03/zhou2018straus_epmc.json; sources/stage03/strausdata_resource.html; sources/stage03/straus_final_attempt_web.json

## 阶段04自查

18虚拟例/90序列/2700体数据有据；3模板×6状态和engineering strain仍缺完整方法支持，保持未知，不判错误。

实际回查位置：Published abstract; official Overview/Methodology/database。证据文件与散列见 stage04_self_check.csv；此记录不提高既有全文阅读等级。
