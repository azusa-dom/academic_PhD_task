# cine-CMR 分层文献核验任务

本任务以用户提供的 cine_cmr_reviewed_20261011.zip 为唯一稿件基准，采用 peer-review skill 做文献与论断对应审阅。先核对第一层 17 篇文献（原清单 16 组，其中 DeepStrain 含两篇），再核对 4 篇重建研究，随后覆盖其余 71 条书目。必要时将摘要级条目升级为相关章节全文核验。92 条书目与 250 次初步识别的引用出现均有索引；原压缩包与解压文件保持不变。

阶段顺序：01_CORE → 02_CORE_RECON → 03_REMAINING → 04_SYNTHESIS。任务要求逐篇保存进度、证据位置、实际阅读深度、支持程度和精确修改建议。本文是 critical narrative review；输出是作者内部审阅草稿，不是独立人类同行评审或投稿认证。没有授权自动改写正文，因此只交付可审阅的修改建议。

模型沿用此前作者明确选择的 gpt-6-astra / high；仅当模型明确不可用时允许 gpt-6.1-sol / high。Slurm: serial, 1 CPU, 4 GB, 12 小时。资源限制不是完成时间承诺。查看 runs/submission.json 取得作业号，远端 runs/<job>/status 查看实际阶段。后续结果保存在 delivery/ 和 cine_cmr_citation_audit_20261011.zip。

任务方法见 TASK_COMMON.md；授权和 peer-review 通用本地门禁的适配见 AUTHORIZATION_AND_SCOPE.md。书目核验与阅读深度必须如实记录，未能读到全文的关键问题不得标为已核实。
