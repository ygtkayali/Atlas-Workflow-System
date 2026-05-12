# Clarified Context Handoff Schema

Status: [[Tags/status-settled]]
Parent: [[Main Hubs/Workflow Schemas Hub]]
Related: [[clarify-intent]], [[note-manager]], [[note-ready-handoff]]
Created: 2026-04-24
Last Reviewed: 2026-05-06
Source: [[LLM Wiki Lossy Compression and Integrity Risks]]
Decisions: Rename `Source Context` to `Interpretation Basis` so handoffs preserve origin, interpretation, tone, inference boundaries, and validation targets.
Dependencies:
Tasks:

---

## Purpose

This schema defines the minimum structure for the clarified context artifact produced by `clarify-intent`.

The clarified context handoff preserves the result of clarification without designing the durable note.
It exists to give `Note Manager` enough settled context to decide whether to create or update notes, which note type to use, which target note should change, and what exact content should be drafted.
It may clarify either user intent from ideation or implementation-backed context from review/sync.

A clarified context handoff may preserve one durable subject or multiple durable subjects.
When multiple subjects are present, the handoff should separate them by semantic coherence, not by expected target note.
Subject-to-note mapping belongs to `Note Manager`.

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
- task id when the handoff opens or continues a serialized task lane
- task status when the handoff is stored in `docs/In-flight/`
- created date
- related idea, request, feature, or note if known

### 2. Clarified Subject / Subjects
- the subject or subjects that survived clarification in compact form
- enough context to distinguish each subject from the original rough idea when needed
- when multiple subjects are present, each subject should have a stable label or id
- each subject should keep its own relevant facts, affected files or evidence, decisions, uncertainty, and boundaries

### 3. Interpretation Basis
- origin type, such as user prompt, fleeting note, source material, prior note, implementation report, review finding, or mixed context
- original input or upstream artifact, such as exact prompt text, note path, packet, report, review context, source excerpt, or redacted equivalent
- relevant context used during clarification, including user-supplied note paths, retrieval results, source material, implementation artifacts, or workflow constraints
- interpreted intent and the tone or stance that downstream note work should preserve
- claims treated as user intent versus claims treated as agent inference
- open ambiguity and things downstream roles should not imply
- validation target for downstream review, especially what intent, tone, uncertainty, or inference boundary should be checked later

### 4. User Goal
- the outcome the user is trying to achieve
- why this subject matters now if known

### 5. Decided
- decisions worth preserving from clarification
- narrowed scope or direction that should not be silently broadened later

### 6. Proposed
- optional direction that seems plausible but is not yet durable fact
- options that `Note Manager` may consider without treating them as binding structure

### 7. Unclear / Blocked
- unresolved questions that may remain visible in the downstream note action
- missing information that should return the work to clarification if it would force note-structure guesswork

### 8. Boundaries / Non-goals
- adjacent areas that should not be folded into `Note Manager` by default
- limits on what the next note action should try to capture

### 9. Relevant Context Already Known
- specific user-supplied note paths, related notes, or known constraints
- context the user has already provided that `Note Manager` may use

### 10. Readiness For Note Manager
- whether to continue clarification, proceed to `Note Manager`, or defer
- why the current state is or is not ready for bounded note work

## Status Semantics

### `draft`
Relevant clarification state has been captured, but the subject is still rough or incomplete.

### `needs_clarification`
Important uncertainty, contradiction, or missing decisions would force `Note Manager` to guess through durable subject, note type, target note, or note placement.

### `ready_for_note_manager`
The clarified subject is stable enough that `Note Manager` can decide a bounded create or update action from the handoff and the user-supplied note context.

## Task Lane Fields

When a handoff is written to `docs/In-flight/`, include:

- `Task ID`: a stable slug shared by the handoff, packet, report, review summary, and archive summary for the same lane
- `Task Status`: one of the task lane status labels from `modes/dev-workflow/docs/vocabulary.md`

Use `Task Status: intake` when the handoff opens important work and no downstream execution artifact exists yet.
Use `Task Status: settled` only when the handoff itself is the stable artifact being sent to review or closeout.
Do not use durable note status tags as a substitute for task lane status.

## Role Boundary

The clarified context handoff must not:
- create implementation files,
- create implementation packets,
- approve work,
- draft final durable note content,
- decide note type as a binding instruction,
- decide target note or placement when the target is unclear,
- split subjects by target note, note type, or final note action,
- decide subject-to-note mapping,
- or act as a substitute for `Note Manager`.

The clarified context handoff may:
- preserve the clarified idea state or implementation-backed review context for durable note work,
- challenge weak assumptions,
- preserve surfaced inconsistencies and important uncertainty,
- narrow scope,
- separate goals from proposed solutions,
- separate decided, proposed, unclear, and blocked points,
- and recommend whether `Note Manager` is the right next step.

## Handoff Quality Bar

Before handoff, check:
- Is the clarified subject clear?
- Is the interpretation basis explicit enough to validate the handoff against its origin?
- Is the original input or upstream artifact preserved, linked, excerpted, or redacted intentionally?
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
- Task ID: <stable-task-slug>
- Task Status: <intake | planned | in_progress | settled | closed | blocked>
- Related to: <idea / request / feature / note>
- Created: YYYY-MM-DD

## Clarified Subject / Subjects

## Interpretation Basis

## User Goal

## Decided

## Proposed

## Unclear / Blocked

## Boundaries / Non-goals

## Relevant Context Already Known

## Readiness For Note Manager
```
