# Technical Project Documentation Governance

Status: [[status-active]]
Type: [[idea-note]]
Related: [[Dev Workflow Documentation Model]], [[note-manager]], [[review-agent]], [[Workflow Artifact Lifecycle and Closeout]], [[Two-Phase Workflow Boundary]], [[Durable Notes Follow Accepted Implementation]]
Created: 2026-05-13
Last Reviewed: 2026-05-14
Priority:

---

## Idea

Technical project documentation in `dev-workflow` needs clearer governance before more tools are built on top of it.

The workflow should define what a technical project must document, how `Project Subject` and `Design Note` differ, how transient task artifacts become durable knowledge, and how review/sync plus Note Manager should be gated so they do not silently take action.

## Prompt 1: Technical Documentation Rules And Note Types

The starting concern was how to define documentation rules and note types for a technical project, especially around:

- `docs/Templates/Design Note Template.md`
- `docs/Templates/Project Subject Template.md`

A technical project should document enough for a future maintainer to answer:

- what exists,
- why it exists,
- how it works,
- and how to safely change it.

Decided:

- `Project Subject` should be the default durable note for one active technical area, such as a feature, workflow behavior, module, tool, integration, or implementation concept.
- `Design Note` should be rarer and should explain cross-cutting design, reusable behavior, architecture constraints, or decisions that affect multiple subjects.
- Every accepted idea should not automatically become a design note.

Proposed:

- Keep the documentation type set small.
- Sharpen the templates so project subjects preserve local technical state, while design notes preserve broader constraints and rationale.

Unclear:

- Whether the next durable design outcome should update an existing documentation model note or create a new governance/design note later.

## Prompt 2: Transient Task Artifacts And Post-Implementation Durable Notes

The next concern was that task packets and implementation reports should become transient workflow evidence, not permanent durable knowledge notes.

Post-implementation work should naturally create or update durable notes related to the feature subject or design. This may happen from the implementation report, or by promoting an idea note when implementation settles it.

Decided:

- Task packets and implementation reports are workflow evidence.
- Durable note creation or update should happen through Note Manager.
- Post-implementation review should identify whether accepted implementation created durable knowledge.
- Idea notes may become promotion candidates when accepted implementation settles or materially advances them.

Proposed:

- Add a post-implementation documentation sync review step.
- Review/sync identifies bounded documentation-sync subjects.
- Note Manager receives one bounded subject at a time and decides whether to create, update, promote, defer, or return to clarification.

Unclear:

- Whether documentation sync review should happen for every accepted implementation or only when durable knowledge changed.
- Whether `promote` should become a first-class Note Manager action.

## Prompt 3: Confirmation Before Immediate Action

A governance problem was identified: review/sync and Note Manager should not immediately act without confirmation.

Before any immediate action, the proposed action should be shown to the user with a short explanation of:

- reason,
- expected output,
- planned behavior,
- and requested approval.

Decided:

- Review/sync may analyze and propose.
- Note Manager may decide or draft proposed note actions.
- Neither should execute durable action without confirmation.
- Confirmation is required before durable note mutation, artifact cleanup, archiving, deletion, movement, or idea promotion.

Proposed:

- Add an action confirmation gate before a role proceeds into a proposed action.
- Add a write confirmation gate before durable mutation is applied.

Example confirmation shape:

```text
Proposed action: update existing feature subject note
Reason: accepted implementation changed feature behavior and the current note is stale
Expected output: one draft note update with refreshed metadata and links
Planned behavior: Note Manager will prepare the update only; it will not write until approved

Approve this action?
```

Unclear:

- Whether action confirmation is required before every draft action or only before higher-impact draft preparation.
- Whether this prompt shape should become a reusable template.

## Prompt 4: Review Role Overload And Hard Gates

The final concern was that review/sync may be overloaded.

It currently risks combining several jobs:

- comparing task packet and report with actual code,
- deciding whether implementation passes,
- handling in-flight cleanup,
- summarizing task artifacts,
- analyzing documentation sync,
- owning documentation proposals.

These are different responsibilities and should not run as one automatic process.

Decided:

- Implementation conformance review, documentation sync analysis, and artifact closeout are separate jobs.
- They need hard gates between them.
- Review/sync should not silently combine them into one continuous flow.

Proposed:

- Keep `project-review-sync` as an umbrella only if it has explicit modes:
  - implementation review,
  - documentation sync analysis,
  - task-lane closeout.
- Each mode should produce a proposal and stop.
- No mode should automatically enter the next mode.

Possible gated sequence:

```text
implementation report
-> implementation review
-> user confirms next phase
-> documentation sync analysis
-> user confirms Note Manager handoff
-> Note Manager manifest or draft
-> user confirms durable write
-> user confirms artifact closeout
-> archive summary / cleanup
```

Unclear:

- Whether documentation sync analysis should remain under review/sync or become a separate role.
- Whether artifact closeout should remain under review/sync or become a separate closeout tool.
- Whether implementation review should always stay lean and stop before documentation sync.

## Current Working Direction

The workflow should become more automatic in detection, but more explicit in execution.

Review/sync should identify possible next actions, but stop at gates. Note Manager should decide concrete note actions, but stop before drafting or writing unless confirmed.

## Implementation Status

Part of this idea was implemented on 2026-05-14 through `docs/In-flight/report-technical-project-documentation-governance.md`.

Implemented:

- `project-review-sync` now has hard phase gates between implementation review, documentation sync analysis, Note Manager handoff, durable write, and task-lane closeout.
- Documentation Sync Analysis is now an explicit review/sync mode.
- `dw-note-manager` now distinguishes action confirmation from durable-write confirmation.
- Project Subject and Design Note templates were sharpened to preserve the intended note-type boundary.
- Atlas project sync and skill sync propagated the reusable mode-source changes.
- A follow-up compression-path update replaced mandatory handoff/manifest/draft chaining with compact sync proposal tables: clear rows can go directly to Note Manager, while uncertain rows still route to `dw-clarify-intent`.

Still unresolved:

- Whether documentation sync review should be required for every accepted implementation or only triggered when durable knowledge changed.
- Whether idea promotion should become a first-class Note Manager action.
- Whether documentation sync analysis or task-lane closeout should eventually become separate tools.
- Whether the confirmation prompt shape should be treated as a broader reusable template beyond the affected skills.
- How much of the old in-flight evidence chain should be archived or summarized after the compression path is in place.

This note is active because it now tracks implemented workflow behavior plus unresolved governance follow-up. It is not settled.

## Open Questions

- Should documentation sync review be a required closeout phase or only triggered when durable knowledge changed?
- Should idea promotion become an explicit Note Manager action?
- Should review/sync remain one skill with hard modes, or should documentation sync and artifact closeout become separate tools?
- Should confirmation prompts be standardized in mode source?
- Which durable notes and skills need updates if this idea is accepted?

## Source

Created from `docs/In-flight/handoff-technical-project-documentation-governance.md`.
