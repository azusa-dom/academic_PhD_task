# StrainNet：相关完整章节阅读记录（作者审阅工作稿）

身份：Wang et al., Radiology: Cardiothoracic Imaging 2023;5(3):e220196，DOI 10.1148/ryct.220196。已从 RSNA 正文独立确认题名、作者、年卷及 DOI。主来源 https://pubs.rsna.org/radiology/doi/full/10.1148/ryct.220196 。

实际阅读：摘要、Introduction、Materials and Methods 的全部小节、Results 的全部小节、Discussion 全部及局限；网页行 72–222。看过 Fig.1–6 图注，并在后续合法PMC CDN路径实际查看Table2与Fig5像素。初始下载403/挑战页的失败记录仍保留在retrieval_log。未读到 Appendix S1、Table S1、Figs S1–S3 内容。深度 SELECTED_FULLTEXT，不称全部正文与补充材料已读。

研究为八中心回顾性开发，324 人中排除 19 人，305 人包含 161 患者、99 健康成人和45儿童青少年。按参与者分层随机80:20拆分：243人670切面训练，62人190切面内部测试；训练集五折调参。中心数不等同外部验证。

模型输入为轮廓二值序列，2D+time U-Net；监督是 DENSE 相位得到的 Lagrangian displacement。训练和位移 EPE 实验用 DENSE magnitude contours；EPE 全心肌全时间序列均值0.75±0.35 mm。独立 cine 分析输入 suiteHeart 5.0.4 轮廓，降采样至 DENSE 平均像素尺寸2.73 mm，形态膨胀匹配壁厚，比较匹配切面 DENSE。59/62 人具备基底、中部、心尖图像而进入应变比较。统计端点是收缩末全局和 AHA16节段 Ecc，而非峰值时间。

Results Correlations and Agreement（网页189–200）：全局ICC0.87/0.72、节段0.75/0.48（StrainNet/FT对DENSE）；正文全局偏倚−0.51百分点，LoA−5.74至4.72；节段偏倚−0.55，LoA−9.16至8.07。这些是方法一致性，不是临床可互换性。结果包含健康者分层分析及个案曲线，但不等同病灶定位/边界误差的定量试验。

Discussion（215–220）：DENSE噪声、屏气、层面、轮廓及生理变异均影响参考；StrainNet重复性待研究，基底性能不足，未纳入径向比较，纵向为未来工作；作者明确指出没有使用外部数据集。因此稿件“无外部数据集验证”有直接证据，不能据此推断确有泄漏。

当前未解决项是Appendix S1及精确Green–Lagrange实现，原文访问主文仅显示Lagrangian并引用既有方法；不能由此认定稿件错误。Table2与Fig5像素访问已解决，当前稿件的EPE/cine分离总体忠实。

## 后续图像复核（MRXCAT阅读期间找到合法PMC CDN路线）
已实际查看原Table2和Fig5像素：Table2的StrainNet全局Bias±95%LoA为−0.51±5.15；算术区间−5.66至4.64，而正文及Fig5均为−5.74至4.72。差0.08百分点/端点，属于来源内部不一致，稿件披露是正确的。Table2节段−0.55±8.61，Fig5为−9.16至8.07，上界有0.01的报告精度差，不能称严格算术完全一致；更适宜说大致一致。FT全局表2为1.62±6.64（−5.02至8.26），图5/正文约1.6、−4.97至8.09，也存在源内差别。此差异不改变四个ICC或模型优于所测试FT的结论。截图源文件见 sources/figures/wang2023strainnet_*。附录仍未取得。


阶段02定位到期刊直接Appendix S1 PDF链接，但web只返回Cookie Absent页面。没有得到新的公式证据，WANG-12保持NOT_VERIFIED；未重复请求已失败的主文/PDF。


## 阶段04自查

本轮再次查看Table2和Fig5原像素：StrainNet全局表−0.51±5.15推得−5.66至4.64，图/正文−5.74至4.72；节段表推得上界8.06、图文8.07，保留精度差异。305、243/62、670/190、59与四ICC及EPE实验输入均获正文支持。另纠正前笔记遗漏：FT表/正文偏差为正，Fig5A/B偏差标注却为−1.6/−1.5；不据图标注自行改写稿件。Appendix S1与精确GL实现仍未核。

实际回查位置：Methods Data preprocessing / Performance evaluation / split; Results EPE / Correlations; Discussion limitations; Table2; Fig5A/B。证据文件与散列见 stage04_self_check.csv；此记录不提高既有全文阅读等级。
