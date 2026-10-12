# 2026-10-11 定向来源核验附录

这是对既有稿件中心论断的查证，不是重新执行2026-09-03历史检索，也不构成新的系统性纳入/排除流程。没有新统计筛选人数；没有改变1 September历史cutoff。访问时区为Europe/London，报告日期2026-10-11。

## 主代理实际web查询

按调用顺序保存查询内容，另有DOI/已知官方URL直接打开及requests下载。

1. `MRXCAT2.0 DeepStrain 0.24 0.20 strain`
2. `Jahromi 2026 cine DENSE 3.5 equivalence`
3. `STRAUS synthetic cardiac motion 18 3 2018`
4. `Stanford cardiac performance MRI xt223hz2438`
5. `"StrainNet" "670" "190"`
6. `"MRXCAT2.0" "Student" "test"`
7. `"Cardiac Performance" "51" DENSE Stanford`
8. `"Multivendor Comparison" "Militaru" PMC 0.92 0.94`
9. `"Clinical validation" "Kihlberg" "0.87" 0.83 2020`
10. `"Strain-8" PMC repeatability`
11. `"Accelerated Cardiac MRI Cine" "222878" PMC`
12. `"In-silico heart model phantom to validate cardiac strain imaging" full text`
13. `"Image Feature Determinants of Global and Segmental" strain cine 2014`
14. `"Deep-learning cardiac motion analysis for human survival prediction" PMC`
15. `"A Framework for the Generation" "741" Zhou pdf`
16. `"A Framework for the Generation of Realistic Synthetic" pdf Zhou 2018`

上述查询是发现/核验入口；判断仅依据已识别的原论文、作者站或官方数据页，不把搜索片段当详细实验结果。未返回可用全文的候选不自动判为不存在。每个实际使用来源及读取深度见claim_evidence.csv的CE-001至CE-028。

## 直接访问、存证和读源范围

主代理requests结果含URL、HTTP及文本长度，记录于source_snapshots下`fetch_log.json`、`central_fetch_log.json`、`final_fetch_log.json`。HTML/PDF文本快照用于复查，保存不意味着整篇每页已读。MRXCAT原始Figure14另存JPG并实际目检；STRAUS作者PDF15页，重点读II-C/D、III及regional Engineering strain段；论文身份通过题名/作者/DOI交叉确认。

中央来源原文相关方法/结果和局限已阅读：MRXCAT2.0、Jahromi、StrainNet、Militaru、Cao、Kihlberg、Wehner、Strain-8、REGAIN、Bello、Mukherjee。官方资料包括Stanford lab、DataCite、STRAUS、CMAC及Elsevier AI政策。未下载任何subject-level dataset或病例ZIP。

## 失败、纠错和访问限制

- 最初Bello下载误指PMC6466226，实际为不相关公共卫生论文。身份检查发现后弃用，改取正确PMC6382062；保留错误文件作为检索痕迹，不算证据。不相关网页不构成Bello不存在或研究矛盾。
- 主代理DLSS出版社请求403，独立核验经可用网页读取相关全文；在独立表中记实际来源和深度，不以主代理失败取消该证据。
- JCMR官方Guide for Authors返回403，未认证当前Review摘要/字数/图数/投稿程序。Elsevier官方一般AI政策可读，访问日如上，不能替代JCMR全部要求。
- CMRxRecon2025主代理直取仅得到JS占位内容，web打开失败；其身份核验另见独立记录，root不声称读完整个网站或数据release。
- MRXCAT2.0代码仓库对子代理返回反机器人页面，即使HTTP200也不算读到内容；论文原文可读不代表仓库license/文件可用已验。
- 未做付费访问、信用额度重置、原始数据下载、通信或期刊投稿。

## 独立引用核验

`citation_audit_retrieval/`保存脚本、查询和响应；`independent_citation_audit.csv`逐条列94条的查询状态、metadata、读源深度与尚未核验的详细论断。三类Crossref查询（标题、第一作者/关键词/年份、关键词）共282次，6次HTTP200、276次429；后续串行DOI请求确认87个Crossref身份，另6官方身份、1仓库未定。76条EuropePMC记录返回，但“获得摘要”不等于全部摘要逐句审阅。全部具体成功/失败与身份状态以CSV为准。

本次没有把原始历史筛选的253/21/232重新认证；它们只能保留为所给记录的断言。新发现和未决进入AUD问题，不能反写成过去已经完成的核查。

## 第二阶段修订追加核验（同日，独立于上文审计与历史搜索）

目的仅为补足授权修订需要的证据。没有重做历史筛选、扩大论文类型或重新统计纳入数。

主代理直接重新打开 MRXCAT2.0、StrainNet 的PMC页面与Jahromi DOI，前两项返回CAPTCHA，后者浏览访问失败；因此对这些来源的有关方法/结果使用本工作区此前取得的原文快照回读。取得全文文件本身不代表所有段落均重新核验。JCMR Guide for Authors 本轮仍403；Elsevier官方生成式AI政策页面可读，读取图像/插图、数据图与graphical abstract相关条款。政策不被等同为本稿已获得权利/期刊批准。官方URL见上文CE-026。当前代码衍生图没有使用生成式图像模型，适用解释和作者声明仍待确认。

fresh-context代理对12项来源作三类定向检索，具体原始URL、Methods/Results定位、实际阅读深度、失败/限制及可支持的新表述记录于 revision_independent_sources.csv 和 revision_independent_sources_zh.md；后者记录实际query，不能反写成September工作。Buoso补读了人体landmark及猪cine标注参照，Portal读取出版者索引返回的评估点定义；这两个新增细节据实际读取加入正文/S3。其余集中于DLSS、aligned strain、StrainNet、Jahromi、MRXCAT2.0、Militaru、MyoNet、Tsuneta、Cao和Kihlberg。

修订后额外一次分类核验使用精确题名 `DENSE-Guided Deep Motion Networks`，读取 [PubMed摘要](https://pubmed.ncbi.nlm.nih.gov/42626382/)。摘要报告DENSE监督及实验strain improvement；[PMC13491192](https://pmc.ncbi.nlm.nih.gov/articles/PMC13491192/)现可发现但本轮未读全文。图3 CSV据此标记摘要深度，不增加样本/误差或测试拆分等未核验细节。该单条核验也不是新的系统检索。
