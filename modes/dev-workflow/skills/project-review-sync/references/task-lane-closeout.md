# Task Lane Closeout

Review settled in-flight task lanes and closeable idea-note task reminders. Produce distilled archive summaries when lane artifacts exist. Route cleanup and deletion through the local approval path.

## Steps

1. Read only the named in-flight artifact set, task lane scope, or idea note.
2. Group artifacts by `Task ID` when present. Group only when filenames and artifact links make the lane unambiguous if Task IDs are missing.
3. Select lanes with `Task Status: settled` for closeout. Leave unsettled lanes in place. If closing an idea note without lane artifacts, require evidence that implementation/review passed or that changed durable notes supersede the reminder.
4. For each settled lane, compare the handoff, packet, implementation report, review notes, and touched files or diff when available.
5. For idea-note closeout, decide whether the idea was promoted into durable note output or should be archived. Do not close an idea note by marking it `[[status-settled]]` while leaving it as `[[idea-note]]`.
6. Produce one distilled archive summary per reviewed lane when lane artifacts exist (see shape below). A standalone idea-note reminder may use a concise resolution in the note instead of a separate archive summary.
7. Recommend whether consumed in-flight artifacts should be deleted, moved to a raw archive, or retained as evidence.
8. Do not delete or move in-flight artifacts unless the user has explicitly approved.
9. Route durable documentation changes through documentation sync first when needed. Clear approved rows may go directly to `dw-note-manager`; uncertain rows should route through `dw-clarify-intent -> dw-note-manager`.
10. If documentation sync has not been completed, explicitly deferred, or judged unnecessary, report that closeout is gated and stop before cleanup recommendations.

If a lane lacks `Task Status: settled`, report it as still active, blocked, or unclear. Do not close it unless the user explicitly asks.

## Idea-Note Closeout

An `[[idea-note]]` can close only through one of these dispositions:

- `promote` — the idea became durable project knowledge. Route the approved note action through `dw-note-manager` to convert or move it into the appropriate durable note type, normally `[[feature-subject-note]]` for one bounded subject or `[[design-note]]` for cross-subject design rationale.
- `archive` — the idea was a reminder, superseded prompt, or historical task seed. Route the approved note action through `dw-note-manager` to mark it `[[status-archived]]` and apply any local archive placement or link cleanup.
- `follow-up-needed` — evidence, durable target, or promotion/archive disposition is unclear. Route through `dw-clarify-intent` before any note mutation.

Settled implementation evidence, completed review/sync output, or changed durable notes can satisfy the closeout evidence requirement even when no formal task packet exists.

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
