# Workflow Artifact Lifecycle and Closeout

Status: [[Tags/status-settled]]
Type: [[design-note]]
Related: [[Workflow Mode Skill Governance]], [[Two-Phase Workflow Boundary]], [[clarify-intent]], [[note-manager]], [[review-agent]], [[Dev Workflow Documentation Model]]
Created: 2026-05-11
Last Reviewed: 2026-05-12
Source: promoted from `docs/Idea Backlog/Workflow Artifact Lifecycle and Closeout.md`; created from `docs/In-flight/handoff-workflow-artifact-lifecycle-closeout.md` and updated from `docs/In-flight/handoff-settled-task-review-queue.md`
Project Subjects: workflow artifact lifecycle, in-flight task lanes, review closeout, archive summaries
Tasks:
Reports: `docs/In-flight/report-workflow-artifact-lifecycle-closeout.md`

---

## Design Scope

This note defines how `dev-workflow` treats workflow artifacts as a lifecycle rather than disconnected planning, implementation, and review files.

It covers `docs/In-flight/` as the primary active workflow-state folder, serialized task-lane artifacts, settled-lane review closeout, `docs/Archieved/Tasks/` for distilled task history, and `docs/Archieved/Notes/` for archived durable notes.

It does not define every future cleanup policy, raw evidence retention rule, or automation mechanism.

## Context

Earlier workflow state relied on separate planning, report, and active-context files. That made it easy for raw chat or stale singleton state to become the hidden source of truth.

The current design makes active workflow state file-visible:

```text
docs/In-flight/
```

`active-context.md` has been removed. Agents should reconstruct active workflow state from in-flight task-lane artifacts instead.

## Chosen Design

The lifecycle is:

```text
handoff opens work
packet plans approved work when needed
implementation report records completed work
review/sync closes settled work
archive summary preserves distilled learning
```

Important work should start with a durable handoff before it enters Note Manager, planner, or implementer work.

Handoffs are required when the task changes durable notes, workflow rules, architecture, implementation direction, project structure, or future agent behavior. Handoffs are optional for tiny mechanical edits and simple inspection.

## Task Lanes

Each important task should form a serialized task lane with one stable `Task ID`.

```text
Task ID: workflow-artifact-lifecycle-closeout

handoff-workflow-artifact-lifecycle-closeout
  -> packet-workflow-artifact-lifecycle-closeout
  -> report-workflow-artifact-lifecycle-closeout
  -> review-workflow-artifact-lifecycle-closeout
  -> archive-workflow-artifact-lifecycle-closeout
```

Each in-flight artifact should carry:

- `Task ID`
- `Task Status`

The task status belongs to the artifact lane, not to a durable note. It should use the task-lane labels from `modes/dev-workflow/docs/vocabulary.md`.

## In-Flight Usage

`docs/In-flight/` is the primary location for active workflow state.

Agents should inspect it when:

- resuming after compaction or interruption
- checking whether a task lane is open, planned, blocked, settled, or closed
- finding the active handoff, packet, report, or review artifact for a task
- deciding whether related work must continue or close before starting new work

`docs/In-flight/` is not a global hard blocker. Multiple task lanes may coexist. Related or conflicting work may need continuation or review first, but unrelated work can continue while other lanes wait.

## Review Closeout

Review/sync owns closeout for settled task lanes.

Review/sync should inspect `docs/In-flight/`, group artifacts by `Task ID` when possible, select lanes with `Task Status: settled`, leave unsettled lanes in place unless they conflict with the current request, and create or draft one distilled archive summary per closed lane.

Review/sync must not delete or move in-flight artifacts without explicit approval.

## Archive Usage

Completed task lanes should close into distilled archive summaries under:

```text
docs/Archieved/Tasks/
```

Archive summaries should preserve original intent, work done, important decisions, final files, verification, reusable pattern, and remaining risk or follow-up.

Raw handoffs, packets, and reports should be retained only when they contain important evidence that the distilled summary cannot adequately capture.

Archived durable notes belong under:

```text
docs/Archieved/Notes/
```

## Rationale

This design keeps workflow state inspectable from files instead of chat reconstruction.

It also gives review/sync a concrete operational job: close settled work, preserve reusable learning, and keep active state clean enough that future agents can continue without stale singleton state.

Distilled archive summaries are better long-term learning sources than raw artifacts because they can support build guides, decision patterns, failure modes, workflow improvements, and reusable implementation sequences.

## Constraints

- Durable note mutation still routes through `dw-note-manager`.
- In-flight artifacts are workflow artifacts, not durable knowledge notes by themselves.
- `docs/In-flight/` is the active state surface; do not recreate `active-context.md` as a parallel manual state file.
- Do not treat every non-empty in-flight folder as a blocker for unrelated work.
- Review/sync should operate on settled lanes for closeout.
- High-impact settled tasks still need normal review rigor.

## Technical Shape

The current folder model is:

| Path | Role |
| --- | --- |
| `docs/context-map.md` | Stable project structure and context-entry guide |
| `docs/In-flight/` | Active workflow state for handoffs, packets, reports, review artifacts, gates, and next actions |
| `docs/Archieved/Tasks/` | Distilled task closeout summaries and archived workflow task artifacts |
| `docs/Archieved/Notes/` | Archived durable notes retained for historical reference |

The reusable mode source should keep this model in:

- `modes/dev-workflow/manifest.yaml`
- `modes/dev-workflow/agents-bridge.md`
- `modes/dev-workflow/docs/vocabulary.md`
- relevant skill schemas and review/sync instructions
- `modes/dev-workflow/docs/context-map.md`
- `modes/dev-workflow/docs/Templates/Task Archive Summary Template.md`

After source changes, run:

```bash
python3 tools/atlas.py sync
python3 tools/atlas.py skills sync --mode dev-workflow
```

## Impacted Project Subjects

- Two-phase workflow boundary
- Note Manager gate
- Planner packet creation
- Implementer report creation
- Review/sync closeout
- Atlas mode starter folder structure
- Workflow archive and learning extraction

## Open Questions

- What exact examples define the boundary between important work and tiny mechanical work?
- Should review/sync delete consumed in-flight artifacts by default, or always ask before deletion?
- When should raw artifacts be preserved as evidence?
- Should archive summaries live directly under `docs/Archieved/Tasks/` or under a `summaries/` subfolder?
- Does `settled` mean implementation complete, human accepted, stable checkpoint reached, or some combination?
- Should review ignore unsettled tasks entirely or report them as still active during bulk review?
- When is smaller-model review acceptable, and when must review stay on the normal high-rigor path?

## Review Notes

Promoted from idea note to design note after the folder model changed: `active-context.md` was removed, `docs/In-flight/` became the primary active workflow-state folder, and `docs/Archieved/Tasks/` plus `docs/Archieved/Notes/` became the archive surface.
