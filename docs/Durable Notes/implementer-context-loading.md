# Implementer Context Loading

Status: [[Tags/status-draft]]
Type: [[design-note]]
Parent: [[implementer-agent]]
Related: [[implementer-agent]], [[implementer-approval-gate]]
Created: 2026-05-15
Last Reviewed: 2026-05-15
Source: modes/dev-workflow/skills/project-implementer/SKILL.md
Decisions:
Dependencies:
Tasks:

---

The implementer loads only the context needed for the approved change and stops. This is a deliberate design choice, not a performance optimization. Broad context loading creates pressure to act on what was found — nearby issues, adjacent code smells, tests that seem relevant. The minimum-context rule prevents that pressure from becoming scope creep.

## Loading Order

1. Local `AGENTS.md`, if it exists — applies project-level constraints that override the skill
2. The approved execution artifact (packet, direct request, or equivalent)
3. Files directly implicated by that artifact
4. Constraints, decisions, or prior reports explicitly named by the artifact

Each layer is loaded only when the previous layer does not provide enough context to proceed. The artifact is the boundary, not a starting point for broader investigation.

## Why Discovery Beyond the Artifact Boundary Is Not Allowed

If the artifact does not name a file, that file is out of scope unless the artifact clearly requires it. Scanning for "related" context is how scope quietly expands — the agent finds something adjacent, judges it relevant, and acts on it. This is invisible to the human approving the work.

The rule forces the artifact to be the boundary rather than a center of gravity. This makes the implementation predictable: the human knows that what is not named in the artifact was not touched or influenced.

## The Safety-Convenience Tradeoff

This policy accepts the cost of occasional escalations when the artifact names too few files to implement safely. That cost is intentional. An implementer that discovers context freely is harder to reason about: the human cannot know what the agent inspected or what that inspection influenced.

When the approved artifact does not provide enough context, the correct response is to escalate — not to widen discovery to fill the gap.

## Notebooks

When changes involve notebooks, only the cells directly implicated by the approved change are in scope. Adjacent cells require explicit approval even when they appear related.
