# Note-Ready Handoff Schema

Status: draft
Parent: [[Workflow Schemas Hub]]
Related: [[implementation-report-schema]], [[project-vault-phase-1-roadmap]], [[clarify-intent]], [[note-creation]]
Created: 2026-04-14
Last Reviewed:
Source:
Decisions:
Dependencies:
Tasks:

---

## Purpose

This schema defines the minimum structure for a note-ready handoff produced by `clarify-intent` before durable note creation begins.

The note-ready handoff exists to preserve the clarified idea state once the subject is strong enough for bounded note work.
It is the default successful output of clarification in this repository's Phase 1 workflow.
It exists to support note creation, not planner handoff.
It is not an implementation packet and it must not be treated as approval to implement.

The handoff should make it clear whether note creation should:
- create a new note,
- update an existing note,
- consider a broader organizing note such as a `Sub Hub`,
- or return to clarification because the durable subject is still weak.

---

## Required Sections

### 1. Header
- handoff title
- artifact type: `note-ready-handoff`
- status: `draft`, `needs_clarification`, or `ready_for_note_creation`
- created date
- related idea, request, feature, or note if known

### 2. Idea Summary
- the surviving idea in compact form
- enough context to distinguish the current clarified direction from the original rough idea when needed

### 3. User Goal
- the outcome the user is trying to achieve
- why this subject matters now if known

### 4. Confident Decisions
- decisions worth preserving from clarification
- narrowed scope or direction that should not be silently broadened later

### 5. Boundaries / Non-goals
- adjacent areas that should not be folded into note creation by default
- limits on what the next note action should try to capture

### 6. Open Questions
- unresolved questions that may remain visible in the note
- missing information that does not yet justify another clarification loop

### 7. Candidate Note Actions
- likely next action such as `create idea note`, `create general note`, `update existing note`, or `consider sub hub`
- any note-type uncertainty that note creation must handle explicitly rather than guess through

### 8. Provided Context Needed For Note Creation
- the notes or note paths that should be supplied to `note-creation`
- any required parent or related-note context already known

### 9. Recommended Next Step
- whether to continue clarification, proceed to note creation, or defer
- why the current state is or is not ready for bounded note work

---

## Status Semantics

### `draft`
Relevant clarification state has been captured, but the subject is still rough or incomplete.

### `needs_clarification`
Important uncertainty, contradiction, or missing decisions would force note creation to guess through durable subject, note type, or note placement.

### `ready_for_note_creation`
The clarified subject is stable enough that `note-creation` can draft a bounded create or update action without silently deciding major intent.

---

## Role Boundary

The note-ready handoff must not:
- create implementation files,
- create implementation packets,
- approve work,
- decide durable note placement when the target is unclear,
- or act as a substitute for planner output.

The note-ready handoff may:
- preserve the clarified idea state for durable note work,
- challenge weak assumptions,
- preserve surfaced inconsistencies and important uncertainty,
- narrow scope,
- separate goals from non-goals,
- record confident decisions worth preserving,
- and recommend the next note-creation step.

---

## Handoff Quality Bar

Before handoff, check:
- Is the idea summary clear?
- Is the user goal distinct from the proposed solution shape?
- Are the confident decisions explicit?
- Are boundaries or non-goals visible?
- Are unresolved questions separated from settled points?
- Is the candidate note action explicit?
- Is it clear which note context needs to be provided next?
- Is note creation happening only because the subject is actually durable enough?
- Is status accurate?

If any answer is no, refine the handoff or mark it `needs_clarification`.

---

## Minimal Handoff Template

```md
# <Handoff Title>

- Type: note-ready-handoff
- Status: <draft | needs_clarification | ready_for_note_creation>
- Related to: <idea / request / feature / note>
- Created: YYYY-MM-DD

## Idea Summary

## User Goal

## Confident Decisions

## Boundaries / Non-goals

## Open Questions

## Candidate Note Actions

## Provided Context Needed For Note Creation

## Recommended Next Step
```
