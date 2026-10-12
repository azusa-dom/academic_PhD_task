# jacob2025cmrfm：阶段03阅读记录

作者授权的AI辅助工作稿。实际深度：SELECTED_FULLTEXT。

来源：https://pmc.ncbi.nlm.nih.gov/articles/PMC12745146/
版本：Publisher record: Journal of Cardiovascular Magnetic Resonance; volume 27; issue 2; pages/article 101967; issued [[2025]]
已读：Final Methods§2.1–2.4; Table1/2; Results Table3任务及Discussion相关段落。

原图／表像素：未检查，除非下列具体记录另作说明。未运行研究代码或下载受试者数据。

## 当前稿件用途与证据

### S03-74-01 / body.tex:158

稿件：`36 million images from 27,524 subjects`

来源定位：Methods p0070。

证据：DINO ViT-S/8；16,230 UKB+10,073 center1+1,221 center2=27,524；包含多序列，不只是cine。

判断：SUPPORTED；当前窄主张与已读取来源相符；不外推材料真值或临床干预获益。

### S03-74-02 / supplement.tex:330

稿件：`Segmentation, landmark localisation, diagnosis, prognostication across independent datasets`

来源定位：Table1 and §2.3 task list。

证据：9任务没有prognostication；三项task5B,7,8A与预训练同分布，部分使用其中带标注样本。

判断：SUPPORTED_WITH_QUALIFICATION；应分清两篇任务与in/out-of-distribution，不能把“independent datasets”泛化至所有任务。

建议：CMR-FM reports nine classification, segmentation, landmark and pathology-detection tasks, including both in-distribution and out-of-distribution evaluations; survival prediction is reported by CineMA.

## 边界与访问
本次阅读足以支撑所列窄主张；未声称全文及全部补充已读。

访问请求及失败详见sources/retrieval_log.csv；本地文件：sources/stage03/jacob2025cmrfm_crossref.json; sources/stage03/jacob2025cmrfm_epmc.json; sources/stage03/jacob2025cmrfm_full.xml; sources/stage03/jacob2025cmrfm_full.txt