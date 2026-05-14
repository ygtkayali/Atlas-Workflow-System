# Maintenance Review

Analyze a bounded maintenance task. Route stale-state, link, health, or artifact-cleanup findings through the local clarification and note-management path.

## Steps

1. Read the maintenance task. Extract scope, goal, and constraints. If scope is too broad or unclear, escalate before beginning.
2. Inspect only the bounded notes, artifacts, or health checks named by that task.
3. Identify findings (see Checklist).
4. Produce a maintenance review report.
5. Route to `dw-clarify-intent` when durable note decisions, note mutation, artifact cleanup, or governance decisions are needed.

## Checklist

- stale implementation state or design state in durable notes
- missing or stale links
- obsolete task packets, implementation reports, or other workflow artifacts
- lint or health findings when the maintenance task requests them
- contradictory durable state
- unclear ownership or missing governance decisions

## Report Shape

Include in the maintenance review report:
- task and scope reviewed
- evidence inspected
- findings
- stale or conflicting notes
- candidate note updates
- candidate artifact cleanup
- risks or unclear ownership
- recommended routing: `dw-clarify-intent` / `note-manager` / implementation follow-up / no action

Report may be returned in conversation as a structured artifact. Does not need to be written as a file by default.

## Disposition

`sync-needed` | `follow-up-needed` | `no-action`

## Output

- maintenance review report
- follow-up tasks or decision candidates
- routing recommendation
- disposition

## Final Check

- Was scope bounded to the task named by the user?
- Are all findings routed through clarification before note mutation?
- Is the maintenance review report complete?
