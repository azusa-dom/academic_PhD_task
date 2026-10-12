# cmrxrecon2025official：阶段03阅读记录

作者授权的AI辅助工作稿。实际深度：SELECTED_FULLTEXT。

来源：https://cmrxrecon.github.io/2025/Data.html
版本：Official2025 challenge pages accessed2026-10-11; no subject-level release inspection
已读：官方2025 Home/Data/Tasks/FAQ页面完整文字；未下载参与者数据。

原图／表像素：未检查，除非下列具体记录另作说明。未运行研究代码或下载受试者数据。

## 当前稿件用途与证据

### S03-57-01 / body.tex:373

稿件：`does not establish tagging/DENSE motion labels or a fully paired cine--LGE cohort`

来源定位：Data/Tasks/FAQ。

证据：Data列tagging acquisition但未宣称dense displacement/strainlabels；task指标SSIMPSNRNMSE。未证实universalpairing。

判断：SUPPORTED_WITH_QUALIFICATION；要区分存在tagging序列与存在运动标签，不应写2025无tagging。

### S03-57-02 / body.tex:398

稿件：`with disease labels`

来源定位：Tasks Regular Task2。

证据：官方说明为避免训练偏倚，不公开training/validation逐例疾病信息。

判断：PARTIALLY_SUPPORTED；“with disease labels”让人误以为可直接用于监督；官方diseasegroups≠公开逐例label。

建议：Multicentre, multivendor reconstruction resource spanning disease groups; per-case disease information is withheld for training and validation.

### S03-57-03 / supplement.tex:248

稿件：`disease labels are not motion truth`

来源定位：Data and Tasks。

证据：600总计划，200/100/300；Data与Tasks新中心数有不一致；本稿无这些数故不强加确定denominator。

判断：SUPPORTED_WITH_QUALIFICATION；避免把覆盖疾病理解为已提供疾病标签；取得具体release后方可确认pairing和files。

## 边界与访问
本次阅读足以支撑所列窄主张；未声称全文及全部补充已读。

访问请求及失败详见sources/retrieval_log.csv；本地文件：sources/stage03/cmrxrecon2025official_home.html; sources/stage03/cmrxrecon2025official_Data.html; sources/stage03/cmrxrecon2025official_Tasks.html; sources/stage03/cmrxrecon2025official_FAQ.html

## 阶段04自查

官方不公开训练/验证逐例疾病信息；稿件with disease labels宜改疾病群覆盖。不能进一步推断test全部无疾病信息。

实际回查位置：Regular Task2 paragraph on disease information。证据文件与散列见 stage04_self_check.csv；此记录不提高既有全文阅读等级。
