# Militaru：全局/区域与比较对象核验

身份：Militaru et al. JCMR 2021;23:54，DOI10.1186/s12968-021-00742-3；PMC官方身份记录与缓存PDF首尾完整16页对应，SHA符合输入manifest。实际读取摘要、Methods pp2–4全节、Results pp4–9全部、Discussion/Clinical implications/Limitations/Conclusion pp9–15；Tables1–4文本；实际查看PDF p10图5a/b及p11图5c的原像素。补充图S1/S2未查看，不称含全部supplement已读。

队列为61例随机选取自已募集队列：18健康、18慢性MI、15DCM、10LVH（5HCM、5AS）；3T Philips单中心。同一图像用cvi42 v5.1、Segment v3.0、Tomtec Image Arena v4.6；tagging HARP2.7。比较跨壁peak-systolic Lagrangian LS/CS/RS，16段；源方法对global计算有波形加权与tagging起始帧外推，不宜当作固定收缩末或统一软件定义。10例observer重复性不是scan–rescan。瘢痕分析18MI，any LGE与分层≥25/50/75%，不能嫁接Kihlberg的>50%条件。

| 比较 | GRS ICC（图5c像素） |
|---|---:|
| cvi42—tagging |0.63|
| Segment—tagging |0.48|
| Tomtec—tagging |0.10|
| cvi42—Segment |0.81|
| cvi42—Tomtec |0.11|
| Segment—Tomtec |0.19|

因此FT对tagging是0.10–0.63，软件间为0.11–0.81。摘要称软件间0.10–0.81，与图5c相差0.01的下界。不能将0.10–0.81误用于tagging；稿件当前已正确区分比较对象，但软件间下界仍沿摘要，建议以产品映射披露差别。图5a的tagging GLS cvi42/Segment/Tomtec分别0.94/0.93/0.92；图5b GCS0.91/0.88/0.91，吻合稿件范围。

区域一致性明显更不稳定，径向尤其；LGE鉴别也产品相关。原文Discussion讨论tagging径向参照自身因tag spacing与薄壁而可能偏低，对Tomtec壁厚替代的说明是作者推测，不是产品算法确定性证明。单中心、性别不平衡、3T条件、只三软件、不评估torsion/layer/RV/strain rate/time-to-peak；作者明确未评估峰值时间是否相同。因此可保留不宜软件互换、不同方向需区别的综述结论。不能把其“gold standard”当无误差真值，也不能以此断言所有FT区域值均无用。

重要源内差异另见摘要与Results p7的部分regional ICC；本稿未精确引用这些值，故不额外扩张纠错范围。所需优先图5c已经实际视觉核对，完成此项。


## 阶段04自查

再次查看Fig5c：cvi42/Segment/Tomtec对tagging分别.63/.48/.10；cvi42–Segment/cvi42–Tomtec/Segment–Tomtec分别.81/.11/.19。稿件.10–.63正确；软件间摘要.10–.81与图.11–.81不同，保留源内差别，非作者捏造或误引。

实际回查位置：Abstract; Methods analysis; Fig5c PDF p11 original pixels。证据文件与散列见 stage04_self_check.csv；此记录不提高既有全文阅读等级。
