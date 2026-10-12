# DeepStrain 原始论文

身份已由Frontiers原文确认：Morales et al., Front Cardiovasc Med 2021;8:730316，DOI 10.3389/fcvm.2021.730316，2021-09-03发表。

实际阅读：摘要；Methods全节（strain definitions、VCN、CarSON、CarMEN）；Experiments全节（datasets、architecture/loss selection、final model training、evaluation metrics、statistics）；Results全部含Tables1–3文本与Figs1–8图注；Discussion全节与Study Limitations。图像像素及Supplementary Sections1–3/Tables/Figures未查看，因此SELECTED_FULLTEXT。

流程：VCN定位，CarSON分割，CarMEN由ED到目标相位估计位移；GL张量、圆柱坐标分量，心肌体积平均global及AHA区域平均。训练损失包括强度、分割解剖监督与平滑。推理时分割不输入运动估计，而用于坐标、区域及容积计算。ACDC150人：CarSON训练100，50用于分割测试；CarMEN最后使用全部150，其中50采用预测分割。不能把150理解为独立测试样本。超参数由ACDC健康应变离散程度与10套MRXCAT模拟运动/应变选定。

CMAC15健康者12 landmarks，两个observer，tagging到cine坐标映射；由于时间不齐，仅收缩末评估in-plane AEPE。Results为2.89±1.52mm（摘要四舍五入2.9±1.5），是稀疏landmark参照，并非整周期密集位移真值。原文也比较MEVIS tagging派生的global收缩末应变；Ecc偏倚−1.17±2.93、Err+1.26±5.37百分点，±为差值SD，不是LoA。未显著偏离零不构成等效检验。10套模拟ED/ES合并EPE1.8±0.2mm，是另一实验，不能与CMAC混合排名。

10健康者同扫描仪重扫，global ESS ICC Ecc0.75、Err0.90，95%CI分别0.22–0.92及0.64–0.97，范围宽；区域部分圆周节段仅moderate。原稿仅说有重复性实验，基本准确。容积相关>0.98单独支持分割/功能测量，不能推导运动准确性。

局限：没有病理区域运动准确性直接评估，无患者重复性，无跨站点/vendor重复性；小训练集、未验证的healthy dispersion启发可能削弱细微病理敏感性。作者关于平滑导致径向偏低是其解释，不能把它推广为MRXCAT2.0误差已被隔离解释。原始论文确有known-motion模拟与MEVIS应变比较，图3/data表把它选为mask虽有“一篇只编码一个端点”说明，仍建议在正文紧邻补充这两项，防止对正面证据失衡。2023 FT相关研究是独立论文、独立比较问题。


## 阶段04自查

CMAC 2.89±1.52mm与10健康重扫可保留。原始论文确有10套模拟运动/应变评估及15健康MEVIS tagging比较，建议补充正面证据属于平衡呈现，不是认定原句错误。

实际回查位置：Experiments Motion/Strain validation; Results motion / tagging strain / repeatability; Study limitations。证据文件与散列见 stage04_self_check.csv；此记录不提高既有全文阅读等级。
