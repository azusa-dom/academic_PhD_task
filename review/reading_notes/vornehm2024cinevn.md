# CineVN：切面应变与分开采集的GRAPPA参照

[PMC作者稿](https://pmc.ncbi.nlm.nih.gov/articles/PMC11518642/)，DOI10.1002/mrm.30260；online2024-08-26，卷期2025;93(1):138–150。读Abstract、完整Methods2.1–2.4、Results3、Discussion4、主表文字/全部图注；实际查看Figure5像素。补充PDF请求返回1817字节HTML，未读补表/视频。

OCMR健康数据268切面分186/44/38训练/验证/测试；论文按切面报告，不自行保证受试者独立划分。模型15级VN，SSIM和复数域损失，CG数据一致性。前瞻18健康者分别采GRAPPA R2、two-shot约R8、real-time约R16，25相位；同一加速数据比较CineVN、vendor CS、TTV-CS。46患者只real-time，没有GRAPPA参照。

Trufi Strain3.0：体积按SAX全栈，应变按个别中室切面PRS/PCS，非局灶节段。初选健康112、患者292切面；健康two-shot2和real-time3切面、患者46切面因任一重建分割失败排除。患者各法失败9/19/33切面，存在重叠。不能把切面数视为独立人；分析单位和筛除可能影响精度解释。

Fig5的BA合并two-shot与real-time。实际图像确认应变CineVN最小bias/最窄LoA；PRS bias−5.7pp、PCS+1.1pp，PCS有符号高估=缩短幅度低估。所有加速PRS低、PCS高，非全体功能参数都有同样排序。患者中推测优劣由健康结果外推，作者自己承认无参照难判断准确性。参考采集并非同一次kspace重建，屏气差异亦存在。Methods/Results/Discussion未设病灶尺度恢复终点；人工瓣膜伪影例不是局灶异常恢复验证。


阶段02书目补核：Wiley期刊页也明确First published 26 August 2024。原bib的27 August应改26 August，或删除可选online-day注释；2025卷年及旧key2024均保留。


## 阶段04自查

18健康有GRAPPA、46患者无常规参照支持；CineVN应变优势须限定所比重建、切面与协议合并；圆周有符号偏高为更不负。

实际回查位置：Methods prospective datasets; Fig5 caption; Discussion4.3。证据文件与散列见 stage04_self_check.csv；此记录不提高既有全文阅读等级。
