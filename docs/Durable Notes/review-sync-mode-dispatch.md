# Review-Sync Mode Detection and Dispatch

Status: [[Tags/status-draft]]
Type: [[design-note]]
Parent: [[review-agent]]
Related: [[review-agent]], [[review-sync-phase-gates]], [[review-sync-scope-cap]]
Created: 2026-05-15
Last Reviewed: 2026-05-15
Source: modes/dev-workflow/skills/project-review-sync/SKILL.md
Decisions:
Dependencies:
Tasks:

---

The skill routes incoming requests into one of four modes — Implementation Review, Documentation Sync Analysis, Maintenance Review, Task Lane Closeout — using a signal table keyed on keywords in the request. Mixed or absent signals do not trigger a default mode; the skill asks instead.

## Design Scope

Mode determines what inputs are required, what phase gates apply, and what outputs are produced. Selecting the wrong mode silently bypasses the gate structure of the other modes, which would let a maintenance sweep become an implementation review or a closeout become a documentation write without the human authorizing the shift.

## Chosen Design

| Signals in request | Mode |
|---|---|
| implementation, approved packet, does it match, post-merge review | Implementation Review |
| doc sync, documentation update, approved to sync | Documentation Sync Analysis |
| stale notes, bloated notes, note refactor, note split, design notes, feature subject notes, health check, maintenance, link check, artifact cleanup | Maintenance Review |
| closeout, archive, In-flight cleanup, settled lane | Task Lane Closeout |

When signals are mixed or absent, the skill asks before proceeding: "Which mode — implementation review / doc sync / maintenance / closeout?"

## Rationale

Mode detection is explicit rather than inferred because each mode loads different required inputs, triggers different phase gates, and produces different output types. Conflating modes silently would produce the wrong gate structure for the actual task and make phase-gate violations invisible.

## Open Questions
