# Task Packet Schema

Status: [[Tags/status-settled]]
Parent: [[Main Hubs/Workflow Schemas Hub]]
Related: [[note-ready-handoff]], [[implementation-report-schema]], [[planner-agent]]
Created: 2026-04-14
Last Reviewed:
Source:
Decisions:
Dependencies:
Tasks:

---

## Purpose

This schema defines the minimum structure for an implementation task packet prepared by the planner for human approval before coding begins.

The task packet exists to turn note-backed project state into a bounded execution artifact that an implementer can act on without guessing through core intent, scope, or constraint boundaries.
It should also be usable by an external implementer that does not have planning-vault context beyond what the packet explicitly names.

It is not approval by itself.
Implementation must not begin until the current packet revision is explicitly approved by the human.

---

## Required Sections

### 1. Header
- packet title
- artifact type: `task-packet`
- status: `draft`, `approval_pending`, `approved`, or `blocked`
- created date
- related feature, task, request, or note if known
- packet revision if revisions are being tracked

### 2. Objective
- the specific outcome the implementation should achieve
- why this work is being done now if known

### 3. Scope
- what is in scope
- the bounded area the implementer is allowed to change

### 4. Non-goals
- related work that should not be folded into this packet
- areas intentionally excluded even if nearby

### 5. Relevant Context
- the minimum note or code context needed to implement safely
- only the files, directories, components, tests, or artifacts the implementer is allowed to inspect
- linked documentation the implementer should read first, if any

### 6. Allowed Implementation Area
- the exact files or bounded directories the implementer may edit
- any files that may be read but not changed
- whether discovery beyond the listed context is prohibited

### 7. Constraints
- product, architectural, technical, security, workflow, or approval constraints
- documented rules that limit how the change should be executed

### 8. Acceptance Criteria
- concrete conditions that determine whether the task is complete
- expected behavior or outputs

### 9. Verification Expectations
- exact tests, commands, or validation steps the implementer should run when known
- any verification limitation already accepted at planning time

### 10. Risks / Open Questions
- unresolved items still visible at planning time
- risks the implementer should preserve or escalate rather than silently resolve

### 11. Assumptions
- planning assumptions that remain visible to the implementer
- assumptions that should trigger escalation if code reality differs

### 12. Confidence Assessment
- planner confidence level
- short explanation of why confidence is high, medium, low, or mixed

### 13. Approval Status
- explicit state of approval
- evidence of approval when approved
- any remaining decision needed before implementation can begin

---

## Recommended Optional Sections
- dependencies
- rollout or migration notes
- documentation impact
- follow-up candidates

---

## Status Semantics

### `draft`
The packet exists, but planning is still incomplete or the packet is not ready for review.

### `approval_pending`
The packet is complete enough for human review, but implementation must not begin yet.

### `approved`
The human has explicitly approved this exact packet revision for implementation.

### `blocked`
The packet cannot proceed because an unresolved issue, missing note, or required decision still prevents safe implementation.

---

## Approval Rules

- Approval must be explicit.
- Approval applies to the current packet revision, not to the general idea.
- If the packet changes materially after approval, it should return to `approval_pending` unless the user explicitly re-approves the new revision.
- The implementer should stop and escalate if approval evidence is unclear.

---

## Packet Quality Bar

Before handoff, check:
- Is the objective specific?
- Is scope bounded?
- Are non-goals visible?
- Is the context set minimal but sufficient?
- Is the allowed implementation area explicit?
- Are constraints explicit?
- Are acceptance criteria concrete?
- Are verification expectations concrete?
- Are risks or open questions surfaced?
- Is confidence stated with a reason?
- Is approval status explicit?

If any answer is no, refine the packet or escalate.

---

## Minimal Packet Template

```md
# <Task Packet Title>

- Type: task-packet
- Status: <draft | approval_pending | approved | blocked>
- Related to: <feature / task / request / note>
- Revision: <v1>
- Created: YYYY-MM-DD

## Objective

## Scope

## Non-goals

## Relevant Context

## Allowed Implementation Area

## Constraints

## Acceptance Criteria

## Verification Expectations

## Risks / Open Questions

## Assumptions

## Confidence Assessment

## Approval Status
```
