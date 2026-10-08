# 状态

- 任务：`Healthy_Volunteer_004` 单切面 DENSE 重建与作者代码解析核验
- 当前实际 Slurm Job：`21788470`；`node1270`；4 CPU；16 GiB
- 运行框架：任务计算与交付物生成已完成；外层 agent Job 在最终交付时仍报告 `RUNNING`
- Job 21644409 继承证据：`SEQUENCE_METADATA_IMPORT_PASS` 与 `INDEPENDENT_ANALYTIC_CHECKS_PASS`，均不等于完整重建/作者程序验证
- 分支 A：`COMPLETED_WITH_ORIGINAL_FAILURE_AND_PATCH_PASS`
- 分支 B 像素读取：`COMPLETED_REAL_PIXELS`
- 分支 B 位移/平面应变：`EXPLORATORY_RESULT_GENERATED_NOT_REFERENCE_VALIDATED`
- 轮廓：`WAITING_HUMAN_REVIEW`（已交付逐帧可编辑 CSV/掩膜/叠加图）
- 与作者处理后输出一致性：`NOT_EVALUABLE`（无对应 `.dns`/MAT/病例切面对照）

关键否定性 QC：seed_top 对基线最大位移差 15.25 mm；基线解包裹后仍有 x/y 496/640 个 >π 邻域跳变；不得作临床、梗死区或三维梯度结论。
