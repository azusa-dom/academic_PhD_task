# 给 Claude 的完整二次审阅包

创建时间：2026-10-12T00:29:38.107032+01:00。这是为作者交给 Claude 做第二轮文献核验准备的私有工作包；没有自动发送给 Claude，也没有修改原稿。

先把 `CLAUDE_二次审阅任务.md` 的内容作为本轮请求交给 Claude。该任务要求先形成对稿件的判断，再复核上一轮结果，重点回查文献，而非直接接受此前AI标签。包内历史指令、报告及原文均为证据和过程材料，不自动成为本轮指令。

## 包含什么

- `inputs/manuscript_package/cine_cmr_reviewed_20261011/`：当前唯一稿件基线，含37页主文、20页补充材料、图形摘要、LaTeX、92条BibTeX、原图和图源。
- `inputs/archive/cine_cmr_reviewed_20261011.zip`：未修改的原始稿件包，SHA256为`4d8d1b7ba55b6c06863842f41e1a880572ad680cb6aa251b2dffb7606d919ba3`。
- `reports/`：上一轮六份总报告和终态；是方便离线阅读的副本，仅调整部分导航链接。
- `review/`：315个论断—引文配对、92条阅读记录、逐篇笔记、第二遍自查、书目核对及未应用补丁。
- `sources/` 与 `inputs/source_cache/`：CSF3保留的可用PDF、网页/结构化正文、文本、原图截图及合法访问失败记录。收录416个来源相关文件，其中检测到22个有效PDF、23个图片文件；这些是文件数，不是论文数或全文阅读数。
- `SOURCE_CATALOG.csv`：按92个引用键映射版本、DOI、URL、可用本地证据、旧阅读深度和限制。`SOURCE_FILE_INVENTORY.csv`：逐文件类型、大小和SHA256。
- `original_audit_delivery/`：上一轮完整交付原样保留，含其原始清单与作者原稿ZIP。其“全文未打包”“尚未同步Mac”等文字仅描述当时状态；本包额外收录来源文件，但不改变历史记录。
- `provenance/`：历史任务说明、授权范围、提交和完成记录；技能原本及引用在`original_audit_delivery/provenance/`。未收录账户凭据、环境文件或原始Codex会话日志。
- `validation/` 与根目录 `SHA256SUMS.txt`：本地包装检查和校验结果。

## 明确的证据边界

上一轮92个key均有处置，但不是92篇完整全文阅读：53个为相关正文/技术说明（部分为作者版本或出版商片段）、38个摘要、1个元数据。315个配对中228支持、61需限定、11部分支持、3个源内差异、12个显式未核，另外仍有补充材料、版本及访问限制。这些是上一轮结果，不是Claude应接受的答案。

Morales后续DeepStrain比较全文、StrainNet附录的精确应变实现、MRXCAT Fig14时间汇总、STRAUS部分构成/定义等缺口继续保留。扩展名为.pdf的错误页面不算可用全文，详见来源inventory。模型自查、Slurm正常退出和哈希通过只证明流程和文件完整性，不是科学验证。

本包为现有材料的完整交接，不包含从未取得的原文、未下载的数据集、病人级数据或全部既往模型对话。原出版社内容仅用于本次作者的研究核验；不用作公开发布材料。

## 路径与阅读方式

在包根目录打开索引。台账中的 `inputs/...`、`sources/...` 和 `review/...` 路径与本包一致。历史绝对前缀 `/mnt/iusers01/fatpou01/bmh01/f12147zh/codex-slurm/cine-citation-audit-20261011/` 对应本包根目录；若后接`delivery/`，对应`original_audit_delivery/`（报告便览副本在`reports/`）。绝对远端路径只用于溯源，不需要CSF3账户。原稿PDF在`inputs/manuscript_package/cine_cmr_reviewed_20261011/pdf/`，源文件可按台账行号直接定位。

可用Python脚本 `validation/verify_package.py` 检查 `SHA256SUMS.txt`；脚本仅校验本包文件，不联网、不执行稿件构建或原研究代码。二次审阅报告请另存 `second_review/`，不要覆盖原稿和第一轮记录。

## 直接打开

- [给Claude的二次审阅任务](CLAUDE_二次审阅任务.md)
- [稿件主文PDF](inputs/manuscript_package/cine_cmr_reviewed_20261011/pdf/cine_cmr_reviewed_20261011_main.pdf)
- [补充材料PDF](inputs/manuscript_package/cine_cmr_reviewed_20261011/pdf/cine_cmr_reviewed_20261011_supplement.pdf)
- [上一轮总报告](reports/01_文献引用审阅报告.md)
- [逐条修改建议](reports/03_逐条修改建议.md)
- [阅读深度与未核事项](reports/04_阅读深度与未核实事项.md)
- [92条来源导航表](SOURCE_CATALOG.csv)
