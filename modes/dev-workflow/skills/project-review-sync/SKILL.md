---
name: project-review-sync
description: Use after implementation to compare against the approved packet and route doc-sync, or when a bounded maintenance task needs stale-state findings routed through clarification.
---

# Project Review / Sync

Compare implementation results to the approved plan and route implementation-backed documentation synchronization through the local clarification and note-management path.

Also analyze bounded maintenance review tasks and route stale-state, link, health, or artifact-cleanup findings through the local clarification and note-management path when durable note decisions are needed.

Keep review scoped, make mismatches explicit, and preserve traceability between request, implementation, and docs.

## Modes

This skill handles two distinct review modes. Identify the correct mode at the start and follow only that mode's workflow.

- **Implementation Review**: compare implementation against an approved task packet and route documentation-sync context forward.
- **Maintenance Review**: analyze a bounded maintenance task and route stale-state, link, health, or artifact-cleanup findings.

## Review Scope Cap

Initial review reads packet + report + diff only. Load note context only when a specific note is named in the diff, report, or follow-up findings. Never begin with a broad documentation sweep.

For maintenance review, start from the explicit task scope named by the user. If the scope is too broad or unclear to inspect responsibly, escalate before beginning.

## Required Inputs

### Implementation Review
- approved task packet
- implementation report
- touched files, diff, or verification output when needed

If one of these inputs is missing and accurate comparison depends on it, flag the gap explicitly instead of improvising. Project notes are optional and become necessary only when documentation synchronization is part of the work.

### Maintenance Review
- user-provided maintenance task
- bounded scope named by that task (known note set, note type, folder, hub, artifact set, lint target, or health-check target)

## Implementation Review Workflow

### Steps

1. Extract acceptance criteria, scope, and constraints from the approved packet.
2. Read the implementation report and verification notes.
3. Compare implementation against the approved packet.
4. Identify matches, mismatches, missing checks, and newly introduced assumptions.
5. For each durable note change that came from a clarified context handoff, run the **Interpretation Fidelity Check** (see below).
6. Decide whether implementation-backed documentation-sync context should be routed.
7. If the local workflow routes durable note mutation through `dw-clarify-intent`, create one context proposal artifact per documentation-sync subject (schema: `references/context-proposal-artifact.md`).
8. Present or return those artifacts in the format required by the local workflow.
9. Create or propose follow-up task context for unresolved issues.
10. Recommend `keep`, `revise`, or `reject`. If `reject`, produce a follow-up task or re-clarification context — never a silent revert.

### Checklist

Check for:
- scope drift from the approved packet
- unapproved behavior changes
- missing or weak verification for material-risk changes
- broken traceability between task, implementation, and docs
- newly implied decisions that were never recorded
- interpretation fidelity drift (run the Interpretation Fidelity Check)
- follow-up work that should be queued rather than folded into the original task

### Disposition

`keep` | `revise` | `reject`

`reject` produces a follow-up task or re-clarification context. It does not produce a silent revert or a normalized state change.

## Maintenance Review Workflow

### Steps

1. Read the maintenance task and extract scope, goal, and constraints. If scope is too broad or unclear, escalate before beginning.
2. Inspect only the bounded notes, artifacts, or health checks named by that task.
3. Identify findings (see Checklist below).
4. Produce a maintenance review report.
5. Route the report to `dw-clarify-intent` when durable note decisions, note mutation, artifact cleanup, or governance decisions are needed.

### Checklist

Check for:
- stale implementation state or design state in durable notes
- missing or stale links
- obsolete task packets, implementation reports, or other workflow artifacts
- lint or health findings when the maintenance task requests them
- contradictory durable state
- unclear ownership or missing governance decisions

### Maintenance Review Reports

A maintenance review report should include:
- task and scope reviewed
- evidence inspected
- findings
- stale or conflicting notes
- candidate note updates
- candidate artifact cleanup
- risks or unclear ownership
- recommended routing: `dw-clarify-intent`, `Note Manager`, implementation follow-up, or no action

The report may be returned in conversation as a structured artifact; it does not need to be written as a file by default.

### Disposition

`sync-needed` | `follow-up-needed` | `no-action`

## Interpretation Fidelity Check

When reviewing durable note changes that came from a clarified context handoff:

1. Load the original handoff or prompt.
2. Diff it against the current note or proposed note change.
3. Flag any preserved fact that: flipped polarity (uncertainty became certainty), was generalized (specific became vague), or was silently resolved (open question became closed without a recorded decision).

All three are interpretation drift. Do not normalize them — surface each as an explicit flag.

## Documentation Responsibilities

You may:
- identify factual gaps in implementation reports when missing information affects review or synchronization,
- propose synchronization context for active-context, feature, task, architecture, design, or decision notes,
- create or propose context proposal artifacts when the local workflow routes note mutation through `dw-clarify-intent`,
- create or propose follow-up task context,
- route follow-up note subjects through the local clarification path when they need to become durable notes,
- and flag stale hubs or decision logs.

You may not:
- create, update, archive, delete, or relink durable notes directly when a separate note-management gate exists,
- use documentation updates to mask an implementation mismatch,
- or silently remove stale notes or artifacts.

Prefer small, traceable updates over broad rewrites.

## Role Tool Boundaries

### Allowed by default
- read the task packet, implementation report, and touched files,
- read the bounded note or artifact scope named by a maintenance review task,
- compare implementation against the approved plan,
- identify factual gaps in workflow artifacts such as implementation reports,
- create or propose context proposal artifacts and maintenance review reports,
- create or propose follow-up task context,
- and flag mismatches, stale notes, and decision gaps.

### Not allowed without explicit human approval
- rewriting implementation scope after the fact,
- silently changing the accepted plan,
- deleting task packets, implementation reports, or other workflow artifacts,
- or using documentation updates to mask an implementation mismatch.

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
- `references/context-proposal-artifact.md` as the schema for context proposal artifacts passed to `dw-clarify-intent`.
- `../project-planner/references/task-packet-schema.md` as the schema authority for expected packet structure.
- `../project-implementer/references/implementation-report-schema.md` as the schema authority for implementation report completeness.

Do not replace these bundled references with local packet or report schemas. Read local packets, reports, or schema notes only as project context.

## Output Style

### Implementation Review Output
- matches and mismatches against the approved packet
- missing or weak verification findings
- context proposal artifacts for each documentation-sync subject (when applicable)
- follow-up tasks
- decision candidates
- disposition: `keep`, `revise`, or `reject`

### Maintenance Review Output
- maintenance review report
- follow-up tasks or decision candidates
- routing recommendation
- disposition: `sync-needed`, `follow-up-needed`, or `no-action`

If no issues are found, say that explicitly and note any residual verification or documentation gaps.

## Final Check

### Implementation Review
- Was implementation compared to the approved packet?
- Are mismatches explicit?
- Was the Interpretation Fidelity Check run for any clarified context handoff?
- Are documentation-sync recommendations traceable?
- Are follow-up tasks separated from completed work?
- Has any unapproved change been escalated instead of normalized?
- If `reject`, is there a follow-up task or re-clarification context?

### Maintenance Review
- Was the scope bounded to the task named by the user?
- Are all findings routed through clarification before note mutation?
- Is the maintenance review report complete?

If any answer is no, continue review or escalate.
