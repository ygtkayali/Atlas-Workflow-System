# Clarified Context Handoff Schema

Status: [[status-settled]]
Parent: [[Workflow Schemas Hub]]
Related: [[clarify-intent]], [[Note Manager]], [[note-ready-handoff]]
Created: 2026-04-24
Last Reviewed: 2026-04-24
Source:
Decisions:
Dependencies:
Tasks:

---

## Purpose

This schema defines the minimum structure for the clarified context artifact produced by `clarify-intent`.

The clarified context handoff preserves the result of clarification without designing the durable note.
It exists to give `Note Manager` enough settled context to decide whether to create or update notes, which note type to use, which target note should change, and what exact content should be drafted.

It is not:
- a durable note draft,
- a note structure proposal,
- a planning brief,
- an implementation packet,
- or approval to implement.

## Required Sections

### 1. Header
- handoff title
- artifact type: `clarified-context-handoff`
- status: `draft`, `needs_clarification`, or `ready_for_note_manager`
- created date
- related idea, request, feature, or note if known

### 2. Clarified Subject
- the subject that survived clarification in compact form
- enough context to distinguish it from the original rough idea when needed

### 3. User Goal
- the outcome the user is trying to achieve
- why this subject matters now if known

### 4. Decided
- decisions worth preserving from clarification
- narrowed scope or direction that should not be silently broadened later

### 5. Proposed
- optional direction that seems plausible but is not yet durable fact
- options that `Note Manager` may consider without treating them as binding structure

### 6. Unclear / Blocked
- unresolved questions that may remain visible in the downstream note action
- missing information that should return the work to clarification if it would force note-structure guesswork

### 7. Boundaries / Non-goals
- adjacent areas that should not be folded into `Note Manager` by default
- limits on what the next note action should try to capture

### 8. Relevant Context Already Known
- specific user-supplied note paths, related notes, or known constraints
- context the user has already provided that `Note Manager` may use

### 9. Readiness For Note Manager
- whether to continue clarification, proceed to `Note Manager`, or defer
- why the current state is or is not ready for bounded note work

## Status Semantics

### `draft`
Relevant clarification state has been captured, but the subject is still rough or incomplete.

### `needs_clarification`
Important uncertainty, contradiction, or missing decisions would force `Note Manager` to guess through durable subject, note type, target note, or note placement.

### `ready_for_note_manager`
The clarified subject is stable enough that `Note Manager` can decide a bounded create or update action from the handoff and the user-supplied note context.

## Role Boundary

The clarified context handoff must not:
- create implementation files,
- create implementation packets,
- approve work,
- draft final durable note content,
- decide note type as a binding instruction,
- decide target note or placement when the target is unclear,
- or act as a substitute for `Note Manager`.

The clarified context handoff may:
- preserve the clarified idea state for durable note work,
- challenge weak assumptions,
- preserve surfaced inconsistencies and important uncertainty,
- narrow scope,
- separate goals from proposed solutions,
- separate decided, proposed, unclear, and blocked points,
- and recommend whether `Note Manager` is the right next step.

## Handoff Quality Bar

Before handoff, check:
- Is the clarified subject clear?
- Is the user goal distinct from the proposed solution shape?
- Are decided points separate from proposed or unclear points?
- Are boundaries or non-goals visible?
- Is unresolved uncertainty separated from settled context?
- Is known relevant note context listed without designing the note action?
- Is `Note Manager` happening only because the subject is actually durable enough?
- Is status accurate?

If any answer is no, refine the handoff or mark it `needs_clarification`.

## Minimal Handoff Template

```md
# <Handoff Title>

- Type: clarified-context-handoff
- Status: <draft | needs_clarification | ready_for_note_manager>
- Related to: <idea / request / feature / note>
- Created: YYYY-MM-DD

## Clarified Subject

## User Goal

## Decided

## Proposed

## Unclear / Blocked

## Boundaries / Non-goals

## Relevant Context Already Known

## Readiness For Note Manager
```
