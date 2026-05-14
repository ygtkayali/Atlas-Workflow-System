# Compact Workflow Outputs and Handoffs

Status: [[Tags/status-draft]]
Type: [[idea-note]]
Related: [[Workflow Mode Skill Governance]], [[Workflow CLI Mode System]]
Created: 2026-05-14
Last Reviewed: 2026-05-14
Priority: [[docs/Tags/priority-high|priority-high]]

---

## Idea

The workflow should make CLI expected output and proposed handoffs as compact as possible without reducing important information.

This should become a repo policy and then flow into the relevant `dev-workflow` skills, references, schemas, and templates.

The goal is to reduce recurring output-token cost in workflow review, Note Manager intake, and CLI-facing implementation while preserving the actual decision surface.

## Policy Direction

- CLI expected output should default to summaries, status labels, key lines, and file paths instead of full pasted output.
- Proposed handoffs should be short, structured, and reference-heavy.
- Handoffs should preserve target, action, reason, evidence pointers, uncertainty, constraints, and requested downstream decision.
- Handoffs should avoid repeated prose, duplicated context, full transcripts, and broad restatement of source artifacts.
- Review/sync should still create one proposed handoff per durable note change so Note Manager decisions remain isolated.
- One-time artifact creations, final durable writes, accepted implementation reports, task packets, archive summaries, and other durable final artifacts may remain full enough to be useful.

## Important Boundary

Compact output must not remove:

- decisions,
- uncertainty labels,
- blockers,
- target files or notes,
- evidence references,
- approval state,
- verification outcomes,
- user constraints,
- or the specific downstream action being requested.

The compression target is repeated wording and raw output volume, not operational meaning.

## Proposed Handoff Shape

Proposed handoffs should prefer a compact structure like:

```text
Target: <note path or artifact>
Action: create | update | metadata | archive | closeout
Reason: <one sentence>
Evidence: <file/path refs, command refs, or artifact refs>
Uncertainty: decided | proposed | unclear | blocked
Constraints: <only constraints that affect this action>
Requested decision: <one sentence>
```

If more context is necessary, link to or name the source artifact instead of copying it into the handoff.

## Proposed CLI Output Shape

CLI-facing expected outputs and verification reports should prefer a compact structure like:

```text
Command: <command>
Result: pass | fail | blocked | not run
Relevant output: <only failing lines or key lines>
Full output: omitted | saved at <path> | available in terminal history
Next action: <only when needed>
```

Full command output should appear only when it is the artifact being reviewed, needed to diagnose a failure, or explicitly requested.

## Implementation Surface

This likely requires updates to:

- root repo policy in `AGENTS.md` or a linked durable policy note,
- `modes/dev-workflow/agents-bridge.md`,
- `modes/dev-workflow/skills/project-review-sync/SKILL.md`,
- `modes/dev-workflow/skills/dw-note-manager/SKILL.md`,
- handoff references under `modes/dev-workflow/skills/*/references/`,
- task packet and implementation report schemas where they specify CLI output or expected handoff shape,
- any templates that encourage large copied output blocks.

After source changes, Atlas sync should update the project copy rather than manually maintaining reusable behavior in both places.

## Open Questions

- Should compact handoff shape become the default for all proposed handoffs, or only review/sync to Note Manager handoffs?
- Should full command output be saved to a file when omitted, or only when debugging value is high?
- Should skills define a maximum expected line count for CLI output snippets?
- Should review/sync use a compact proposal table instead of separate handoff files when the user has not approved durable note mutation yet?

## Priority Reason

This is high priority because repeated CLI output and repeated handoff prose create recurring token cost during ordinary workflow operation.

Reducing this cost should improve daily usability without weakening the gates, final writes, or Note Manager review quality.
