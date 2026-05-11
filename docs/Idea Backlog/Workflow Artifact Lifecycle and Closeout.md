# Workflow Artifact Lifecycle and Closeout

Status: [[Tags/status-draft]]
Type: [[idea-note]]
Related: [[Workflow Mode Skill Governance]], [[Two-Phase Workflow Boundary]], [[clarify-intent]], [[note-manager]], [[review-agent]], [[Dev Workflow Documentation Model]]
Created: 2026-05-11
Last Reviewed: 2026-05-11
Priority: [[priority-high]]

---

## Idea

`dev-workflow` should treat workflow artifacts as a lifecycle, not as disconnected planning, implementation, and review files.

The core shift:

- handoff opens work
- review closes work
- `docs/Reports/in-flight/` shows whether work is still open
- `docs/Reports/archive/` stores distilled learning, not raw clutter

This would make workflow state easier to inspect, reduce hidden decision state in chat, and give review/sync a concrete closeout responsibility.

## Handoff as Intake

Important work should start with a durable handoff before it enters Note Manager, planner, or implementer work.

The general shape:

```text
idea / request
  -> handoff
  -> note-manager OR planner OR implementer
```

Examples:

```text
create/update notes
  -> clarified handoff
  -> note-manager draft/write

implement feature
  -> clarified handoff
  -> planner packet
  -> implementation

workflow/governance change
  -> clarified handoff
  -> note-manager or planner, depending on the action
```

The handoff preserves intent, uncertainty, boundaries, and decision context before execution begins. This prevents raw chat from becoming the hidden source of truth.

The intake rule should stay practical:

- Handoff required when the task changes durable notes, workflow rules, architecture, implementation direction, project structure, or future agent behavior.
- Handoff optional for tiny mechanical edits and simple inspection.

## Review as Closeout

Review/sync should not only inspect and summarize. It should own closeout for active workflow artifacts.

Review/sync should:

- inspect `docs/Reports/in-flight/`
- decide what is still active
- check whether downstream docs need synchronization
- archive or distill completed artifacts
- leave `in-flight/` clean

This gives review/sync a clear operational job: cleanup and continuity.

## In-Flight as Open Work State

`docs/Reports/in-flight/` should become the visible signal for open workflow work.

The first version of this idea treated non-empty `in-flight/` as a hard blocker:

```text
if docs/Reports/in-flight/ is non-empty:
  do not start unrelated important work
  first continue or review/close out current work
```

The refined model is softer and more useful for parallel work:

- `in-flight/` may contain more than one serialized task lane.
- Each lane needs a stable task ID shared by its handoff, packet, implementation report, review summary, and archive summary.
- `in-flight/` means "these are the currently open lanes," not "all unrelated important work must stop."
- Related or conflicting work may still need review or continuation first.
- Unrelated work can continue while other lanes wait for review.

This makes active workflow state inspectable from files instead of requiring agents to reconstruct it from chat history or a manually maintained status note.

## Serialization and Task Lanes

The handoff, task packet, implementation report, review summary, and archive summary should be serializable into one task lane.

Example:

```text
task_id: workflow-artifact-lifecycle-closeout

handoff-workflow-artifact-lifecycle-closeout
  -> packet-workflow-artifact-lifecycle-closeout
  -> report-workflow-artifact-lifecycle-closeout
  -> review-workflow-artifact-lifecycle-closeout
  -> archive-workflow-artifact-lifecycle-closeout
```

The goal is not necessarily a rigid naming scheme. The goal is reliable traceability when multiple tasks are open at the same time.

Each serialized lane should be able to show:

- open or intake-only work
- planned work
- in-progress implementation
- completed but not settled work
- settled work ready for review
- reviewed and archived work

## Settled Task Review Queue

Review should only run for task lanes that have reached settled status.

Routing rule:

```text
review/sync only runs on task lanes with settled status
```

Review/sync should not treat every in-flight artifact as immediately reviewable or blocking. It should scan `in-flight/`, select settled task lanes, and leave unsettled lanes alone unless they conflict with the current request.

This turns review into a soft gate and batchable queue:

- Review can summarize multiple settled tasks at once.
- Unsettled task lanes can remain in-flight without forcing immediate closeout.
- The review queue becomes a reminder and archive mechanism rather than a constant interruption.
- High-impact settled tasks may still need full review instead of lightweight summary.

The status should probably belong to the task lane or artifact chain, not only to an individual durable note. It is still unclear whether this should reuse `[[status-settled]]` or introduce an artifact-specific field such as `task_status: settled`.

## Distilled Archive

Completed handoffs, packets, and reports should not automatically remain forever as separate raw files.

A better closeout product is one distilled archive summary per completed task:

```text
docs/Reports/archive/2026-05/context-map-active-context-simplification.md
```

Suggested archive summary shape:

```md
# Context Map And Active Context Simplification

Date: 2026-05-11
Status: closed

## Original Intent

Short summary of the handoff intent.

## Work Done

- Created/updated X
- Changed Y
- Deferred Z

## Important Decisions

- Handoff is mandatory for important workflow changes.
- In-flight folder is current workflow state.
- Review owns closeout.

## Final Files

- `docs/context-map.md`
- `modes/dev-workflow/docs/context-map.md`

## Verification

- Files read back
- Diff reviewed
- Remaining risk

## Reusable Pattern

How to do similar work in another project.
```

During review closeout:

```text
handoff + packet + report -> distilled archive summary
raw in-flight files -> deleted or moved to raw archive only if needed
in-flight/ -> cleaned
```

Raw handoffs and reports should be kept only when they contain important evidence.

An expanded archive structure could exist later:

```text
docs/Reports/archive/summaries/
docs/Reports/archive/raw/
```

The simpler starting point is one distilled archive area.

## Project-End Learning

Distilled archive summaries are more useful than raw artifacts for extracting project-level learning.

At project end, they can support:

- step-by-step build guides
- decision patterns
- failure modes
- workflow improvements
- reusable implementation sequences

Raw handoffs and reports are likely too verbose and duplicated for this purpose.

For archive-only summaries, review may be able to use a smaller model when the task is only summarization, classification, or analytics preparation. That smaller-model path should not own high-impact decisions about correctness, governance, architecture, security, or future agent behavior.

## Recommended Lifecycle

1. Important request arrives.
2. Create a handoff in `docs/Reports/in-flight/`.
3. Route the handoff to Note Manager, planner, or implementer.
4. Create packet/report artifacts in `in-flight/` as needed.
5. The serialized task lane remains in-flight while work is open.
6. Work reaches settled status.
7. Review/sync selects settled task lanes for closeout, optionally in bulk.
8. Review creates one distilled archive summary per reviewed task lane.
9. Review deletes or moves consumed in-flight artifacts.
10. Unsettled lanes remain in `in-flight/`; reviewed lanes leave it.

## Current Working Model

The workflow can be organized around three operational pieces:

| Path | Role |
| --- | --- |
| `docs/context-map.md` | stable project structure |
| `docs/Reports/in-flight/` | current active workflow state |
| `docs/Reports/archive/` | distilled task history and reusable learning |

Under this model, `active-context.md` may become unnecessary or generated from `in-flight/` rather than maintained by hand.

## Open Questions

- Should `active-context.md` be removed, retained as a thin pointer, or generated from `in-flight/`?
- What exact examples define the boundary between important work and tiny mechanical work?
- Should review/sync delete consumed in-flight artifacts by default, or always ask before deletion?
- When should raw artifacts be preserved as evidence?
- Should archive summaries live directly under `docs/Reports/archive/` or under a `summaries/` subfolder?
- What exact serialization fields should connect handoffs, packets, reports, review summaries, and archive summaries?
- Should task-lane status reuse existing status tags or use a separate artifact-specific field?
- Does settled mean implementation complete, human accepted, stable checkpoint reached, or some combination?
- Should review ignore unsettled tasks entirely or report them as still active during bulk review?
- When is smaller-model review acceptable, and when must review stay on the normal high-rigor path?
- How should this model change `AGENTS.md`, `modes/dev-workflow/agents-bridge.md`, `project-review-sync`, and starter docs?

## Boundary

This note is an idea note for the workflow model.

It does not directly change workflow governance, skill behavior, managed mode assets, or cleanup rules. Those changes should happen through later approved note-management, planning, implementation, and review steps.

## Source

Created from `docs/Reports/in-flight/handoff-workflow-artifact-lifecycle-closeout.md`.

Updated from `docs/Reports/in-flight/handoff-settled-task-review-queue.md`.

This note supersedes `docs/Idea Backlog/Task and Report Artifact Lifecycle.md`.
