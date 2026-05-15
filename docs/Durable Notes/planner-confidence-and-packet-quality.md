# Planner Confidence and Packet Quality

Status: [[Tags/status-draft]]
Type: [[design-note]]
Parent: [[planner-agent]]
Related: [[planner-agent]]
Created: 2026-05-15
Last Reviewed: 2026-05-15
Source: modes/dev-workflow/skills/project-planner/SKILL.md
Decisions:
Dependencies:
Tasks:

---

The planner makes planning uncertainty visible in the packet artifact itself rather than resolving it silently before handoff. Two mechanisms enforce this: the Confidence Rubric and the packet quality bar.

## Confidence Rubric

The rubric has four levels. Each packet must state the confidence level and a short reason.

**High** — all four hold: scope is explicit and bounded; constraints are documented; acceptance criteria are concrete and testable; no architectural unknowns remain.

**Medium** — all four planning questions have answers, but one or more constraints, risks, or acceptance details remain uncertain. Implementation can proceed with noted caution.

**Low** — one or more of the four planning questions cannot be answered from available notes. The packet should not proceed without additional clarification.

**Mixed** — at least one section of the packet is unclear or blocked while others are settled. The unclear sections must be named explicitly.

## Packet Revision Protocol

When updating an existing packet rather than producing a new one:

- Emit only the changed sections, not the full packet.
- Add a `Revision Notes` block at the top listing what changed, which sections moved status, and any new open questions introduced.
- Approval resets to `approval_pending` on any material change unless the user explicitly re-approves the new revision in the same message.

## Packet Quality Bar

Before handoff, the packet must satisfy:

- The intended outcome is clear.
- Scope is bounded.
- Constraints are explicit.
- Context is minimal but sufficient.
- Assumptions are visible.
- Unresolved decisions are surfaced.
- Confidence is stated with a reason.
- Approval status is explicit.
- The packet is usable without implementer guesswork.

A packet that fails any of these requires refinement or escalation — it does not proceed.

Output shape: the final packet ends in a complete schema-shaped artifact, not a loose prose summary. Unresolved items are separated clearly from settled portions. Unresolved design questions are not silently converted into implied defaults.
