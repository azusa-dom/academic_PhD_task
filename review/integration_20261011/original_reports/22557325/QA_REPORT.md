# 审计与基线构建 QA

日期：2026-10-11。本报告是audit-only交付的检查结果，不是修订稿QA，更不是科学/临床有效性证明。

## 输入保全和机械状态

- 输入与工作稿均对开始时SHA-256清单逐一复核，无内容变化；清单与结果在qa/input_sha256_before.json、qa/working_sha256_before.json和qa/audit_checks.json。
- 独立审计项目为review/.git，起始revision为3f5b6d10cee3e481f8a5cb086ea897a6a4c58e16。未修改外层AGENTS.md、TASK、launcher或verifier；未操作Codex数据库。
- 先读取build_manuscript.sh和static_qa.py再运行。构建命令：`bash working/manuscript/scripts/build_manuscript.sh /mnt/iusers01/fatpou01/bmh01/f12147zh/codex-slurm/cine-review-astra-20261011/review/qa/baseline_build`。使用已有pdflatex/BibTeX/TinyTeX，未安装共享环境。stdout在qa/build_stdout.log，最终日志在对应main/supplement子目录。
- 主文36页、补充20页，全为portrait，所有页面均有可提取文本。pdffonts显示全部字体embedded；完整结果在audit_checks.json。
- 最终main.log/supplement.log无Warning/Error/Overfull/undefined匹配。第一遍编译stdout中的暂时未定义引用不可当最终失败。
- static_qa：94引用keys/94Bib条目、90 DOI字段、27labels/42references，无缺失图/标签/引用或重复DOI；该脚本只遍历其设定路径中的2个CSV，未涵盖全部证据台账。本次报告CSV另验证行列、ID和引用对应。

新构建与输入PDF页数相同，但提取文本不字节相同；已保存main_rebuild_text.diff与supplement_rebuild_text.diff。观察到表格断词/换行及数学帽号文本编码差别。未宣称两份PDF视觉或二进制完全相同。源码及插图资产哈希未变，重建仅用于工具链和当前排版审计。

## 实际视觉覆盖

| 对象 | 实际操作 | 可以说明什么 |
|---|---|---|
| 输入main36页+supplement20页 | 每页渲染PNG，全部5张contact sheet目检 | 全文版面、长表跨页、图位置和明显裁切；不是每页逐字目检 |
| 5主图+3supp图+GA | 9个独立PDF渲染图逐幅打开 | 图内数据/标签/箭头、概念与经验数据区分、整体内容 |
| 输入main p5/8/15/17/19；supp p8/12 | 页面图放大检查 | 图1/3/4与密集主表/S1/S3的实际插入可读性 |
| 新构建main p5/15/17；supp p8 | 渲染并打开图像 | 新工具链下关键图文关系与表格未出现明显裁切；字体仍偏小 |
| MRXCAT原始Figure14 | 下载出版社提供PMC图像并打开 | 不同指标箱线分布不能合并成一个worst排序；原图不提供scar属性误差 |

新构建另外渲染了main p24和supp p3/4/5/12用于保留检查材料，未把未打开的页面冒称逐页视觉检查。图源本轮没有重新渲染，既有PDF及SVG/脚本承担内容核对。

## 有效字号

| 图 | 源宽mm | 插入宽mm | 最小源字号pt | 有效最小pt |
|---|---:|---:|---:|---:|
| F1 | 190 | 160 | 6.46 | 5.44 |
| F2 | 190 | 160 | 6.19 | 5.21 |
| F3 | 190 | 160 | 7.07 | 5.95 |
| F4/F5 | 190 | 160 | 7.06 | 5.95 |
| S1 | 190 | 166 | 6.73 | 5.88 |
| S2/S3 | 190 | 166 | 7.07 | 6.17 |
| GA | 260 | 独立资产 | 7.93 | 7.93（未假设期刊缩放） |

这些是PDF实际文字span和几何缩放所得，包含下标，不把最小下标与普通标签混为一谈。主图多数普通最小标签约7.06×160/190=5.95pt；仍需要修复最终尺寸下的可读性。GA不是正文插图，不能机械套160mm。建议字号阈值属于本项目后续QA目标，未声称刚核实了JCMR要求。

## 内容检查与局限

issues.csv的27条引句在源码确实存在，行号自动定位；后续修改后这些定位需要作为baseline锚点保留。claim_evidence.csv明确区分NEW_THIS_AUDIT与INHERITED，覆盖台账逐项列当前来源而非继承VERIFIED。

图1五个计算读数独立复算为−.01347、−.08000、−.12000、−.15864、−.17833，四舍五入与图一致；牛眼弱节段实际为10而标11，已列AUD-014。图5六值均值−.18、range .16。图2导数、均值和E=e+e²/2审阅正确。没有运行新的模拟研究；这些只是现有解析图的算术核对。S2曲线与Jacobian的代码/说明已检查，未单独重跑其全部数值生成链，不能把生成器旧QA声称为本次新计算。

全文风格候选扫描在qa/style_scan.csv；词频、em-dash、nonrigid等技术词不作为MAJOR标准。未运行外部查重服务，不给原创性百分比。没有完整复核每篇论文的全部实验及补充材料；未核实细节和失败访问在证据表明示。没有运行原始算法验证，也未认证投稿、作者身份或权利许可。
