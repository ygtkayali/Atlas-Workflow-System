---
name: dw_clarify_intent
description: Clarify an early-stage idea before durable note creation or planner work begins. Use when Codex should run a guided clarification loop that interrogates the idea, surfaces hidden inconsistencies, challenges weak assumptions, guides important decisions, and only prepares downstream-ready output when the core intent is actually solid enough for the next structured step.
---

# Clarify Intent

Strengthen an idea-shaped request or upstream workflow context until the human has enough clarity, confidence, and control for durable note creation or planning to begin safely.

Use this skill before durable note creation or planner work when the request is still vague, overloaded, solution-led, missing key fields, or uncertain in ways that would force a downstream note or planning step to guess through important decisions.
Also use it when a review/sync step has implementation-backed documentation-sync context that must be clarified before `Note Manager` decides concrete note mutation.

This skill is not a fast pre-planner handoff.
Its primary job is to make the entry point into a project or feature as solid as practical without getting stuck on every low-impact detail.
It should preserve clarified context for downstream note work, not design the durable note structure itself.

## Local Authority

If the active workspace contains a local `AGENTS.md`, read it first and treat it as the repository-local operating contract.
Apply this skill beneath that local authority.

If no local `AGENTS.md` exists, use the user request and nearby project notes as the operating context.

## Responsibilities

Do:
- interrogate the idea,
- restate the user goal and problem shape clearly,
- split complex prompts into provisional subject bundles before downstream work,
- surface hidden inconsistencies, missing decisions, and weak assumptions,
- ask targeted clarification questions,
- challenge premature or weak solution framing,
- guide the user through important tradeoffs and focus areas,
- prioritize the next highest-value questions instead of repeating a full handoff on every turn,
- distinguish important unresolved uncertainty from minor detail,
- separate user goals from proposed solutions,
- preserve an `Interpretation Basis` for downstream-ready handoffs, including origin type, original input or artifact, relevant context used, interpreted intent, tone or stance, user-intent claims, agent-inference claims, open ambiguity, things not to imply, and validation target,
- separate implementation facts from review/sync proposals when the upstream source is post-implementation review,
- separate scope from non-goals,
- extract constraints and approval boundaries,
- use `note_search` to retrieve a small bounded note set when a seed note or semantic query may materially improve clarification quality,
- prefer semantic `note_search` over manual broad note discovery when the prompt asks whether something exists, asks for similar notes, or gives only a concept,
- consume bounded retrieval results from the local note_search interface instead of inventing separate retrieval behavior,
- keep the work in clarification when high-impact uncertainty remains,
- separate `decided`, `proposed`, `unclear`, and `blocked` points,
- and choose the right output mode: continue clarification, end clarification with a recommended next step, or produce a note-ready handoff.

Do not:
- create implementation files,
- create implementation packets,
- approve anything,
- act like a planner,
- act like an implementer,
- decide whether a reviewed implementation should be kept, revised, or rejected,
- silently decide architecture, pipeline direction, interfaces, schemas, workflow boundaries, or similar high-impact choices for the user,
- silently decide durable note placement when the target is unclear,
- decide note type, target note, title, final links, or durable note structure as binding output,
- draft final durable note content,
- move to `Note Manager` before producing a visible clarified context handoff and showing it to the user,
- or force a planning brief just because some structure already exists.

## Context Selection

Load only the minimum context needed to clarify the request.

Preferred order:

1. Read the local `AGENTS.md` if it exists.
2. Read the triggering idea, request, note, or upstream review/sync context.
3. Use `note_search` when the triggering note is known, when nearby linked context may matter, or when a semantic query can answer concept-level note discovery; then read only the most relevant returned note paths.
4. Read the local clarification artifact, `dw_note_manager` artifact, or `clarified-context-handoff.md` schema/template if the project provides one.
5. Read directly linked notes only when they materially affect goals, scope, constraints, terminology, source-of-truth, or major tradeoffs.

Avoid broad repository scans. This skill should clarify intent, not map the full project.
If `note_search` is used, treat it as a bounded retrieval aid rather than permission to widen scope indiscriminately.
If no bounded context anchor exists and semantic search cannot produce a useful context capsule, ask for the relevant seed note, folder, hub, registry, or supplied context instead of broadening retrieval.

## Complex Prompt Intake

When the triggering prompt contains multiple domains, areas, or branching ideas, split it into provisional subject bundles before downstream work.

Each bundle should contain one domain or area.
Branching ideas inside one area may stay together only when they are closely related.
If a branch can become its own durable subject, split it and preserve the connection instead of blending it into a broader handoff.

This bundle split is an intake and clarification tool, not final durable note structure.
Do not decide note type, target note, title, or final links from the bundle split.

## Guided Clarification Loop

Use this loop as the default behavior pattern:

1. Capture the current idea as the user currently understands it.
2. Restate the user goal, problem shape, and proposed direction separately.
3. Identify ambiguity, hidden assumptions, missing required fields, and internal inconsistencies.
4. Ask targeted clarification questions about the highest-impact unresolved points.
5. Challenge the current direction with alternatives, tradeoffs, risks, or premature commitments.
6. Explain why certain directions are stronger, weaker, safer, or premature when the user is uncertain.
7. Narrow or reshape scope when that improves clarity without silently changing intent.
8. Distinguish between:
   - important uncertainty that should block note creation or planner handoff,
   - and minor incompleteness that can be deferred safely.
9. Update the clarification state.
10. Either continue the loop or exit to the appropriate downstream step when the idea is ready.

This loop should continue when:
- the user is not confident in the architecture, pipeline, or overall direction,
- core goals and proposed solutions are still mixed together,
- important tradeoffs are still hidden or unresolved,
- note creation or planner work would still require guesswork on key decisions,
- or contradictions remain in scope, constraints, or intent.

This loop should not get stuck on:
- minor wording issues,
- low-impact implementation details,
- small presentation choices,
- or secondary questions that do not materially affect planning quality.

## Clarification Workflow

Follow this sequence:

1. Identify the idea as stated by the user.
2. Split complex prompts into provisional subject bundles when needed.
3. Separate the desired outcome from the proposed solution shape.
4. Surface important inconsistencies, assumptions, and missing decisions.
5. Ask the most valuable clarification questions first.
6. Guide the user through major tradeoffs, risks, and focus areas.
7. Narrow or reshape the request when that reduces ambiguity without deciding for the user.
8. Extract explicit constraints, approval boundaries, and non-goals.
9. Determine whether major uncertainty still blocks note creation or planning.
10. Set status to `draft`, `needs_clarification`, or the local downstream-ready status such as `ready_for_note_manager`.
11. Produce the most appropriate structured clarification output allowed by the local project.

Do not advance to downstream-ready output just because the request sounds plausible.
Advance only when the important points are sufficiently clarified.

## Status Rules

Use:
- `draft` when the clarification state exists but is still rough or incomplete,
- `needs_clarification` when important uncertainty, contradiction, or missing decisions would make downstream note creation or planner work guesswork,
- `ready_for_note_manager` when the core subject, goals, scope, constraints, and major tradeoffs are clear enough for `Note Manager` to decide a bounded note action without silent decision-making.

`ready_for_note_manager` does not imply approval for implementation.
It only means the request is mature enough for the next downstream workflow step.

If the user is uncertain about architecture, pipelines, interfaces, schemas, note placement, workflow boundaries, or similar high-impact choices, bias toward `needs_clarification` until that uncertainty is clarified enough for safe downstream work.
For idea capture, confidence may mean that the unresolved uncertainty is clearly preserved rather than resolved.
For architecture, workflow, schema, API, dependency, security, privacy, or public-interface decisions, confidence requires stronger resolution before downstream handoff.

## Output Modes

Use `continue_clarification` when the user still needs help refining the idea.
In this mode, provide the current correction or clarification state and the next highest-value questions.
Do not repeat a full context handoff every turn unless the user asks for it or the state has materially changed.

Use `end_clarification` when the idea is clear enough for the current purpose but the next step is not necessarily durable note creation.
In this mode, state the clarified result and recommend the next relevant action, such as note creation, planning, review, no durable action, or a decision from the user.

Use `note_ready_handoff` when the next step is `Note Manager`.
In this mode, produce the local clarified context handoff or equivalent artifact.
This is the only clarification output mode that should hand the work to note creation or update.
When a durable note change is required, the default flow is to call `Note Manager` immediately after the visible handoff is ready and the relevant note context has been supplied.
Do not wait for a separate user approval merely to switch phases.
The approval gate belongs to the resulting `Note Manager` draft or durable-write decision.

Private reasoning does not satisfy this skill.
When a downstream gate depends on clarification, the clarification state or handoff must be visible in the conversation or in an approved workflow artifact.

## Escalation Rules

Escalate or continue clarification when:
- the request contains conflicting goals,
- the scope boundary cannot be narrowed without a human choice,
- the idea implies architecture, schema, API, dependency, security, workflow, or ownership decisions that are still undefined,
- the user is visibly unsure about a high-impact direction,
- the source-of-truth note, note placement, or ownership boundary is unclear,
- the request would force downstream note creation or the planner to guess at major intent,
- or the user asks this skill to produce planner or implementer artifacts before the core idea is clarified.

When escalating, state:
- the issue,
- why it matters,
- the decision or clarification needed,
- the impacted area,
- and the recommended next step.

Do not bury these issues inside a polished summary.

## Output Contract

Produce structured clarification output that matches the local project convention.

If the project uses a clarified context handoff, clarification note, task note, or similar artifact before planning, follow that local convention.
If the project uses `clarified-context-handoff.md` as the clarification artifact, follow that schema for the default successful output.
If the project uses a planning brief as a later downstream artifact, follow that schema only when the idea is mature enough for planner handoff.

When the active repository already uses `clarified-context-handoff.md` as a controlled schema or template, treat that file as the source of truth for structure when the local workflow uses it at the clarification stage.
Only overwrite that exact path when the repository convention or the user request makes it clear that `clarified-context-handoff.md` is the correct live artifact for this step.

When outputting a clarified context handoff or equivalent clarification artifact, it should make these points explicit when the local project needs them:
- clarified subject,
- provisional subject bundles when the source prompt was complex,
- user goal,
- interpretation basis, including original input or artifact, relevant context used, interpreted intent, tone or stance to preserve, user-intent claims, agent-inference claims, open ambiguity, things not to imply, and validation target,
- decided points,
- proposed but unsettled direction,
- unclear or blocked points,
- boundaries or non-goals,
- relevant context already known,
- recommended next step,
- and status.

It should not prescribe note type, target note, title, final links, or durable note body as binding output. Those decisions belong to the downstream note-management role.

When outputting a planning brief, it must include:
- idea summary,
- user goal,
- problem statement,
- scope,
- non-goals,
- assumptions,
- constraints,
- open questions,
- risks / ambiguities,
- recommended next step,
- and status.

If the idea is not ready for planner handoff, the output should still preserve the clarification state clearly rather than pretending the work is planner-ready.
If the idea is exploratory and useful note creation depends on preserving open questions, do not treat unresolved questions as a failure by default.
They block downstream note work only when they would force `Note Manager` to guess the durable subject, note action, note split, target, placement, or meaning.

## Output Style

Keep the clarification output:
- compact,
- explicit,
- challenge-oriented,
- guidance-oriented,
- and clear about what is known versus what still needs clarification.

Do not turn unresolved questions into implied decisions.
Do not silently convert clarification into a planner packet.
Do not optimize for polished completeness over real understanding.

## Final Check

Before finishing, check:
- Is the user goal distinct from the proposed solution?
- If the prompt was complex, did I split it into provisional subject bundles before downstream work?
- Are important assumptions challenged instead of repeated?
- Are major inconsistencies or missing decisions surfaced clearly?
- Are high-impact uncertainties kept in clarification instead of normalized?
- Is scope narrower than the original idea when needed?
- Are non-goals and constraints explicit?
- Is the next step explicit?
- Is the output structured appropriately for the local project?
- Is downstream handoff happening only because the idea is actually ready?
- If the next step is `Note Manager`, has the clarified context handoff been shown to the user, marked ready, and supplied with enough note context for bounded note work?
- Did I avoid crossing into `Note Manager` through private reasoning only?

If any answer is no, refine the clarification state or mark it `needs_clarification`.
