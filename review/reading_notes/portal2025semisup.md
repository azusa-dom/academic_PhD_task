# portal2025semisup：阶段03阅读记录

作者授权的AI辅助工作稿。实际深度：SELECTED_FULLTEXT。

来源：https://pubmed.ncbi.nlm.nih.gov/40701021/
版本：Publisher record: Computers in Biology and Medicine; volume 196; issue ; pages/article 110739; issued [[2025, 9]]
已读：发表摘要；出版商索引可见§4.1reference与§4.2metrics、Table3片段；不是完整连续全文。

原图／表像素：未检查，除非下列具体记录另作说明。未运行研究代码或下载受试者数据。

## 当前稿件用途与证据

### S03-82-01 / body.tex:154

稿件：`271 patients`

来源定位：Published abstract。

证据：1.02/.95/.91mm及RAFT1.19；globalpeakRS/CS .83/.90；摘要一致。

判断：SUPPORTED；当前窄主张与已读取来源相符；不外推材料真值或临床干预获益。

### S03-82-02 / body.tex:154

稿件：`propagated by conventional feature tracking`

来源定位：Publisher §4.1 indexed fulltext passage。

证据：firstframe人工初始、conventionalFT传播、人工校正failure；点只用于test非training，ED/ESseg用于training。

判断：SUPPORTED；当前窄主张与已读取来源相符；不外推材料真值或临床干预获益。

### S03-82-03 / supplement.tex:326

稿件：`not dense material truth`

来源定位：§4.1–4.2。

证据：EPE到上述pointreference，属另一估计流程agreement；与dense物质真值不同。

判断：SUPPORTED；当前窄主张与已读取来源相符；不外推材料真值或临床干预获益。

## 边界与访问
Direct Elsevier/ScienceDirect fullpage failed403/500, but targeted primary-publisher indexed passages (§4.1–4.2) were actually read; only those passages, not complete Methods/Results. Focal experiments remain NOT_VERIFIED.

访问请求及失败详见sources/retrieval_log.csv；本地文件：sources/stage03/portal2025semisup_crossref.json; sources/stage03/portal2025semisup_epmc.json; sources/stage03/method_search5_web.json; sources/stage03/targeted_escalations_web.json