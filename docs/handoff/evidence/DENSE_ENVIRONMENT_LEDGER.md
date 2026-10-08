# 环境台账

- Provider：CSF3 当前 Slurm 分配；Job `21788470`；node1270；4 CPU；16 GiB；无 GPU 命令。
- Python：复用只读旧项目 `.venv`；Python 3.12.8，NumPy 1.26.4，SciPy 1.13.1，pydicom 2.4.4，Matplotlib 3.9.2。
- MATLAB：`apps/binapps/matlab/R2025b`，运行时报告 `25.2.0.3177638 (R2025b) Update 5`。
- 未重建环境、未下载权重、未训练模型。
- Python 命令均设置 `PYTHONDONTWRITEBYTECODE=1`，避免写入只读作者目录；线程限制为 4。
- MATLAB 在工具沙箱内最小 witness 曾无输出退出；在当前已授权分配的非沙箱运行后正常。失败空日志与后续真实日志均保留。
- 首次 Matplotlib 运行受已加载 MATLAB `libstdc++` 污染而失败；只对 Python 命令卸载 MATLAB 模块后通过，环境未改变。
- 任务结束前查询 `sacct/scontrol` 时控制器/数据库暂不可达；Job ID、节点和运行态由 Slurm 环境与 `run-state/status` 记录。
