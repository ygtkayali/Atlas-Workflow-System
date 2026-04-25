# Two-Phase Workflow Boundary

Status: [[status-settled]]
Parent: [[Workflow Hub]]
Related: [[clarify-intent]], [[Note Manager]], [[planner-agent]], [[review-agent]]
Created: 15-04-2026
Last Reviewed: 2026-04-25
Source:
Decisions:
Dependencies:
Tasks:

---

## Summary

This note is the durable workflow-boundary note for the repository beneath `AGENTS.md`.

The workflow should keep two phases, and each phase should handle a different kind of ambiguity.

Phase 1 handles idea ambiguity and bounded durable note work.
Phase 2 handles implementation ambiguity and delivery.

This boundary exists to prevent implementation requests from being forced through ideation-style note creation when the real uncertainty is technical planning.

## Details

The intended split is:

- Phase 1: `idea -> clarify-intent -> clarified context handoff -> Note Manager`
- Phase 2: `existing notes or request -> planner -> task packet -> approval -> implementer -> implementation report -> review/sync -> clarify-intent -> clarified context handoff -> Note Manager`

In this model:

- `clarify-intent` is used when the idea or request itself is still unclear
- `clarify-intent` produces clarified context, not durable note structure
- `Note Manager` decides create vs update, note type, target note, and final note content from that clarified context plus supplied note paths
- `planner` is used when the goal is understood but implementation needs technical shaping
- `planner` consumes notes and request context, then produces a `task packet`
- `implementer` produces an `implementation report`
- `review/sync` decides whether durable notes should change after accepted implementation
- `review/sync` may also analyze bounded maintenance review tasks and produce maintenance review reports
- `review/sync` passes implementation-backed documentation-sync context to `clarify-intent`
- `clarify-intent` turns that context into a `clarified context handoff`
- `task packet`, `implementation report`, and `clarified context handoff` are workflow artifacts, not durable knowledge notes by themselves

This keeps ideation and implementation as separate but connected parts of the system.

It also preserves a clearer rule for role boundaries:
- ideation should not be overloaded with implementation planning
- implementation should not rely on planner-oriented clarification briefs as the default handoff
- durable notes remain the long-term project knowledge layer, while packet and report artifacts support delivery work
- maintenance review reports are analysis artifacts that route stale state, link, health, or artifact-cleanup findings toward clarification and note management
- planner-owned planning notes may exist, but durable note mutation should stay bounded behind the current note-management path unless a later workflow decision explicitly changes that

## Open Questions

- How should this boundary be reflected in planner role wording where it still suggests planner-owned note updates?
