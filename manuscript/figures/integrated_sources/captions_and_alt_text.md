# Final captions and figure descriptions

Captions below mirror the final TeX source. Citation keys resolve in references.bib. Scientific values and provenance are stated in the captions and manuscript declarations.

## integrated/Figure_1_two_track_evidence_map.pdf

```tex
From image cues to a regional measurement. (a) Conceptual chain: correspondence is inferred and strain depends on the measurement definition. The registration objective shown is one example; other families optimise other targets. Segment~11 is reduced; all curve readouts are calculated illustrations. Input (I), estimation (E) and representation (R) tests probe potentially coupled errors. (b) Selected empirical endpoints, shown without pooling or ranking. MRXCAT2.0 reports slice averages~\cite{mrxcat2023}. Militaru intraclass correlation coefficients (ICCs) for longitudinal, circumferential and radial strain (LS, CS, RS) compare feature tracking (FT) with tagging; the global RS range is 0.10--0.63~\cite{militaru2021}. Cao reports mid-slice peak circumferential strain (Ecc)~\cite{cao2018}; StrainNet reports end-systolic cine--DENSE Ecc agreement~\cite{wang2023strainnet}. REGAIN assesses reconstruction-plus-analysis agreement~\cite{yoon2023regain}; Strain-8 assesses repeatability~\cite{bell2025strain8}. Kihlberg's receiver operating characteristic (ROC) analysis uses end-systolic segmental Ecc and late gadolinium enhancement (LGE)~\cite{kihlberg2020clinical}. Bello's corrected C index concerns right-ventricular (RV) survival prediction in chronic thromboembolic pulmonary hypertension (CTEPH)~\cite{bello2019}; the deep-learning synthetic strain (DLSS) area under the curve (AUC) evaluates reader-defined wall-motion abnormality across thresholds~\cite{masutani2023dlss}. The axis value 0.5 is a scale reference only; no result is plotted there.
```

## integrated/Figure_2_same_contours_analytic.pdf

```tex
Identical contours do not determine the same material correspondence. (a) Schematic of the information each acquisition supplies: routine cine provides boundaries and weak texture, tagging a prepared pattern, DENSE phase-encoded displacement; only tagging and DENSE carry a material label in the signal. (b) Two material mappings between the same annular contours (\(r\mapsto r\)): angular identity, \(\theta\mapsto\theta\), and \(\theta\mapsto\theta+a\sin\theta\) with \(a=0.5\). Both give identical masks (Dice~\(=1\), Hausdorff~\(=0\)). (c) Their circumferential stretch, \(\lambda_\theta=1\) and \(\lambda_\theta=1+a\cos\theta\), differs; the latter ranges from 0.5 to 1.5 and preserves orientation for \(|a|<1\), while both mappings have the same mean stretch over \(\theta\) (1.0). The figure is an analytic counterexample; no estimator error is measured, and the stretch ratio is a different quantity from Green--Lagrange strain.
```

## integrated/Figure_3_method_timeline.pdf

```tex
Selected method and evaluation records by year (Supplementary Table~S3). One marker denotes a plotted entry; entries are neither independent cohorts nor unique algorithms. Related non-cine methods and separate evaluations are included. The three early clinical feature-tracking studies and the MRXCAT2.0 evaluation of DeepStrain are plotted as separate entries, and the generic feature-tracking family row of Table~S3 is not plotted. Colours identify one selected documented endpoint per entry; studies may report several endpoints. They do not rank validation strength. Motion Pyramid Networks (MPN) include model-generated imposed-motion tests, which are distinct from independent physiological references. ``Endpoint not verified'' and ``other-task validation'' are separate categories, neither of which means that a study performed no validation. Source-specific reading depths and populations are documented in the figure data. The selective map is not a prevalence estimate for the field. Years 2001--2008, which have no selected entries, are compressed.
```

## integrated/Figure_5_attribute_specific_recovery.pdf

```tex
Prescribed tissue strain and reported DeepStrain errors in MRXCAT2.0. (a) Remote-to-scar peak systolic strain: radial strain is markedly reduced (0.95 to 0.30), circumferential strain approaches zero (\(-0.18\) to 0.01), and longitudinal strain changes little (\(-0.18\) to \(-0.17\)); infarct-case ejection fraction (EF) is 49\%. Differences are arithmetic scar-minus-remote values. (b) Source-reported means and standard deviations (SD): Ecc error \(0.02\pm0.04\), Err error \(-0.24\pm0.21\) across cases and \(-0.20\pm0.21\) in the infarct case. Source Figure~14 averages over three mid-ventricular short-axis slices. The all-case summary includes the infarct case; SD overlap does not establish equivalence, and no uniform case ranking is inferred. (c) The inspected results do not quantify scar-level magnitude, localisation, extent or peak-time error. Profile glyphs define attributes and are conceptual. Source values are retained~\cite{mrxcat2023}; the redraw adds no new experiment. The separate evaluating team and shared ACDC image domain are discussed in the text.
```

## integrated/Figure_4_validation_targets_programme.pdf

```tex
What each validation target can establish, and a staged programme for regional or focal claims. (a) Five targets, a direct claim each supports, and what each leaves open on its own. (b) A proposed programme of complementary tests, with the resources reviewed in \cref{tab:resources} placed alongside tests they can serve; counts denote resource units and are not counts of independent test participants. (c) Two fields with an equal global strain of \(-0.18\) and different regional content (segment values \(-0.22\), \(-0.22\), \(-0.06\), \(-0.18\), \(-0.20\) and \(-0.20\) against a uniform \(-0.18\)): recovering the mean is no evidence of regional recovery. Conceptual synthesis; no study data.
```

## integrated/Figure_S1_strain_definition_traps.pdf

```tex
The same motion gives different numbers under different definitions. (a) Engineering strain \(e\) and Green--Lagrange strain \(E=e+e^2/2\) differ by 0.02 at \(e=-0.20\); the table converts five values. (b) Endocardial, mid-wall and epicardial layers and local radial and circumferential axes, with the choices a report must state. (c) One segmental curve read as peak systolic (\(-0.17\)), end-systolic (\(-0.14\)) and post-systolic peak (\(-0.21\)). (d) The minimum of a segment-mean curve (\(-0.10\)) differs from the mean of pointwise minima (\(-0.20\)). Conceptual and analytic schematics with no measured scale; printed values are computed from the drawn curves.
```

## integrated/Figure_S2_error_attributes_mapping_validity.pdf

```tex
Regional error attributes and mapping validity. (a) Reference and estimate profiles separating magnitude, location, extent and support errors. (b) Temporal magnitude and timing errors. In a, and again in b, every estimate has the same root-mean-square error against its reference (0.17 and 0.16), so a single mean-squared error cannot tell these failures apart. (c) A smooth invertible mapping (minimum \(\det J=0.81\)), which can still be wrong, and a folded mapping with \(\det J\le 0\) in 5 of 121 outlined cells (minimum \(-1.13\)). Prescribed schematics with no measured scale.
```

## integrated/Figure_S3_training_vs_inference_controls.pdf

```tex
Training-time versus inference-time controls. A training-loss weight requires matched retraining; a test-time parameter can be varied only when the implementation exposes it. Candidate models or outputs are compared on the same held-out cases under the same estimand, reference and attribute-specific losses. Conceptual schematic.
```

## Graphical abstract

Routine cine supports bounded regional strain claims under matched definitions. The observed image cues pass through an estimator and prior to inferred correspondence and a defined strain quantity. Schematic profiles separate magnitude, location, extent and timing. Known-motion, paired material-sensitive and clinical endpoints address complementary questions; no field-wide prevalence is asserted.
