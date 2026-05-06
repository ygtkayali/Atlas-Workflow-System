# Clarify Intent

Status: [[status-settled]]
Parent: [[Agent Roles Hub]]
Related: [[clarified-context-handoff]], [[note-manager]], [[Two-Phase Workflow Boundary]]
Created: 2026-04-14
Last Reviewed: 2026-05-06
Source: [[LLM Wiki Lossy Compression and Integrity Risks]]
Decisions: Clarified context handoffs use `Interpretation Basis` to preserve original input, interpreted intent, tone, inference boundaries, and downstream validation targets.
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
- preserve the interpretation basis for downstream handoffs, including original input or artifact, interpreted intent, tone or stance, user-intent claims, agent-inference claims, open ambiguity, things not to imply, and validation target
- separate implementation facts from review/sync proposals when the upstream source is post-implementation review
- split complex prompts into provisional subject bundles before downstream work
- expose ambiguity, assumptions, and missing decisions
- challenge weak or premature solution framing
- ask or answer the highest-value clarification points first instead of repeatedly restating the whole handoff
- use bounded note context through `note-search` when a known seed note, semantic query, or local retrieval anchor can materially improve clarification
- prefer semantic `note-search` over manual broad note discovery when the prompt asks whether something exists, asks for similar notes, or gives only a concept
- keep work in clarification when high-impact uncertainty remains
- produce a structured clarified context artifact only when downstream note work is the right next step and will not require guesswork
- when upstream context contains multiple possible durable subjects, separate them by semantic subject rather than by target note or note action
- preserve each subject's relevant facts, affected files or evidence, decisions, uncertainty, and boundaries so `Note Manager` can map subjects to note actions later
- separate `decided`, `proposed`, `unclear`, and `blocked` points so downstream note work does not have to infer them from chat

## Expected Output

`clarify-intent` has three valid output modes:

- `continue_clarification`: keep clarifying with updated questions, corrections, inconsistencies, or context-aware guidance
- `end_clarification`: state that the idea is clear enough for the current purpose and recommend the next relevant action
- `note_ready_handoff`: produce a [[clarified-context-handoff]] when the next step is [[note-manager]]

The downstream-ready output in this repository is a [[clarified-context-handoff]].
Clarification should not repeatedly output the full handoff on every turn when the useful next step is a smaller question, correction, or updated understanding.

That handoff should preserve:
- clarified subject
- provisional subject bundles when the source prompt was complex
- interpretation basis, including origin type, original input or artifact, relevant context used, interpreted intent, tone or stance to preserve, user-intent claims, agent-inference claims, open ambiguity, things not to imply, and validation target
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
Those decisions belong to [[note-manager]].

For idea capture, confidence may mean that the important uncertainty is clearly preserved rather than resolved.
For architecture, workflow, schema, API, dependency, security, privacy, or public-interface decisions, confidence requires stronger resolution before downstream handoff.

## Complex Prompt Intake

When a prompt contains multiple domains, areas, or branching ideas, `clarify-intent` should split it into provisional subject bundles before downstream work.

Each bundle should contain one domain or area.
Branching ideas inside one area may stay together only when they are closely related.
If a branch can become its own durable subject, split it and preserve the connection instead of blending it into a broader handoff.

This bundle split is an intake and clarification tool, not final durable note structure.

## Boundaries

`clarify-intent` should not:
- create durable notes directly
- draft final durable note content
- move to [[note-manager]] before producing a visible clarified context handoff and showing it to the user
- decide note type, target note, title, final links, or durable note placement as binding output
- split context by target note, note type, or final note action
- decide subject-to-note mapping
- decide whether a reviewed implementation should be kept, revised, or rejected
- create planning packets
- approve implementation work
- silently decide architecture, workflow, schema, or note-placement choices for the user
- satisfy a downstream gate through private reasoning only

## Next Step

When clarification succeeds and durable note work is appropriate, the normal next step is [[note-manager]] with the clarified context handoff plus the specific relevant notes supplied by the user.
When a durable note change is required, the default flow is to call [[note-manager]] immediately after the visible handoff is ready and the relevant note context has been supplied.
Do not wait for a separate user approval merely to switch phases.
The approval gate belongs to the resulting [[note-manager]] draft or durable-write decision.
For post-implementation documentation sync, [[review-agent]] supplies implementation-backed context first; `clarify-intent` then produces the clarified context handoff for [[note-manager]].
