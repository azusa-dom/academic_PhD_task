# 最终质量检查报告（2026-10-11）

产物构建通过；不据此作科学批准、作者批准或投稿认证。本轮是同上下文finalizer定向回查，不是新的独立评审。独立报告03_independent_review_zh.md原样保留，当前处理结果以issue_resolution.csv和finalizer_targeted_recheck.csv为准。

## 编译与静态检查

正文39页、补充23页，均为A4竖向。每份执行pdfLaTeX → BibTeX → pdfLaTeX → pdfLaTeX。最后日志无未定义引用/交叉引用、无要求重跑、无overfull、无float-too-large或BibTeX警告。补充S3一处Underfull hbox（badness 1721，源码299行）已查看，无裁切或重叠；保留为无害排版提醒。全部62页有可提取文字，字体全部嵌入，无文字边界超出页面。

static_qa.py检查通过：3个TeX、2个CSV、94个引用key及94条书目、90个DOI、27个标签及33个交叉引用。输入清单中253个文件SHA-256保持不变。git diff --check通过。这些检查不验证科学论断、原始数据真实性或个体身份独立性。

## 实际视觉检查范围

已将每页渲染为72dpi缩略图和150dpi细节图，制作16张四页联系表。已实际查看全部联系表：正文1–39页、补充1–23页。另放大查看150dpi页：正文5、9、17、21、22、29；补充11、12、14、15、16、17。独立240dpi查看Figure 1、2、4、5、S1、S2、S3及图形摘要；Figure 3在正文17页150dpi查看。没有发现可见裁切、标签重叠或表格越界。表格信息密集，需要放大阅读。

190mm设计在约160mm正文中缩放；实际PDF图中文字常见约7.06pt以上，少量最小约6.20–6.73pt。不保证所有字符达到7pt，也未进行实际纸张印刷校样。联系表用于全页布局审查，不等于逐页逐字的原尺寸校对。没有改变全文边距来掩盖缩放。详见visual_inspection.json及technical_qa.json；交付包含全部缩略图/联系表和已放大检查的细节图。

## 证据与修订验证

最终定向检索为3条查询、9个直接URL打开：6个可用原始来源页面、Chen页面验证挑战、DOI及现行JCMR指南2次失败；同时复读同日独立阶段保存的相关原始来源段落/表格。具体访问深度和定位见FINALIZER_RECHECK_zh.md。失败访问不是来源不存在，也没有把全文可得称为全文已读。53条新增意义记录及8处纯语言润色分别保留。历史检索不能由本次有界检索追认。

完整未决科学/作者/权利项目见REMAINING_CONCERNS.md及FINAL_STATUS.json。交付源在干净目录独立重建成功，全部62页提取文本及72dpi像素逐页一致。结果在finalizer/clean_rebuild_checks.json；指定verifier及归档检查另存verify_delivery.json。以上只检验工件。

## 归档和指定验证器

已执行未修改的 `python3 slurm/verify_delivery.py`：artifact_checks_passed=true，errors为空；scientific_acceptance_assessed_by_script=false。ZIP完整性测试通过，包含完整delivery目录；根SHA256SUMS覆盖所有交付文件（清单自身除外），根目录另附ZIP的SHA256。干净源重建与最终PDF逐页内容一致。Obsidian阅读镜像已写入CSF3指定路径并核对文件哈希；未验证Mac/iCloud同步。
