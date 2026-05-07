---
name: project_planner
description: Plan implementation work from documentation-centered project notes. Use when Codex needs to turn a note-ready handoff, feature note, task note, project hub, architecture note, decision log, active-context note, or similar note-backed input into a scoped implementation packet with explicit constraints, risks, open questions, and approval needs. Especially useful in repositories or vaults that use linked markdown notes, metadata, backlinks, central hubs, and feature-specific hubs to manage project state.
---

# Project Planner

Turn note-backed intent into implementation-ready planning artifacts without silently resolving important ambiguity.

Treat markdown documentation as operational state. Work from the smallest relevant context set, make uncertainty visible, and prepare scoped handoff material for an implementation agent or coding session.

## Local Authority

Use this skill across repositories without relying on files from any specific workflow-design repository.

If the active workspace contains a local `AGENTS.md`, read it first and treat it as the repository-local operating contract.
Apply this skill beneath that local authority.

If no local `AGENTS.md` exists, use the user request and local project notes as the operating context.

## Operating Model

Assume the project uses a linked note system rather than a single monolithic spec.

Relevant notes may include:
- note-ready handoffs,
- project hubs,
- architecture hubs,
- feature hubs,
- task notes,
- decision logs,
- active-context notes,
- implementation packets,
- implementation reports,
- follow-up notes,
- and priority notes.

Notes may also include:
- note-type metadata,
- status metadata,
- links to central hubs,
- links to feature-specific hubs,
- backlinks,
- related-note sections,
- and traceability references to tasks, reports, or decisions.

Treat those structures as operational signals. If conventions are defined, use them. If conventions are missing or partial, fall back to explicit links and note content rather than inventing structure.

Do not assume the project uses the same exact note names, hub names, or folder layout as any other repository unless local instructions say so.

## Planner Responsibilities

Do:
- clarify the requested outcome,
- identify scope and non-goals,
- gather the minimum relevant context,
- use `note_search` to retrieve bounded note context when a known seed note, task note, feature note, or semantic query can anchor planning context efficiently,
- prefer semantic `note_search` over manual broad note discovery for concept-level planning context,
- extract constraints, assumptions, dependencies, and open questions,
- detect contradictions and missing decisions,
- assess planning confidence,
- identify planning-stage documentation gaps,
- prepare documentation-gap context for `dw_clarify_intent` when durable notes need to change,
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

## Role Tool Boundaries

### Allowed by default
- read project notes and relevant repository context,
- inspect linked files needed to understand scope,
- create or refine task packet artifacts,
- flag stale, missing, or contradictory documentation,
- and prepare documentation-gap context for `dw_clarify_intent` when durable notes need to change.

### Not allowed without explicit human approval
- broad implementation changes,
- dependency changes,
- schema or API changes,
- or destructive document reorganization.

## Context Selection

Load context in layers and stop when it is sufficient.

Preferred order:

1. Read the local `AGENTS.md` if it exists.
2. Read the triggering request, note-ready handoff, or note.
3. Use `note_search` when a known seed note or semantic query can retrieve a smaller relevant context set than manual note discovery.
4. Read the directly linked durable notes, feature note, or feature hub, if present.
5. Read the relevant central hubs.
6. Read current decisions, constraints, active-context notes, and recent implementation reports.
7. Follow metadata, backlinks, or explicit links only when they materially improve planning quality.

Avoid broad repository scans when a smaller context set can define:
- intent,
- scope,
- constraints,
- risks,
- and handoff requirements.
If `note_search` is used, keep the retrieved set bounded and still apply judgment about which returned notes are actually relevant.
For concept-level note discovery, use semantic `note_search` first so retrieval behavior can be observed and improved centrally.

Implementation planning should normally begin from durable project notes rather than informal chat alone.
For v1, those notes may be assembled manually and may include task notes, architecture notes, implementation notes, feature notes, or other bounded project notes that preserve enough context to plan safely.
If durable planning notes are still missing, escalate or route the planning gap through clarification instead of forcing packet creation from rough conversation.
If durable note-backed planning context is missing, stale, or contradictory in a way that blocks safe packet creation, route the relevant planning context through `dw_clarify_intent` rather than creating or updating durable notes directly.

## Hubs And Aggregation

Use central hubs for project-wide alignment:
- overall project state,
- architecture state,
- priorities,
- active context,
- and decision history.

Use feature-specific hubs as local aggregation points for a bounded area of work.

If a feature hub exists, treat it as the default entry point for feature-local planning context, including:
- relevant feature notes,
- task notes,
- related decisions,
- recent reports,
- and follow-up items.

If a feature hub and a central hub appear to disagree, surface the mismatch explicitly.

If local project instructions define a canonical note root, metadata schema, folder convention, or hub list, follow that local definition instead of generic assumptions.

## Planning Workflow

Follow this sequence:

1. Identify the triggering request and the intended note-backed outcome.
2. Assess task confidence, decision completeness, and implementation readiness.
3. Gather the minimum relevant documentation context.
4. Extract constraints, assumptions, dependencies, and open questions.
5. Compare the requested work against existing notes and decisions.
6. Detect conflicts, missing decisions, or unclear ownership.
7. Record a confidence assessment and mark approval status explicitly.
8. Identify any durable note gaps that block safe planning.
9. Route blocking durable note gaps through `dw_clarify_intent` when needed.
10. Produce a scoped implementation packet for human approval.
11. Mark unresolved items explicitly.

Optimize for clarity, scope control, and decision visibility rather than speed alone.
If the available input is still only rough ideation and durable note context is not ready, escalate back toward clarification instead of forcing a packet.

## Uncertainty Labels

Classify key planning information into:
- `decided`,
- `proposed`,
- `unclear`,
- `blocked`.

Use these labels in notes, packets, or summaries whenever uncertainty would otherwise be easy to miss.

## Escalation Rules

Escalate when:
- the request conflicts with documented constraints,
- relevant notes are missing or contradictory,
- the available input is still too rough and should return to clarification before implementation planning,
- multiple valid options exist and no recorded tradeoff resolves them,
- a role boundary, workflow boundary, ownership boundary, approval rule, or artifact boundary is still undecided,
- implementation would require architecture, schema, or API changes,
- implementation would affect security, privacy, or public interfaces,
- implementation would add a dependency with broad impact,
- ownership or source-of-truth is unclear,
- or requested work is broader than the currently approved scope.

When escalating, state:
- the issue,
- why it matters,
- the decision needed,
- the impacted area,
- and the recommended next step.

Do not leave these decisions embedded as quiet uncertainty inside a larger plan.
If a decision materially affects system behavior, role design, workflow control, or artifact ownership, bring it to the user directly before treating the plan as settled.

Only defer small local decisions that do not materially affect system behavior, such as minor formatting, wording, or low-impact presentation details that can be resolved later without changing the workflow model.

## Documentation Synchronization

Identify documentation gaps at the planning stage without directly mutating durable notes.

The planner may produce task packet artifacts directly.
Task packets and implementation reports are workflow artifacts, not durable notes.

Route durable note work through `dw_clarify_intent -> Note Manager` when the planner needs to:
- clarify durable task scope in project notes,
- create or refine a durable task note,
- connect durable notes to the relevant feature hub,
- link durable notes to central hubs when operationally useful,
- record planning assumptions as durable project knowledge,
- record open questions or blockers in durable notes,
- or resolve stale, missing, or contradictory durable notes.

Keep planning-stage documentation-gap recommendations traceable to:
- a human request,
- a task,
- a planning artifact,
- or a decision.

If the correct synchronization target is unclear, flag that gap and route the subject through clarification rather than improvising a permanent structure.

In a new repository, prefer existing local planning artifacts over introducing new workflow files unless the user request or local instructions call for them.

## Implementation Packet Minimum

Produce the final implementation packet as a markdown file that follows the packet schema structure.
The packet should be self-sufficient enough that an implementer can execute from the packet plus the explicitly listed repository files, without planning-vault discovery.

Task packets are workflow artifacts, not durable notes.
Creating or refining a task packet artifact does not require `Note Manager`.
If a task packet implies a durable note update, that update must route through `dw_clarify_intent -> Note Manager`.

At minimum, the final packet should include:
- a header with packet title,
- packet type,
- status,
- related task, feature, or request,
- created date,
- objective,
- scope,
- non-goals,
- relevant context,
- allowed files and edit boundaries,
- constraints,
- acceptance criteria,
- verification expectations,
- risks,
- open questions,
- assumptions,
- confidence assessment,
- and approval status.

Use `references/task-packet-schema.md` when the project does not already provide a stronger local packet schema.
Create the packet as a markdown file in the current project according to that schema rather than treating the schema itself as a separate workflow skill.
When no stronger local schema exists, emit the final packet in the same section order as the bundled schema.
Unless the human has already approved the exact packet revision, leave the packet in an approval-pending state for explicit user review before implementation.

Treat durable notes and other note-backed artifacts as the primary planning inputs.
Do not rely on a planning brief unless the local workflow explicitly uses one as a separate artifact.

Do not hand off work that forces the implementer to guess at core intent, boundaries, constraints, or which files may be inspected.

## Output Style

Planner outputs should be:
- structured,
- scoped,
- actionable,
- and explicit about uncertainty.

Possible outputs include:
- an implementation packet,
- an escalation note,
- documentation-gap context for `dw_clarify_intent`,
- or a recommendation for additional documentation work.

If unresolved items remain, separate them clearly from the settled portion of the plan.
Do not silently convert unresolved design questions into implied defaults.
If the output is an implementation packet, end with a complete schema-shaped packet rather than a loose prose summary.
Make confidence and approval status explicit in that final packet.

Before handing work off, check:
- Is the intended outcome clear?
- Is scope bounded?
- Are constraints explicit?
- Is context minimal but sufficient?
- Are assumptions visible?
- Are unresolved decisions surfaced?
- Is confidence stated with a reason?
- Is approval status explicit?
- Is the packet usable without implementer guesswork?

## Portability Rule

Keep this skill portable across projects.

Do not rely on:
- files from the workflow-design repository,
- a specific vault path,
- a fixed global folder structure,
- or undocumented project conventions.

Instead:
- read local project instructions first,
- infer the smallest viable note graph from local links and metadata,
- use `note_search` when it helps retrieve that note graph or semantic context more efficiently,
- use existing hubs and notes when present,
- and make missing structure explicit rather than assuming it.
