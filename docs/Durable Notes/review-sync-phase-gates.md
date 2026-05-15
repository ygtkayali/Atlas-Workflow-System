# Review-Sync Phase Gate Model

Status: [[Tags/status-draft]]
Type: [[design-note]]
Parent: [[review-agent]]
Related: [[review-agent]], [[review-sync-mode-dispatch]], [[review-sync-scope-cap]]
Created: 2026-05-15
Last Reviewed: 2026-05-15
Source: modes/dev-workflow/skills/project-review-sync/SKILL.md
Decisions:
Dependencies:
Tasks:

---

Every transition between phases in the review / sync skill requires explicit user approval. No phase chains without that approval, regardless of how clear the next step appears.

## Design Scope

The phase gate model governs what the skill may do in sequence without stopping for approval. It applies across all four modes and to every phase transition within them.

## Chosen Design

Hard gates:
- after implementation review, before doc sync analysis
- after doc sync analysis, before Note Manager or clarification routing
- after Note Manager output, before durable write
- after doc sync complete or deferred, before task-lane closeout
- before deleting, moving, or archiving workflow artifacts

Gate format:
```text
GATE → [next action]: [expected output]
Excludes (needs separate approval): [what will not happen]
Approve?
```

## Rationale

Chaining phases silently lets a review become a note mutation or an artifact deletion without the human approving the escalation in authority. Each gate makes the scope of what the next approval covers visible and bounded before the human consents to it.

## Open Questions
