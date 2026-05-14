# Technical Project Documentation Governance

- Type: task-archive-summary
- Status: closed
- Task ID: technical-project-documentation-governance
- Date: 2026-05-14

## Original Intent

Establish the accepted parts of the `Technical Project Documentation Governance` idea in the reusable `dev-workflow` mode source and synced project documentation.

The task focused on making technical documentation governance clearer while preserving human approval gates between review, documentation sync, Note Manager, durable writes, and task-lane closeout.

## Work Done

- Added hard phase gates to `project-review-sync`.
- Added Documentation Sync Analysis as an explicit review/sync mode.
- Clarified that review/sync proposes documentation sync but does not mutate durable notes.
- Separated Note Manager action confirmation from durable-write confirmation.
- Sharpened Project Subject and Design Note templates.
- Synced reusable mode-source changes into managed project files and installed skills.
- Ran implementation review and documentation sync.
- Updated related durable notes and left `Technical Project Documentation Governance` active because unresolved governance questions remain.

## Important Decisions

- `project-review-sync` stays an umbrella skill for now, but implementation review, documentation sync analysis, and task-lane closeout are separate gated phases.
- Durable note mutation remains owned by `dw-note-manager`.
- Transient packets, reports, handoffs, context proposals, manifests, and drafts are workflow evidence, not durable knowledge by themselves.
- Project Subject remains the default durable note for one active technical area; Design Note remains for cross-cutting design and constraints.
- The source idea note was not marked settled because role splitting, sync trigger policy, idea promotion, prompt standardization, and archive policy remain open.

## Final Files

- `modes/dev-workflow/skills/project-review-sync/SKILL.md`
- `modes/dev-workflow/skills/dw-note-manager/SKILL.md`
- `modes/dev-workflow/agents-bridge.md`
- `modes/dev-workflow/docs/Templates/Project Subject Template.md`
- `modes/dev-workflow/docs/Templates/Design Note Template.md`
- `AGENTS.md`
- `CLAUDE.md`
- `docs/Templates/Project Subject Template.md`
- `docs/Templates/Design Note Template.md`
- `docs/Durable Notes/review-agent.md`
- `docs/Durable Notes/note-manager.md`
- `docs/Durable Notes/Durable Notes Follow Accepted Implementation.md`
- `docs/Durable Notes/Dev Workflow Documentation Model.md`
- `docs/Durable Notes/Workflow Artifact Lifecycle and Closeout.md`
- `docs/Idea Backlog/Technical Project Documentation Governance.md`

## Verification

- `python3 tools/atlas.py sync` passed.
- `python3 tools/atlas.py skills sync --mode dev-workflow` passed.
- Final Atlas sync reruns reported no changes needed.
- `git diff --check` passed.
- Implementation review disposition: `keep`.

## Reusable Pattern

Use `docs/In-flight/` for active workflow evidence, then distill settled task lanes into one archive summary once implementation review and documentation sync are complete or explicitly deferred.

For governance-heavy workflow changes, keep durable notes updated through Note Manager, but archive raw handoffs and packets once their evidence has been consumed.

## Remaining Risk Or Follow-up

- Decide whether Documentation Sync Analysis should eventually become a separate skill.
- Decide whether Task Lane Closeout should eventually become a separate tool.
- Decide whether idea promotion should become a first-class Note Manager action.
- Decide whether confirmation prompt shapes should be standardized beyond the affected skills.
- Decide long-term raw archive policy for consumed workflow artifacts.
