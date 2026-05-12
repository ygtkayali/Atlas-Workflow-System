# Settled Task Review Queue Handoff

- Type: clarified-context-handoff
- Status: ready_for_note_manager
- Related to: idea note amendment for serialized workflow artifact lifecycle and review queue behavior
- Created: 2026-05-11

## Clarified Subject / Subjects

### Subject 1: Review Processes Settled Tasks Only

The workflow idea is that review should only run for tasks that have reached a settled status.

In the serialized multi-task model, `docs/In-flight/` may contain multiple task lanes at the same time. Review should not treat every in-flight artifact as immediately reviewable or blocking.

Instead, each task lane should carry enough state to distinguish:

- open or intake-only work
- planned work
- in-progress implementation
- completed but not settled work
- settled work ready for review
- reviewed and archived work

Review/sync should operate on the subset of tasks marked settled, rather than interrupting other active lanes.

### Subject 2: Review as Soft Gate and Batch Queue

This modifies the earlier "in-flight non-empty means pause unrelated important work" model.

The improved model is:

- `in-flight/` may contain more than one serialized task lane.
- Review is a soft gate and reminder queue, not always a hard interruption.
- Review can batch settled tasks.
- Unsettled tasks can remain in-flight without forcing immediate review.
- Related or conflicting work may still require review before continuing, but unrelated work should not be blocked just because other in-flight tasks exist.

### Subject 3: Settled Status as Review Eligibility

The important routing rule is:

```text
review/sync only runs on task lanes with settled status
```

The status should belong to the task lane or artifact chain, not just to an individual note title.

Review eligibility should be explicit enough that agents can inspect in-flight artifacts and decide:

- which lanes are reviewable now
- which lanes are still active
- which lanes should be ignored by bulk review
- which lanes need human clarification before review

## Interpretation Basis

Origin type: direct user prompt / amendment to current workflow artifact lifecycle idea.

Original user input preserved:

```text
Review would on go for the tasks with setteled status. Create another handoff for this
```

Interpreted user intent:

- "on go" is interpreted as "only go".
- "setteled status" is interpreted as "settled status".
- The user wants a separate handoff preserving this refinement.
- The refinement belongs with the new serialized artifact lifecycle idea, where multiple tasks can be in-flight at the same time and review becomes a soft gate.

Relevant context used:

- `docs/In-flight/handoff-workflow-artifact-lifecycle-closeout.md` introduced the lifecycle model where handoff opens work, review closes work, in-flight shows open state, and archive stores distilled learning.
- `docs/Durable Notes/Workflow Artifact Lifecycle and Closeout.md` replaced the older task/report lifecycle note and preserves that broader model.
- The immediately preceding user idea introduced serialization so more than one task can be active at the same time, making review a soft gate and batchable reminder rather than a hard interruption.

User intent versus agent inference:

- User intent: create a handoff for the settled-status review rule.
- User intent: review should only go for tasks with settled status.
- Agent inference: this is an amendment to the serialized multi-task lifecycle idea.
- Agent inference: "settled" probably needs to be represented as task-lane status or artifact-chain status, not only as a durable note status.
- Agent inference: downstream Note Manager should decide whether to update the existing idea note or create a separate note.

Open ambiguity and downstream cautions:

- The exact status vocabulary for task lanes is not yet fixed.
- It is unclear whether "settled" should reuse `[[status-settled]]` or become a task artifact status field such as `task_status: settled`.
- It is unclear whether review should process only settled implementation reports, settled task lanes, or both.
- Bulk review behavior should not silently weaken high-impact review when a task affects workflow rules, architecture, schema, security, or future agent behavior.

Validation target:

- Downstream Note Manager should preserve the rule that review targets settled task lanes only.
- It should preserve the distinction between in-flight as "open lanes" and settled as "review-ready lanes."
- It should not restore the older hard rule that any non-empty `in-flight/` blocks unrelated important work.

## User Goal

Preserve a refinement to the workflow artifact lifecycle model: review should operate only on tasks that are settled, so multiple in-flight task lanes can coexist without review becoming an interruption.

## Decided

- A separate handoff should capture this refinement.
- Review should only go for tasks with settled status.
- The idea belongs to the serialized multi-task workflow artifact lifecycle discussion.
- Review should be a soft gate for eligible settled tasks rather than a hard blocker for all in-flight work.

## Proposed

- Add task-lane serialization so handoff, packet, report, review, and archive artifacts can share a task ID.
- Add or clarify a task-lane status field that can mark a lane as settled.
- Let review/sync scan `docs/In-flight/` and select only settled task lanes for review.
- Let bulk review summarize multiple settled tasks at once.
- Keep active or unsettled task lanes in `in-flight/` without forcing immediate closeout.

## Unclear / Blocked

- Whether task-lane status should reuse existing status tags or use a separate artifact-specific field.
- Whether "settled" means implementation is complete, human has accepted the result, or the task has reached a stable checkpoint.
- Whether review should ignore unsettled tasks entirely or report them as still active.
- How to handle tasks that are settled but high-impact enough to require full review rather than lightweight summary.

## Boundaries / Non-goals

- Do not implement serialization from this handoff alone.
- Do not change review/sync behavior from this handoff alone.
- Do not edit workflow governance, skill files, templates, or managed mode assets from this handoff alone.
- Do not make small-model review responsible for high-impact decisions.
- Do not make all non-empty `in-flight/` state block unrelated work.

## Relevant Context Already Known

- Related handoff: `docs/In-flight/handoff-workflow-artifact-lifecycle-closeout.md`.
- Related design note: `docs/Durable Notes/Workflow Artifact Lifecycle and Closeout.md`.
- Current workflow status vocabulary includes `[[status-settled]]`, but task-lane status semantics may need a separate design decision.

## Readiness For Note Manager

Ready for Note Manager.

This handoff is narrow and stable enough for Note Manager to decide whether to update `docs/Durable Notes/Workflow Artifact Lifecycle and Closeout.md` or create a separate linked design note for serialized task review eligibility.
