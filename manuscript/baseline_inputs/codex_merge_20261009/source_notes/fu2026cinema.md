# fu2026cinema

Metadata/source access checked by OpenAI Codex on 9 October 2026; independent human verification pending.

Title: Development and Validation of a Versatile Foundation Model for Cine Cardiac Magnetic Resonance Image Analysis
DOI: 10.1038/s43856-026-01636-0
PMID: 42129472
PMCID: PMC13396196
Access: fulltext

Background Cardiac magnetic resonance imaging is central to cardiovascular diagnosis and management, yet extracting key clinical measurements remains time-consuming, subjective, and of limited reproducibility. Current deep learning methods often require a separate model trained from scratch for each task, and generating sufficient labelled training data demands substantial clinical expertise. Methods We developed CineMA, a multi-view conv-transformer masked autoencoder foundation model, pre-trained on 15 million cine cardiac magnetic resonance images from 74,916 studies. The model was fine-tuned and evaluated on eight independent datasets for segmentation, landmark localisation, disease diagnosis, and prognostication, representing the largest such benchmark to date. Performance was compared against convolutional neural network baselines, including nnUNet. Results Here we show, without dataset-specific hyperparameter tuning, CineMA approaches nnUNet performance in ventricle segmentation and ejection fraction estimation while achieving higher consistency across repeated scans. CineMA surpasses convolutional baselines in cardiovascular disease detection with notably improved specificity, and matches their performance in long-axis function measurement. Beyond cardiac diseases, CineMA shows potential for predicting systemic conditions and survival outcomes, with comparable performance across demographic subgroups. Conclusions CineMA demonstrates accuracy, learning efficiency, adaptability, and fairness across diverse cardiac image analysis tasks, offering a strong alternative to task-specific model training for automated cardiac image analysis.
