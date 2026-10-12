# tobongomez2013cmac：阶段03阅读记录

作者授权的AI辅助工作稿。实际深度：SELECTED_FULLTEXT。

来源：https://pubmed.ncbi.nlm.nih.gov/23708255/
版本：Med Image Anal2013;17(6):632–648; abstract plus official companion README (not complete paper)
已读：出版摘要完整；共同资源官方README pp1–4；未取得论文全文。

原图／表像素：未检查，除非下列具体记录另作说明。未运行研究代码或下载受试者数据。

## 当前稿件用途与证据

### S03-43-01 / body.tex:371

稿件：`12 landmarks (four walls at three LV levels)`

来源定位：Abstract; official README p1。

证据：两观察者在3DTAG追踪人体12点；phantom实际8点，不应笼统把12点套用phantom。

判断：SUPPORTED；当前窄主张与已读取来源相符；不外推材料真值或临床干预获益。

### S03-43-02 / body.tex:392

稿件：`median inter-observer variability of 0.84~mm`

来源定位：Abstract; README p3 Excluding criteria。

证据：人体0.84、phantom0.77；排除依末点闭合和观察者差异75th percentile规则，跨时间中位数。

判断：SUPPORTED_WITH_QUALIFICATION；数字得到官方技术说明独立于摘要的核实；建议把筛选条件和一致性性质写清。

建议：The reported median inter-observer distances were 0.77 mm in the phantom and 0.84 mm in volunteers, after the stated landmark exclusions.

### S03-43-03 / supplement.tex:242

稿件：`sparse point error, not dense field truth`

来源定位：README mesh/landmark sections。

证据：mesh由手动LV模型及配准产生，不能把方法生成mesh称为独立dense应变真值；SSFP原误差只比末帧和ES。

判断：SUPPORTED；当前窄主张与已读取来源相符；不外推材料真值或临床干预获益。

## 边界与访问
HAL author PDF returned an anti-bot HTML page; paper Methods/Results unavailable, but official full technical README independently supports the audited resource specifics.

访问请求及失败详见sources/retrieval_log.csv；本地文件：sources/stage03/tobongomez2013cmac_crossref.json; sources/stage03/tobongomez2013cmac_epmc.json; sources/stage03/cmac2011_readme.pdf; sources/stage03/cmac2011_readme.txt

定位校正：最终claim_citation_audit.csv使用确切当前源文本；早期笔记中的简写定位由该表取代。


像素复核：官方README p3已实际渲染并查看，确认0.84 mm在排除标准后计算、cine SSFP评估仅ES及finalframe。图文件sources/stage03/cmac_readme_p3.png。


## 阶段04自查

.77/.84由官方共同技术说明支持；未获得整篇论文，不能把README阅读计为论文全文完成。

实际回查位置：Official companion README p3。证据文件与散列见 stage04_self_check.csv；此记录不提高既有全文阅读等级。
