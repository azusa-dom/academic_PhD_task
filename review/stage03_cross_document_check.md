# 阶段03跨文档核对

检查范围：149处Tier2/3显式引用（正文与补充材料）；main.tex:65–71摘要；body.tex:418–430限制／结论；补表S2/S3；figures/integrated_sources/captions_and_alt_text.md；Figure3的47行源CSV；9个SVG可提取文字。检查文字和来源映射，不声称每张图进行了像素／美术审查。

重点同步：

- IG-BiReg摘要已取得，正文158、S3:328、Figure3源CSV最后一行的metadata-only/primary-inaccessible状态均过时。若作者据此更新图3，selected endpoint从nr改mask，统计由20 mask +1 nr变21 mask +0 nr，总数仍47；这只是选择性地图重编码，不是新增一篇研究或扩大检索。
- STRAUS正文367、表4:388、S2:238及Figure5中的3 templates×6 states均属于本阶段未核的细节，不可仅更新正文而保留图中已认证印象。18virtual、90seq/2700vol及数据类型则有官方说明。
- CMAC正文371、表4:392、S2:242应同步0.84mm的筛选／观察者一致性含义及ES/finalframe比较限制。Stanford图5“55; pairs unverified”与当前边界一致。
- CMRxRecon正文398“with disease labels”及S2:248需区别疾病群覆盖和逐例可用标签。2025 Data确有tagging序列描述，但不等于运动真值。
- CardioMorphNet body156与S3:320须一致限定registration-intensity loss；DeepMesh S3:312说明2D segmentation弱监督；TransMorph S3:295限定appearance uncertainty。
- 基础模型正文158/S3:330保留studies/subjects分母与multi-sequence/cine区别，预后任务不套给CMR-FM。Figure3的other-task类别可以保留。
- 部分figure-source s3_line为旧稿行号。stage03_figure3_proposed_updates.csv列出当前映射，不修改图源；数组含多个key时保留所有相应补表行。

原子台账linked_locations包含每篇全部显式重复用途，覆盖表audit_ids是该篇原子集合，不能理解为每个原子在每处重复。source-level verdict不抹平同一行内部的参照、数字和推断差别。

摘要的局灶测试稀少及限制段的文献分布描述仍为叙述性综合，不把47图示条目当完整分母，不宣称复现历史检索／饱和判断。无需要求本文转成系统综述。框架、数学示意图与推荐实验保持作者提出的组织方式；本轮不是新实验、推导审计或图形重绘。
