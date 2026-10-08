# 执行说明

## 最小合同和阶段

从用户材料确定一句主张、图的角色、证据、交付模式和修改边界。规划模式到计划为止；预览继续生成并检查 PNG；精修处理指定变更；审计不修改图。用户要求自动完成时，合同和 panel 计划作为内部产物，只有材料无法确定的科学含义才需要补充。

默认：研究论文、学术风格估计、中文说明、英文图内标签、PNG 预览。未指定期刊时 `style_status=ESTIMATED`，不能声称符合期刊当前要求。用户要求投稿合规时查阅当前官方或用户提供的有效指南。记录素材来源、必保留文字和不可新增含义；正文与图注冲突时列出冲突源，可先完成无歧义部分的计划。

## Claim 与图形结构

用 `02_claims.csv` 记录每个实质主张的来源位置、证据状态、observable、推断目标、条件、视觉元素、关系与图注边界。证据状态可为 observed、literature_result、analytic、conditional_inference、hypothesized、illustrative 或 unresolved；记录依据而非仅贴标签。装饰性对象不必逐个建 claim。

| 论证 | 可选结构 |
|---|---|
| 输入如何限制推断 | 观测—估计—测量定义—输出，附假设与验证分支 |
| 相同表观结果不能唯一识别隐藏量 | 配对状态或反例，共同观测与不同潜在解释 |
| 方法假设或信息来源比较 | 共享输入/输出、中间平行分支 |
| 预测与监督关系 | 明确 prediction 与 target 汇合，损失指向实际优化/采样对象 |
| 区域异质性和聚合 | 区域模式—曲线—指定聚合 |
| 生物机制 | 区室、角色、过程、有证据状态的关系 |

这些是选择依据，不要求每张图固定六段。不把流程、相关或测量关系自动画成生物因果关系。

## Cine-CMR 条件检查

仅在 cine-CMR motion/strain/conditional recoverability 任务中使用：cine intensity、边界、纹理和时间信息属于可获得的图像信息；没有额外材料点编码依据时，稠密材料对应需推断。位移、形变映射、应变定义、坐标轴、层、参考时相、区域支持、峰值和聚合影响结果，图只需呈现与论证相关的合同部分。

Segmentation overlap、image similarity 或平滑性不能单独证明 material correspondence 或 regional strain validity。人工解析映射和曲线须标为解析/概念例子；如果全局曲线声称是区域均值，按指定权重逐点计算并核对。Conditional recoverability 尚未验证时表达为研究问题、条件性推断或研究设计。仿真参考结论受仿真假设及参考定义限制，不据此宣称患者获益。这份清单不建立新的实验结果，具体事实仍依据当前素材。

## 版式

按实际使用尺寸排版。双栏图可从约 175–180 mm 宽、主体标签 7.5–9 pt、标题 9–10 pt 开始；这是可调整预设，不是期刊通用规定。单栏、海报或幻灯片需另定尺寸。压缩空白不能牺牲字号、箭头或技术对象。白底、灰黑文字、少量低饱和强调色，语义一致；错误/异常用颜色时辅以线型、符号或标签。按需使用 lowercase panel labels。参考样本优先于预设；没有 Zoya 等具体样本时记录为文字偏好预设。

## Backend 和交付验证

| 格式 | 制作路径 | 验证 |
|---|---|---|
| PNG | 代码/矢量渲染或图像生成 | 实际像素、标签、拓扑、caption 与证据 |
| 数值图 | Python/R 或已有脚本 | 源表、单位、轴、权重、样本、不确定性含义 |
| SVG | text/path/shape/group | 文本保持为文本，语义对象独立，整图没有被 bitmap 替代 |
| AI | 支持的 Illustrator 保存路径 | 重开原生文件，检查文字、路径、图层及 raster/placed 对象 |
| PPTX | 原生文本、形状、连接线 | 重开/渲染，检查独立对象及布局 |
| PDF | 矢量渲染/应用导出 | 字体与 raster/vector 结构；不能自动等于 native editability |

真实 MRI/WSI 可作为 raster panel，框、文字和箭头可分别编辑；如实报告范围。Outlined text 不等于可编辑文本，bitmap wrapper 不等于可编辑机制图。K-Dense scientific-schematics 的生成模型评分不能代替科学源核对或实际视觉检查，其当前安装版依赖 OpenRouter 且输出 PNG；运行前依据实际配置核对能力。

## 文件和状态

新任务复制需要的模板到独立 job，然后填写实际内容。规划用 01_task、02_claims、03_panels；预览/编辑版再添加实际 source（有时）、preview、04_caption、05_audit、06_delivery，以及所需 exports。精修保存新版本与变更记录；审计仅写报告；继续时核对源材料、上一版图稿和检查记录，旧 ready 状态不能直接沿用。

这些文件不等于 scientific-figure-suite project memory。需要 suite memory 时先读其 `shared/figure_memory_protocol.md`，按它的脚本和 schema 初始化，不把简化模板导入其 memory 工具。

至少核对科学源与箭头，打开实际保存的预览并检查最终尺寸。数据图核对源值，原生图核对对象结构，修改任务核对边界。需要保存原状的输入按风险核对修改前后哈希。源表没有区间或误差时不新增误差棒。报告中区分实际执行的源核对、程序检查、视觉检查和未执行检查。

存在 unsupported causal claim、伪造数据或 estimand 错配时先修正，再生成交付。期刊未验证只阻止投稿合规声明，不阻止已检查的预览。`06_delivery.json` 只记录实际存在的文件、实际 backend、可编辑/raster 范围和检查结果。
