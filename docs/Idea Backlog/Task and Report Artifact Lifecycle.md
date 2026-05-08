# Task and Report Artifact Lifecycle

Status: [[Tags/status-draft]]
Type: [[idea-note]]
Parent:
Related: [[Workflow CLI Tooling System]], [[Workflow Mode Skill Governance]], [[Two-Phase Workflow Boundary]]
Created: 2026-05-07
Last Reviewed: 2026-05-07

---

## Idea

`dev-workflow` needs a clearer lifecycle for task packets and implementation reports.

The current folder proposal gives technical workflow artifacts their own folders:

- `Tasks/`
- `Reports/`

The unresolved question is whether completed task packets and reports should become archived historical artifacts, or whether they should be treated as transient working artifacts that can be removed after review once durable notes preserve the important state.

## Current Decision

For V2, Atlas should not delete task packets or reports automatically.

Task and report cleanup should remain explicit and approval-gated until real project use shows which lifecycle is better.

Atlas sync approval should apply to the whole proposed sync run for V2.
Partial approval per file, tool, task artifact, or report artifact is deferred.
This should resurface only if real sync plans become large enough that all-or-nothing approval is too coarse.

## Options

### Archive Completed Artifacts

Completed tasks and reports remain in their folders and move to `[[status-archived]]` after review or closeout.

This preserves traceability, but large projects may accumulate too many operational artifacts.

### Treat Completed Artifacts As Transient

Tasks and reports act as working artifacts during planning, implementation, and review.

After closeout, accepted decisions, outcomes, and follow-ups are preserved in durable notes, while the original task and report files may be removed or compacted through an explicit cleanup step.

This keeps large project vaults cleaner, but weakens raw historical traceability unless summaries and accepted outcomes are preserved well.

## Open Questions

- Should `dev-workflow` default to archiving all completed task packets and reports?
- Should large projects use a transient artifact policy after durable notes are synchronized?
- What minimum implementation trace should remain after a task or report is removed?
- Should Atlas only report old task and report accumulation, or eventually offer an approved cleanup command?
- Should cleanup be based on status, review closeout, age, linked durable notes, or explicit user selection?
- When would sync plans become large enough to justify partial approval instead of whole-run approval?

## Boundary

This note is about the lifecycle of workflow artifacts.

It does not change the current rule that implementation decisions, accepted outcomes, stale documentation findings, and follow-ups should be synchronized into durable notes through the approved review and note-management flow.
