# 修订版技术与人工检查记录

日期：2026-10-11。检查对象为 `working/manuscript/`，最终构建目录 `review/qa/revision_build_03/`。这是第二阶段修订检查，不覆盖第一阶段QA，也不认证临床/科学有效性。

## 源码、证据和输入完整性

- 主文、补充、书目、全部主/补表与图注经过源文件读取与修订；94当前citekeys均有具体位置映射，无缺引、重复key或重复DOI。4个主表、3个编号补表及2个note表保留方法/尺度/参考信息。
- 252个输入manifest文件逐个SHA-256匹配，零变化。Git检查原始editable_sources、原PDF和baseline_inputs无修改。MRXCAT CSV与原版逐字节相同，SHA-256 `f0df33ccc5721072b9f7439d64a794523486245ca980c1aa94554d71385f81cc`。
- 176条变更记录；27项issue处理；94当前引文位置表；175条证据行含163历史/审计行与12追加源核验；371条覆盖行。历史字段保留，新增revision字段区分落实状态。135条历史记录经key/DOI别名对齐后10条不对应当前引用，保留作历史而非当前支持。
- 12项重点来源由fresh-context AI复核，随后定向回读正文/图源；F01–F05残余项已处理。未把identity、摘要或可下载全文升级为逐条详细claim已证实。独立报告不是临床专家认证。

## 构建与字体

先读取现有 `scripts/build_manuscript.sh`、`scripts/static_qa.py`；没有为得到PASS修改它们。采用现有pdflatex + BibTeX（每文档三轮TeX与一轮BibTeX）。最终日志无Warning、Overfull或undefined引用。静态检查通过括号、环境、label/cite、引用文件、CSV形状及可移植性。

主文38页、补充23页，全部A4 210×297mm竖版，61页都有可提取文字。`pdffonts`显示全部字体嵌入并有Unicode映射。PDF文字包围框未越出页面。完整机器记录见 `qa/final_pdf_metrics.json`、`qa/revision_technical_results.json`及字体列表。

最终图页：主文5/7/16/18/26，补充4/6/8。主文图普通文字最低约7.066pt，补图约7.059pt；数学上下标最低约6.199pt和6.731pt。这里的“普通文字”指SVG图内sans-serif正文，不是论文正文的11pt；测量直接来自最终PDF。图1约6.47pt、图2约6.20pt及S1约6.73pt的小字为公式下标/上标。正文边距25/22mm未变，图宽190mm，页面边缘留10mm。专页排版保留留白，不声称已经符合尚未取得的JCMR版式规范。

图源从现有agarwood代码创建独立衍生目录，保留原文件。原代码的Python3.12 f-string在当前Python3.9失败；仅修衍生代码并使用已有librsvg/Cairo、PyMuPDF和字体工具，未安装共享环境。修正librsvg默认DPI导致的物理尺寸差异，显式72dpi和精确PDF框。文字测宽使用Liberation Sans；最终Cairo嵌入Nimbus Sans及必要的Liberation/DejaVu fallback字体。实际依赖版本在衍生requirements.txt。

## 实际渲染及目检范围

1. 九幅独立衍生图（Figures1–5、S1–S3、GA）全部渲染PNG并通过图像工具逐幅查看。发现并修正图1底部贴边/跨列、S3底部留白和tspan公式间距。修后重新查看Figures1/2/S3；Figure3数据说明调整不改变图形数值。
2. build02的主文38页、补充23页全部65dpi渲染，分8张contact sheet实际逐张查看；放大130dpi查看主文16/18/20/30、补充11/13。后两处语言改动（Tsuneta重复说明、结论longitudinal歧义）形成build03。
3. build03全部61页重新渲染。机器逐页像素比较确认其余页未变；主文28–38因文字/行号变化，重新查看覆盖25–38页的两张contact sheet。最终130dpi还实际查看主文5/7/26和补充4/6/8；加上像素相同的build02主文16/18，全部八个最终图页均已放大检查。没有把仅生成但未打开的detail PNG计入已目检。
4. 所检图页无文字裁切、显著碰撞或错误面板号，Figure4数值/SD范围说明与正文一致。主表与补表检查包括全部源单元格、全页总览，以及上述重点页放大；并非每一个最终表单元格均再次高倍率视觉逐字核验。摘要/结论/声明经过源文回读及页面总览。

中间构建和失败日志保留，不替换为成功日志。最终渲染位于 `review/rendered_revision_final/`；机器测试不替代以上真实目检，也不证明发表条件已满足。

## 可复现交付

干净目录重编译、ZIP完整性、文件非零和交付checksums由本报告后续验收记录补充。原始输入、全文快照、缓存、环境和庞大日志不放入交付包；工作区保留查证痕迹。归档包含清稿、原图/修订可编辑图源、报告、证据与差异文件，不含Git状态数据库或凭证。

作者声明、历史筛选原始数据、部分来源详细结果、StrainNet源内LoA差异和JCMR具体要求保持未决。构建完成不关闭这些事项。

### 干净目录复现验收

已从精简交付源码复制到 `/tmp/slurm.22557325/cine_revision_clean_3oc_yc7h/`，用原build脚本从零重编译。主文38页、补充23页，最终日志无Warning/Overfull/undefined；与交付PDF逐页抽取文字及72dpi像素均完全相同。PDF二进制中的时间戳/ID可不同，不将其误报为内容差异。机器结果见 `qa/clean_rebuild_result.json`。

可编辑图源亦在同一干净副本单独重新生成九幅PDF/SVG/PNG；九幅PDF的72dpi像素与交付图均相同，见 `qa/clean_figure_rebuild_result.json`。这验证当前图源路径/依赖可重建，未重复任何临床实验。

CSF3阅读镜像已成功写入并对8个文件记录SHA-256；Mac/iCloud未验证。镜像记录为 `qa/obsidian_revision_export.json`。

### 交付包验收

`cine_cmr_review_author_revision_20261011.zip`已通过ZIP CRC完整性检查、逐个内部SHA-256核验、必需文件存在/非零检查，共164个文件。交付根目录提供 `REVISION_SHA256SUMS` 及ZIP单独的 `.sha256`。精简源码已完成上述干净目录重编译；归档检查结果见 `qa/revision_archive_result.json`（工作区外部记录，避免ZIP对自身checksum循环引用）。所有未决科学/作者/权利状态保持原样。
