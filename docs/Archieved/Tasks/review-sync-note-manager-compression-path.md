# Review Sync Note Manager Compression Path

- Type: task-archive-summary
- Status: closed
- Task ID: review-sync-note-manager-compression-path
- Date: 2026-05-14

## Original Intent

Reduce documentation-sync overhead after the technical documentation governance lane produced too many intermediate handoffs, manifests, and drafts.

The goal was to keep explicit approval gates while replacing mandatory artifact chaining with a compact proposal table that can route clear rows directly to Note Manager.

## Work Done

- Updated `project-review-sync` so Documentation Sync Analysis defaults to one compact proposal table.
- Defined proposal-table fields: subject, target note or uncertainty, action, evidence, proposed change, uncertainty, constraints, and route.
- Routed clear approved rows directly to `dw-note-manager`.
- Kept uncertain rows routed through `dw-clarify-intent`.
- Updated `dw-note-manager` to handle multiple bounded note writes in one approved batch without requiring a separate manifest or draft artifact.
- Preserved draft-first behavior when write authorization is ambiguous.
- Updated `agents-bridge` and related durable notes to reflect the compressed path.

## Important Decisions

- Gates remain necessary; full rewritten artifacts at every gate are not.
- Clear sync proposal rows can go directly to Note Manager after approval.
- Note Manager can handle multiple approved note writes in one bounded batch.
- Review/sync still cannot mutate durable notes directly.
- Existing in-flight artifacts from the earlier governance lane were left for a separate cleanup pass, which this closeout now performs.

## Final Files

- `modes/dev-workflow/skills/project-review-sync/SKILL.md`
- `modes/dev-workflow/skills/dw-note-manager/SKILL.md`
- `modes/dev-workflow/agents-bridge.md`
- `AGENTS.md`
- `CLAUDE.md`
- `docs/Durable Notes/review-agent.md`
- `docs/Durable Notes/note-manager.md`
- `docs/Durable Notes/Durable Notes Follow Accepted Implementation.md`
- `docs/Idea Backlog/Technical Project Documentation Governance.md`

## Verification

- `python3 tools/atlas.py sync` passed.
- `python3 tools/atlas.py skills sync --mode dev-workflow` passed.
- `git diff --check` passed.
- Source and installed skill text inspection confirmed proposal-table routing, direct bounded batch write support, and write-authorization signals.
- Final Atlas sync reruns reported no changes needed.

## Reusable Pattern

Use a compact proposal table as the documentation-sync decision surface when rows are clear enough for Note Manager. Route only uncertain rows to clarification.

This reduces token and artifact bloat while preserving explicit gates and row-level approval.

## Remaining Risk Or Follow-up

- Confirm through later use that the compressed path is easier without weakening approval boundaries.
- Keep raw implementation evidence out of durable notes unless it has been distilled through the appropriate review or Note Manager gate.
