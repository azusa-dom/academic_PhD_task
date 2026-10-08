---
name: medical-ai-figure-workflow
description: Create, revise, or audit medical-imaging and AI paper schematics, method frameworks, and graphical abstracts using a reusable personal work package. Use when the user invokes this skill or asks for their personal research-figure workflow; supports planning, PNG previews, focused revisions, editable delivery, and resuming figure work.
---

# 医学与 AI 科研绘图工作包

Accept Chinese requests and ordinary filenames; inspect supplied materials before asking the user to repeat information. Explain in Chinese and use English in-figure labels by default, unless explicit instructions or manuscript language indicate otherwise. Read `references/workflow.md` for execution. The files in `assets/workpack/` are templates to adapt, not scientific evidence or completed artifacts.

## 调用模式

| User wording | Mode | Deliverable |
|---|---|---|
| 规划 / plan | Plan | Primary claim, visual mapping, panel and arrow plan; no rendering |
| 预览 / preview / 做图 | Preview | Inspected PNG and supporting notes/source as applicable |
| 精修 / revise | Revise | Revised derivative within the requested change boundary and inspected preview |
| 编辑版 / editable | Editable | Requested native/vector file, preview, and actual editability checks |
| 审计 / audit | Audit | Evidence-based findings only; modify only if requested |
| 继续 / resume | Resume | Reopen the selected job, verify saved state, continue the authorized stage |

`使用 $medical-ai-figure-workflow 预览：素材是……` is sufficient. Infer mode from intent; creation defaults to preview. Do not force full production onto a small revision or audit. If preview/full production is authorized, planning is an internal phase; continue to rendering without requesting redundant approval.

## Defaults and scientific contract

Extract the primary claim from supplied manuscript/caption/data. A reference image conveys style unless its scientific content is independently supported. Resolve conflicting scientific inputs explicitly. Missing journal, palette, font or figure number alone does not block a preview; use estimated manuscript style and record reversible choices. Ask only when scientific meaning or an indispensable output choice remains unresolved.

Use a compact white-background layout, restrained semantic colors, short labels and technically meaningful objects. Review delivery defaults to PNG; preserve actual source when available, and expose only requested formats. Follow user-selected native format; otherwise choose a supported appropriate format and state the choice before production. A named “Zoya” style requires samples; until then use written academic preferences and mark calibration as incomplete.

Distinguish observations, literature results, analytic constructions, conditional inferences, hypotheses and illustrations. Mark conceptual/analytic panels accurately without labeling an entire mixed figure a mockup. Never add invented results, uncertainty bands, algorithms, clinical outcomes or synthetic scans portrayed as patient data.

Each substantive scientific claim needs a source and a visual element. Each arrow needs source, target, relation type and evidence status. For imaging tasks distinguish segmentation agreement from material correspondence, displacement from deformation/strain, the estimand from its surrogate, regional validity from global aggregation, and accuracy/association from clinical utility. Apply the cine-CMR checklist in `references/workflow.md` only to relevant strain/motion tasks.

## Routing

Use the installed `scientific-figure-suite` for relevant planning, schematic, caption and audit phases: read its root, then selected workflows and necessary references. Locate it alongside this skill. Its command names are prompt aliases, not shell executables. If missing, use this package's contract and report the missing integration.

For numerical panels use an appropriate available plotting skill such as `scientific-visualization` or `nature-figure`, inspect source values and run actual code. For raster ideation read the available image-generation instructions. K-Dense `scientific-schematics` is an optional OpenRouter PNG route; installation does not establish API access or editable export. Follow existing authorization before sending private research to a newly introduced service.

For editable delivery, create actual editable text, paths, shapes, connectors and semantic groups through a supported application/backend. Raster inspiration does not prove editability. Mixed figures may retain real MRI panels as raster while labels/framework are editable; report both scopes. If a requested native application is unavailable, report the limitation and do not mislabel a derivative as that native format.

## Work package and completion

Create a unique `figure_jobs/<descriptive-name>_<timestamp>/` in the user-selected output directory or current project for creation/full-package work. Copy only templates needed for the mode from `assets/workpack/`; save derivatives without overwriting input assets or previous versions. On resume use the explicitly selected existing job. Small revisions and audits need only relevant records.

These lightweight records are not the upstream suite's schemas or personal Codex memory. When upstream artifacts are required, create their own validated formats separately. Initialize suite project memory only when requested; do not write personal memory under `/Users/hydra/.codex/memories/` through this skill.

Inspect saved outputs at full resolution and intended manuscript size. Check claim/arrow meaning, source values, labels, crop, overlap, density and source preservation in proportion to scope. Reopen native files before claiming native delivery. Record unperformed checks as unverified; unresolved scientific errors prevent a ready status.

Hand off saved results with clickable absolute paths and show the PNG when available. State what changed, what was verified and material limitations. Installation, completed scripts and unrendered files do not prove a finished figure.
