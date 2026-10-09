# hammouda2020

Metadata/source access checked by OpenAI Codex on 9 October 2026; independent human verification pending.

Title: A New Framework for Performing Cardiac Strain Analysis from Cine MRI Imaging in Mice
DOI: 10.1038/s41598-020-64206-x
PMID: 32382124
PMCID: PMC7205890
Access: fulltext

Cardiac magnetic resonance (MR) imaging is one of the most rigorous form of imaging to assess cardiac function in vivo. Strain analysis allows comprehensive assessment of diastolic myocardial function, which is not indicated by measuring systolic functional parameters using with a normal cine imaging module. Due to the small heart size in mice, it is not possible to perform proper tagged imaging to assess strain. Here, we developed a novel deep learning approach for automated quantification of strain from cardiac cine MR images. Our framework starts by an accurate localization of the LV blood pool center-point using a fully convolutional neural network (FCN) architecture. Then, a region of interest (ROI) that contains the LV is extracted from all heart sections. The extracted ROIs are used for the segmentation of the LV cavity and myocardium via a novel FCN architecture. For strain analysis, we developed a Laplace-based approach to track the LV wall points by solving the Laplace equation between the LV contours of each two successive image frames over the cardiac cycle. Following tracking, the strain estimation is performed using the Lagrangian-based approach. This new automated system for strain analysis was validated by comparing the outcome of these analysis with the tagged MR images from the same mice. There were no significant differences between the strain data obtained from our algorithm using cine compared to tagged MR imaging. Furthermore, we demonstrated that our new algorithm can determine the strain differences between normal and diseased hearts.
