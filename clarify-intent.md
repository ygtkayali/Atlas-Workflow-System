# Clarify Intent

Status: [[status-settled]]
Parent: [[Agent Roles Hub]]
Related: [[clarified-context-handoff]], [[Note Manager]], [[Two-Phase Workflow Boundary]]
Created: 2026-04-14
Last Reviewed: 2026-04-24
Source:
Decisions:
Dependencies:
Tasks:

---

## Summary

`clarify-intent` is the workflow context-clarification skill.

Its first job is to strengthen an idea-shaped request until the goal, problem shape, boundaries, and major uncertainties are clear enough for bounded durable note work.
Its second job is to clarify implementation-backed context from review/sync before durable note mutation.
It is a guided clarification and challenge loop, not a planner.
It preserves clarified context; it does not design durable note structure.

## Responsibilities

- separate user goals from proposed solutions
- separate implementation facts from review/sync proposals when the upstream source is post-implementation review
- expose ambiguity, assumptions, and missing decisions
- challenge weak or premature solution framing
- keep work in clarification when high-impact uncertainty remains
- produce a structured clarified context artifact only when downstream note work will not require guesswork
- when upstream context contains multiple possible durable subjects, separate them by semantic subject rather than by target note or note action
- preserve each subject's relevant facts, affected files or evidence, decisions, uncertainty, and boundaries so `Note Manager` can map subjects to note actions later
- separate `decided`, `proposed`, `unclear`, and `blocked` points so downstream note work does not have to infer them from chat

## Expected Output

The default successful output in this repository is a [[clarified-context-handoff]].

That handoff should preserve:
- clarified subject
- user goal
- decided points
- proposed but unsettled direction
- unclear or blocked points
- boundaries or non-goals
- relevant context already known from the user or supplied notes
- recommended next step
- status

When a handoff contains multiple durable subjects, `clarify-intent` should label each subject separately and keep the relevant context attached to that subject.

A durable subject is one coherent piece of project knowledge, decision, workflow rule, or implementation-backed fact that could be preserved independently.

It should not choose note type, target note, title, final links, or durable note structure as binding output.
Those decisions belong to [[Note Manager]].

## Boundaries

`clarify-intent` should not:
- create durable notes directly
- draft final durable note content
- move to [[Note Manager]] before producing a visible clarified context handoff, showing it to the user, and receiving approval to switch phases
- decide note type, target note, title, final links, or durable note placement as binding output
- split context by target note, note type, or final note action
- decide subject-to-note mapping
- decide whether a reviewed implementation should be kept, revised, or rejected
- create planning packets
- approve implementation work
- silently decide architecture, workflow, schema, or note-placement choices for the user

## Next Step

When clarification succeeds, the normal next step is [[Note Manager]] with the clarified context handoff plus the specific relevant notes supplied by the user.
For post-implementation documentation sync, [[review-agent]] supplies implementation-backed context first; `clarify-intent` then produces the clarified context handoff for [[Note Manager]].
