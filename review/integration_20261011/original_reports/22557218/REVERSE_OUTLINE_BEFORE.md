# Reverse outline of the supplied baseline

Each entry records the role of a substantive paragraph or display in the baseline; line numbers refer to `working/manuscript/body.tex` unless stated otherwise.

## Abstract and front matter

| Locator | Paragraph role | Evidence or reasoning | Overlap/gap |
|---|---|---|---|
| main:61 | Define the regional measurement problem | Cine lacks persistent material labels; four abnormality attributes | Strong opening; long sentence |
| main:63 | State review method and principal evidence synthesis | Method families and validation targets; circumferential/radial/focal comparison | “one” and “preserved” overstate search and endpoint |
| main:65 | State reconciliation and proposed programme | Separate representation, estimation and input; match claims to evidence | Proposal/result boundary needs explicit label |
| main:71 | Explain clinical problem for non-specialists | Small abnormality despite preserved global pump measure | Clear |
| main:73 | Explain different validation targets | Contour, repeatability, scar, outcome answer different questions | Clear |
| main:75 | Explain practical consequence | Judge magnitude/location/extent/timing and pre-specify definitions | “reliable” should remain claim-specific |

## 1. Why regional function is distinct

| Locator | Paragraph role | Evidence or reasoning | Overlap/gap |
|---|---|---|---|
| 3 | Move from chamber-level EF to regional dysfunction | Compensation, cancellation and timing | Good funnel |
| 5 | Separate association, analytical validity and utility | Prognostic/biological studies | “justify the measurement” too broad |
| 7 | Position against earlier reviews | Physics/practice/DL reviews; focal validation gap | Useful contribution statement |
| 9–13 | State primary question | Four attributes and intended-use tolerance | Central organising question |
| 15 | Reject information-free and contour-is-truth extremes | Image cues constrain but do not identify correspondence | Strong transition |
| 19 | Define critical narrative scope and citation expansion | Core papers; thematic stopping | Needs reproducibility caveat |
| 21 | Describe bounded structured search and verification | 18 queries; cutoff; targeted source checks | Fresh verification must be separated |
| 23 | State search/screening/reading limits | Caps, single screen, mixed depth | Overclaims ledger coverage |
| 25 | Define six comparison axes and no pooling | Heterogeneous metrics | Strong methodological contract |

## 2. From cine images to measurement

| Locator | Paragraph role | Evidence or reasoning | Overlap/gap |
|---|---|---|---|
| 31 | Define observed signal and four overlapping estimator archetypes | Cine cues; feature/registration/mechanics/learning assumptions | Clear |
| 33–38 | Figure 1 evidence map | Estimation chain and validation targets | Scientifically useful; visually dense at placement size |
| 40–47 | Define map, deformation gradient and strain; expose definition-dependent error | Equations and comparison conventions | Strong technical foundation |
| 57 | Prove contours do not identify internal correspondence | Annular analytic counterexample | Correctly bounded |
| 59–64 | Figure 2 and consequence by spatial scale | Identical masks/different stretch; validation should match finest claim | Strong |
| 70–81 | List complete estimand components | Eight choices and radial-strain caveat | Useful; could say “when material” rather than universal minimum |

## 3. Estimator families and assumptions

| Locator | Paragraph role | Evidence or reasoning | Overlap/gap |
|---|---|---|---|
| 87 | Explain why assumptions, not labels alone, organise comparison | Families overlap; Table 1 | Strong section thesis |
| 89–113 | Table 1 | Inputs, outputs, representations, priors, targets and endpoints | Good compact reference |
| 118 | Write common registration objective and mapping convention | Data term plus regulariser | Clear |
| 120 | Separate representation, estimation and input information | Analytic non-uniqueness | Core reasoning |
| 122 | Propose attribution experiment | Sweep regularisation/project known field/re-image | Proposal, not reported evidence |
| 124 | Distinguish temporal tracking strategies | Reference/sequential/groupwise; cycle closure | Useful assumption |
| 136 | Describe feature-tracking family and product dependence | Contours, meshes, vendor differences | Good mechanism-first paragraph |
| 138 | Catalogue early feature-tracking studies | Maret, Hor, Augustine, Vigneault, Puyol-Antón | Citation-dense; duplicates S3 |
| 140 | Bound contour-tracking inference and evaluation dependence | Boundary vs transmural material strain | Strong synthesis |
| 144 | Catalogue conventional registration methods | FFD, groupwise, optical flow, Laplace, assimilation | Too many sequential summaries |
| 146 | Introduce amortised learned registration | VoxelMorph, TransMorph | General-purpose detail weakly tied to CMR question |
| 148 | Compare field representations | B-spline/Fourier/etc.; band-limit attribution | Important distinction; can be shorter |
| 152 | Catalogue cardiac joint-task methods | Joint motion, apparent flow, MPN, FOAL, semi-supervised | Dense chronology |
| 154 | Catalogue multi-view/mesh/shape methods | MulViMotion, DeepMesh, CardioMorphNet, STCMT | Dense chronology |
| 156 | Catalogue temporal/foundation-model methods | Recurrent, ODE, workshop, foundation models | Peripheral detail in main text |
| 158 | Synthesize cardiac-specific validation | Masks/landmarks dominate | Essential closing paragraph |
| 162 | Compare mechanics-informed approaches | VAE prior, WarpPINN, FE, INR | Useful family distinction but catalogue-like |
| 164 | Bound mechanics inference | Assumptions may fail in heterogeneous tissue | Essential synthesis |
| 168 | Separate learning by supervision target; DeepStrain | Tagging comparator; workflow and internal validation | Useful |
| 170 | Separate StrainNet's two tests | DENSE contours/EPE versus cine Ecc | Central positive evidence |
| 172 | Add recent DENSE-supervised/rodent designs | Lei and MyoNet | Abstract-level, secondary |
| 174 | Separate downstream-label supervision from motion truth | LGE, reader and outcome targets | Essential validation logic |
| 178 | Summarise reviewed method record | Masks/landmarks dominate; focal known-motion rare | Strong but count/classification needs qualification |
| 180–185 | Figure 3 | Year/family/evidence classification | Dense and based partly on abstract metadata |

## 4. What validation establishes

| Locator | Paragraph role | Evidence or reasoning | Overlap/gap |
|---|---|---|---|
| 189 | Reorganise evidence by validation target | Controlled to clinical | Strong pivot; arrives late |
| 193 | Establish role of known-motion tests | Phantoms, MRXCAT, DENSE-SIM, sonomicrometry precedent | Good |
| 195 | Report MRXCAT focal prescription and DeepStrain metrics | Four cases; scar/remote and slice-average errors | Mixes regional truth with slice error unless carefully parsed |
| 197 | Interpret MRXCAT result | SD overlap; component-specific recovery | Statistical rationale invalid; “survived” too strong |
| 199–204 | Figure 4 | Prescription, slice-average error and attribute status | Caption conflicts with figure/source wording |
| 206 | State what controlled tests can/cannot show | No identified graded lesion sweep; simulation boundary | Search-bounded absence needed |
| 210 | Define strengths/errors of tagging and DENSE | Material-sensitive, not literal truth | Strong |
| 212 | Compare Gao/Cao/Wehner | Circumferential/radial/definition-specific results | Good synthesis |
| 214 | Compare Militaru and Brandt | Product dependence and segmental timing | Good |
| 216 | Report Jahromi 2026 | Phantom/healthy, layer/component equivalence | Omits simultaneous significant difference/effect size |
| 220–276 | Tables 2 and 3 plus transition | Measurement contracts and four-attribute inspection | Strong; dense; some metrics visually adjacent |
| 281 | Define scan–rescan claim boundary | Strain-8 and multicentre study | Clear |
| 285 | Define LGE claim boundary | Tissue association, not displacement | Clear |
| 287 | Report Kihlberg | AUC/sensitivity at threshold | Correctly bounded |
| 289 | Relate other scar/outcome studies | Biological qualification | Some repetition with section 1 |
| 293 | Bound outcome evidence | Prognostic association vs decision impact | Strong |

## 5. Reconciling apparent contradictions

| Locator | Paragraph role | Evidence or reasoning | Overlap/gap |
|---|---|---|---|
| 297 | State reconciliation thesis | Input/estimand/target differences | Strong |
| 301 | Explain coexistence of global and regional results | Averaging and boundary constraints | Strong |
| 303 | Explain inverse case and task dependence | Localisation despite scale bias | “At minimum” list too universal |
| 307 | Explain radial instability | Thin wall, boundary effects, varying definition | Strong |
| 311–319 | Separate representation, estimation and input | Three questions and tests | Core synthesis; repeats section 3 but worth consolidating |
| 323 | Separate uncertainty/QC from calibrated error | Coverage and selective workflow | Strong |

## 6. Proposed validation programme and resources

| Locator | Paragraph role | Evidence or reasoning | Overlap/gap |
|---|---|---|---|
| 327 | Present programme | Claim strength matched to evidence | Must stay explicitly proposed |
| 331 | Pre-specify contract and analysis unit | Acquisition/estimator/estimand/statistics | Strong |
| 333 | Match primary endpoint to claimed attribute | Location/extent/magnitude/timing losses | Strong |
| 337 | Stage 1 known-motion perturbations | Factor sweeps and representation projection | Proposed future work |
| 339 | Equal-mean counterexample | Global success not regional success | Repeats earlier averaging logic but adds test design |
| 343 | Stage 2 paired in-vivo acquisition | Alignment, blinding, disease and independence | Proposed future work |
| 345 | Reference sensitivity analysis | Tagging/DENSE processing uncertainty | Strong |
| 349 | Stage 3 tissue/decision link | LGE/outcome/impact studies | Strong |
| 351–356 | Figure 5 | Evidence hierarchy and staged programme | Useful synthesis |
| 360 | Explain complementary resources | No single complete resource | Strong |
| 362 | STRAUS scope | 18 virtual cases from three anatomies | Useful denominator correction |
| 364 | Stanford resource scope | 51/55 versioned counts, processing required | Useful but detailed |
| 366 | CMAC and MRXCAT scope | Sparse landmarks vs generators | Useful |
| 368 | CMRxRecon scope | Reconstruction robustness, no motion truth | Useful |
| 372–395 | Table 4 | Resource contract | Strong; supports shortening prose |
| 399 | REGAIN and CineVN | Global reconstruction-plus-analysis evidence | Endpoint-specific |
| 401 | DLR/interpolation/DENT | Reconstruction effects and missing focal endpoint | Catalogue-like but relevant |

## 7–9. Practice, limitations and conclusions

| Locator | Paragraph role | Evidence or reasoning | Overlap/gap |
|---|---|---|---|
| 405 | Condense reporting template | Contract, unit, target, failure policy | Strong |
| 407 | Translate to clinical/technical audiences | Interpret maps with images and tissue; connect technical metrics | Strong |
| 409 | Bound software/version claims | Clearance/reference ranges not analytical validation | Strong |
| 413 | Evidence-base limitations | small/single-centre, alignment, proprietary methods | Strong |
| 415 | Review limitations | targeted search, mixed depth, no pooling | Must correct ledger reproducibility |
| 417 | Bound framework status | organising approach, not regulatory standard | Essential |
| 421 | Positive conclusion | specified circumferential estimands; StrainNet; complementary evidence | Needs synthesis wording rather than hierarchy claim |
| 423 | Boundary conclusion | local/radial/definition and MRXCAT limitations | Too long; unbounded absence phrases |
| 425 | Actionable conclusion | name full contract and combine resources | Strong; clearly proposal |

## Supplement

The supplement has a coherent role: methods provenance; strain-definition, validation-target and control-point notes; a pre-specification template; regulatory/reconstruction context; study-level examples; and detailed empirical/resource/method tables. The principal gap is provenance wording in lines 39–51. Tables S1–S3 carry useful detail that permits the main-text method catalogue to be shortened. No major content block is irrelevant, but inherited counts and reading-depth claims require correction.

## Argument-level diagnosis

The baseline funnel is sound, but the main-text sequence spends roughly one third of the narrative on method chronology before reaching the validation evidence that answers the stated question. The revision should preserve family coverage while making every family paragraph answer: what information/constraint is added, what quantity is produced, and what endpoint has actually been validated? Validation evidence should remain the centre, and proposals should be visibly separated from findings.
