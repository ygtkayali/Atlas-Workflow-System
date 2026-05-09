---
name: project-planner
description: Use when note-backed project context is ready and must become a scoped implementation packet with explicit constraints, risks, and approval state before coding begins.
---

# Project Planner

Turn note-backed intent into implementation-ready planning artifacts without silently resolving important ambiguity.

Treat markdown documentation as operational state. Work from the smallest relevant context set, make uncertainty visible, and prepare scoped handoff material for an implementation agent or coding session.

## When Planning Is Needed

A request is ready for direct implementation (skip planner) only if all four answers are yes:
- **Clear objective** — the intended outcome is explicit?
- **Bounded scope** — the area to change is known and narrow?
- **Known files** — the exact files to edit are identifiable without discovery?
- **Concrete acceptance** — success criteria are testable without interpretation?

If any answer is no, the request needs planning before implementation begins.

## Note Ecosystem

Assume the project uses a linked note system rather than a single monolithic spec.

Relevant notes may include note-ready handoffs, project hubs, architecture hubs, feature hubs, task notes, decision logs, active-context notes, implementation packets, implementation reports, follow-up notes, and priority notes. Notes may also carry type metadata, status metadata, backlinks, hub links, and traceability references.

Treat those structures as operational signals. If conventions are defined, follow them. If conventions are missing or partial, fall back to explicit links and note content rather than inventing structure.

**Central hubs** provide project-wide alignment: overall project state, architecture state, priorities, active context, and decision history.

**Feature hubs** are local aggregation points for a bounded area of work. If a feature hub exists, treat it as the default entry point for feature-local planning context — relevant feature notes, task notes, decisions, recent reports, and follow-up items.

If a feature hub and a central hub appear to disagree, surface the mismatch explicitly.

Do not assume the project uses the same exact note names, hub names, or folder layout as any other repository unless local instructions say so.

## Planner Responsibilities

Do:
- clarify the requested outcome,
- identify scope and non-goals,
- gather the minimum relevant context — cap at ~5–8 notes; if more are needed, route the remaining gap through `dw-clarify-intent` rather than expanding note loading indefinitely,
- use `note-search` to retrieve bounded note context when a known seed note or semantic query can anchor planning context efficiently,
- prefer semantic `note-search` over manual broad note discovery for concept-level planning context,
- extract constraints, assumptions, dependencies, and open questions,
- detect contradictions and missing decisions,
- assess planning confidence using the **Confidence Rubric**,
- identify planning-stage documentation gaps,
- prepare documentation-gap context for `dw-clarify-intent` when durable notes need to change,
- and produce a scoped implementation packet for explicit human approval.

Do not:
- force a rough idea directly into packet creation when clarification or durable notes are still missing,
- create or update durable notes directly,
- choose final durable note targets,
- draft final durable note content,
- invent architecture or schema decisions,
- approve medium-impact or high-impact changes on behalf of the human,
- broaden scope for convenience,
- treat missing documentation as permission to improvise,
- or present unresolved ambiguity as already decided.

**Scope expansion rule:** When satisfying the acceptance criteria would require expanding the `Allowed Implementation Area` beyond what the note context supports, escalate before drafting — do not widen scope to make the packet self-consistent.

## Role Tool Boundaries

### Allowed by default
- read project notes and relevant repository context,
- inspect linked files needed to understand scope,
- create or refine task packet artifacts,
- flag stale, missing, or contradictory documentation,
- and prepare documentation-gap context for `dw-clarify-intent` when durable notes need to change.

### Not allowed without explicit human approval
- broad implementation changes,
- dependency changes,
- schema or API changes,
- or destructive document reorganization.

## Planning Workflow

This is the canonical planning sequence. Context loading is embedded within it.

1. **Assess the request.** Apply the four-question test from **When Planning Is Needed**. If all four pass, surface this and let the user decide whether to proceed with planning or route directly to implementation.
2. **Read local authority.** Read `AGENTS.md` if it exists.
3. **Load note context in layers.** Start from the triggering request, note-ready handoff, or seed note. Use `note-search` when a known seed note or semantic query can retrieve a smaller relevant context set than manual discovery — process `read_first` notes before `graph_expansion` notes. Follow direct links to the feature hub, feature notes, or relevant central hubs. Read current decisions, constraints, active-context notes, and recent implementation reports. Follow backlinks or metadata only when they materially improve planning quality. **Stop at ~5–8 notes.** If the context is still insufficient, route the remaining gap through `dw-clarify-intent`.
4. **Extract planning elements.** Identify constraints, assumptions, dependencies, open questions, and conflicts.
5. **Compare against existing notes and decisions.** Detect missing decisions, unclear ownership, or scope contradictions.
6. **Assess confidence.** Apply the **Confidence Rubric**. Mark each key planning element with an uncertainty label: `decided`, `proposed`, `unclear`, or `blocked`.
7. **Identify documentation gaps.** Flag durable note gaps that block safe planning. Route blocking gaps through `dw-clarify-intent` instead of improvising note content.
8. **Produce the packet.** Follow the schema in `references/task-packet-schema.md`. Mark approval status as `approval_pending` unless the user has already approved the exact revision.
9. **Check packet quality.** Apply the quality bar from `references/task-packet-schema.md` before handoff.

Optimize for clarity, scope control, and decision visibility. If the available input is still rough ideation and durable note context is not ready, escalate back toward clarification instead of forcing a packet.

## Confidence Rubric

**High** — all four hold: scope is explicit and bounded; constraints are documented; acceptance criteria are concrete and testable; no architectural unknowns remain.

**Medium** — all four planning questions have answers, but one or more constraints, risks, or acceptance details remain uncertain. Implementation can proceed with noted caution.

**Low** — one or more of the four planning questions cannot be answered from available notes. The packet should not proceed without additional clarification.

**Mixed** — at least one section of the packet is unclear or blocked while others are settled. Name the unclear sections explicitly.

State the confidence level and a short reason for the rating in the `Confidence Assessment` section of the packet.

## Packet Revision Protocol

When updating an existing packet rather than producing a new one:
- Emit only the changed sections, not the full packet.
- Add a `Revision Notes` block at the top of the output listing what changed, which sections moved status, and any new open questions introduced.
- Approval resets to `approval_pending` on any material change unless the user explicitly re-approves the new revision in the same message.

## Escalation Rules

Escalate when:
- the request conflicts with documented constraints,
- relevant notes are missing or contradictory,
- the available input is still too rough and should return to clarification,
- multiple valid options exist and no recorded tradeoff resolves them,
- a role boundary, workflow boundary, ownership boundary, approval rule, or artifact boundary is still undecided,
- implementation would require architecture, schema, or API changes,
- implementation would affect security, privacy, or public interfaces,
- implementation would add a dependency with broad impact,
- ownership or source-of-truth is unclear,
- satisfying acceptance criteria would require expanding the Allowed Implementation Area beyond what the note context supports,
- or requested work is broader than the currently approved scope.

When escalating, state: the issue, why it matters, the decision needed, the impacted area, and the recommended next step.

Do not leave these decisions embedded as quiet uncertainty inside a larger plan. If a decision materially affects system behavior, role design, workflow control, or artifact ownership, bring it to the user directly before treating the plan as settled.

Only defer small local decisions that do not materially affect system behavior, such as minor formatting, wording, or low-impact presentation details.

## Implementation Packet

Use `references/task-packet-schema.md` as the schema authority for all packet output. The schema defines the required sections, status semantics, approval rules, and quality bar.

Packet status and uncertainty labels are defined in `vocabulary.md`.

The packet must be self-sufficient: an implementer should be able to execute from the packet plus the explicitly listed files, without planning-vault discovery.

Task packets are workflow artifacts, not durable notes. Creating or refining a packet does not require `Note Manager`. If a packet implies a durable note update, that update must route through `dw-clarify-intent → Note Manager`.

Do not hand off work that forces the implementer to guess at core intent, boundaries, constraints, or which files may be inspected.

## Documentation Synchronization

Identify documentation gaps at the planning stage without directly mutating durable notes.

Route durable note work through `dw-clarify-intent → Note Manager` when the planner needs to: clarify durable task scope in project notes, create or refine a durable task note, connect durable notes to the relevant feature hub, record planning assumptions as durable project knowledge, record open questions or blockers in durable notes, or resolve stale, missing, or contradictory durable notes.

Keep planning-stage documentation-gap recommendations traceable to a human request, a task, a planning artifact, or a decision. If the correct synchronization target is unclear, flag the gap and route through clarification.

In a new repository, prefer existing local planning artifacts over introducing new workflow files unless the user request or local instructions call for them.

## Output Style

Planner outputs should be structured, scoped, actionable, and explicit about uncertainty.

Possible outputs:
- an implementation packet,
- an escalation note,
- documentation-gap context for `dw-clarify-intent`,
- or a recommendation for additional documentation work.

If unresolved items remain, separate them clearly from the settled portion of the plan. Do not silently convert unresolved design questions into implied defaults. If the output is an implementation packet, end with a complete schema-shaped packet rather than a loose prose summary.
