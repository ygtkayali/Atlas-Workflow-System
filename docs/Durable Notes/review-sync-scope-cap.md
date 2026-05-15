# Review-Sync Scope Cap

Status: [[Tags/status-draft]]
Type: [[design-note]]
Parent: [[review-agent]]
Related: [[review-agent]], [[review-sync-phase-gates]], [[review-sync-mode-dispatch]]
Created: 2026-05-15
Last Reviewed: 2026-05-15
Source: modes/dev-workflow/skills/project-review-sync/SKILL.md
Decisions:
Dependencies:
Tasks:

---

Each mode in the review / sync skill loads only the minimum context needed for that mode's task. Scope expansion before escalation is not allowed.

## Design Scope

The scope cap constrains what the skill reads, inspects, and loads in each mode. It applies at the start of any mode and determines when the skill must escalate before acting.

## Chosen Design

| Mode | Allowed scope | Escalate when |
|---|---|---|
| Implementation Review | packet + report + diff; note context only when a specific note is named in findings | scope is unclear or unnamed |
| Documentation Sync Analysis | accepted implementation review disposition or explicit approval, packet, report, touched files or diff, and bounded sync subject | bounded sync subject or approval basis is missing |
| Maintenance Review | named scope from the task only | scope is too broad or unclear before beginning |
| Task Lane Closeout | named in-flight artifacts only | a broad sweep would be needed |

Broad sweeps are not allowed as a starting point in any mode.

## Rationale

Broad sweeps produce findings the skill has no authority to act on, inflate context, and blur accountability between what was asked and what was inspected. Escalating when scope is unclear keeps the boundary between inspection and action visible.

## Open Questions
