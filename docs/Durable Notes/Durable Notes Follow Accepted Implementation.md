# Durable Notes Follow Accepted Implementation

Status: [[Tags/status-settled]]
Parent:
Related: [[Two-Phase Workflow Boundary]], [[planner-agent]], [[implementer-agent]], [[review-agent]], [[task-packet-schema]], [[modes/dev-workflow/skills/project-implementer/references/implementation-report-schema]], [[clarify-intent]], [[clarified-context-handoff]], [[note-manager]]
Created: 15-04-2026
Last Reviewed: 2026-05-14
Source:
Decisions: Documentation sync should compress accepted implementation context into compact proposal tables; clear approved rows can go directly to Note Manager, while uncertain rows still route through clarify-intent.
Dependencies:
Tasks: `docs/In-flight/report-technical-project-documentation-governance.md`, `docs/In-flight/report-review-sync-note-manager-compression-path.md`

---

## Summary

Durable notes should normally be updated after implementation has been accepted, not during planning.

The intended evidence chain is:

`task packet -> implementation report -> implementation review -> documentation sync analysis when needed -> compact sync proposal table -> Note Manager for clear approved rows / clarify-intent for uncertain rows -> durable-write approval`

This rule exists to prevent speculative planning from overwriting durable architecture, design, or feature knowledge before implementation proves out.

## Details

Within the current workflow:

- `planner` produces a `task packet`, not durable note truth
- `implementer` produces an `implementation report`
- `review/sync` performs implementation review and proposes documentation sync analysis when accepted implementation may have durable knowledge impact
- documentation sync analysis is a separate gated phase; it produces a compact proposal table with one bounded row per documentation-sync subject
- clear approved rows route directly to `Note Manager`
- uncertain rows route to `clarify-intent`, which produces a [[clarified-context-handoff]] that separates decided, proposed, unclear, and blocked points
- `Note Manager` drafts or applies durable note changes through bounded note mutation from the approved proposal row or clarified context handoff, with durable-write approval as a separate gate

This keeps planning artifacts, implementation artifacts, and durable knowledge distinct from each other.

It also preserves a cleaner authority model:
- planning can shape execution without silently changing durable source-of-truth notes
- implementation reports capture what actually happened
- review/sync identifies implementation-backed context that may need to persist into the long-term note graph and compresses it into a proposal table
- clarify-intent clarifies only rows whose subject, target, evidence, durable meaning, or constraints are unclear
- Note Manager decides and applies which notes should be created or updated from approved proposal rows or clarified context and supplied note paths
- durable note updates happen from accepted implementation evidence rather than plausible planning intent

For now, `review/sync` may make these proposals from the implementation context it already has.
Later, the same review step may use a search tool to retrieve stronger note context before proposing handoffs.
That future retrieval support should improve proposal quality, but it does not change the current authority split.

This does not mean every implementation result should create a new durable note. It also does not mean documentation sync analysis must run after every implementation review. Review/sync should propose the phase when durable knowledge may have changed, and stop unless the user approves continuing. In many cases the right action will be to update an existing architecture, design, feature, decision note, or in-flight workflow-state artifact.

Idea-stage notes may later be merged into existing durable notes or relinked from idea context into architecture, design, or feature context. That merge behavior is part of the larger note lifecycle, but this note does not define all of those rules.

## Packet And Report Cleanup

Task packets and implementation reports are workflow artifacts, not long-term durable knowledge notes.

After review, these artifacts may be removed only when:
- the related implementation has been committed in git,
- review has consumed the packet and report,
- architectural, design, implementation-state, decision, or other durable notes have been updated or routed for update,
- and the packet or report is no longer the only useful record of the change.

If the implementation is uncommitted, the packet and report should remain available as review evidence.

If durable notes are stale or incomplete, review should create a compact proposal table first. Clear approved rows can go directly to `Note Manager`; uncertain rows should route through `clarify-intent -> Note Manager` before artifact cleanup is treated as complete.

## Open Questions

- What exactly counts as `accepted implementation` for triggering durable note updates?
- Should merge versus relink be chosen by note type, by owner, or by review decision?
- Which durable note domains should be treated as first-class sync targets: architecture, design, feature, active context, or decision log?
