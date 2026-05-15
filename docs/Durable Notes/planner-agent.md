# Planner Agent

Status: [[Tags/status-settled]]
Type: [[design-note]]
Parent:
Related: [[implementer-agent]], [[review-agent]], [[clarify-intent]], [[clarified-context-handoff]], [[note-manager]]
Created:
Last Reviewed: 2026-05-15
Source:
Runtime: modes/dev-workflow/skills/project-planner/SKILL.md
Decisions:
Dependencies:
Tasks:

---

The project-planner skill turns note-backed intent into implementation-ready planning artifacts without silently resolving important ambiguity. It exists to make uncertainty visible before implementation begins — surfacing missing decisions, contradictions, and scope risks as explicit planning output rather than letting them silently reach an implementer.

## Design Notes

- [[planner-entry-gate]] — When planning is required vs. when direct implementation is safe
- [[planner-context-loading]] — Layered context loading strategy and the note ecosystem model
- [[planner-role-boundaries]] — What the planner may and may not do
- [[planner-confidence-and-packet-quality]] — Confidence rubric, packet revision protocol, and quality bar
- [[planner-documentation-sync]] — Documentation gap detection and routing through dw-clarify-intent
