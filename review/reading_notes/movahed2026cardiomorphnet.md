# movahed2026cardiomorphnet：阶段03阅读记录

作者授权的AI辅助工作稿。实际深度：SELECTED_FULLTEXT。

来源：https://pubmed.ncbi.nlm.nih.gov/42242080/
版本：Publisher record: Medical Image Analysis; volume 113; issue ; pages/article 104149; issued [[2026, 9]]
已读：arXiv2508.20734v2 8Jun2026 §3.2–3.4 losses/inference；Results dataset overview；Discussion strain limitation。

原图／表像素：未检查，除非下列具体记录另作说明。未运行研究代码或下载受试者数据。

## 当前稿件用途与证据

### S03-54-01 / body.tex:156

稿件：`without an intensity-based similarity loss`

来源定位：§3.3 Eqs5/6/11。

证据：没有fixed-versus-warped intensityregistrationloss，但有VAE reconstruction Lrec=像素MSE；正文应明确是registration项。

判断：SUPPORTED_WITH_QUALIFICATION；避免扩大为完全无intensity-based loss；保持warp-mask驱动DVF区别。

建议：CardioMorphNet supervises registration through segmentation-map alignment rather than a warped-image intensity-similarity term; its VAE objective still includes an image-reconstruction loss.

### S03-54-02 / supplement.tex:320

稿件：`without an intensity loss`

来源定位：§3.3 Eq11。

证据：总loss实际含image-reconstructionMSE，表格无registration限定使原文范围扩大。

判断：PARTIALLY_SUPPORTED；此处需要改窄。

建议：SAX cine volumes; registration guided by segmentation maps, without a warped-image similarity term; VAE image-reconstruction loss retained.

### S03-54-03 / body.tex:156

稿件：`UK Biobank and M\&Ms`

来源定位：v2 Abstract/Results; final published abstract。

证据：两数据最终摘要与v2一致；v1只UKB不可替代。DVFuncertainty非直接校准focalerror。

判断：SUPPORTED；当前窄主张与已读取来源相符；不外推材料真值或临床干预获益。

### S03-54-04 / supplement.tex:320

稿件：`not focal motion accuracy`

来源定位：Discussion limitation。

证据：作者明确无tagged/可靠strainGT，未作定量strain评估；mask、形态functional与motionaccuracy应区分。

判断：SUPPORTED；当前窄主张与已读取来源相符；不外推材料真值或临床干预获益。

## 边界与访问
Final2026 identity/abstract verified; methods inspected in author v2 dated8June2026, not a byte-identical publisher VOR.

访问请求及失败详见sources/retrieval_log.csv；本地文件：sources/stage03/movahed2026cardiomorphnet_crossref.json; sources/stage03/movahed2026cardiomorphnet_epmc.json; sources/stage03/movahed2026cardiomorphnet_arxiv.pdf; sources/stage03/movahed2026cardiomorphnet_arxiv.txt

## 阶段04自查

Lrec明确为图像重建MSE，省略的是warped-image registration similarity；缩窄补表without an intensity loss，避免扩大范围。版本仍是作者v2，未声称逐字同最终版。

实际回查位置：Author v2 §3.3 Eqs5/6/11 pp10–11。证据文件与散列见 stage04_self_check.csv；此记录不提高既有全文阅读等级。
