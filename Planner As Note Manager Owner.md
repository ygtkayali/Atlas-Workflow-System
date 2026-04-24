# Planner As Note Manager Owner

Status: [[status-pending]]
Parent: [[Idea Hub]]
Related: [[Note Manager]], [[planner-agent]], [[Two-Phase Workflow Boundary]]
Created: 15-04-2026

## Summary

Possible long-term direction: allow `planner` to become an `owner` that can send bounded note actions through `Note Manager`.

This should remain an idea, not current workflow truth. The motivation is that some long-running or high-context features may need controlled note mutation before implementation is fully finished, especially when the planner is the role that sees the structure problem first.

## Details

The current preferred workflow keeps `planner` out of the active `Note Manager` owner list. That is still the source of truth.

This idea exists because some feature work may be too large or iterative for a strict model where note mutation only happens from `clarify-intent` or after accepted implementation through `review-sync`.

If introduced later, planner ownership should still stay bounded:
- planner would not mutate notes directly
- planner would send explicit note actions through `Note Manager`
- planner-owned note mutation would need narrow authority and clear traceability
- durable architecture or design truth should still not be overwritten just because planning produced a plausible direction

The strongest use case is not ordinary tasks. It is larger feature work where implementation planning exposes a note-structure problem that cannot be safely ignored until the very end.

## User Stories Where It Helps

- `Long-running feature decomposition`
  A feature spans multiple implementation packets over time. The planner sees that the existing feature note is too broad and that task context will fragment unless a bounded organizing note is created early. Planner-as-owner could ask `Note Manager` to create that organizing note without pretending the whole feature is already implemented.

- `Cross-cutting implementation planning`
  A planned change affects several existing notes across one domain. The planner identifies that the current note links make packet preparation noisy and ambiguous. A bounded planner-owned note update could improve traceability before implementation begins, while still preserving packet-bound execution.

- `Documenting approved pre-implementation structure`
  The human explicitly approves a workflow or design structuring choice before coding starts. Planner-as-owner could route that approved structural note update through `Note Manager` instead of leaving the vault in an intentionally outdated state until later.

## User Stories Where It Goes Bad

- `Speculative feature planning`
  The planner proposes one direction, implementation fails or changes course, and now early note updates have recorded structure that never survived contact with the code. This creates churn and weakens trust in durable notes.

- `Small task overhead`
  A small feature or bugfix does not need any pre-implementation note mutation. Allowing planner ownership by default would encourage unnecessary note changes and make the workflow feel heavier than the work justifies.

- `Authority creep`
  Planner-owned note mutation starts as a narrow exception, then gradually becomes a way to update durable notes before implementation has actually validated the plan. That would blur the boundary between planning artifacts and durable knowledge.

## Open Questions

- What exact threshold should justify planner as an owner: feature size, duration, cross-cutting scope, or explicit human approval?
- Should planner ownership be limited to creating or reshaping provisional notes rather than updating durable source-of-truth notes?
- If enabled later, what note actions should remain disallowed even when planner is the owner?
- How would `review-sync` decide whether a planner-originated note change should be kept, merged, revised, or superseded after implementation?
