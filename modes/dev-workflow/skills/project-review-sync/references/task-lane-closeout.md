# Task Lane Closeout

Review settled in-flight task lanes. Produce distilled archive summaries. Route cleanup and deletion through the local approval path.

## Steps

1. Read only the named in-flight artifact set or task lane scope.
2. Group artifacts by `Task ID` when present. Group only when filenames and artifact links make the lane unambiguous if Task IDs are missing.
3. Select lanes with `Task Status: settled` for closeout. Leave unsettled lanes in place.
4. For each settled lane, compare the handoff, packet, implementation report, review notes, and touched files or diff when available.
5. Produce one distilled archive summary per reviewed lane (see shape below).
6. Recommend whether consumed in-flight artifacts should be deleted, moved to a raw archive, or retained as evidence.
7. Do not delete or move in-flight artifacts unless the user has explicitly approved.
8. Route durable documentation changes through documentation sync first when needed. Clear approved rows may go directly to `dw-note-manager`; uncertain rows should route through `dw-clarify-intent -> dw-note-manager`.
9. If documentation sync has not been completed, explicitly deferred, or judged unnecessary, report that closeout is gated and stop before cleanup recommendations.

If a lane lacks `Task Status: settled`, report it as still active, blocked, or unclear. Do not close it unless the user explicitly asks.

## Archive Summary Shape

Write archive summaries under `docs/Archieved/Tasks/`.

```
# <Task Title>

- Type: task-archive-summary
- Status: closed
- Task ID: <stable-task-slug>
- Date: YYYY-MM-DD

## Original Intent
## Work Done
## Important Decisions
## Final Files
## Verification
## Reusable Pattern
## Remaining Risk Or Follow-up
```

Raw handoffs, packets, and reports should be preserved only when they contain important evidence that the distilled summary cannot adequately capture.

## Disposition

`archive-ready` | `retain-in-flight` | `follow-up-needed`

## Output

- lanes inspected and their task status
- lanes selected for closeout
- archive summary draft or written path
- consumed in-flight artifacts and recommended cleanup action
- durable documentation sync context if needed
- closeout recommendation

## Final Check

- Were only settled task lanes selected?
- Were unsettled lanes left in place or reported without being silently closed?
- Was one distilled archive summary produced or drafted per closed lane?
- Did deletion or movement of in-flight artifacts receive explicit approval?
