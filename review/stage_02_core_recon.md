# 阶段02：核心方法、临床终点与重建来源核查

本阶段按指定顺序审计了剩余8篇Tier 1及4篇Tier 1.5，新增75条原子主张记录。主要数值和验证层级总体有来源支持；需要优先澄清Brandt的分析分母、Chen不同终点的比较对象，以及Strain-8重复性与个体最小可检测变化的区别。所有建议均供作者审定，原稿、图、原始书目未改。

这是作者授权的AI辅助内部工作稿，不是独立人类同行评审，也不是对全部92篇引用的认证。已读取阶段01全部9篇笔记及85条台账；旧模型结论仅作为待核检查点。执行依据为TASK_COMMON、AUTHORIZATION_AND_SCOPE及本地peer-review技能，具体适配和原通用验证器BLOCKED记录保留于SKILL_EXECUTION_LOG.md。没有增加系统综述要求。

## 覆盖与证据边界

累计92篇中，20篇达到相关全文章节深度，1篇仍仅摘要，71篇尚未阅读。本阶段12篇均实际取得主文，按结果解释需要阅读Methods/Results及限制；没有把所有来源标成“全文与全部补充已读”。31处显式引用逐处核对，并检查摘要、结论、无直接引用的DLSS监督描述、Figure1源数据与SVG文字、Figure3数据及补表。精确原稿行号/PDF物理页见[覆盖表](stage02_occurrence_coverage.csv)和[跨文档核对](stage02_cross_document_check.md)。

| 顺序／来源 | 本次实际证据 | 可保留的核心主张及限制 |
|---|---|---|
| [Bell / Strain-8](reading_notes/bell2025strain8.md) | PMC主文Methods、Results、Discussion、表1–4文字及图注；补充下载为HTML，未读 | 20健康者、同日8协议；已测global CoV点估计≤20%，区域尤其纵向/径向更变。并非所有方向×协议均测得；非疾病准确性或个体MDC验证。 |
| [Yoon / REGAIN](reading_notes/yoon2023regain.md) | PMC相关全文，实看Figure4 | 1616训练患者；前瞻181，屏气配对130=94患者+36健康，应变49。分开采集GRAPPA参照；三方向global LoA数值与稿件吻合。 |
| [Masutani / DLSS](reading_notes/masutani2023dlss.md) | PMC相关全文，实看Table4 | 223检查/219患者开发，53患者/846节段临床测试；4D-flow速度和分割监督与四读者WMA终点分开。AUC .90，30%阈值敏感度86%、特异度85%可保留。 |
| [Koehler / aligned strain](reading_notes/koehler2025alignedstrain.md) | PMC完整相关Methods/Results/Discussion、图注 | 57开发、82同中心时间留出；LGE用于患者级纤维化分类。研究也有节段/相位关联分析，不能把“患者级分类终点”扩大成所有实验均无区域分析。 |
| [Bello](reading_notes/bello2019.md) | PMC作者稿相关Methods/Results/Discussion、表文字 | 302 CTEPH、RV运动、内部bootstrap校正C .75 vs常规人工变量模型 .59；非外部预测效用或治疗获益试验。 |
| [Chen](reading_notes/chen2024.md) | PMC全文与既有缓存身份核对；Methods/Results/表文字 | 20模拟、100 ACDC、16临床；LLR与GLR均减少相对pairwise的漂移，但LLR不在所有漂移指标优于GLR；tagging径向ICC优势是另一比较。 |
| [Gao](reading_notes/gao2014cine.md) | 作者机构期刊PDF，Methods2.1–2.5、全部Results/Discussion/Appendix、表文字 | 3健康、41 MI；ES定义的区域峰值与DENSE比较，还包含LGE区域分类。径向高估主要见健康/非梗死区域；未量化病灶边界或局灶峰时误差。 |
| [Brandt](reading_notes/brandt2024.md) | 作者所在公司期刊PDF相关全文；实看Results p7、Figure5 p11 | 42入组，圆周tagging–FT实际30；纵向FT–US36。整体/间隔/侧壁峰时ICC .82/.74/.74，有个体差值；未测径向。 |
| [CineVN](reading_notes/vornehm2024cinevn.md) | PMC作者稿相关Methods/Results/Discussion；实看Figure5；期刊日期核对 | 18健康GRAPPA配对，应变按中室切面；BA合并two-shot/real-time。46患者无常规参照且有分割失败排除。 |
| [Tsuneta DLR](reading_notes/tsuneta2025dlr.md) | PMC全文；实看Figure4和Supplementary Table1 | 10健康男性；同R的CS/DLR共享rawdata，R1参照另采。R6/8 GCS差值SD减小，偏差及GRS低估仍在；precision非scan–rescan。 |
| [Grob](reading_notes/grob2025interp.md) | PMC相关全文和六幅图注，缓存身份核对；补表未读 | 19人/51次采集，同次数据生成有无插值输出；体积相近而global峰值应变改变。重复采集相关性未入模型，不能当51独立人。 |
| [DENT](reading_notes/morales2024dent.md) | PMC全部Methods/Results/Discussion、图/视频图注；实看Table1/Figure1；未播放视频 | 5840包含训练/验证/内外测试；B组49临床+12健康主观比较。图像回填误差、读者评价不等于strain或形变向量验证，作者明确承认后者未评估。 |

## 建议作者优先处理的对应关系

| 位置／原子记录 | 证据及问题 | 建议处理 |
|---|---|---|
| body.tex:218；main PDF p18；BRANDT-01 | “In 42 participants”紧接圆周比较，易将入组数当分析数。Results p7显示30例。 | “Among 42 enrolled participants, 30 contributed to the circumferential tagging–feature-tracking comparison.” |
| body.tex:146；main p9；CHEN-03 | 稿件把减漂移与径向相关性共同归于相同三个比较对象。LLR晚舒张绝对GCS/GRS残余1.00/1.98，GLR为0.74/1.60；不能说LLR漂移优于GLR。 | 将“groupwise相对pairwise减漂移”与“LLR在若干节段tagging径向ICC较好”分成两句，详见台账英文替换。 |
| supplement.tex:290；supplement p11；CHEN-05 | disease composition NV是旧阅读状态，现已查到16例临床构成：正常3、冠心病4、结缔组织病4、非缺血性心肌病3、其他2。 | 更新病种组成；不要把“NV”误读为来源未报告。模拟/ACDC病种与临床队列分别写。 |
| supplement.tex:216；supplement p8；BELL-05 | 作者用CoV上限讨论变化量，未建立通用个体MDC。 | “Same-day scan–rescan precision under controlled conditions; no validated individual change threshold or accuracy claim.” |
| supplement.tex:268；supplement p10；BELL-07、BRANDT-05 | 组合引用同时声称疾病队列、区域及径向agreement较弱。Bell为健康重复性；Brandt未测径向。 | 拆清每篇支撑的范围；保留Militaru等实际测径向来源，不把重复性当跨方法一致性。 |
| body.tex:405；main p27；YOON-06–08 | LoA数字正确，正文以%表达绝对差，图中已写% points。 | 三方向分别写−7至6、−2至3、−3至3 percentage points，与图保持一致。 |
| body.tex:216/266；main pp18/20；GAO-02–06 | 原稿仅“abstract depth”低估已可得证据；区域峰值按ES识别，径向偏差依组织类别而异。 | 更新为全文深度、保留六区模式及LGE分类正面结果，同时不冒称边界/局灶峰时准确性。 |
| body.tex:218；main p18；BRANDT-02/04 | 中等至良好ICC并不保证个体峰时接近；有区域差值分析，不应被“focal endpoint未建立”遮蔽。 | 去掉过时“abstract inspected”，明确global、septal、lateral范围。 |
| body.tex:405；main p27；CINEVN-02/03 | strain BA合并两协议；PCS是负数，overestimation可能被读成收缩更强。 | 写明pooling；使用“less negative peak circumferential strain”。 |
| supplement.tex:163；supplement p7；DENT-06 | “improved…reader-rated”略强：B为非劣效，C为描述性高帧率偏好。 | 分开图像RMSE改善、B组非劣效和C组偏好趋势。 |
| references.bib；CineVN | Wiley及PMC均为2024-08-26，note写27日。 | 改26日或删可选日期注释；卷年2025、key含2024保留。 |

完整英文替换、精确片段、来源章节和重复位置在[原子台账](claim_citation_audit.csv)与[建议修正](targeted_corrections.md)。以上是局部事实/推断范围修正，不要求重写叙述性综述。

## 不应误改的内容与来源内部差别

DLSS的敏感度86%、特异度85%由Abstract、Results和原Table4支持，不能因Key Points倒置便交换稿件数字；AUC .90对应WMA而非LGE透壁性。Bello .75/.59是bootstrap校正后的两个特定模型，既不是表观 .86/.60，也不是另一strain模型或临床联合模型。Koehler的时间留出不应改称多中心外部验证，亦不应声称LGE监督形变网络。

Brandt图5图注的“均值差95%CI”与Methods中LoA措辞不一致；本阶段只采用明确的ICC、均值差/SD，不擅自重构界线含义。DENT主文读者人数存在14/15的小内部不一致，稿件没有引该数，无需替作者猜值。这些局部问题不等同于否定研究主结果。

重建四篇的设计不同：REGAIN/CineVN用另次常规采集作参照；Tsuneta同一加速rawdata比较两重建，再与另次全采样比较；Grob对同一次采集改变插值输出；DENT区分降帧回填RMSE和前瞻主观高帧率评价。它们支持“重建与分析共同影响测量”的动机，不能独自证明深度学习擦除局灶异常。相关Methods/Results及明确限制已读，否定性边界并非根据摘要未出现关键词推断。

## 前阶段未解决项的有限续查

新找到Springer官方Additional file1，已读取MRXCAT2.0补充方法pp1–5：确认ED参考、GL张量及瘢痕参数定义。原下载访问缺口解除，但仍未定义Figure14误差的完整时间采样或确切DeepStrain发布版，**MRX-17保持NOT_VERIFIED**。这次补充阅读不把整篇此前的相关章节阅读夸大成无边界全文认证。

StrainNet新定位的直接Appendix S1链接返回Cookie Absent HTML，**WANG-12仍未核实**。Morales 2022在线/2023卷年比较研究的新UC3M机构记录路线返回403；没有重复请求旧Harvard失败链接，仍保留ABSTRACT深度，Tier1完整Methods/Results要求未满足。可得摘要支持的窄人数/相关主张不因此变成错误。

## 交付与续接

[progress.json](progress.json)保存原Job ID 22636451、项目/运行目录、stdout/stderr和最终消息路径。主文原始压缩包SHA256为`4d8d1b7ba55b6c06863842f41e1a880572ad680cb6aa251b2dffb7606d919ba3`；验证结果见[validation_stage02.json](validation_stage02.json)。文件/枚举/散列核验仅证明交付完整性，不证明科学结论自动正确。

项目的.git为只读保护目录、无可读取revision；沿用不可变输入散列和stage02_baseline快照，不伪造Git版本。按项目“只在本项目工作”的限制，阅读镜像暂存[delivery/obsidian-stage02](../delivery/obsidian-stage02/00-阅读导航.md)，未写外部Obsidian目录，未验证Mac或iCloud同步。当前任务停在阶段02完成并显式保留限制；后续若继续TASK_03，从buss2015开始，71篇未读列表完整保留。
