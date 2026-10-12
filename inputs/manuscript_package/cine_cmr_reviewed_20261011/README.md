# cine-CMR 综述：审阅与润色后版本（2026-10-11，分支 claude/trusting-cray-ictohs，提交 c2cb2a9）

先看 `pdf/` 里的主文（37 页）与补充材料（20 页）；图形摘要单独一份（260 × 100 mm）。本版相对上一版的变化是摘要与 §1 入口的改写（见 `review/22` 第三轮）：摘要点明材料对应问题与"验证目标须匹配主张"的主线并补入缺口句；§1 以临床场景开头，新增路线段，§1.1 压缩。核对文献按 `review/23_承重文献核对清单.md` 做：第一层 16 篇逐篇写了稿件依赖的句子、要读的章节和要对照的数字，MRXCAT2.0 与 Wehner 2018 已按全文核过；第二层读摘要确认一项即可；第三层只需知道内容。

这一版改了什么、依据是什么、验证了什么，见 `review/22_整合稿审阅与润色_改动与验证日志.md`；审阅发现与仍待作者决定的事项见 `review/21_整合稿科学审阅_问题表.md` 第 B 节。`review/15`、`review/17` 是上一版的作者任务清单与逐项清单，页码按旧 PDF，★ 项仍然有效。整合包自带的 83 条处置表和综合建议随附，便于追溯。

`manuscript/` 是可编辑源：`main.tex` 引入 `body.tex`，`supplement.tex` 独立，`references.bib` 92 条，图件在 `figures/integrated/`（PDF/SVG/PNG），图源在 `figures/integrated_sources/`（Python + 数据 CSV，渲染需 Python 3、Pillow、pypdf、Node.js 与 Playwright/Chromium）。重建 PDF：在 `manuscript/` 下运行 `bash scripts/build_manuscript.sh /新建目录`，脚本先跑 `scripts/static_qa.py`，再用 Tectonic 或 pdflatex + bibtex 编译；本版 PDF 由 pdflatex + bibtex（TeX Live）生成，无 overfull、无 undefined、字体全嵌入。

仍需作者填写或决定：通信地址、利益冲突、资助、作者贡献、致谢；AI 声明最终措辞；JCMR 对摘要字数（现 283 词）、关键词、缩写表与图形摘要的要求；书目年份口径；是否按配色规范重渲染图件；导师或同门独立通读。本版不是投稿版，也不是独立人类评审的结果。

`SHA256SUMS.txt` 覆盖包内除自身外的全部文件。
