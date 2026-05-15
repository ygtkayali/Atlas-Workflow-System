# Clarify Intent Output Modes

Status: [[Tags/status-draft]]
Type: [[design-note]]
Parent: [[clarify-intent]]
Related: [[Two-Phase Clarification Architecture]], [[Interpretation Basis]], [[clarify-intent]]
Created: 2026-05-15
Last Reviewed: 2026-05-15
Decisions: Private reasoning does not satisfy a gate. Clarification state or handoff must be visible before downstream work begins. Iteration cap is three full loops; partial_clarification is the only valid response after the cap.
Source: modes/dev-workflow/skills/dw-clarify-intent/SKILL.md
Dependencies:
Tasks:

---

## Design

`dw-clarify-intent` chooses exactly one output mode per turn. The mode determines whether the turn continues clarification, ends it, produces a handoff artifact, or issues a structured pause. Each mode carries a distinct commitment.

## Modes

### continue_clarification

Used when the loop should continue. Provides the current state plus the next highest-value questions. Does not repeat the full handoff every turn unless the state has materially changed or the user asks — repetition makes the loop unworkable in practice.

### end_clarification

Used when the idea is clear enough for the current purpose but the next step is not necessarily note-manager. States the clarified result and recommends the next relevant action: note creation, planning, review, no durable action, or a user decision. End does not require a handoff.

### note_ready_handoff

Enters Phase 2. Produces the clarified-context handoff as an approval-pending artifact under `docs/In-flight/`. The handoff must be visible in the conversation or as an approved workflow artifact — private reasoning does not satisfy this gate.

### partial_clarification

Issued after the iteration cap is reached: three full loop iterations on the same subject without reaching `ready_for_note_manager`. The skill stops iterating and produces a structured summary containing:
- what is settled,
- what is still blocking progress,
- explicit options: defer / narrow scope / escalate / abandon.

The skill then waits for the user to direct the next move. `partial_clarification` is the only valid response after the cap — not another clarification turn, and not a premature handoff that normalizes remaining uncertainty.

## Iteration Cap Design

The cap prevents indefinite cycling on subjects that cannot progress without a human decision. Without it, the skill can appear productive while repeating the same questions in slightly different forms. The structured pause forces the blocking issue into the open.

## Private Reasoning Rule

No output mode is satisfied by private reasoning. This applies most critically to `note_ready_handoff`: the handoff artifact must exist and be readable before any downstream skill is invoked.
