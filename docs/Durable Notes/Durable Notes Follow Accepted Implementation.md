# Durable Notes Follow Accepted Implementation

Status: [[Tags/status-settled]]
Parent:
Related: [[Two-Phase Workflow Boundary]], [[planner-agent]], [[implementer-agent]], [[review-agent]], [[task-packet-schema]], [[modes/dev-workflow/skills/project-implementer/references/implementation-report-schema]], [[clarify-intent]], [[clarified-context-handoff]], [[note-manager]]
Created: 15-04-2026
Last Reviewed: 2026-04-25
Source:
Decisions:
Dependencies:
Tasks:

---

## Summary

Durable notes should normally be updated after implementation has been accepted, not during planning.

The intended evidence chain is:

`task packet -> implementation report -> review/sync decision -> clarify-intent -> clarified context handoff -> Note Manager update`

This rule exists to prevent speculative planning from overwriting durable architecture, design, or feature knowledge before implementation proves out.

## Details

Within the current workflow:

- `planner` produces a `task packet`, not durable note truth
- `implementer` produces an `implementation report`
- `review/sync` determines what implementation-backed context may need durable note synchronization after accepted implementation
- `review/sync` sends one bounded context handoff per documentation-sync subject to `clarify-intent`
- `clarify-intent` produces a [[clarified-context-handoff]] that separates decided, proposed, unclear, and blocked points
- the user checks the clarified context before it is sent to `Note Manager` when confirmation is required
- `Note Manager` applies durable note changes through bounded note mutation from the clarified context handoff

This keeps planning artifacts, implementation artifacts, and durable knowledge distinct from each other.

It also preserves a cleaner authority model:
- planning can shape execution without silently changing durable source-of-truth notes
- implementation reports capture what actually happened
- review/sync identifies implementation-backed context that may need to persist into the long-term note graph
- clarify-intent clarifies that context before note mutation
- Note Manager decides which notes should be created or updated from the clarified context and supplied note paths
- durable note updates happen from accepted implementation evidence rather than plausible planning intent

For now, `review/sync` may make these proposals from the implementation context it already has.
Later, the same review step may use a search tool to retrieve stronger note context before proposing handoffs.
That future retrieval support should improve proposal quality, but it does not change the current authority split.

This does not mean every implementation result should create a new durable note. In many cases the right action will be to update an existing architecture, design, feature, active-context, or decision note.

Idea-stage notes may later be merged into existing durable notes or relinked from idea context into architecture, design, or feature context. That merge behavior is part of the larger note lifecycle, but this note does not define all of those rules.

## Packet And Report Cleanup

Task packets and implementation reports are workflow artifacts, not long-term durable knowledge notes.

After review, these artifacts may be removed only when:
- the related implementation has been committed in git,
- review has consumed the packet and report,
- architectural, design, implementation-state, decision, or other durable notes have been updated or routed for update,
- and the packet or report is no longer the only useful record of the change.

If the implementation is uncommitted, the packet and report should remain available as review evidence.

If durable notes are stale or incomplete, review should route a maintenance or documentation-sync report through `clarify-intent -> Note Manager` before artifact cleanup is treated as complete.

## Open Questions

- What exactly counts as `accepted implementation` for triggering durable note updates?
- Should merge versus relink be chosen by note type, by owner, or by review decision?
- Which durable note domains should be treated as first-class sync targets: architecture, design, feature, active context, or decision log?
