# Note-Ready Handoff Schema

Status: [[status-archived]]
Parent: [[Workflow Schemas Hub]]
Related: [[clarified-context-handoff]], [[implementation-report-schema]]
Created: 2026-04-14
Last Reviewed: 2026-04-24
Source:
Decisions:
Dependencies:
Tasks:

---

## Purpose

This schema is retained as a legacy note-change handoff reference.

It is no longer the default successful output of `clarify-intent`.
For Phase 1 clarification, use [[clarified-context-handoff]].
It is also no longer the active review/sync handoff path.
For post-implementation documentation sync, route review/sync context through `clarify-intent` and use [[clarified-context-handoff]] before `Note Manager`.

The note-ready handoff previously existed to propose or carry a bounded durable note change when an upstream role already had enough context to identify the note mutation.
It is kept for historical compatibility, not as the current handoff contract.
It is not an implementation packet and it must not be treated as approval to implement.

The handoff should make it clear what durable note change is being proposed and what evidence or accepted review context supports it.
`Note Manager` still evaluates and drafts the final bounded note action.

---

## Required Sections

### 1. Header
- handoff title
- artifact type: `note-ready-handoff`
- status: `draft`, `needs_clarification`, or `ready_for_note_manager`
- created date
- related idea, request, feature, or note if known

### 2. Proposed Durable Note Change
- the bounded durable note change being proposed
- whether the proposal is a create, update, or explicit request for `Note Manager` judgment

### 3. Basis
- the accepted implementation, review outcome, decision, or other upstream basis for the proposed note change
- why the durable documentation should change now

### 4. Settled Context
- facts, decisions, or implementation results worth preserving
- scope that should not be silently broadened later

### 5. Boundaries / Non-goals
- adjacent areas that should not be folded into `Note Manager` by default
- limits on what the next note action should try to capture

### 6. Open Questions
- unresolved questions that may remain visible in the note
- missing information that `Note Manager` must not guess through

### 7. Note Action Context
- likely note mutation if already known from review or accepted implementation context
- any target-note, note-type, or placement uncertainty that `Note Manager` must handle explicitly rather than guess through

### 8. Provided Context For Note Manager
- the notes or note paths that should be supplied to `note-manager`
- any required parent or related-note context already known

### 9. Recommended Next Step
- whether to continue clarification, proceed to `Note Manager`, or defer
- why the current state is or is not ready for bounded note work

---

## Status Semantics

### `draft`
Relevant clarification state has been captured, but the subject is still rough or incomplete.

### `needs_clarification`
Important uncertainty, contradiction, or missing decisions would force `Note Manager` to guess through durable subject, note type, target note, or note placement.

### `ready_for_note_manager`
The upstream note-change context is stable enough that `Note Manager` can draft a bounded create or update action without silently deciding major intent.

---

## Role Boundary

The note-ready handoff must not:
- create implementation files,
- create implementation packets,
- approve work,
- decide durable note placement when the target is unclear,
- or act as a substitute for planner output.

For clarification-stage or review-sync work, this artifact must not replace [[clarified-context-handoff]] or push note-structure decisions outside the current clarification path.

The note-ready handoff may:
- preserve old note-change context for historical reference,
- help migrate older artifacts into [[clarified-context-handoff]],
- and explain why older workflow notes may still mention `note-ready-handoff`.

---

## Handoff Quality Bar

Before handoff, check:
- Is the proposed durable note change clear?
- Is the upstream basis explicit?
- Is settled context explicit?
- Are boundaries or non-goals visible?
- Are unresolved questions separated from settled points?
- Is the note action context explicit without replacing `Note Manager`?
- Is it clear which note context needs to be provided next?
- Is `Note Manager` happening only because the subject is actually durable enough?
- Is status accurate?

If any answer is no, refine the handoff or mark it `needs_clarification`.

---

## Minimal Handoff Template

```md
# <Handoff Title>

- Type: note-ready-handoff
- Status: <draft | needs_clarification | ready_for_note_manager>
- Related to: <idea / request / feature / note>
- Created: YYYY-MM-DD

## Proposed Durable Note Change

## Basis

## Settled Context

## Boundaries / Non-goals

## Open Questions

## Note Action Context

## Provided Context For Note Manager

## Recommended Next Step
```
