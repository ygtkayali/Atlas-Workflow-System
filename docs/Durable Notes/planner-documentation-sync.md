# Planner Documentation Synchronization

Status: [[Tags/status-draft]]
Type: [[design-note]]
Parent: [[planner-agent]]
Related: [[planner-agent]]
Created: 2026-05-15
Last Reviewed: 2026-05-15
Source: modes/dev-workflow/skills/project-planner/SKILL.md
Decisions:
Dependencies:
Tasks:

---

The planner detects documentation gaps at the planning stage but routes all durable note changes through `dw-clarify-intent → Note Manager` rather than mutating notes directly.

## Why the Separation Exists

Task packets are workflow artifacts, not authoritative documentation. If the planner could write durable notes directly, planning-stage reasoning — which may include unresolved assumptions, rough scope calls, or mid-session decisions — would silently become permanent project knowledge without human review. The routing step preserves human ownership of what the durable documentation actually says.

Creating or refining a task packet artifact does not require Note Manager. Only durable note changes do.

## What Routes Through dw-clarify-intent → Note Manager

The planner routes durable note work through clarification when it needs to:

- clarify durable task scope in project notes
- create or refine a durable task note
- connect durable notes to the relevant feature hub
- record planning assumptions as durable project knowledge
- record open questions or blockers in durable notes
- resolve stale, missing, or contradictory durable notes

## Traceability Requirement

All planning-stage documentation-gap recommendations must be traceable to a human request, a task, a planning artifact, or a decision. If the correct synchronization target is unclear, the planner flags the gap and routes through clarification rather than improvising a permanent structure.

## New Repository Behavior

In a new repository, the planner prefers existing local planning artifacts over introducing new workflow files unless the user request or local instructions call for them.
