# Workflow Artifact Lifecycle And Closeout Packet

- Type: task-packet
- Status: approved
- Task ID: workflow-artifact-lifecycle-closeout
- Task Status: planned
- Related to: `docs/Durable Notes/Workflow Artifact Lifecycle and Closeout.md`
- Revision: v1
- Created: 2026-05-12
- Approval evidence: user replied "go on" after reviewing the packet in conversation.

## Objective

Implement the first governance slice of the workflow artifact lifecycle model:
handoffs open task lanes, packets/reports stay traceable by task lane, review/sync closes settled lanes, and archive summaries preserve distilled learning.

## Scope

- Define task-lane lifecycle expectations in the reusable dev-workflow runtime contract.
- Update workflow artifact schemas to include task identity/status traceability.
- Update review/sync behavior so it scans settled lanes for closeout and produces distilled archive summaries.
- Keep this as governance and workflow-documentation behavior only.

## Non-goals

- `active-context.md` has been removed in a follow-up workflow update; use `docs/In-flight/` as the primary active workflow state.
- Do not implement generated active context.
- Do not add smaller-model review routing.
- Do not delete current in-flight artifacts in this step.
- Do not create raw archive subfolder policy yet.

## Relevant Context

Read first:

- `docs/Durable Notes/Workflow Artifact Lifecycle and Closeout.md`
- `docs/In-flight/handoff-workflow-artifact-lifecycle-closeout.md`
- `docs/In-flight/handoff-settled-task-review-queue.md`
- `docs/Durable Notes/review-agent.md`
- `docs/Durable Notes/Two-Phase Workflow Boundary.md`
- `docs/Durable Notes/Dev Workflow Documentation Model.md`

## Allowed Implementation Area

Editable:

- `modes/dev-workflow/agents-bridge.md`
- `modes/dev-workflow/docs/vocabulary.md`
- `modes/dev-workflow/skills/dw-clarify-intent/references/clarified-context-handoff.md`
- `modes/dev-workflow/skills/project-planner/references/task-packet-schema.md`
- `modes/dev-workflow/skills/project-implementer/references/implementation-report-schema.md`
- `modes/dev-workflow/skills/project-review-sync/SKILL.md`
- optional new archive summary template under `modes/dev-workflow/docs/Templates/`

Sync target after source edits:

- run `python3 tools/atlas.py sync`

Do not directly hand-edit synced copies unless Atlas sync requires follow-up.

## Constraints

- Local `AGENTS.md` remains authoritative.
- Durable note mutation still routes through `dw-note-manager`.
- Review/sync may close workflow artifacts only within approved review/closeout scope.
- In-flight is not a global hard blocker; only related/conflicting or settled lanes affect routing.
- Existing status vocabulary may be extended only if needed and clearly scoped.

## Acceptance Criteria

- Runtime contract describes `docs/In-flight/` as open task-lane state.
- Artifacts have a stable way to carry `task_id` and lane/status traceability.
- Review/sync distinguishes unsettled lanes from settled review-ready lanes.
- Review/sync owns closeout for settled lanes, including distilled archive summary creation.
- Archive summary shape is documented.
- Deferred questions remain visible rather than silently decided.

## Verification Expectations

- `python3 tools/atlas.py sync`
- `git diff --check`
- read back changed files
- inspect resulting diff for managed-source and synced-copy consistency

## Risks / Open Questions

- Exact task status field name is still a design choice.
- Meaning of `settled` must be explicit enough for review routing.
- Deletion vs moving consumed artifacts should probably require explicit closeout approval.
- Active workflow state is checked through `docs/In-flight/`; separate generation from that folder remains a future possibility, not current scope.

## Assumptions

- First implementation should be narrow and governance-focused.
- Source of truth for reusable behavior is `modes/dev-workflow/`.
- Current in-flight artifacts are evidence for the design, not cleanup targets for this packet.

## Confidence Assessment

Medium-high. The desired model is clear, but a few policy details should be implemented conservatively and left extensible.

## Approval Status

approved
