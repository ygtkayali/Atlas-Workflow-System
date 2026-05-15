# Implementer Approval Gate

Status: [[Tags/status-draft]]
Type: [[design-note]]
Parent: [[implementer-agent]]
Related: [[implementer-agent]], [[planner-agent]], [[planner-entry-gate]], [[clarify-intent]]
Created: 2026-05-15
Last Reviewed: 2026-05-15
Source: modes/dev-workflow/skills/project-implementer/SKILL.md
Decisions:
Dependencies:
Tasks:

---

The implementer requires an explicitly approved artifact before doing any work. This is not a safety check bolted on top — it is the foundational design principle that separates the implementer from a general-purpose coding agent. Approval gates enforce that intent, scope, constraints, and acceptance criteria were set by the human, not derived by the agent.

## What Counts as Approved

Two forms of input satisfy the gate:

- An explicitly user-approved implementation packet
- A direct user coding request that makes objective, scope, constraints, and intended behavior clear without inference

The threshold for a "sufficiently specific direct request" is whether scope is already determined or whether the agent would have to decide it. A vague request forces scope invention; a specific request hands scope over. The implementer is not authorized to resolve scope ambiguity — that belongs to the planner or clarify-intent path.

## Why Silent Scope Expansion is Prohibited

Scope expansion during implementation is invisible. The output looks complete, but the boundary has shifted without approval. The implementer treats the approved artifact as an execution boundary, not as guidance that can be exceeded when nearby improvements seem convenient. Self-widening scope is the failure mode this gate exists to prevent.

## What Happens When the Gate Fails

If the approval basis is unclear, missing, or contradictory, the implementer must escalate rather than guess. A partial or inferred approval does not authorize proceeding. The escalation must name the blocking issue, why it prevents safe implementation, the decision needed, and the recommended next step.

## Why This Shapes Everything Else

Because the approval gate is where scope gets fixed, every other constraint in the skill — context loading, escalation threshold, verification, reporting — assumes a known and bounded scope. If the gate is skipped or weakened, those downstream constraints lose their anchor.
