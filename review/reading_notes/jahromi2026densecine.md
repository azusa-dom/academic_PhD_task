# Jahromi 2026

身份：Naqizadeh Jahromi et al., Biomechanics and Modeling in Mechanobiology2026;25:103，2026-09-15公开，DOI10.1007/s10237-026-02120-3；出版社与25页缓存一致，出版社原PDF已成功下载。完整阅读Methods2.1–2.5 pp2–7、合并Results/Discussion3.1–3.4 pp7–19、Conclusion跨pp19/23/24以及Appendix A说明和Fig15–18图注；Table1–4均阅读。实际查看原PDF pp14–15（Table1/2，Fig9/10/11），其他图主要依赖文字/图注，不宣称全部图像已检查。

40健康志愿者（19男21女，38.75±12.9岁），各2相邻中室短轴；非80独立人。DENSE segmentation由20volunteers130slices3789frames作5fold80/20，4通道magnitude+xyzphase，五折bestepoch集成；cine segmentation另20volunteers152slices约1200images，明确每折16/4人。两套网络与40人评估队列逐人重叠关系未明确核实；Fig2只声明所示图未用于训练/验证，不能据此外推所有40人都独立，也不能指控泄漏。

DENSE-Analysis+RBF interpolation→GLtensor；two-slice可取纵向梯度，one-slice仅二维梯度，所以Ecc/Err相近，Ell改用面积/不可压假设。cine只用轮廓周长、壁厚及面积：Ecc为周长比平方变换，Err360角度壁厚应变取median，Ell体积守恒/面积比。均忽略部分through-plane/torsion，非逐材料点追踪。reference为beginning systole，RR归一化不能消除所有心率/配准差异。

phantom为可解析厚壁圆柱（25/35mm），简化形变；DENSE SNR20，两种测试分开exact vs estimateddisplacements；cine用解析轮廓或DENSE magnitude近似cine（SNR1000/20，10次噪声）。Ecc相对稳健，radial对分割/位移处理敏感；模拟真值结果不等于健康人DENSE误差为零。

志愿者§3.2 pp13–15+Table1/2：统计对象是每slice peak median systolic endocardialEcc；cine−two-slice DENSE mean−2.7pp，TOST所选±3.5pp，plower<.05/pupper<.001；与零差异显著并不矛盾。Table2同终点差值median−3.0[−5.2,0.1]pp，不能当mean或LoA。Fig6群体平均曲线的peak差≈1%属于不同汇总，不能替换−2.7。Table1总体repeated-measuresANOVA/Friedman+Bonferroni未明确同人两slice聚类，未找到margin预先注册/临床阈值论证；保持“不明确”，不能断言没有处理或事后择界值。个体曲线差异存在，TOST不证明逐个体可互换。

§3.3两个敏感性实验：softmax阈值.05/.95 vs.5，和另用ACDC训练nnU-Net。后者100train/val50test，40volunteers仍为原评估场景；不能叫疾病应变外部验证。ACDC替换后Ecc绝对差中位数≤1pp、Err10.7pp，检验分割模型影响，不等于在病变群体验证。

§3.4明确可能不能泛化至cardiomyopathies；单sliceEcc/Ell不能按AHA区域评估；体积守恒、DENSE处理噪声、圆柱幻影及magnitude近似cine均限制推断。原文含时序曲线讨论，稿件只能说未报告“focal timing error”，不能说完全无时间信息。

§2.4及Data availability明确40人数据属于Stanford purl xt223hz2438；这是来源重叠声明，不是个体映射核验。官方代码README已读取，未执行代码、未下载受试者数据。Stanford落地页本次web超时，不影响论文自身归属声明；仓库51/55总数属其他key后续核查。没有从README推断数据泄漏。后续Crossref出版商存入元数据确认issue5；原书目无需更改。

未核实：预先界值/聚类细节、各网络训练者与40人逐一对应、所有appendix曲线像素和代码复算。主稿对此保持了适当边界。


## 阶段04自查

40人×2切面、特定endoEcc均值差−2.7pp、所选±3.5pp TOST保留。Table1重复测量方法名称不能证明同人切面依赖已处理；亦不能反推确未处理；预设界值与训练逐人重叠仍未知。

实际回查位置：Methods2.4/2.5; Results3.2 pp13–15; Table1。证据文件与散列见 stage04_self_check.csv；此记录不提高既有全文阅读等级。
