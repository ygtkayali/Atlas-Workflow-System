# Clarify Intent

Status: [[Tags/status-settled]]
Type: [[design-note]]
Parent:
Related: [[clarified-context-handoff]], [[note-manager]], [[Two-Phase Workflow Boundary]], [[Clarification Depth Model]], [[Two-Phase Clarification Architecture]], [[Subject Bundle Splitting]], [[Interpretation Basis]], [[Clarify Intent Output Modes]]
Created: 2026-04-14
Last Reviewed: 2026-05-15
Source: [[LLM Wiki Lossy Compression and Integrity Risks]]
Runtime: modes/dev-workflow/skills/dw-clarify-intent/SKILL.md
Decisions: Clarified context handoffs use `Interpretation Basis` to preserve original input, interpreted intent, tone, inference boundaries, and downstream validation targets.
Dependencies:
Tasks:

---

## Overview

`clarify-intent` is the workflow skill that strengthens a vague, overloaded, or solution-led request into something solid enough for bounded durable note work or planning to begin safely. It exists because the cost of entering a downstream skill with the wrong intent is higher than the cost of a focused clarification loop — misframed notes require cleanup, misframed plans require rework. The skill operates in two phases: an interactive clarification loop that surfaces and preserves uncertainty, and a handoff synthesis step that records the settled state for downstream use.

## Design Notes

- [[Clarification Depth Model]] — why two depth levels exist, when to escalate, and the high-impact taxonomy
- [[Two-Phase Clarification Architecture]] — why the loop and handoff synthesis are separate phases and what each owns
- [[Subject Bundle Splitting]] — how multi-domain prompts are split by semantic subject, and why the split is intake evidence not note structure
- [[Interpretation Basis]] — what the handoff preserves and why, including the depth-conditional requirement
- [[Clarify Intent Output Modes]] — the four-mode taxonomy, the iteration cap, and the private-reasoning rule
