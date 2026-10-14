> 示例输出：skill v0.1.0 在 2026-10-14 由一个 Claude 子代理按本 skill 生成，未经人工逐句核对。数字以原文为准；用于任何稿件前请对照原文 PDF 与补充材料核实。原论文为 JCMR 开放获取论文（DOI 10.1186/s12968-018-0485-4）。

# 精读拆解：Wehner 2018，cine feature tracking 与 DENSE 的应变/扭转比较

Wehner GJ, Jing L, Haggerty CM, Suever JD, Chen J, Hamlet SM, Feindt JA, Dimitri Mojsejenko W, Fogel MA, Fornwalt BK. Comparison of left ventricular strains and torsion derived from feature tracking and DENSE CMR. *J Cardiovasc Magn Reson*. 2018;20(1):63. PMID 30208894；PMCID PMC6136226；DOI [10.1186/s12968-018-0485-4](https://doi.org/10.1186/s12968-018-0485-4)（书目信息经 PubMed 元数据核实）。
阅读日期：2026-10-14

## 阅读范围

全文正文来自 PubMed Central（经 PubMed MCP `get_full_text_article` 取得 PMC6136226），读了 Background、Methods（Study population、Image acquisition、DENSE strain analysis、Feature tracking strain analysis、Statistics）、Results、Discussion、Limitations、Conclusion 和摘要。MCP 返回的正文去掉了表格、公式和参考文献编号，因此另从 Europe PMC 的同一 PMC 记录下载 JATS XML，读到了 Table 1–5 的全部数值、唯一的公式（2D Lagrangian Green strain = ε + ½ε²）以及 Fig. 1–5 的图注。**图像本身没有看到**：Fig. 1–5 只读了图注，因此下文凡涉及图的判断只依据图注和对应表格，不对 Bland–Altman 图的散点形态（如比例偏差、离群点）作任何判断。**四个补充材料均未读到**（Additional file 1 文献综述、2 心内膜应变比较、3 应变公式推导、4 Circle 软件验证；只知道其标题），Circle 的结果只有正文里一段文字概述。参考文献列表在获取的文本中编号缺失，文中"前人研究"的具体出处无法逐条对应。无代码或数据。

论文类型：回顾性、双中心、方法间一致性（validation/agreement）研究，内嵌一个"等价性"子问题（FT 片层应变 vs 仅用 ED/ES 轮廓长度的应变）和一个小型文献计数。采用的尺子是"验证/方法间一致性"那一行（参考标准误差与独立性、定义可比性、一致性界限而非相关、统计单位），报告规范以 GRRAS 作提示；同时按心脏运动/应变领域检查表核对应变定义、参考态、心肌层、时相，以及全局与局灶的区分。

## 一句话判断

在 88 名以年轻健康者为主的受试者中，这篇论文较可靠地表明：经应变定义换算后，TomTec FT 的中段片层 Ecc 与 2D spiral DENSE 无系统偏差（但一致性界限 ±6.3 个百分点并不窄），基底/心尖 Ecc 有系统性高估，扭转和 dyssynchrony 一致性差；同时 TomTec 报告的片层应变几乎等于它自己传播出的 ED/ES 轮廓长度变化。最大的保留意见有两条：结论里"只有中段准确、Ell 不准确"的分类所用判据与 Methods 预设的 CoV<20% 判据不一致；"手工画 ED/ES 轮廓即可替代 FT"这一推广并未被检验，因为比较用的是 FT 自己追踪出来的 ES 轮廓。

## 第一层：研究路线

### 作者的结论

作者在 Conclusion（与摘要 Conclusion 几乎同文）中说：以 DENSE 为参考标准，FT 对心尖和基底 LV Ecc、Ell、扭转和 dyssynchrony 的定量不准确，只对中段 Ecc 准确 [原文事实：Conclusion 第 1–2 句]。FT 对全局峰值应变"不必要"，因为只处理 ED 和 ES 轮廓即可得到非常相近的结果 [原文事实：Conclusion 第 3 句]。因此当前商用 FT 技术对心脏力学定量的效用有限 [原文事实：Conclusion 末句]。Discussion 还给出了更宽的版本："manual contour delineation at just ED and ES can replace results from feature tracking" [原文事实：Discussion, Slice-wise strains 小节末段]。

### 路线重建

作者从"已有认识"出发：应变、扭转、dyssynchrony 有预后价值，tagging、DENSE、SENC、TPM 可作参考标准但临床上不实用，因此 FT 被广泛用来近似这些量（Background 第 1 段）。缺口被表述为两层：既往 FT 验证多与 tagging 或 TPM 比较、样本小或只看中段，且从未与 DENSE 直接比较（Background 第 2–3 段）；另外，他们对 62 篇 FT 研究的计数显示 63% 报告片层应变、21% 只报告片层应变，而片层应变在原理上只依赖 ED 和 ES 两帧的轮廓长度，不需要节段追踪（Background 第 4 段，Table 1）。由此提出两个假设：FT 的应变、扭转、dyssynchrony 与 DENSE 一致性不好；片层应变的"轮廓法"与 FT 一致性好（Background 末段）。值得注意的是第一个假设是以"不一致"为方向写的，但 Methods 没有预先定义"一致性好/不好"的完整判据，只给出 CoV<20% 视为可接受（Statistics）。

设计是回顾性数据库检索，取 2013–2016 年 University of Kentucky（3 T Trio）与 CHOP（1.5 T Avanto）中同一位置同时有 spiral cine DENSE 和 bSSFP 的数据，不按诊断排除（Methods, Study population; Image acquisition）。数据为 89 人，排除 1 人（DENSE 触发异常），最终 88 人、186 对图像：基底 39、中段 69、心尖 38、四腔 40；扭转和 dyssynchrony 用同时有三层短轴的 38 人（Results, Study population；Table 2）。人群平均年龄 22–27 岁，短轴各层健康者 61–74%，四腔 98% 健康，疾病主要是法洛四联症，HCM 和缺血性心肌病各只有 1–2 人（Table 2）。

方法上，DENSE 用 DENSEanalysis（MATLAB）：手工分割、半自动相位解缠、空间平滑、10 阶多项式时间拟合，用 2D Lagrangian Green 应变张量求 Ecc（短轴）和 Ell（四腔），扭转为 twist 对长轴位置的线性回归斜率，dyssynchrony 为节段 Ecc 曲线相对于个体参考曲线的互相关延迟的标准差（Methods, DENSE strain analysis）。FT 用 TomTec 2D CPA MR 1.1.2.36：短轴手工画 ED 心内膜和心外膜轮廓后自动传播，四腔只画心内膜，追踪不佳时重画直到"视觉可接受"；短轴取心内膜与心外膜应变的平均作为透壁值；FT 应变为 1D Lagrangian 应变（引文和厂商邮件确认）（Methods, Feature tracking strain analysis）。轮廓法用 TomTec 导出的 ED 和 ES 两帧轮廓坐标，ES 定义为轮廓周长最小的帧，同样算 1D Lagrangian 应变。作者提出对 1D 应变加 ½ε² 换算为 Green 应变，再与 DENSE 比较。第二家软件 Circle cvi42 作为验证放在 Additional file 4。

评价用 Bland–Altman、CoV（<20% 视为可接受，依据前人研究）以及配对 t 检验判断偏差是否不为零（Methods, Statistics）。主要结果见 Table 3–5：换算前 FT 在三层 Ecc 都显著高估（偏差 −6.5、−2.3、−6.0 个百分点），换算后中段偏差 −0.4（p=0.36，LoA ±6.3，CoV 10.9%），基底 −4.0（±6.7，17.8%），心尖 −2.4（±10.8，14.8%，p=0.01），Ell −0.2（±9.3，19.3%，p=0.77）；扭转 2.1 vs 3.5 deg/cm（偏差 −1.4，±2.4，CoV 41.1%）；dyssynchrony 42 vs 16 ms（偏差 26，±56，CoV 76.3%）；FT 与轮廓法偏差 −1.3 到 0.2，LoA ±2.2 到 ±3.8，CoV 3.2–7.0%。

### 决策分叉

| 分叉 | 作者选择（位置） | 可行替代 | 收益 / 代价 | 换做法后可能的变化 [读者推断] | 是否给理由 |
|---|---|---|---|---|---|
| 参考标准 | 2D spiral cine DENSE 视为 reference standard（Background 第 3 段；Methods） | tagging/HARP；3D DENSE；有真值的体模或仿真 | 像素级位移、空间分辨率高于 tagging；代价是 DENSE 本身也是 2D、经过空间平滑和 10 阶多项式时间拟合，且有手工分割，误差未在本文量化 | 若参考误差较大，所有 LoA 会被放大（LoA 包含两种方法的误差）；DENSE 平滑若压低峰值，会让 FT "高估"看起来更大，但这无法解释中段一致而基底不一致的层级差异 | 给了（引 DENSE 体模和重复性前作） |
| 应变定义换算 | 对 FT 的 1D Lagrangian 应变加 ½ε² 换算为 Green 应变后再比较（Methods, 公式；Additional file 3） | 反过来把 DENSE 的 Green 应变换成 1D 伸长率 √(1+2E)−1；或两者都报 | 消除了定义不同造成的系统偏差，这是本文的方法学亮点；对单一线元而言该换算是精确的，不是近似 | 换算方向不改变结论方向，只改变数值标度；未换算时所有层都"显著高估"，说明定义差异本身占了偏差的大头（中段 −2.3 → −0.4） | 给了（附推导与教科书出处） |
| 心肌层匹配 | 短轴取 FT 心内膜与心外膜应变的平均；四腔只用心内膜（Methods, FT 小节） | 用 FT 的 mid-wall 轮廓；DENSE 只取心内膜层与 FT 心内膜比较 | 简单；代价是"心内膜与心外膜两条轮廓应变的平均"不等于 DENSE 在全部心肌像素上的平均，Ell 则把心内膜值与 DENSE 透壁值相比 | 短轴方向不确定；四腔 Ell 用心内膜会使 FT 幅值偏大（心内膜 Ell 通常略大于透壁平均），与观察到的未换算偏差 −1.5 方向一致 | 部分给了（称 Ell 透壁差异小，未给数据） |
| 一致性判据 | CoV<20% 视为可接受，同时用配对 t 检验判断偏差（Statistics） | 预先设定临床可接受的绝对差值（如 ±2–3 个百分点）；报告 LoA 置信区间；等价性检验（TOST） | CoV 方便与前人比较；但 CoV 的计算公式未报告，且与 t 检验判据会给出相互矛盾的分类（见断点 1） | 若用预设绝对容差，中段 Ecc 的 ±6.3 很可能也会被判为不可接受；若只用 CoV 判据，基底、心尖和 Ell 都会被判为可接受 | 部分（仅"based on similar analyses in previous studies"） |
| 轮廓法的轮廓来源 | 用 TomTec 自己传播得到的 ED/ES 轮廓，而不是观察者独立手画（Methods, FT 小节第 2 段） | 由独立观察者手工画 ED、ES 轮廓（临床常规方式） | 去除了观察者变异，能"纯粹"地检验区域追踪信息是否改变片层应变；代价是 ES 轮廓本身就是追踪的产物，比较几乎是同一几何量的两种读法 | 若用独立手画轮廓，FT–轮廓法的 LoA 会增宽，至少增加 ES 轮廓的观察者间变异；增宽多少无从估计 | 给了，并断言"there should be no fundamental difference in manually-drawn contours and the TomTec propagated contours"，未给证据 |
| 分析的空间尺度 | 片层平均 Ecc/Ell、扭转、dyssynchrony；不直接报告节段应变一致性；排除径向应变（Methods；Limitations） | 报告 AHA 节段 Ecc 的 FT–DENSE 一致性（数据本身已足以计算，dyssynchrony 就用到了节段曲线） | 聚焦最常被报告的量；代价是"区域"层面的 FT 准确性只能从 dyssynchrony 间接推断 | 节段一致性大概率比片层差（片层平均会抵消节段间方向相反的误差），具体幅度未知 | 径向给了理由（重复性差），节段未说明 |
| 样本构成 | 数据库内所有配对数据，不排除诊断，跨两中心两场强（Study population） | 按中心/场强分层报告；按疾病分组报告 | 样本量比前人大；代价是中心、场强、年龄和疾病相互纠缠，四腔几乎全是健康人 | 作者自己推断功能差、through-plane 运动小的人群一致性会更好（Limitations）；中心/场强分层后差异方向不确定 | 部分（Limitations 承认人群代表性） |

### 路线断点

**断点 1：判据在 Methods 和 Conclusion 之间漂移。** Methods 预设 CoV<20% 为可接受（Statistics）。按这个判据，换算后基底 Ecc（17.8%）、心尖 Ecc（14.8%）、Ell（19.3%）都可接受，Results 自己也写"Those same CoVs dropped below 20% after the adjustment"（Results, Comparison between FT and DENSE 第 3 段）。但 Conclusion 写"inaccurate for quantification of apical and basal LV Ecc, Ell"，"only accurate for mid LV Ecc"。基底和心尖被判不准，依据实际是配对 t 检验偏差显著；Ell 偏差 p=0.77 且 CoV<20%，却也被归入"不准确"，而摘要 Results 同时把 Ell 称为"borderline-acceptable"。也就是说，同一摘要内部对 Ell 的判定前后不一，Conclusion 中的分类没有一个一致的、预先声明的决策规则支撑。数值本身不受影响，但"准确/不准确"的二分结论是作者推断，且推断规则不一致。

**断点 2："FT 不必要，手工 ED/ES 轮廓即可替代"超出了检验内容。** 实验检验的是"TomTec 报告的片层应变 ≈ TomTec 自己传播出的 ED 与 ES 轮廓的长度变化"（Methods, FT 小节第 2 段；Table 5）。由于片层应变本身就定义为整条轮廓的长度变化，这一一致性很大程度上是几何上的预期，作者在 Background 第 4 段也正是这样论证的；它说明区域追踪信息不改变片层应变，但 ES 轮廓本身是追踪结果。Discussion 和 Conclusion 把结论推广到"manual delineation of borders at two time points"，而手工轮廓从未被画过、比较过；"no fundamental difference" 是未经检验的断言。因此"手工轮廓可替代 FT"在本文中是 [作者推断]，不是 [原文事实]。

**断点 3：误差机制被归因于 through-plane 运动和小梁，但没有被测量。** 基底/心尖偏差被解释为基底 through-plane 运动和心尖乳头肌/小梁使心内膜难以追踪（Discussion 第 2 小节），扭转偏差被解释为沿室壁方向缺乏图像梯度（Discussion, Torsion 小节）。这些解释合理，但论文没有测量 through-plane 位移（例如由长轴片测 MAPSE）并检验它与偏差的关系，也没有按层显示心内膜追踪质量。机制在本文中是 [作者推断]。

## 第二层：证据核对

### 主张–证据台账

| # | 主张（位置） | 支撑证据（位置） | 成立条件 | 未被证明的部分 | 证据强度 |
|---|---|---|---|---|---|
| 1 | 换算后 FT 中段 Ecc 与 DENSE 一致性可接受（摘要；Discussion 首段第 1 点；Conclusion） | [原文事实] Table 3：−17.5 vs −17.2%，p=0.36；Table 4：偏差 −0.4，LoA ±6.3，CoV 10.9%；Circle 中段偏差 0.7%、CoV 11%（Results, Circle 小节） | 69 名以年轻健康者为主的受试者；片层平均；FT 心内外膜平均 vs DENSE 透壁；经 1D→Green 换算；两中心 1.5/3 T；时相未明确 [未报告] | "准确"实际指无系统偏差；±6.3 个百分点的个体一致性对多数临床分组差异而言并不窄 [读者推断]；LoA 置信区间未报告（读者重算约 ±1.3） | 中：偏差证据强，个体层面一致性的"可接受"取决于未预设的临床容差 |
| 2 | FT 高估基底和心尖 Ecc 幅值，破坏了 DENSE 中可见的基底→心尖梯度（Results 第 3 段；Discussion） | [原文事实] Table 3：换算后基底 −19.3 vs −15.2，心尖 −21.9 vs −19.4；Table 4 偏差 −4.0、−2.4；DENSE 三层均值 −15.2、−17.2、−19.4 | 三层的受试者不同（39/69/38，非完全配对）；梯度未作正式受试者内检验 [未报告] | 梯度"被破坏"是对三组均值的比较；through-plane 归因未检验 | 偏差：强（基底 t≈−7.3）；心尖：中（p=0.01）；梯度论断：弱–中 |
| 3 | FT 对 Ell 不准确（Conclusion）／临界可接受（摘要 Results） | [原文事实] Table 3–4：换算后偏差 −0.2，p=0.77，LoA ±9.3，CoV 19.3% | 40 人，98% 健康；FT 仅心内膜 vs DENSE 透壁；单一四腔切面 | 两种表述相互矛盾；按预设 CoV 判据应为可接受 | 数值：中；"不准确"的分类：不足 |
| 4 | FT 扭转与 dyssynchrony 一致性差（扭转低估、dyssynchrony 高估）（Results；Discussion） | [原文事实] Table 3–4：扭转 2.1 vs 3.5 deg/cm，偏差 −1.4，±2.4，CoV 41.1%；dyssynchrony 42 vs 16 ms，偏差 26，±56，CoV 76.3%；Circle 扭转反向高估 1.5 deg/cm（正文概述） | 38 人三层短轴；dyssynchrony 依赖节段 Ecc 曲线与帧率（bSSFP 时间分辨率 20.2–49.7 ms，DENSE 17–34 ms） | dyssynchrony 的高估部分可能来自估计量本身对噪声和时间分辨率的正向偏倚，而非仅追踪误差 [读者推断]；DENSE 16±20 ms 提示分布偏态，Bland–Altman 的正态假设可疑 [读者推断] | 中–强（"一致性差"成立；"FT 系统性低估扭转"只对 TomTec 成立，两家方向相反） |
| 5 | FT 片层应变与轮廓法几乎相同，故 FT 对片层应变"不必要"，手工轮廓可替代（Results；Discussion；Conclusion） | [原文事实] Table 5：偏差 −1.3 到 0.2，LoA ±2.2–±3.8，CoV 3.2–7.0% | 轮廓来自 TomTec 自身传播，仅 TomTec（Circle 的轮廓法比较在已读正文中未见） | 独立手画轮廓是否等价未检验；Ell 的 −1.3 偏差按读者重算 t≈−6.7，为系统差异却称"excellent"；Fig. 5 图注显示软件存在额外处理（作者推测为曲线拟合） | "TomTec 片层应变 ≈ 自身轮廓长度变化"：强；"手工轮廓可替代 FT"：不足 |
| 6 | 当前商用 FT 技术对心脏力学定量效用有限（Conclusion 末句） | 上述 1–5 的综合 | 两家软件 2018 年前后版本；2D；年轻、以健康为主人群；未直接评价节段应变、应变率、预后 | 推广到"current commercial FT technology"整体和所有人群 | 弱–中（方向有依据，范围外推） |

### 发现的问题（按严重度）

**致命（针对具体结论，而非全文数据）**

问题 A：分类结论的决策规则不一致（Statistics vs Conclusion；摘要内部）。作者预设 CoV<20% 为可接受，但最终"只有中段准确"的分类依赖偏差的显著性检验，而偏差显著性又随各层样本量变化。在这种条件下，"准确/不准确"的边界可以通过换判据而改变：按 CoV 判据，四个换算后的片层应变全部可接受；按"偏差 p≥0.05"，中段和 Ell 可接受；Conclusion 却只保留中段。来源：[读者推断]，作者未在 Limitations 讨论。能消除疑问的是：预先设定临床可接受的绝对容差，并报告 LoA 及其置信区间，或做等价性检验。这一问题动摇的是 Conclusion 的二分措辞，不动摇 Table 3–4 的数值。

问题 B："手工 ED/ES 轮廓可替代 FT"未被检验（Methods, FT 小节；Discussion；Conclusion）。轮廓法用的是 FT 自己追踪出的 ES 轮廓，使比较几乎成为同一几何量的两种读法；在临床手画轮廓时，ES 帧选择、小梁/乳头肌处理和观察者间变异都会引入额外差异，LoA 会增宽，幅度未知。来源：[读者推断]；作者以"no fundamental difference"一句带过，并引用前人类似建议（参考文献编号在所得文本中缺失，未能核对）。消除方法：由独立观察者手画 ED/ES 轮廓，与 FT 和 DENSE 三方比较，并报告观察者间重复性。这一问题对论文最常被引用的那句话（"FT unnecessary for global strain"）影响最大。

**限定**

问题 C：参考标准误差未量化，且 DENSE 本身也是 2D、经过平滑（Methods, DENSE 小节）。LoA 同时包含两种方法的误差；没有 DENSE 自身的重复性或观察者间数据，就无法判断 ±6.3 中有多少属于 FT。来源：[读者推断]；作者在 Discussion 提到"Inter-test variability in both techniques ... also contributes"，属部分承认。可补：同一数据的 DENSE 重复分析或扫描–重扫，作为一致性的上限。

问题 D：人群谱、中心与场强混杂（Table 2；Methods, Image acquisition）。3 T 数据全部来自 Kentucky，1.5 T 全部来自 CHOP，两中心的人群构成也可能不同；正文未按中心/场强分层报告 [未报告：已查 Methods、Results、Discussion、Limitations；补充材料未读]。3 T bSSFP 的伪影和不同场强下 DENSE 的 SNR 都可能改变一致性。四腔 98% 健康，Ell 的结论只适用于健康年轻人。作者在 Limitations 承认人群未覆盖所有患者，并推断功能差者一致性可能更好。

问题 E：时相与参考态未在正文中明确（Methods 各小节）。比较的是峰值应变还是收缩末期应变、两种方法是否在同一时点取值，正文未写明 [未报告：已查 Methods、Results、表注、图注；补充材料未读]。只有轮廓法明确 ES = 周长最小帧。ED 帧在 bSSFP 中如何选定、DENSE 的参考态（编码时刻）是否与之匹配，也未报告。若一方取各自峰值而另一方取固定帧，偏差中会混入时相差异。两方法时间分辨率不同（bSSFP 20.2–49.7 ms，DENSE 17–34 ms），且 DENSE 做了 10 阶多项式时间拟合，峰值可能被平滑。来源：[读者推断]。

问题 F：误差机制（through-plane、小梁、切向梯度弱）是推断而非结果（Discussion）。见断点 3。对作者结论的方向影响不大，但对想据此改进算法的读者很关键。

问题 G：结论外推到"区域"和"整体技术"（Conclusion 末句）。论文没有直接报告节段应变的 FT–DENSE 一致性，dyssynchrony 是唯一使用节段信息的指标，而它对噪声敏感；只评价了两家软件的特定版本。来源：[读者推断]。

问题 H：dyssynchrony 指标的估计偏倚（Methods, DENSE 小节；Table 3–4）。"节段延迟的标准差"在节段曲线带噪声时会被系统性抬高，而 bSSFP 的帧间隔（最长约 50 ms）与 FT 的 42 ms 数值同一量级。所以 FT 的 dyssynchrony "高估"既反映追踪误差，也可能反映指标对噪声和时间分辨率的固有偏倚。来源：[读者推断]；作者解释为节段应变重复性差，二者并不矛盾，但后者未被拆开。

**次要**

问题 I：正文与表格数字不一致（重算见下）。Results 写换算前 Ecc 高估"between 2.3 and 6.0%"，而 Table 4 基底为 −6.5；写 Ell 高估 1.4%，Table 4 为 −1.5，Table 3 均值差为 −1.6；写换算后基底、心尖"by 4.1 and 2.5% ... [p<0.001 for both]"，而 Table 3 心尖 p=0.01、摘要也写 p=0.01，Table 4 偏差为 −4.0 与 −2.4（4.1/2.5 恰为 Table 3 均值之差，属四舍五入来源不同）。都不改变结论。

问题 J：CoV 的公式未报告，读者用常见定义（差值标准差 ÷ 两法均值、或再除以 √2）都无法重现 Table 4 的 CoV（例如换算后基底按前者得约 19.8%，报告 17.8%；中段约 18.5%，报告 10.9%）。CoV 恰是 Methods 的预设判据，这使断点 1 更难评估。LoA 未给置信区间。

问题 K：心肌层匹配不完全（Methods, FT 小节）。心内外膜两条轮廓应变的平均不等于 DENSE 全部像素的平均；Ell 用心内膜对 DENSE 透壁。作者把心内膜比较放在 Additional file 2（未读）。

问题 L：FT 与轮廓法 Ell 偏差 −1.3、LoA ±2.4（Table 5），读者按 SD≈1.22、n=40 重算 t≈−6.7，是明确的系统差异，正文统称"excellent agreement"且未报告该比较的 p 值。另外据图注，Fig. 4 的差值方向（轮廓法 − FT）与 Fig. 2–3（FT − DENSE）相反，引用时需注意符号。

### 探针覆盖情况

关键支点：查过，发现问题。"中段一致"的唯一支点是 Table 4 中段一行（Circle 文字概述为旁证）；"FT 不必要"的唯一支点是 Table 5，而 Table 5 的轮廓来源决定了它的解释范围（问题 B）。构念一致性：查过，发现问题，片层应变一致 ≠ 区域追踪正确，作者自己在 Background 第 4 段已指出这一点，但结论仍外推到"心脏力学"整体（问题 G）。参考标准：查过，发现问题（问题 C）。统计单位与独立性：查过，未见问题，各层分析单位为受试者、每层每人一个切面（186 = 39+69+38+40，与 Table 2 各列 n 一致），未见把节段当独立样本；只是不同层的受试者不同，层间比较不是配对的。数据泄漏：不适用（无训练过程），但"追踪不佳时重画直到视觉可接受"属于对 FT 有利的人工干预，分析者是否对 DENSE 结果设盲 [未报告]。多重比较与选择性报告：查过，未见实质问题，指标较少且主要 p 值很小；Circle 详细结果放在补充材料（未读），正文只给概述。混杂与替代解释：查过，发现问题（问题 D、E、H）。外部有效性：查过，发现问题（问题 D、G）。效应量与不确定性：查过，发现问题，未报告 LoA 置信区间，CoV 不可重现（问题 J）。内部一致性：查过并重算，发现问题（问题 I、L）。

### 重算记录

由 Table 3 均值重算均值差：换算前基底 −21.7−(−15.2)=−6.5，中段 −2.3，心尖 −6.0，Ell −1.6（Table 4 为 −1.5）；换算后基底 −4.1，中段 −0.3，心尖 −2.5，Ell −0.3（Table 4 分别为 −4.0、−0.4、−2.4、−0.2，差异在四舍五入范围内）。

换算公式核对：对单一线元，Green 应变 E = ½(λ²−1)，λ = 1+ε，故 E = ε + ½ε²，公式在数学上精确。代入 Table 3 未换算均值：基底 −21.7% → −19.35%，中段 −19.5% → −17.60%，心尖 −25.4% → −22.17%，Ell −15.4% → −14.21%；若计入组内方差项（E[ε²] = 均值² + SD²），得 −19.26、−17.51、−21.87、−14.08，与 Table 3 换算值（−19.3、−17.5、−21.9、−14.1）一致，说明换算是逐个受试者做的，表内数字自洽。

由 LoA 反推差值标准差（SD = LoA/1.96）并重算配对 t 检验：换算后基底 t≈−7.3（p<0.001），中段 t≈−1.0（p≈0.30，报告 0.36，差异来自偏差四舍五入），心尖 t≈−2.7（p≈0.011，与 Table 3 的 0.01 一致，与 Results 文字"p<0.001 for both"不一致），Ell t≈−0.27（p≈0.79，报告 0.77）；未换算 Ell t≈−1.74（p≈0.09，报告 0.083）；扭转 t≈−7.0，dyssynchrony t≈5.6。FT vs 轮廓法 Ell：t≈−6.7（p<0.001），中段 t≈−3.7（p≈0.0004）。

LoA 95% 置信区间近似半宽（Bland–Altman 近似，SE ≈ √(3·SD²/n)）：换算后中段约 ±1.3 个百分点，基底约 ±1.9，心尖约 ±3.0，Ell 约 ±2.6；dyssynchrony 约 ±16 ms。也就是说中段 LoA 的上下界本身就有约 1.3 个百分点的不确定性。

文献计数：39/62 = 62.9%，13/62 = 21.0%，与正文 63% 和 21% 一致。

CoV：尝试两种常见定义均无法重现 Table 4，记为不可重算（问题 J）。

以上为读者基于表格汇总数字的近似重算，没有原始数据。

## 自我反驳

为作者辩护的最强论证是：这是一篇针对"FT 被当作 DENSE/tagging 替身"这一常见做法的验证研究，在当时首次用 DENSE 做直接比较，样本比既往同类研究大，并且主动处理了 1D 与 Green 应变的定义差异、心肌层差异，还用第二家软件复核，这在 2018 年的同类文献中是相当仔细的；"准确/不准确"的措辞只是对清楚的数值结果做通俗概括，读者完全可以直接看 Table 4。轮廓法用 FT 自身轮廓，作者明确说是为了去除观察者变异、"纯粹地"检验追踪信息，这是一个有意的、有理由的设计。

据此我做了以下删改。"样本量小"不作为问题：各层 38–69 人，在一致性研究中不算小，且大于作者引用的前作。"未评价预后价值"删除：超出本研究问题，作者已在 Limitations 承认。"排除径向应变"不列出：作者给了理由，且该理由在领域内被普遍接受。"文献计数不是系统综述"不列出：Table 1 只用于说明动机，不承担结论。"多重比较未校正"降为探针中一句：主要 p 值远小于任何合理校正阈值。"DENSE 不是真值"保留但降为限定而非致命：用独立运动编码成像作参考是该类在体研究的常规上限，问题在于未量化其误差，而不是选择了它。

保留为致命的两条（A、B）经得起反驳：A 不是"我更喜欢另一种统计量"，而是论文自己预设的判据与自己的结论冲突，且冲突体现在摘要内部；B 不是对设计选择的偏好，作者的设计选择本身合理，问题在于结论把一个只针对 FT 自身轮廓的结果推广到了从未检验过的手工轮廓。

关于前提：这篇论文问的是"FT 片层应变能否替代 DENSE 片层应变"。对临床读者这是对的问题；但对关心区域运动的读者，更关键的问题是"FT 的区域/材料点对应是否正确"，本文只通过扭转和 dyssynchrony 间接触及，而 Table 5 恰恰说明片层应变根本测不到这一层。这一点是本文对你的工作最有用的启示，而不是它的缺陷。

## 第三层：下一步

以下结合你在做的 cine-CMR 区域运动/应变综述和探索性工程来写；它们是候选做法，不是既定方向。

### 可以借鉴的

最值得复用的是"无追踪基线"的思路：用 ED/ES 轮廓长度变化作为一个不含区域追踪信息的对照，再看追踪方法是否在该基线之上提供了额外信息。对你的工程而言，任何声称改善区域运动的 cine 方法（包括深度学习配准），都可以同时报告一个"仅轮廓/仅分割"的基线，用来区分"边界运动好"和"材料点对应好"。复用前提是基线要在你关心的尺度上定义：片层尺度上它几乎必然与追踪一致（本文 Table 5），只有在节段、局灶和时序层面，追踪才有机会显示差异。

第二个可借鉴的是应变定义的显式换算：比较 1D Lagrangian（工程）应变与 Green–Lagrange 应变前先换算，本文显示仅这一步就让中段偏差从 −2.3 降到 −0.4 个百分点。你在综述中比较不同研究的数值，或在工程里与 DENSE/tagging 对比时，可以把定义、参考态、心肌层和时相写成固定字段。

第三是按切面水平分层报告，而不是把基底、中段、心尖合并成一个全局值；本文的主要信息恰恰来自层间差异。

### 要避开的

不要只用 CoV 或 p 值给一致性下"准确/不准确"的结论；先设定绝对容差（个百分点），并报告 LoA 和其置信区间。不要把"与自身轮廓一致"写成"与手工轮廓一致"，也不要把片层应变一致外推为区域追踪正确。若使用 DENSE 作参考，应报告或引用其自身重复性作为一致性的上限，并检查平滑与时间拟合对峰值的影响。分层报告中心/场强，尤其是 3 T bSSFP。dyssynchrony 类"延迟离散度"指标需要考虑噪声与帧率造成的正向偏倚，最好用仿真或重复扫描估计其零假设下的分布。

### 引用这篇时可以这样写

"In a retrospective two-centre cohort of 88 predominantly healthy young participants, TomTec feature-tracking slice-wise circumferential strain agreed with 2D spiral cine DENSE without systematic bias only at the mid-ventricular level after converting 1D Lagrangian to Green strain (bias −0.4 percentage points, 95% limits of agreement ±6.3), whereas basal and apical Ecc were overestimated and torsion and dyssynchrony agreed poorly; feature-tracking slice-wise strains were nearly identical to strains computed from the software's own propagated end-diastolic and end-systolic contours (Wehner et al., 2018)."

中文可写作：在以年轻健康者为主的 88 人双中心回顾性样本中，经应变定义换算后，TomTec FT 的中段片层 Ecc 与 2D DENSE 无系统偏差（一致性界限 ±6.3 个百分点），基底和心尖 Ecc 被高估，扭转与 dyssynchrony 一致性差；FT 片层应变与其自身传播的 ED/ES 轮廓长度变化几乎相同。引用依据的阅读深度：正文全文与 Table 1–5 已读，图仅读图注，补充材料未读。避免引用为"手工轮廓可替代 FT"或"FT 对 Ell 不准确"，这两点本文没有直接证据或判据不一致。

### 还没被回答的问题与最小实验

问题一：在节段尺度上，cine 追踪是否比"无追踪基线"更接近运动编码参考？最小分析是在同一切面配对的 cine 与 DENSE（或 tagging）数据上，分别计算 AHA 节段 Ecc 的三种估计：FT/配准方法、仅由 ED/ES 轮廓按等弧长对应得到的节段应变、DENSE；以受试者为聚类单位，用混合效应模型或按受试者自助法估计一致性。若追踪方法与 DENSE 的一致性不优于轮廓基线，说明在该尺度上追踪没有提供额外的材料点信息；若优于，才支持"区域追踪有用"。这需要已授权的配对数据，本交接不授权获取新数据。

问题二：基底 Ecc 偏差是否确实由 through-plane 运动驱动？最小分析是用同一受试者的长轴 cine 测量二尖瓣环纵向位移（MAPSE）作为 through-plane 位移的代理，检验受试者层面的基底 FT−DENSE 偏差是否与之相关；若相关明显，支持作者机制并提示需要切面跟随或 3D 方法；若不相关，需要考虑切面位置不匹配或 ES 定义等其他解释。

问题三：独立手画 ED/ES 轮廓是否与 FT 片层应变等价？最小实验是让一至两名独立观察者在同一 bSSFP 上手画 ED/ES 轮廓，与 FT 和 DENSE 三方比较，并报告观察者间 LoA；若手画–FT 的 LoA 接近本文 Table 5，作者的推广成立，否则"FT 不必要"只能限定为"区域追踪不改变片层应变"。

## 局限与核实提示

这是 AI 辅助的单人精读，不等于独立同行评审。图像本身和四个补充材料没有读到，凡涉及图形形态、心内膜单独比较、Circle 详细结果和公式推导的判断都应在取得原文 PDF 与补充材料后复核。重算均基于表格汇总数字的近似，不是原始数据分析；CoV 的定义未能重现。用于你自己的稿件前，请对照原文核实这些关键数字：Table 4 中段换算后偏差 −0.4、LoA ±6.3、CoV 10.9%；基底 −4.0/±6.7/17.8%；心尖 −2.4/±10.8/14.8%（p=0.01，而非正文所写 p<0.001）；Ell −0.2/±9.3/19.3%；扭转 2.1 vs 3.5 deg/cm；dyssynchrony 42 vs 16 ms；Table 5 FT–轮廓法 LoA ±2.2–±3.8；人群构成（Table 2，四腔 98% 健康）。"决策规则不一致"和"手工轮廓未检验"两条主要批评属于读者推断，建议你读原文 Statistics、Discussion 首两小节和 Conclusion 后自行判断。正文中引用的前人研究在获取文本中缺少编号，无法逐条核对。

信息来源：According to PubMed / PubMed Central (PMC6136226)，DOI [10.1186/s12968-018-0485-4](https://doi.org/10.1186/s12968-018-0485-4)；表格与图注另取自 Europe PMC 同一记录的 JATS XML。
