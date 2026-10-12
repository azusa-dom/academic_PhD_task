# 阶段 01：核心文献引证核查

**状态：已按指定顺序完成九篇的有边界审计并保存检查点；八篇达到相关完整章节阅读，Morales 后续比较仍仅摘要可访问。** 这是供作者修改决定使用的AI辅助工作稿，不是独立人工同行评审，也不表示全稿引证均已验证。原稿、图、原书目、输入和外部文献库均未修改。

## 基线、范围与覆盖

唯一基线为2026-10-11稿件包，归档SHA256为`4d8d1b7ba55b6c06863842f41e1a880572ad680cb6aa251b2dffb7606d919ba3`。当前92条书目、250次引用键出现、92个不同键，无未知键；主稿37页、补充20页。载荷清单81项，连同清单本身共82个提取条目，全部哈希匹配。全文和补充的论证结构、摘要、结论、表格、图注与有关图形数据已定位；本轮源文核查限以下九篇。其余83篇的阅读及书目核验仍在台账标为待后续阶段。

台账共有85个原子主张／来源配对：62项SUPPORTED、18项SUPPORTED_WITH_QUALIFICATION、3项SOURCE_INTERNAL_DISCREPANCY、2项NOT_VERIFIED。三个源内差异记录不等于三处作者数值错误；两项待核是StrainNet精确Green–Lagrange实现和MRXCAT估计误差的peak-only时间归类。Morales后续比较的四个窄主张由摘要直接支持，但该篇Tier1完整阅读未完成。70个显式引用位置和无引用标记的摘要／结论／SVG重复已建立链接。计数说明工作覆盖，不是正确率或科研质量评分。

| 顺序／来源 | 实际深度与主要定位 | 核查结论 | 明确未解决项 |
|---|---|---|---|
| 1. wang2023strainnet | 全部Methods/Results/Discussion；原Table2与Fig5像素；[笔记](reading_notes/wang2023strainnet.md) | 305、243/62、670/190、59及ICC均有原文支持；DENSE轮廓EPE与cine应变测试已正确分开 | AppendixS1及补充图表未得；精确GL实现待核；表文LoA差异保留 |
| 2. mrxcat2023 | 全Methods、Results、Discussion/limitations；原Fig12/14像素；[笔记](reading_notes/mrxcat2023.md) | 规定瘢痕与估计误差、三中室层平均、SNR30、去纹理和共同ACDC来源均已核 | 技术补充不可得；权重/版本、Fig14时间汇总未完全明确；不能推出瘢痕内误差或泄漏 |
| 3. morales2021 | 全Methods/Experiments/Results/Discussion、Tables1–3文本；[笔记](reading_notes/morales2021.md) | CMAC2.9±1.5mm、10人重扫正确；原文还含模拟运动/应变和MEVIS tagging应变比较 | 补充及原图像素未核；不将文中未见扩大为整篇未报告 |
| 4. morales2022comparison | 出版摘要、出版史；[笔记](reading_notes/morales2022comparison.md) | 47健康/533患者、GRS r.83–.85/GCS r.88–.91与摘要一致；2022 online/2023卷年不是错引 | Wiley全文未得，Harvard公版PDF403；Methods/Results全节、原表图、限制段未读 |
| 5. militaru2021 | 全Methods/Results/Discussion/limitations；原Fig5a/b/c像素；[笔记](reading_notes/militaru2021.md) | LS/CS范围正确；GRS对tagging .10–.63正确；厂商间原图.11–.81而摘要.10–.81 | 补充regional bias/ROC图未核；源内范围差异待作者决定如何呈现 |
| 6. cao2018 | 全Methods/Results/Discussion/limitations；原Tables2–5/Fig3像素；[笔记](reading_notes/cao2018.md) | 95招募/87分析；DENSE–tagging ICC.778、bias.155pp、LoA−6.166至6.476正确 | 排除人数重叠未清楚；补充视频未看；建议明确tagging-minus-DENSE方向 |
| 7. wehner2018 | 全Methods/Results/Discussion/limitations；Tables2–5及图文；[笔记](reading_notes/wehner2018.md) | strain定义换算、88人/186对、38人子集及bias/CoV正确 | 原图像素/补充1–4未看；主数字限TomTec；Ell摘要的边界评价应保留 |
| 8. kihlberg2020clinical | 全Methods/Results/Discussion/limitations；原Fig6像素；[笔记](reading_notes/kihlberg2020clinical.md) | 116人、34人84节段>50%LGE、ES节段AUC及80%特异度敏感度均正确 | 机构PDF403但完整缓存/PMC可读；节段聚类未明确；不与患者层面ROC混淆 |
| 9. jahromi2026densecine | 全§2、§3、Conclusion；AppendixA说明/图注；原PDF14–15页与代码README；[笔记](reading_notes/jahromi2026densecine.md) | 40健康、每人2中层、指定endoEcc mean−2.7pp、所选±3.5pp TOST均支持 | 预先界值、同人两slice相关处理、训练评估逐人关系未确立；未检查全部附录曲线或复算代码 |

访问等级统一谨慎记为8篇SELECTED_FULLTEXT、1篇ABSTRACT，没有任何一篇标成FULLTEXT_AND_RELEVANT_SUPPLEMENTS。未取得的附录不能被本轮主文阅读“补齐”。所有本次检索只使用公开题名/DOI/资源地址，未发送未发表稿件段落，也未下载受试者数据。

## 最值得作者处理的事项

**Militaru的产品映射已由原图确认。** Fig5c对tagging的cvi42/Segment/Tomtec ICC依次.63/.48/.10；厂商间cvi42–Segment、cvi42–Tomtec、Segment–Tomtec依次.81/.11/.19。稿件已区分FT–tagging与FT–FT，但后者仍沿摘要写.10–.81，建议用原图映射并披露摘要差异。Figure1的.10–.63本身正确。[原文](https://pmc.ncbi.nlm.nih.gov/articles/PMC8117295/)

**StrainNet的表文差异不是旧台账的未经复核结论。** 原Table2与Fig5均已实际查看。全局表格−.51±5.15对应−5.66至4.64，与正文/图−5.74至4.72不一致；现稿披露合理。节段上界有8.06与8.07的0.01pp精度差，应写“大致一致”。0.75±0.35mm仍是DENSE-magnitude轮廓输入下的位移EPE，不能作为普通cine输入的密集位移误差。现稿已保持此区分。[原文](https://pmc.ncbi.nlm.nih.gov/articles/PMC10316292/)

**MRXCAT2.0的主要限制有直接图文依据。** Fig14是三个中室短轴切面平均，不是瘢痕内部恢复评分。规定远端/瘢痕Err.95/.30、Ecc−.18/.01、Ell−.18/−.17，与总体Err误差−.24±.21、梗死整例−.20±.21必须分开。现稿正确拒绝由两均值或重叠SD作统一病例排名；共同ACDC来源也不足以认定泄漏。[原文](https://pmc.ncbi.nlm.nih.gov/articles/PMC10116689/)

其余建议集中于推断精度与证据平衡：保留Wehner摘要对Ell的borderline-acceptable评价；给DeepStrain原始模拟与tagging应变比较应有篇幅；Cao补差值方向；Morales后续比较明确本轮仍为摘要深度。Kihlberg的瘢痕判别与Jahromi的限定均值等效均不能提升为材料运动准确性、诊疗获益或个体可互换。具体当前位置、影响与英文替换见[定点修改建议](targeted_corrections.md)。

另外，补充Methods的“current94-reference set”与本基线92条不符，应同步当前数目；历史94条身份台账可继续标为历史。九篇书目身份均与所访问主记录吻合，未发现必须更改的标题/DOI/卷年页。Jahromi卷25期5文章103已由出版商存入Crossref的记录确认；Morales引用键含2022不要求改名。当前结果不涵盖其余83篇身份正确性。

## 交接与验收边界

可复核材料包括[原子台账](claim_citation_audit.csv)、[92篇阅读登记](source_reading_register.csv)、[书目身份登记](bibliography_identity_register.csv)、[检索与失败日志](../sources/retrieval_log.csv)、[稿件定位说明](manuscript_orientation.md)与九篇笔记。原图文件、公开PDF和缓存身份/哈希均保留。检查点按九篇顺序落盘；后续源访问解决旧缺口时明确更新记录，并不把前一模型阶段算独立验证。

Job ID22636451；路径、run目录、stdout/stderr及最终消息路径见[progress.json](progress.json)。本阶段退出后不要重跑初始化脚本，它会重建台账。继续点为TASK_02所列下一组，从`bell2025strain8`开始；Morales全文与本轮补充访问缺口另列为待回补。请继续追加现有92行总登记，不能把未读83篇当已核。

本项目限制禁止写外部目录，因此 curated Obsidian 阅读镜像仅暂存在项目`delivery/obsidian-stage01/`。尚未复制到外部CSF3 export目录，也未核验Mac/iCloud更新。只读Git保护目录无有效starting revision；输入哈希是本轮版本基线。generic skill validator的BLOCKED原结果保留，按AUTHORIZATION_AND_SCOPE.md作者授权适配执行；这不是本轮自动审批拒绝，也不是期刊AI政策已获许可。

文件/哈希/CSV检查证明交付可追踪，不证明科学结论全部正确。源文缺口和两条NOT_VERIFIED在最终状态保持可见。
