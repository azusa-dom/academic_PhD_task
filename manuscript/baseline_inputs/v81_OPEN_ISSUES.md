# OPEN_ISSUES — items the author must decide or verify

Nothing in this list was guessed, filled in or worked around. Each item is either a rights question,
a journal requirement that could not be read, or a source that could not be verified.

**Round-2 update, 9 October 2026.** Round 2 closed B5 (the graphical abstract now exists) and added
C9 below. **Nothing else on this list moved.** In particular the three image-rights items A1–A3 are
still unresolved, the review proposal A5 has still not been sent, and the seven unreadable guideline
items in section B were **not** re-checked, because the ScienceDirect page still returns HTTP 403 to
this compute node. No item was upgraded without new evidence.

## A. Blocking before submission

| # | Item | State | What the author must do |
|---|---|---|---|
| A1 | **Figure 2 image credits.** The artwork credits "cine, Kaggle DSB case 233; tagging, Shehata et al. 2009 (CC BY 2.0); DENSE, Wehner et al. 2015 (CC BY 4.0)." Only Shehata 2009 was confirmed to exist with a CC BY licence field in Europe PMC. "Wehner 2015" matches **two** J Cardiovasc Magn Reson 2015 papers (doi 10.1186/s12968-015-0196-z and 10.1186/s12968-015-0119-z), both CC BY; which one, and which panel, is unknown. | UNRESOLVED | Identify the exact article and panel, confirm the licence version, and correct the credit line in the drawio. Do not publish the figure until this is settled. |
| A2 | **Kaggle Data Science Bowl case 233.** Competition data are released under competition rules, not an open content licence. Republication rights were not checked in this run. | UNRESOLVED | Check the competition terms, or replace the cine panel with an image you own. |
| A3 | **Figure 1 panels a and c contain real cine images** that the Figure 2 credit line does not cover. | UNRESOLVED | Establish and state their provenance and rights. |
| A4 | **AI-use declaration.** The declaration in the manuscript uses JCMR's required template verbatim and names the tools actually used. | DRAFTED, NEEDS AUTHOR SIGN-OFF | Read it, confirm it is accurate and complete, and accept responsibility for the content. |
| A5 | **Review proposal to the editorial office.** The guide says review proposals should first be emailed to jcmroffice@scmr.org with a rationale and outline. No contact was made by this pipeline, and none should be inferred. | NOT DONE | Send the proposal yourself before submitting. |

## B. Journal requirements that could not be verified (see `qa/jcmr_guidelines_notes.md`)

| # | Item | Why |
|---|---|---|
| B1 | The official **JCMR recommended abbreviations** .docx | Could not be downloaded from this compute node. The abbreviation list follows recent JCMR usage, not the official list. Download it and reconcile. |
| B2 | Whether a **Review abstract must be structured**, and its word limit | The 350-word structured rule is stated for Original Research. v8 complies with the stricter reading (structured, 348 words). |
| B3 | **Suggested reviewers** — required, optional or forbidden | The retrieved guide text says nothing. |
| B4 | **Preprint policy, cover-letter requirement, ORCID, line numbering, double spacing, separate title page, blinding** | Not retrieved. v8 uses line numbers and 1.20 spacing, with the title page in the main file. |
| B5 | **Graphical abstract** — the guide says one is mandatory (min. 531 × 1328 px; TIFF/EPS/PDF/MS Office) | **Done.** `submission_package/Graphical_abstract.{drawio,pdf,png}`, 2602 × 1002 px (w × h), vector PDF for submission. The requirement itself was read from the guide and is not in doubt. |
| B6 | Article-processing charge and open-access licence options | Not retrieved. |

## C. Scientific items the author may want to resolve

| # | Item |
|---|---|
| C1 | **`bell2026inr` (Implicit neural representations of intramyocardial motion and strain, STACOM 2026).** No abstract exists in Crossref or Semantic Scholar and no full text was retrievable, so its row in Table 4 is `not reported` throughout. If you can obtain the paper, the row can be completed. |
| C2 | **Point-tracking models transferred from echocardiography** (EchoTracker, MyoTracker and similar) could not be found in Europe PMC, Crossref or arXiv under those names in this run, so they are not cited. If they can be verified they would strengthen Table 9. |
| C3 | **CMRxRecon2024 participant numbers and splits** are deliberately absent from Table 6 because the abstract text could not be retrieved. |
| C4 | **The MRXCAT2.0 "worst in infarct" reading.** The paper says the infarcted case performed worst, but the radial error it reports for that case (−0.20 ± 0.21) is smaller in magnitude than the across-case average (−0.24 ± 0.21). §5.1 reports both and declines to quote it as an ordering. Reading Figure 14 of that paper directly would settle it. |
| C5 | **Which DeepStrain release and weights** the MRXCAT2.0 evaluation used is not stated in the record read, so the result cannot be tied to a version. |
| C6 | **Title choice.** The two candidates in TASK were considered; the one used is "Recovering regional myocardial dysfunction from routine cine CMR: methods, validation evidence and open questions", because it names the clinical target, the modality constraint and the three-part funnel without phrasing the title as a question. The alternative remains available. |
| C7 | **Whether a second person should repeat the screening.** This review had no independent duplicate screening and says so. |
| C8 | **Figure 3 and Table 5 cover the same classification.** Round 2 restated what the figure adds that the table does not (the two-column *supports / does not establish alone* contrast that §4.2--§4.8 then walk down), and the implanted-physical-marker row added to Table 5 has deliberately not been added to the figure, so the two displays are no longer interchangeable. If the editor asks for fewer display items, **Figure 3 is the first to drop**: its content survives in Table 5, which also carries the metric column the figure lacks. |

## D. Length

The JCMR guide states no word limit for Reviews, so no compression was applied. Round 2 added
evidence rather than text for its own sake, and the manuscript grew from 50 to 55 pages; see
`qa/round2_response.md` for what was added and why, and `qa/word_count.md` for the current count. If an editor asks for a shorter manuscript, the order that costs least evidence is:
(1) merge Tables 3 and 4 into one landscape table; (2) move Table 6 (datasets) to the supplement;
(3) compress §4.6 and Table 7 into one paragraph; (4) move the §2.4 worked example to a box.
Do not cut §5 or §6: they are the review's contribution.

---

## C (continued) — added in round 2

| # | Item |
|---|---|
| C9 | **Three wordings that may carry scientific weight were flagged, not changed.** The `paper-polish` pass in round 2 found three sentence edits that would improve the prose but could shift meaning. They are listed with before/after text in `qa/round2_polish_flags.md` §2 and are **yours to decide**. Seven further candidate edits were deliberately left alone with reasons recorded. |
| C10 | **Page 6 of the artwork keeps the label "Hold the comparison contract fixed".** The pre-submission review listed it among the in-artwork figure titles that JCMR requires be removed; round 2 judged it a content label rather than a title, because its parent in the drawio source is the `contract` box and it labels a band and two descending arrows. The reasoning is in `figures_v8_1/figure_change_log.md` so you can overrule it. |
