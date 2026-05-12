---
name: dw-clarify-intent
description: Use when a request is vague, overloaded, solution-led, or touches a high-impact area and intent must be solidified before durable note creation or planning begins.
---

# Clarify Intent

Strengthen an idea-shaped request or upstream workflow context until the human has enough clarity, confidence, and control for durable note creation or planning to begin safely.

Use this skill before durable note creation or planner work when the request is still vague, overloaded, solution-led, missing key fields, or uncertain in ways that would force a downstream note or planning step to guess through important decisions.
Also use it when a review/sync step has implementation-backed documentation-sync context that must be clarified before `Note Manager` decides concrete note mutation.

This skill is not a fast pre-planner handoff.
Its primary job is to make the entry point into a project or feature as solid as practical without getting stuck on every low-impact detail.
It preserves clarified context for downstream note work; it does not design the durable note structure itself.
It has two distinct phases: first clarify through simple interaction, then synthesize the clarified state into a handoff only when downstream workflow state needs it.

## Clarification Depth

Choose depth before starting the loop:

- `light` — low-impact, narrow, or already mostly-clear requests. Restate goal in 2-4 lines, ask at most 2 high-value questions, and either end clarification or produce a compact handoff. The full `Interpretation Basis` may be omitted when the origin is the direct user prompt with no hidden context, source material, or upstream artifact being interpreted.
- `full` — ideas that touch any high-impact area (see below) or multi-domain bundles. Use the full guided loop and full `Interpretation Basis`.

If unsure, start `light` and escalate to `full` the moment a high-impact area surfaces.

## High-Impact Uncertainty

Treat any of these as high-impact and bias toward `full` depth and `needs_clarification` status until resolved enough for safe downstream work:

- architecture or pipeline shape,
- schema, API contract, or public interface,
- new dependency with broad reach,
- security, privacy, or auth behavior,
- workflow gates, ownership boundaries, or note governance,
- conflicts with documented constraints.

Minor wording, presentation, or low-impact implementation detail is not high-impact.

## Responsibilities

Do:
- restate the user goal and problem shape separately from any proposed solution,
- split complex prompts into provisional subject bundles before downstream work,
- surface hidden inconsistencies, missing decisions, and weak assumptions,
- ask the highest-value clarification questions first,
- challenge premature solution framing with concrete tradeoffs,
- preserve an `Interpretation Basis` for `note_ready_handoff` output in `full` depth,
- separate `decided`, `proposed`, `unclear`, and `blocked` points,
- use `note-search` for bounded retrieval when a seed note or semantic query materially improves clarification quality,
- choose the right output mode: `continue_clarification`, `end_clarification`, `note_ready_handoff`, or `partial_clarification`.

Do not:
- act as planner, note-manager, or implementer (the router owns those gates),
- silently decide architecture, schemas, interfaces, note placement, or workflow boundaries,
- draft final durable note content or decide note type as binding output,
- move to `Note Manager` without a visible handoff,
- force a planner-shaped artifact when the idea is still raw.

## Required Inputs

Begin from the triggering idea, request, or upstream review/sync context.

If no bounded context anchor exists and `note-search` cannot produce a useful capsule, ask for the relevant seed note, hub, or supplied context instead of broadening retrieval.

## Context Selection

Load only the minimum context needed to clarify the request.

Preferred order:

1. Local `AGENTS.md` if it exists.
2. The triggering idea, request, note, or upstream review/sync context.
3. `note-search` when a seed note is known or a semantic query can answer concept-level discovery; read only the highest-relevance returned paths.
4. `references/clarified-context-handoff.md` only before producing a `note_ready_handoff`.
5. Directly linked notes only when they materially affect goals, scope, constraints, terminology, source-of-truth, or major tradeoffs.

Avoid broad repository scans. Do not map the full project.

## Complex Prompt Intake

When the prompt contains multiple domains, areas, or branching ideas, split it into provisional subject bundles before downstream work.

Each bundle uses this shape:

- `id` — stable short label,
- `label` — human-readable subject name,
- `summary` — 1-2 line description,
- `scope` — what is in / out for this bundle,
- `why-distinct` — why this should not collapse into a neighboring bundle.

A bundle holds one domain or area. Branches inside a bundle stay together only when closely related.
The split is intake evidence, not final note structure; `Note Manager` owns subject-to-note mapping.

## Phase 1: Clarification Loop

Run this loop until the idea is clear enough for the current purpose, ready for handoff creation, or clearly stuck.
This phase is conversational: ask and answer focused questions, approve or disapprove the user's proposed direction, give reasons, challenge weak assumptions, and keep the current state compact.
Do not synthesize a full handoff during this phase unless the user asks or the state is ready to move into Phase 2.

1. Capture the idea as the user currently states it.
2. Restate user goal, problem shape, and proposed direction *separately*.
3. Split into subject bundles when the prompt is multi-domain.
4. Identify ambiguity, hidden assumptions, missing decisions, and inconsistencies — distinguish high-impact from minor.
5. Ask the highest-value questions and challenge weak directions with concrete tradeoffs.
6. Update the clarification state (`decided` / `proposed` / `unclear` / `blocked`).
7. Continue, end, hand off, or mark `partial_clarification`.

### Iteration cap

After three full loop iterations on the same subject without reaching `ready_for_note_manager`, stop iterating freely.
Produce a `partial_clarification` summary that lists what *is* settled, what is still blocking progress, and explicit options (defer / narrow scope / escalate / abandon). Wait for the user to direct the next move.

### Continue when
- the user is unsure about a high-impact direction,
- core goals and proposed solutions are still mixed,
- important tradeoffs are still hidden,
- contradictions remain in scope, constraints, or intent.

### Do not stall on
- minor wording,
- low-impact implementation detail,
- presentation choices,
- secondary questions that would not change the downstream note action.

## Phase 2: Handoff Creation

Create a handoff only after Phase 1 has produced enough settled context for downstream workflow state.
This phase synthesizes the conversation, source context, decisions, unresolved uncertainty, and boundaries into the `references/clarified-context-handoff.md` shape.
It should not introduce new decisions; it records what has been clarified, what remains proposed, what is unclear, and what is blocked.

When creating a reviewable handoff artifact, write it first as an approval-pending artifact under `docs/In-flight/` and report the path and next gate.
Do not use the handoff as implicit permission to continue into implementation or durable note mutation in the same turn.

## Status Rules

Clarification state labels are defined in `vocabulary.md`. Use them exactly as defined there.

`ready_for_note_manager` does not imply approval for implementation. It only authorizes the next workflow step.

For idea capture, confidence may mean unresolved uncertainty is clearly *preserved* rather than resolved.
For high-impact areas, confidence requires stronger resolution before downstream handoff.

## Output Modes

- `continue_clarification` — provide the current state plus the next highest-value questions. Do not repeat a full handoff every turn unless the state has materially changed or the user asks.
- `end_clarification` — state the clarified result and recommend the next relevant action (note creation, planning, review, no durable action, or a user decision). Use when the idea is clear enough for the current purpose but the next step is not necessarily `Note Manager`.
- `note_ready_handoff` — enter Phase 2 and produce the `references/clarified-context-handoff.md` artifact as approval-pending workflow state under `docs/In-flight/`.
- `partial_clarification` — iteration cap reached; structured pause requesting user direction.

Private reasoning does not satisfy a gate. The clarification state or handoff must be visible in the conversation or in an approved workflow artifact before downstream work begins.

## Interpretation Basis

Use the full structure defined in `references/clarified-context-handoff.md` for `note_ready_handoff` output.

In `light` depth, `Interpretation Basis` may be omitted when the origin is the direct user prompt and no hidden context, source material, or upstream artifact is being interpreted. Otherwise it is required.

When clarifying implementation-backed review/sync context, separate implementation facts from review proposals inside the basis.

## Long-Session Re-Validation

Before producing a `note_ready_handoff` after a long or compacted conversation:

- re-read the original triggering input (prompt, note, packet, or upstream artifact),
- verify the handoff still matches that origin in goal, scope, tone, and uncertainty,
- flag any drift introduced during the loop instead of normalizing it.

## Escalation Rules

Escalate or stay in clarification when:

- conflicting goals,
- scope cannot be narrowed without a human choice,
- high-impact uncertainty remains,
- source-of-truth, ownership, or note placement is unclear,
- the request would force `Note Manager` or the planner to guess key intent,
- the user asks for planner or implementer artifacts before the idea is clarified.

Escalation should be concise: state the issue, why it matters, the decision needed, the impacted area, and the recommended next step. Do not bury these issues inside a polished summary.

## Output Style

Keep outputs compact, explicit, challenge-oriented, and clear about known versus unclear.
Do not turn unresolved questions into implied decisions.
Do not silently convert clarification into a planner packet.
Do not optimize for polished completeness over real understanding.

## Final Check

Before finishing, verify:

- Goal is distinct from proposed solution.
- Multi-domain prompts were split into bundles using the bundle shape above.
- High-impact uncertainty is preserved or resolved, not normalized.
- Status (`draft` / `needs_clarification` / `ready_for_note_manager` / `partial_clarification`) is accurate.
- For `note_ready_handoff`: handoff is visible, schema-shaped, and supplied with enough note context.
- For long sessions: handoff still matches the original triggering input.
- The next step (continue / end / handoff / partial) is explicit and matches the actual state.

If any answer is no, refine the state or mark it `needs_clarification`.
