---
name: writing-assistant
description: Edit and optimize existing academic writing for clarity, coherence, concision, and journal-ready tone while preserving technical meaning. Use when users ask to polish, rewrite, condense, translate academically, or improve logic and readability of paper drafts, responses, or research summaries.
---

# Writing Assistant

## Workflow
1. Preserve meaning first:
- keep original claims, data, and conclusions unchanged unless user asks for content-level revision
- mark ambiguous statements before rewriting

2. Run a three-pass edit:
- Pass 1: sentence clarity and grammar
- Pass 2: paragraph flow and logical transitions
- Pass 3: academic tone and consistency of terminology

3. Optimize for reviewer readability:
- reduce redundancy
- prefer precise verbs over vague phrasing
- keep one idea per sentence when possible

4. Return both improved text and an edit log for transparency:
- revised version
- key edit bullets (what changed and why)

## Output Modes
- `polish`: improve language with minimal structural changes
- `rewrite`: significantly improve flow and structure while preserving claims
- `compress`: shorten to requested word limit

## Guardrails
- Do not fabricate new evidence, references, or experiment details.
- Keep citation markers and equation references intact.
- If meaning changed during rewrite, explicitly flag that sentence.

## References
- Use [references/edit-checklist.md](references/edit-checklist.md) as the final QA checklist.
