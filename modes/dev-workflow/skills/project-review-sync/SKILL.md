---
name: project-review-sync
description: Use after implementation to compare against the approved packet and route doc-sync, or when a bounded maintenance task needs stale-state findings routed through clarification.
---

# Project Review / Sync

Compare implementation results to the approved plan and route implementation-backed documentation synchronization through the local clarification and note-management path.

Also analyze bounded maintenance review tasks and route stale-state, link, health, or artifact-cleanup findings through the local clarification and note-management path when durable note decisions are needed.

Own closeout for settled workflow task lanes when the review task names `docs/In-flight/` or a specific in-flight lane as its scope.
Closeout means inspect the settled lane, compare it to the approved packet and report when present, create or propose one distilled archive summary, and leave unsettled lanes untouched.

Keep review scoped, make mismatches explicit, and preserve traceability between request, implementation, and docs.

Review/sync is an umbrella skill with hard phase gates. It may identify the next review, documentation-sync, Note Manager handoff, or closeout action, but each phase produces a proposal and stops unless the user explicitly approves continuing.

## Modes

This skill handles distinct review modes. Identify the correct mode at the start and follow only that mode's workflow.

- **Implementation Review**: compare implementation against an approved task packet and decide whether documentation-sync analysis should be proposed.
- **Documentation Sync Analysis**: inspect accepted implementation evidence for durable-knowledge impact and produce a compact sync proposal table that routes clear rows to `dw-note-manager` and uncertain rows to `dw-clarify-intent`.
- **Maintenance Review**: analyze a bounded maintenance task and route stale-state, link, health, or artifact-cleanup findings.
- **Task Lane Closeout**: review settled in-flight task lanes, produce distilled archive summaries, and route any cleanup or deletion decision through the local approval path.

## Phase Gates

Do not run multiple modes as one continuous process.

At each boundary, output the proposed next action, reason, expected output, planned behavior, and required approval. Stop there unless the user explicitly approves the next phase.

Hard gates:

- after implementation conformance review, before documentation sync analysis
- after documentation sync analysis, before sending proposal-table rows to Note Manager or clarification
- after Note Manager draft or manifest output, before any durable write
- after durable documentation sync is complete, explicitly deferred, or judged unnecessary, before task-lane closeout
- before deleting, moving, archiving, or otherwise cleaning up workflow artifacts

Confirmation shape:

```text
Proposed action: <next phase or action>
Reason: <why this follows from the reviewed evidence>
Expected output: <artifact, report, handoff, draft, archive summary, or cleanup proposal>
Planned behavior: <what this skill will do and what it will not do without later approval>

Approve this action?
```

## Review Scope Cap

Initial review reads packet + report + diff only. Load note context only when a specific note is named in the diff, report, or follow-up findings. Never begin with a broad documentation sweep.

For maintenance review, start from the explicit task scope named by the user. If the scope is too broad or unclear to inspect responsibly, escalate before beginning.

## Required Inputs

### Implementation Review
- approved task packet
- implementation report
- touched files, diff, or verification output when needed

If one of these inputs is missing and accurate comparison depends on it, flag the gap explicitly instead of improvising. Project notes are optional and become necessary only when documentation synchronization is part of the work.

### Documentation Sync Analysis
- accepted implementation review disposition, or explicit user approval to analyze documentation sync
- approved task packet
- implementation report
- touched files, diff, or verification output when needed
- specific note paths, note-search results, or implementation evidence that make the durable-sync subject bounded

If implementation has not been accepted or the sync subject is not bounded, propose the missing gate or clarification instead of producing Note Manager routing.

### Maintenance Review
- user-provided maintenance task
- bounded scope named by that task (known note set, note type, folder, hub, artifact set, lint target, or health-check target)

### Task Lane Closeout
- user-provided closeout or review task
- bounded scope naming `docs/In-flight/` or one or more specific in-flight task lanes
- settled task lane artifacts with a shared `Task ID` when available

If a lane lacks `Task Status: settled`, do not close it out by default.
Report it as still active, blocked, or unclear unless the user explicitly asks for maintenance findings on unsettled lanes.

## Implementation Review Workflow

### Steps

1. Extract acceptance criteria, scope, and constraints from the approved packet.
2. Read the implementation report and verification notes.
3. Compare implementation against the approved packet.
4. Identify matches, mismatches, missing checks, and newly introduced assumptions.
5. For each durable note change that came from a clarified context handoff, run the **Interpretation Fidelity Check** (see below).
6. Decide whether documentation-sync analysis should be proposed.
7. Create or propose follow-up task context for unresolved issues.
8. Recommend `keep`, `revise`, or `reject`. If `reject`, produce a follow-up task or re-clarification context — never a silent revert.
9. If documentation sync may be needed, output a confirmation prompt for **Documentation Sync Analysis** and stop.

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

## Documentation Sync Analysis Workflow

Use this mode only after accepted implementation evidence exists and the user has approved moving from implementation review into documentation-sync analysis, or when the user directly requests this mode for a bounded accepted implementation.

### Steps

1. Read the accepted implementation review disposition, approved packet, implementation report, and touched files or diff needed to understand durable knowledge impact.
2. Identify implementation-backed facts, decisions, behavior changes, or settled ideas that may need durable documentation.
3. Separate each proposed documentation-sync subject. Use one row per documentation-sync subject; do not bundle unrelated note changes.
4. For each subject, distinguish `decided`, `proposed`, `unclear`, and `blocked` points.
5. Run the **Interpretation Fidelity Check** when the subject came from a clarified context handoff or idea note.
6. Produce a compact **Documentation Sync Proposal Table** using the table shape below.
7. Route clear rows directly to `dw-note-manager` after user approval. Route only uncertain rows to `dw-clarify-intent`.
8. If no durable documentation sync is needed, say that explicitly and propose whether task-lane closeout should be considered next.

### Checklist

Check for:
- accepted implementation facts that changed durable project knowledge
- idea notes that became promotion candidates without treating promotion as automatic
- stale or missing project subject, design, decision, or workflow-state documentation
- multiple subjects that should remain separate
- unclear note target ownership that should go through clarification
- any proposed action that would require Note Manager rather than review/sync

### Documentation Sync Proposal Table

Use one compact table as the default reviewable decision surface. Do not create separate context proposal artifacts or clarified handoffs unless a row is routed to `dw-clarify-intent`.

| subject | target note or uncertainty | action | evidence | proposed change | uncertainty | constraints | route |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <durable subject> | <note path or unclear target> | `create` / `update` / `defer` / `reject` | <packet/report/diff/note evidence> | <small description of note change> | `decided` / `proposed` / `unclear` / `blocked` | <what must not happen> | `note-manager` / `clarify-intent` / `defer` / `reject` |

Route rules:

- `note-manager`: use when the target, action, evidence, durable meaning, and constraints are clear enough for Note Manager to apply or draft the update without guessing.
- `clarify-intent`: use only when subject boundaries are mixed, target ownership is unclear, evidence is weak, durable meaning is unresolved, or the row would force Note Manager to guess.
- `defer`: use when the subject is valid but should not be handled in the current pass.
- `reject`: use when the proposed sync would be misleading, out of scope, or not durable knowledge.

The approval prompt should let the user approve, revise, defer, or reject rows individually or as a batch.

### Disposition

`sync-needed` | `no-sync-needed` | `clarification-needed`

`sync-needed` produces a compact Documentation Sync Proposal Table and waits for approval before routing rows.
`no-sync-needed` may propose task-lane closeout as a next phase, but must stop before closeout.
`clarification-needed` routes the uncertainty through `dw-clarify-intent` before Note Manager.

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

## Task Lane Closeout Workflow

Use this mode when the task is to review or close workflow artifacts in `docs/In-flight/`.

### Steps

1. Read only the named in-flight artifact set or task lane scope.
2. Group artifacts by `Task ID` when present; if task ids are missing, group only when filenames and artifact links make the lane unambiguous.
3. Select lanes with `Task Status: settled` for closeout.
4. Leave unsettled lanes in `in-flight/` unless they conflict with the requested work or the user explicitly asks for a maintenance finding on them.
5. For each settled lane, compare the handoff, packet, implementation report, review notes, and touched files or diff when available.
6. Produce one distilled archive summary per reviewed lane using the archive summary shape below.
7. Recommend whether consumed in-flight artifacts should be deleted, moved to a raw archive, or retained as evidence.
8. Do not delete or move in-flight artifacts unless the user has explicitly approved that cleanup.
9. Route durable documentation changes through `dw-clarify-intent -> dw-note-manager` when needed.
10. If documentation sync has not been completed, explicitly deferred, or judged unnecessary, report that closeout is gated and stop before cleanup recommendations that would remove evidence.

### Archive Summary Shape

Archive summaries should be compact and useful for future project learning:

```md
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

Raw handoffs, packets, and reports should be preserved only when they contain important evidence that the distilled archive summary cannot adequately capture.
The first closeout pass should write distilled task closeout summaries under `docs/Archieved/Tasks/`; raw archive handling remains a deferred design decision.

### Disposition

`keep` | `revise` | `reject` for implementation conformance, plus one closeout recommendation:

- `archive-ready`: settled lane can be summarized and closed after cleanup approval
- `retain-in-flight`: lane is not settled or still affects current work
- `follow-up-needed`: closeout found a missing decision, stale durable note, or implementation gap

## Interpretation Fidelity Check

When reviewing durable note changes that came from a clarified context handoff:

1. Load the original handoff or prompt.
2. Diff it against the current note or proposed note change.
3. Flag any preserved fact that: flipped polarity (uncertainty became certainty), was generalized (specific became vague), or was silently resolved (open question became closed without a recorded decision).

All three are interpretation drift. Do not normalize them — surface each as an explicit flag.

## Documentation Responsibilities

You may:
- identify factual gaps in implementation reports when missing information affects review or synchronization,
- propose synchronization context for feature, task, architecture, design, decision, or in-flight workflow-state artifacts after the documentation-sync phase is approved,
- create compact proposal-table rows that route clear items to `dw-note-manager` and uncertain items to `dw-clarify-intent`,
- create or propose follow-up task context,
- route follow-up note subjects through the local clarification path when they need to become durable notes,
- and flag stale hubs or decision logs.

You may not:
- create, update, archive, delete, or relink durable notes directly when a separate note-management gate exists,
- treat context proposals as durable note actions or durable note approval,
- use documentation updates to mask an implementation mismatch,
- or silently remove stale notes or artifacts.

Prefer small, traceable updates over broad rewrites.

## Role Tool Boundaries

### Allowed by default
- read the task packet, implementation report, and touched files,
- read the bounded note or artifact scope named by a maintenance review task,
- compare implementation against the approved plan,
- identify factual gaps in workflow artifacts such as implementation reports,
- create or propose compact proposal-table rows inside an approved Documentation Sync Analysis phase,
- route clear proposal-table rows directly to `dw-note-manager` after approval,
- create maintenance review reports,
- create or propose follow-up task context,
- and flag mismatches, stale notes, and decision gaps.

### Not allowed without explicit human approval
- rewriting implementation scope after the fact,
- silently changing the accepted plan,
- moving from implementation review into documentation-sync analysis,
- moving from documentation-sync analysis into Note Manager routing,
- moving from documentation sync into task-lane closeout,
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
- proposed next action for documentation-sync analysis when durable knowledge may need sync
- follow-up tasks
- decision candidates
- disposition: `keep`, `revise`, or `reject`

### Documentation Sync Analysis Output
- accepted implementation evidence inspected
- documentation-sync subjects identified
- one compact Documentation Sync Proposal Table
- uncertainty labels for each subject
- proposed next action for each row: `note-manager`, `clarify-intent`, `defer`, or `reject`
- disposition: `sync-needed`, `no-sync-needed`, or `clarification-needed`

### Maintenance Review Output
- maintenance review report
- follow-up tasks or decision candidates
- routing recommendation
- disposition: `sync-needed`, `follow-up-needed`, or `no-action`

### Task Lane Closeout Output
- lanes inspected and their task status
- lanes selected for closeout
- archive summary draft or written archive summary path, depending on user authorization
- consumed in-flight artifacts and recommended cleanup action
- durable documentation sync context, if needed
- closeout recommendation: `archive-ready`, `retain-in-flight`, or `follow-up-needed`

If no issues are found, say that explicitly and note any residual verification or documentation gaps.

## Final Check

### Implementation Review
- Was implementation compared to the approved packet?
- Are mismatches explicit?
- Was documentation-sync analysis only proposed, not run automatically?
- Are follow-up tasks separated from completed work?
- Has any unapproved change been escalated instead of normalized?
- If `reject`, is there a follow-up task or re-clarification context?

### Documentation Sync Analysis
- Was the phase explicitly approved or directly requested for bounded accepted implementation evidence?
- Was the Interpretation Fidelity Check run for any clarified context handoff?
- Are documentation-sync recommendations traceable?
- Does the proposal table route only uncertain rows to `dw-clarify-intent`?
- Did the output stop before Note Manager routing or durable write unless separately approved?

### Maintenance Review
- Was the scope bounded to the task named by the user?
- Are all findings routed through clarification before note mutation?
- Is the maintenance review report complete?

### Task Lane Closeout
- Were only settled task lanes selected for closeout?
- Were unsettled lanes left in place or reported without being silently closed?
- Was one distilled archive summary produced or drafted for each closed lane?
- Did any deletion or movement of in-flight artifacts receive explicit approval?

If any answer is no, continue review or escalate.
