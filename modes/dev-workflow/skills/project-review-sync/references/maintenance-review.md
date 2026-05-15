# Maintenance Review

Analyze a bounded maintenance task for existing workflow docs, durable notes, task artifacts, or note structures. Use this mode when the user names a note, folder, task lane, or workflow artifact and asks whether it is stale, bloated, mis-scoped, poorly linked, structurally wrong, or ready for cleanup.

Maintenance Review may identify candidate durable note refactors, but it does not directly mutate durable notes.

## Steps

1. Read the maintenance task. Extract scope, goal, and constraints. If scope is too broad or unclear, escalate before beginning.
2. Inspect only the bounded notes, artifacts, lanes, folders, or health checks named by that task.
3. Identify findings (see Checklist).
4. Produce a maintenance review report.
5. Route to `dw-clarify-intent` when durable meaning, subject boundaries, ownership, note type, placement, artifact cleanup, or governance decisions are unclear.
6. Route clear durable note actions to `dw-note-manager`.

## Additional Scope

Maintenance Review covers:
- stale implementation state or stale design state in durable notes
- missing, stale, or misleading links
- obsolete task packets, implementation reports, or workflow artifacts
- bloated durable notes that mix multiple durable subjects
- notes that mix runtime contract with design rationale
- procedural content that belongs in mode-owned skill sources or references
- candidate extraction into `design-note`, `feature-subject-note`, or other appropriate durable note types
- candidate compression, split, archive, or source-of-truth clarification actions

## Checklist

- stale implementation state or design state in durable notes
- missing or stale links
- obsolete task packets, implementation reports, or other workflow artifacts
- bloated or mixed-purpose durable notes that should be compressed, split, archived, or repurposed into clearer design/feature subject notes
- lint or health findings when the maintenance task requests them
- contradictory durable state
- unclear ownership or missing governance decisions

## Responsibilities

Maintenance Review should:
- inspect only the named note, artifact, lane, folder, health check target, and directly relevant linked context
- distinguish `decided`, `proposed`, `unclear`, and `blocked` maintenance findings
- identify whether the issue is content staleness, structural bloat, bad placement, missing links, source-of-truth drift, or unclear ownership
- propose one candidate durable note action per affected note
- route unclear subject boundaries, note type choices, target-note choices, placement, or ownership decisions to `dw-clarify-intent`
- route clear durable note actions to `dw-note-manager`
- preserve the rule that reusable runtime behavior belongs in `modes/<mode>/`, not duplicated as project durable notes

Maintenance Review should not:
- rewrite, split, archive, or delete durable notes directly
- decide final note type, target note, title, or placement when unclear
- treat a maintenance proposal as approval to mutate notes
- broaden from a named note into a vault-wide cleanup unless the user explicitly asks

## Report Shape

Include in the maintenance review report:
- task and scope reviewed
- evidence inspected
- findings
- stale or conflicting notes
- candidate note updates
- candidate note-action table when durable note mutation may be needed
- candidate artifact cleanup
- risks or unclear ownership
- recommended routing: `dw-clarify-intent` / `note-manager` / implementation follow-up / no action

Report may be returned in conversation as a structured artifact. Does not need to be written as a file by default.

## Disposition

`sync-needed` | `follow-up-needed` | `no-action`

## Output

- maintenance review report
- follow-up tasks or decision candidates
- proposed note-action table when a finding implies durable note mutation
- routing recommendation
- disposition

When a maintenance finding implies durable note mutation, output a proposed note-action table. Clear rows may route to `dw-note-manager`; uncertain rows must route to `dw-clarify-intent` first.

## Final Check

- Was scope bounded to the task named by the user?
- Are all findings routed through clarification before note mutation?
- Are clear durable note actions separated from uncertain subject-boundary or ownership questions?
- Is the maintenance review report complete?
