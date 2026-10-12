# Bello 2019：右室运动的生存判别

[PMC作者稿](https://pmc.ncbi.nlm.nih.gov/articles/PMC6382062/)，发表身份由Nature DOI10.1038/s42256-019-0019-2核对；2019;1:95–104。读全部Results/Methods/Discussion、表1–2及图注，未看像素与补充说明。

单中心2004–2017的302人、85死亡、中位随访371天；Methods明确Group4 PH与慢性血栓栓塞影像条件，故CTEPH表述成立。1.5T，终点为MRI后全因死亡，手术时删失。FCN分割/landmark与B-spline运动先得到RV表面202点×19相×xyz特征；4Dsurvival以Cox loss+重建loss学习低维表示。不要把生存loss说成直接监督每个材料位移。

Methods Internal Validation明确100 bootstrap，每次重做训练与超参数搜索；PSO用6折选择。分割部分70:30不是生存模型外部测试。Results predictive performance给表观.86、校正.75[.70,.79]；常规RVEDV/RVESV/RVEF模型.60→.59[.53,.65]；另有strain模型.61、影像+临床.64。当前稿正确指向.59的手工常规变量模型，不能称全部人类判断或全部临床模型。

作者明确依赖内部验证、需多中心外部验证。风险判别不是局部运动真值、治疗效应或实际管理获益；术时删失进一步限定生存解释。稿件无须改动所引数值。


## 阶段04自查

Group4 PH+慢性血栓栓塞入组条件支持CTEPH；302人、RV、bootstrap校正.75 vs特定常规变量模型.59核实。不是外部性能或诊疗获益。

实际回查位置：Study Population; Results Predictive performance; Internal validation。证据文件与散列见 stage04_self_check.csv；此记录不提高既有全文阅读等级。
