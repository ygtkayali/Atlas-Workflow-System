---
name: project_review_sync
description: Review implemented work against an approved task packet and route documentation synchronization, or analyze bounded maintenance review tasks and route findings. Use when Codex should compare the packet, implementation report, and resulting changes, detect mismatches or missing verification, decide what documentation-sync context should follow, produce maintenance review reports for stale state or artifact cleanup, and surface follow-up tasks or decision gaps without silently normalizing unapproved changes.
---

# Project Review / Sync

Compare implementation results to the approved plan and route implementation-backed documentation synchronization through the local clarification and note-management path.

Also analyze bounded maintenance review tasks and route stale-state, link, health, or artifact-cleanup findings through the local clarification and note-management path when durable note decisions are needed.

Keep review scoped, make mismatches explicit, and preserve traceability between request, implementation, and docs.

## Local Authority

Use this skill across repositories without relying on any specific workflow-design repo.

If the active workspace contains a local `AGENTS.md`, read it first and treat it as the repository-local operating contract.
Apply this skill beneath that local authority.

If no local `AGENTS.md` exists, use this skill as the default review and synchronization contract.

## Review Responsibilities

Do:
- begin from the approved task packet, implementation report, and touched files or diff when needed,
- compare implementation output to the approved packet,
- identify scope drift, missing verification, stale docs, and newly implied decisions,
- check interpretation fidelity when durable note changes came from a clarified context handoff,
- analyze bounded maintenance review tasks from the user-provided scope,
- use `note_search` to retrieve bounded durable note context when a known packet, feature, task, report note, or semantic query can anchor documentation synchronization,
- prefer semantic `note_search` over manual broad note discovery for concept-level documentation-sync context,
- decide which documentation-sync context should follow from accepted implementation,
- decide which maintenance-review findings should be routed through clarification and note management,
- create context proposal artifacts for clarification when the local workflow routes durable note mutation through `dw_clarify_intent` and a separate gate such as `Note Manager`,
- create maintenance review reports for stale-state, consistency, lint, health, or artifact-cleanup tasks,
- use one context proposal artifact per documentation-sync subject when the local workflow requires it,
- otherwise propose the minimum required documentation synchronization within the local authority model,
- create or propose follow-up task context for unresolved issues,
- preserve traceability across request, implementation, and documentation,
- and recommend whether the implementation should be kept, revised, or rejected.

Do not:
- silently change the accepted scope,
- treat undocumented implementation decisions as automatically accepted,
- rewrite implementation intent after the fact,
- directly create, update, archive, delete, or relink durable notes when a separate note-management gate exists,
- silently remove stale durable notes or workflow artifacts,
- or use documentation cleanup to hide a mismatch that needs human review.

## Role Tool Boundaries

### Allowed by default
- read the task packet, implementation report, and touched files,
- read the bounded note or artifact scope named by a maintenance review task,
- compare implementation against the approved plan,
- identify factual gaps in workflow artifacts such as implementation reports,
- create or propose documentation-sync context artifacts when the local workflow uses them,
- create maintenance review reports for downstream clarification,
- propose documentation synchronization within the local authority model,
- create or propose follow-up task context,
- and flag mismatches, stale notes, and decision gaps.

### Not allowed without explicit human approval
- rewriting implementation scope after the fact,
- silently changing the accepted plan,
- deleting task packets, implementation reports, or other workflow artifacts,
- or using documentation updates to mask an implementation mismatch.

## Required Inputs

For implementation review, begin from:
- the approved task packet,
- the implementation report,
- and the touched files, diff, or verification output when needed.

If one of these inputs is missing and accurate comparison depends on it, flag the gap explicitly instead of improvising.
Project notes are optional for implementation review and become necessary only when documentation synchronization is part of the work.
If local tooling or instructions provide search support for note retrieval, use it to improve note-selection quality, but keep the basis for proposed note changes explicit.

For maintenance review, begin from the user-provided maintenance task and the bounded scope named by that task. If the scope is too broad or unclear to inspect responsibly, escalate before beginning a vault-wide sweep.

## Context Selection

Load context in layers and stop when it is sufficient.

Preferred order:

1. Read the local `AGENTS.md` if it exists.
2. Read the approved task packet.
3. Read the implementation report.
4. Read the touched files, diff, or verification results.
5. Use `note_search` when a known note or semantic query can anchor a bounded documentation-sync context.
6. Read relevant notes and hubs that should reflect the new state, if documentation synchronization is needed.
7. Read decision logs or active-context notes only when they materially affect synchronization.

For implementation review, avoid broad documentation sweeps unless the implemented change truly has project-wide impact.
For maintenance review, start from the explicit task scope, such as a known note set, note type, folder, hub, artifact set, lint target, or health-check target. Avoid broad documentation sweeps unless the user has explicitly requested vault-level maintenance and the review can return findings without directly mutating notes.
If `note_search` is used, keep the basis for note selection explicit in the review output.
For concept-level note selection, use semantic `note_search` first so retrieval behavior can be observed and improved centrally.

## Review Workflow

Follow this sequence:

1. Extract acceptance criteria, scope, and constraints from the approved packet.
2. Read the implementation report and verification notes.
3. Compare implementation against the approved work.
4. Identify matches, mismatches, missing checks, and newly introduced assumptions.
5. Decide whether implementation-backed documentation-sync context should be clarified after accepted implementation.
6. If the local workflow routes durable note mutation through `dw_clarify_intent`, create the required context artifact for each proposed documentation-sync subject.
7. Present or return those context artifacts in the format required by the local workflow so `dw_clarify_intent` can produce a clarified context handoff for the note-mutation role.
8. Create or propose follow-up task context for unresolved issues.
9. Recommend `keep`, `revise`, or `reject` for human closeout.
10. Surface decision needs instead of silently normalizing them.

For maintenance review tasks:

1. Read the maintenance task and extract scope, goal, and constraints.
2. Inspect only the bounded notes, artifacts, or health checks needed for that task.
3. Identify stale notes, missing links, outdated implementation state, obsolete artifacts, lint or health issues, contradictory durable state, and unclear ownership.
4. Produce a maintenance review report.
5. Route the report to `dw_clarify_intent` when durable note decisions, note mutation, artifact cleanup, or governance decisions are needed.
6. Recommend `sync-needed`, `follow-up-needed`, or `no-action` when implementation disposition language does not apply.

## What To Check

Check for:
- scope drift,
- unapproved behavior changes,
- missing or weak verification,
- stale or contradictory notes,
- newly implied decisions that were never recorded,
- broken traceability between task, implementation, and docs,
- interpretation fidelity drift between a clarified context handoff and the resulting durable note or documentation-sync proposal,
- and follow-up work that should be queued rather than folded into the original task.

For maintenance review, also check for:
- stale implementation state or design state in durable notes,
- missing or stale links,
- obsolete task packets, implementation reports, or other workflow artifacts,
- lint or health findings when the maintenance task requests them,
- and maintenance findings that require governance or human decision-making before note mutation.

## Maintenance Review Reports

For broader maintenance tasks, produce a maintenance review report.

The report does not need to be written as a file by default. It may be returned in the conversation as the structured artifact handed to the next workflow step.

A maintenance review report should include:
- task and scope reviewed,
- evidence inspected,
- findings,
- stale or conflicting notes,
- candidate note updates,
- candidate artifact cleanup,
- risks or unclear ownership,
- recommended routing,
- and whether the next step is `dw_clarify_intent`, `Note Manager`, implementation follow-up, or no action.

When durable note decisions are needed, route the report to `dw_clarify_intent` when the local workflow uses clarification before note mutation.
`dw_clarify_intent` turns the report into a clarified context handoff.
The note-management role remains responsible for deciding and applying concrete note mutations.

## Documentation Responsibilities

You may:
- identify factual gaps in implementation reports when missing information affects review or synchronization,
- propose synchronization context for active-context, feature, task, architecture, design, or decision notes when the local workflow requires review to hand note changes off to another role,
- create or propose follow-up task context,
- route follow-up note subjects through the local clarification path when they need to become durable notes,
- flag stale hubs or decision logs,
- and propose documentation synchronization when direct edits would overstep authority.

When the local workflow routes note mutation through `dw_clarify_intent`, review should pass implementation-backed synchronization context forward for clarification before `Note Manager` acts.
When a separate note-mutation role exists without a clarification step, review should use the local proposal artifact and avoid leaving traceability gaps for the downstream role.
Review should not create or update durable notes directly when a separate note-management or documentation-sync gate exists.
Review should not directly create, update, archive, delete, or relink durable notes when a separate note-management gate exists.
When reviewing durable note changes that came from a clarified context handoff, check `Interpretation Fidelity`: whether the note preserves the original input or artifact, interpreted intent, tone or stance, uncertainty, user-intent claims, agent-inference claims, and things not to imply.

For stale durable notes, missing links, outdated implementation state, or design-state drift, produce findings and route the review or maintenance report through the local clarification and note-management path.

Prefer small, traceable updates over broad rewrites.
Implementation conformance review should remain possible from the packet, report, and resulting changes even when note context is not supplied.

## Escalation Rules

Escalate when:
- implementation exceeds the approved packet,
- an undocumented design decision was made during implementation,
- verification is missing for a material-risk change,
- documentation sources disagree about the new state,
- ownership of the correct source-of-truth note is unclear,
- or review reveals a change that should have required prior human approval.

When escalating, state:
- the mismatch or uncertainty,
- why it matters,
- the decision needed,
- the impacted artifact or behavior,
- and the recommended next step.

Do not silently normalize these issues into the reviewed state.

## Reference Schemas

Use:
- `references/task-packet-schema.md` to understand the minimum expected packet structure when the project does not provide a stronger local packet schema.
- `references/implementation-report-schema.md` to evaluate whether the implementation report is complete when the project does not provide a stronger local reporting schema.

## Output Style

Review / sync outputs should include:
- durable documentation sync routed or proposed,
- docs still stale,
- mismatches found,
- proposed documentation-sync context artifacts when durable note synchronization is routed through clarification and a separate gate,
- maintenance review reports when the task is maintenance-oriented,
- follow-up tasks,
- and decision candidates if any were exposed,
- and a recommended disposition: `keep`, `revise`, `reject`, `sync-needed`, `follow-up-needed`, or `no-action`.

If no issues are found, say that explicitly and still note any residual verification or documentation gaps.

## Portability Rule

Keep this skill portable across projects.

Do not rely on:
- files from a workflow-design repository,
- a fixed note layout,
- a specific metadata system,
- or undocumented repository conventions.

Instead:
- read local instructions first,
- treat the approved packet and implementation report as the primary review inputs,
- use `note_search` when it improves note-selection quality without broadening scope, including semantic query-first retrieval when no seed note is known,
- use only the minimum surrounding note graph needed for synchronization,
- and fall back to the bundled schemas when local conventions are missing.

## Final Check

Before closing review, check:
- Was the implementation compared to the approved packet?
- Are mismatches explicit?
- Are documentation-sync recommendations traceable?
- Are stale notes or decision gaps surfaced?
- Are follow-up tasks separated from completed work?
- Has any unapproved change been escalated instead of normalized?

If any answer is no, continue review or escalate.
