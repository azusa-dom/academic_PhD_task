# MRXCAT2.0：相关完整章节与图像核验

身份：Buoso, Joyce, Schulthess, Kozerke，JCMR 2023;25:25，DOI 10.1186/s12968-023-00934-z。已与ETH版本记录和PMC正文核对，缓存19页论文正文具有页码、方法、结果、讨论、参考文献；ETH 20页PDF多一页机构封面，不能混淆物理页码。URL https://pmc.ncbi.nlm.nih.gov/articles/PMC10116689/ 。缓存SHA与交付manifest一致。

实际阅读：缓存源文第3–6页全部Methods（shape model、functional model、foreground/background、tissue properties、synthetic CMR、DeepStrain）；第6–8页全部Results及第8–16页Discussion/Limitations/Conclusions与图注，另核对主来源身份。实际查看Fig12与Fig14原始JPG像素。Additional file1技术补充链接返回挑战页，未读；未运行仓库，也没有确认所用DeepStrain权重版本。

估计目标与来源：统计形状模型基于MMWHS；ACDC用于形状测试/聚类及纹理体系，四种生成情况NOR/DCM/HCM/infarct不是临床四人队列。心脏功能由生物物理模型规定，自由壁椭圆瘢痕并改变局部壁厚/组织参数。EF依序51/34/41/49%，源Results p6给径向/纵向/圆周顺序；瘢痕对远端数值为径向0.30/0.95、纵向−0.17/−0.18、圆周0.01/−0.18。Fig12的远端/瘢痕曲线与分量方向一致；没有逐像素读图反算精确数字。

Methods p6明确心肌纹理被移除、SNR30、8 coils及Cartesian轨迹；CarSON/CarMEN与TextNet都使用ACDC。作者团队独立是一种开发来源描述，不等于样本/域独立，更不证明泄漏。图像重采样1.25mm、16层、128×128×16。

Results p8给Dice0.82（各心动相平均），位移1.0±0.9mm，圆周应变误差0.02±0.04，径向总体−0.24±0.21、梗死−0.20±0.21。Fig14显示NOR/HCM/DCM/Infarcted四组；橙色为ground truth、黑色DeepStrain，底部径向明显低估、圆周较接近；上左梗死Dice较低，但位移和径向误差不能据同一形容词统一排序。图注明确所有数值来自三个中室短轴切面的平均，未给瘢痕内独立误差。Fig12是规定组织曲线，不能冒充Fig14的估计误差。

稿件保留总体和梗死误差并指出不能统一排序，处理合理。局部幅度/边界/范围/峰时未有相应定量错误端点；此判断限定于已读正文与图12/14，不涵盖未得技术补充。主表将“known simulated peak”与误差汇总相邻，宜明确图14汇总的时间取样并未由所读图注完全定义，勿把所有误差强称peak-only。Discussion作者把径向低估推测为DeepStrain限制，实验未隔离纹理、部分容积、训练域和估计约束；稿件对机制的条件性表达合理。

限制：2D中室背景变形、有限形状数据、简化电生理/循环与纤维、信号模型及一类瘢痕。模型权重/发行版在访问Methods未识别；不宣称整个补充材料均未报告。ETH下载429、web截图403，但PMC原图访问成功；访问失败不再作为图14未核实理由。

## 阶段02新增主路线续查

从Springer主文实际链接取得[Additional file 1](https://media.springernature.com/original/springer-static/esm/art%3A10.1186%2Fs12968-023-00934-z/MediaObjects/12968_2023_934_MOESM1_ESM.pdf)，已读6物理页中的全部方法正文（pp1–5），参考目录pp5–6不作逐条审计；页眉of11与实际6页不同，文末方法完整接References，不能据页眉凭空假定缺页。无新图像数值需视读。p3明确模拟后切换ED为位移参考，E=1/2(C−I)，生理方向投影；瘢痕由椭圆和局部厚度/刚度/主动应力参数给定。p4–5补充ACDC纹理数据、切面拆分和合成步骤，但未说明Fig14误差的完整时间采样或DeepStrain具体发布版。故MRX-17继续NOT_VERIFIED，精确峰值汇总不能补猜。此前“技术补充未得”的限制现已解除，仍保留图14聚合歧义。


## 阶段04自查

再次查看Fig14像素和图注：底部为两组应变值而非误差箱线，三个中室切面平均明确，时间样本定义仍不充分；不由图猜peak-only或瘢痕内误差。SNR30、去心肌纹理、共同ACDC、总体−0.24±0.21/梗死−0.20±0.21可核。原文lowest performance措辞不等于按各误差指标统一排序；不指控泄漏。

实际回查位置：Methods Tissue properties / Synthetic CMR / DeepStrain; Results Cardiac functional model / DeepStrain; Fig14 pixels/caption; Discussion。证据文件与散列见 stage04_self_check.csv；此记录不提高既有全文阅读等级。
