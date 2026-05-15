---
name: project-review-sync
description: "Use for any post-implementation or maintenance workflow that requires a review, sync, or closeout. Call this skill when the user asks to review implementation against an approved plan, analyze documentation sync after accepted work, run a maintenance or health check on notes or artifacts, check whether a durable note is stale, bloated, mis-scoped, or should be split into clearer design/feature subject notes, close out or archive settled task lanes, clean up docs/In-flight/, or check whether work matches what was planned. Triggers on: review, sync, closeout, archive, stale docs, bloated notes, note refactor, note split, design notes, feature subject notes, health check, in-flight cleanup, implementation check."
---
---
# Project Review / Sync

Umbrella skill for post-implementation and maintenance workflows. Routes review, sync, maintenance, and closeout through explicit phase gates. No phase chains without user approval between each.

## Modes

- **Implementation Review** — compare implementation against an approved task packet.
- **Documentation Sync Analysis** — inspect accepted implementation evidence for durable-knowledge impact.
- **Maintenance Review** — analyze a bounded maintenance task, including stale or structurally weak durable notes, and route findings.
- **Task Lane Closeout** — review settled in-flight lanes, produce archive summaries, route cleanup.

## Mode Detection

|If the request mentions…|Use mode|
|---|---|
|implementation, approved packet, does it match, post-merge review|Implementation Review|
|doc sync, documentation update, approved to sync|Documentation Sync Analysis|
|stale notes, bloated notes, note refactor, note split, design notes, feature subject notes, health check, maintenance, link check, artifact cleanup|Maintenance Review|
|closeout, archive, In-flight cleanup, settled lane|Task Lane Closeout|

If signals are mixed or absent, ask before starting:

> "Which mode — implementation review / doc sync / maintenance / closeout?"

Once mode is confirmed, read `references/[mode-filename].md` and follow that workflow.

|Mode|Reference file|
|---|---|
|Implementation Review|`references/implementation-review.md`|
|Documentation Sync Analysis|`references/doc-sync-analysis.md`|
|Maintenance Review|`references/maintenance-review.md`|
|Task Lane Closeout|`references/task-lane-closeout.md`|

## Phase Gates

Do not chain modes without explicit approval between each.

Hard gates:

- after implementation review, before doc sync analysis
- after doc sync analysis, before Note Manager or clarification routing
- after Note Manager output, before durable write
- after doc sync complete or deferred, before task-lane closeout
- before deleting, moving, or archiving workflow artifacts

```text
GATE → [next action]: [expected output]
Excludes (needs separate approval): [what will not happen]
Approve?
```

## Review Scope Cap

- Implementation: packet + report + diff only. Load note context only when a specific note is named in findings.
- Maintenance: named scope from the task only. Escalate if scope is too broad or unclear before beginning.
- Closeout: named in-flight artifacts only. Never begin with a broad sweep.

## Required Inputs

### Implementation Review

- approved task packet, implementation report, touched files or diff

### Documentation Sync Analysis

- accepted implementation review disposition (or explicit user approval to proceed)
- approved task packet, implementation report, touched files or diff
- bounded sync subject (specific note paths or evidence)

### Maintenance Review

- user-provided maintenance task with bounded scope
- named note, artifact, task lane, folder, or health check target when the request is about existing workflow state

### Task Lane Closeout

- user-provided closeout task naming `docs/In-flight/` or specific lanes
- settled task lane artifacts (`Task Status: settled`)

Flag missing required inputs explicitly. Do not improvise around them.

## Boundaries

**May do:** read task packet, report, diff, and bounded note scope · identify gaps, mismatches, stale state · produce proposal tables, review reports, archive summaries · route clear rows to `dw-note-manager` and uncertain rows to `dw-clarify-intent` · create follow-up task context.

**May not do without explicit approval:** move between phases · create, update, archive, or delete durable notes · rewrite implementation scope after the fact · use documentation updates to mask implementation mismatches · delete or move in-flight artifacts.

## Interpretation Fidelity Check

Used by Implementation Review and Documentation Sync Analysis when reviewing note changes from a clarified context handoff:

1. Load the original handoff or prompt.
2. Diff against the current or proposed note change.
3. Flag: polarity flip (uncertainty → certainty) · generalization (specific → vague) · silent resolution (open question → closed without recorded decision).

Surface each as an explicit flag. Do not normalize.

## Escalation

Escalate when: implementation exceeds the approved packet · undocumented design decision made during implementation · verification missing for a material-risk change · documentation sources disagree · source-of-truth ownership is unclear · change should have required prior human approval.

State: mismatch or uncertainty · why it matters · decision needed · impacted artifact · recommended next step.

## Reference Schemas

- Packet structure → `../project-planner/references/task-packet-schema.md`
- Implementation report → `../project-implementer/references/implementation-report-schema.md`
