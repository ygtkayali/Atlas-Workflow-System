# Implementer Escalation Threshold

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

Unspecified decisions arise during implementation. The implementer uses a two-tier model to handle them without either pausing on every minor judgment call or silently crossing approval boundaries.

## Tier 1 — Take and Record

Low-impact, reversible decisions: variable names, default values, trivial edge cases where any reasonable choice produces the same observable outcome. The implementer takes the simplest sensible choice and records it in Assumptions Introduced. No pause required.

## Tier 2 — Stop and Ask

Decisions that touch observable behavior, schema, API contracts, or user-visible UX. The implementer pauses and escalates. Silent resolution is prohibited regardless of how obvious the "right" answer seems.

## Why the Threshold Is Where It Is

Tier 1 decisions don't change what the system does. A future developer reading the code could have made the same choice independently. Tier 2 decisions change the observable outcome or cross a boundary that has approval consequences extending beyond this implementation task.

The threshold is behavioral impact, not implementation complexity. A simple naming choice is Tier 1 even if it took thought. A one-line schema field addition is Tier 2 even if it looks trivial.

## Why Partial Hiding Is Prohibited

A common failure mode is to proceed with a partially completed implementation and bury the problematic decision in a footnote. The skill explicitly prohibits this: a hidden escalation issue is worse than an open one because the human cannot evaluate what was decided, reconstruct the intent, or undo it cleanly. When escalating, the issue must be surfaced before implementation continues, not after.

## Escalation Shape

A useful escalation states: the specific issue, why it blocks safe implementation, the decision needed, the impacted area, and the recommended next step. A vague escalation ("something seems off here") creates friction without resolving anything.

## What Is Not an Escalation

Not every judgment call needs a pause. If the decision is reversible and does not change the observable outcome, it is Tier 1. The implementer should record it and move on. Over-escalating minor choices degrades the value of the escalation signal.
