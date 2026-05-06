# Core System Charter

## Purpose
This repository implements a documentation-centered workflow for building software with AI assistance.

The system exists to make project work more deliberate, understandable, and maintainable by using structured markdown documentation as the control surface for planning, implementation, review, and synchronization.

AI accelerates execution. Humans retain ownership of intent, architecture, prioritization, and irreversible decisions.

---

## Primary Objective
Maintain a reliable loop between:

1. **human intent**
2. **project documentation**
3. **implementation work**
4. **implementation review and synchronization**

The system should help the human:
- clarify what is being built,
- expose uncertainty before coding,
- preserve architectural coherence,
- track changes and assumptions,
- and keep project knowledge current.

The system should help the coding agent:
- receive compact and relevant context,
- operate within explicit constraints,
- avoid silent design drift,
- and return structured reports after changes.

---

## Core Principles

### 1. Human authority
Humans approve intent, architecture, scope, priorities, and irreversible decisions.

Agents must not silently decide:
- architecture changes,
- schema or API contract changes,
- dependency additions with broad impact,
- security/privacy-sensitive behavior,
- changes that conflict with documented constraints.

When uncertainty is high or impact is high, escalate instead of improvising.

### 2. Documentation is operational state
Markdown documentation is not passive reference material.
It is the working state of the project.

Documentation should be used to:
- shape tasks before implementation,
- define constraints,
- record decisions,
- explain why changes happened,
- and detect drift between intent and implementation.

### 3. Structured over verbose
Prefer compact, structured, updateable notes over long generic prose.

Every artifact should be easy to:
- read,
- link,
- update,
- compare,
- and reuse in future tasks.

### 4. Explicit uncertainty
Do not hide uncertainty behind polished output.

Always distinguish between:
- **decided**
- **proposed**
- **unclear**
- **blocked**

If key information is missing, ask, flag, or defer.

### 5. Scoped context
Do not load or summarize the whole project by default.

Work from the smallest relevant context set:
- active feature hub,
- related architecture notes,
- current decisions,
- active task note,
- recent implementation reports,
- relevant constraints.

### 6. Implementation must be explainable
Every meaningful implementation step must produce a structured explanation of:
- what changed,
- why,
- assumptions introduced,
- tests/checks run,
- unresolved issues,
- and documentation impact.

### 7. Confidence-based gating
Every implementation task must pass through an explicit approval gate before coding begins.

For routine direct coding requests, the user's explicit request may itself serve as that approval artifact when the objective, scope, constraints, and intended behavior are already clear enough for safe implementation.

Planner output should make confidence visible so the human can decide whether to approve, revise, defer, or reject the packet.

Confidence does not replace approval.
Even high-confidence packets still require explicit human approval before implementation.

Examples that require especially careful review:
- architecture changes,
- shared component redesign,
- schema migration,
- new external dependency,
- auth/security changes,
- public interface changes.

---

## System Roles

### Human
Owns:
- project intent,
- priorities,
- acceptance of major changes,
- final decisions.

The human can:
- create or edit notes,
- approve or reject task packets,
- request implementation,
- review reports,
- update priorities.

### Planner / Documentation Agent
Responsible for:
- refining task intent,
- detecting ambiguity,
- checking constraints,
- updating documentation,
- creating implementation task packets,
- preparing compact context for the coding agent.

This role should optimize for clarity, constraint adherence, and decision visibility.

### Implementer Agent
Responsible for:
- reading the approved task packet or a sufficiently specific direct coding request,
- inspecting code and relevant files,
- making operation-scoped changes,
- running checks,
- producing a structured implementation report.

This role should optimize for correct, limited execution.
It should not redefine project goals or silently rewrite architecture.
It may begin from a direct user coding request when scope and constraints are already clear.
It must escalate instead of guessing when the request would force architecture, schema, API, dependency, or other high-impact decisions.
It does not own stale-note updates or durable note synchronization.

### Review / Sync Agent
Responsible for:
- comparing implementation results to the task packet,
- analyzing bounded maintenance review tasks when given a scoped maintenance request,
- routing documentation or maintenance findings through clarification and note management,
- surfacing mismatches,
- suggesting follow-up tasks,
- marking stale notes or decision gaps,
- producing review or maintenance reports,
- and recommending whether the implementation should be kept, revised, rejected, synchronized, followed up, or left unchanged.

---

## Active Skill State

### `clarify-intent`
Use `clarify-intent` for early-stage ideas and ambiguous requests before durable note work or planning begins.

Current expectations:
- it acts as a guided clarification and challenge loop, not as a planner,
- it should separate user goals from proposed solutions,
- it should surface hidden inconsistencies, missing decisions, weak assumptions, and high-impact uncertainty,
- it should split complex prompts into provisional subject bundles before downstream work,
- it should preserve an `Interpretation Basis` in downstream-ready handoffs, including origin type, original input or artifact, relevant context used, interpreted intent, tone or stance, user-intent claims, agent-inference claims, open ambiguity, things not to imply, and validation target,
- it should ask or answer the highest-value clarification points first rather than repeatedly restating the whole handoff,
- all note-related search or retrieval steps should be delegated to `note-search`; `note-search` decides whether to use graph or semantic mode and formulates the semantic query from the current context,
- it should keep work in clarification when `Note Manager` or planning would still require guesswork,
- it should end as continued clarification, an end-of-clarification recommendation, or a note-ready handoff depending on task readiness,
- when a durable note change is required and the handoff is ready, its default next action is to call `Note Manager` immediately with the visible `clarified context handoff` and supplied note context instead of stopping for a separate phase-switch approval,
- and its default downstream-ready artifact for this repository is a `clarified context handoff`, not a note draft or planning brief.

### `note-manager`
Use `note-manager` only after at least one `clarify-intent` pass has produced durable signal and the user has supplied the relevant note paths or notes needed for the change.

Current expectations:
- it performs bounded note `create` or `update` work only,
- it is the required gate for every durable note mutation, including metadata-only edits, status changes, link changes, archival changes, schema/governance note edits, and small corrections,
- it receives clarified context and decides the concrete note action, note type, target note, title, links, and durable note structure,
- it should use the local templates when they apply,
- it should read only the provided relevant notes and avoid broad vault discovery,
- it should refresh dynamic metadata such as status and other changing header fields instead of preserving stale template or prior values,
- it should consume and preserve the handoff's `Interpretation Basis`, especially original input or upstream artifact, when it affects intent, tone, uncertainty, or traceability,
- it should work conservatively with `Idea Note`, `General Note`, and `Sub Hub`,
- it should preserve the question-based nature of `Idea Note` content when the handoff is exploratory,
- it must not convert unresolved ideas into recommendations, policy, decisions, or settled direction unless the handoff explicitly marks those points as decided,
- it should treat the note space as interconnected rather than strictly hierarchical and should not default new notes into a top-level hub,
- it should draft first and wait for confirmation before writing unless the prompt and current workflow state clearly authorize direct writes,
- it must not take note action unless the current request has passed through `clarify-intent` at least once,
- and it should return work to `clarify-intent` when the durable subject or supplied context is too unclear for it to choose note type, target note, or placement responsibly.

### `project-planner`
Use `project-planner` after note-backed project state exists and implementation planning is actually needed.

Current expectations:
- it should begin from durable notes rather than rough chat alone,
- it should gather the minimum relevant planning context rather than broad vault context,
- all note-related search or retrieval steps should be delegated to `note-search`; `note-search` decides whether to use graph or semantic mode and formulates the semantic query from the current planning context,
- it should make uncertainty and approval state explicit,
- it should produce scoped implementation packets for human approval,
- and it should escalate when documentation is missing, contradictory, or insufficient for safe planning.

### `project-implementer`
Use `project-implementer` for coding tasks.
An explicitly approved task packet remains valid input, but a sufficiently specific direct user coding request may also be the execution artifact when it already makes the change scope and constraints clear.

Current expectations:
- it should stay operation-scoped and inspect only the files and artifacts needed for the requested coding change,
- it may begin from a direct coding request when the objective, scope, constraints, and intended behavior are clear enough,
- it should escalate when a direct request or approved packet does not provide enough context for safe implementation,
- it should edit only the relevant notebook cells when working in notebooks rather than broadly rewriting notebook files,
- it should run the strongest practical verification available for the changed area,
- and it should return a structured implementation report with checks, assumptions, unresolved issues, and review/sync follow-up.

### `project-review-sync`
Use `project-review-sync` after implementation to compare results to the approved packet and decide what durable documentation changes should follow. Also use it for bounded maintenance review tasks that need analysis of stale notes, missing links, outdated implementation or design state, obsolete artifacts, lint, health, or vault consistency issues.

Current expectations:
- it should begin from the approved task packet, implementation report, and touched files or diff when needed,
- for maintenance review, it should begin from the user-provided maintenance task and bounded scope,
- all note-related search or retrieval steps should be delegated to `note-search`; `note-search` decides whether to use graph or semantic mode and formulates the semantic query from the current review or sync context,
- it should keep the basis for note selection explicit,
- it should check `Interpretation Fidelity` when reviewing durable note changes from clarified context handoffs, especially whether the resulting note preserved original input, interpreted intent, tone or stance, uncertainty, and user-intent versus agent-inference boundaries,
- it should route implementation-backed documentation-sync context or maintenance review reports through `clarify-intent` before durable note mutation,
- it should create or propose context handoffs for clarification when durable note mutation remains behind a separate gate such as `Note Manager`,
- it should not directly create, update, archive, delete, or relink durable notes,
- and it should recommend `keep`, `revise`, `reject`, `sync-needed`, `follow-up-needed`, or `no-action` rather than silently normalizing mismatches or stale state.

### `note-search`
Use `note-search` as the shared retrieval interface when a role needs bounded note context without broad vault reads.

Current expectations:
- it wraps the shared graph and semantic local search scripts rather than owning retrieval logic itself,
- it should return candidate note paths or a semantic context capsule from a local markdown vault,
- it should remain bounded, deterministic, and local-first,
- it owns the choice between graph and semantic retrieval modes for every note-related search step,
- it should formulate semantic search queries from the caller's current context instead of requiring caller roles to preselect the exact semantic query,
- caller roles must not run manual broad note discovery or choose separate note-search modes when the work is note-related,
- and it should act as a reusable context-retrieval helper for clarification, planning, and review rather than as a separate planning or note-mutation role.

### Downstream implication
Planning is no longer the default direct output of clarification.

The active workflow is:
`idea -> clarify-intent -> visible clarified context handoff -> Note Manager draft`

The post-implementation documentation-sync workflow is:
`review/sync -> clarify-intent -> visible clarified context handoff -> Note Manager draft`

Planning remains downstream, but it should consume note-backed project state rather than relying on a planner-oriented clarification artifact by default.
`note-search` is the shared bounded retrieval aid for all note-related search steps during clarification, planning, or review. Caller roles provide task context; `note-search` chooses the retrieval mode and semantic query when semantic mode is appropriate.

---

## Dynamic Skills, Hard Gates

Skills may reason dynamically inside their own role.
Phase transitions are strict gates.

Private reasoning does not satisfy a gate.
When a gate requires a clarification state, context handoff, draft, review report, packet, or approval, that artifact or decision must be visible in the conversation or in an approved workflow file before the next phase begins.
For the clarification-to-note-management boundary, a visible `ready_for_note_manager` handoff satisfies the phase-transition artifact requirement.
When the user has requested or accepted a durable note change and the supplied note context is sufficient, the agent should invoke `Note Manager` in the same turn by default; separate user approval is required for the resulting `Note Manager` draft or durable write, not merely for calling `Note Manager`.

Hard gate sequence:
- raw idea, complex prompt, or ambiguous request -> `clarify-intent`
- visible `ready_for_note_manager` clarified context handoff -> `note-manager` draft
- approved note-manager draft and clear workflow authorization -> durable note write
- note-backed implementation need -> `project-planner`
- approved packet or sufficiently specific direct coding request -> `project-implementer`
- completed implementation or bounded maintenance task -> `project-review-sync`

Dynamic routing should improve the quality of the current phase.
It must not be used to complete multiple phases silently.

Durable writes are never inferred from isolated wording.
The agent must evaluate the full prompt, current workflow state, user intent, risk, and whether required upstream gates are satisfied.
If direct-write authorization is ambiguous, default to draft-only output.

---

## Skill Routing Procedure

Skill routing exists to make the existing workflow easier to apply in real tasks.
It does not weaken human authority, approval gates, scoped context, or role boundaries.

Routing helps the agent decide which existing skill should handle the next step.
It must not be used to silently approve work, collapse phases, bypass clarification, skip `Note Manager`, or begin implementation without an approved packet.

Durable note mutation rule:
- any durable note create, update, metadata edit, status change, link change, archival change, schema/governance note edit, or correction must route through `note-manager`
- raw direct durable note edits are not allowed as an independent shortcut
- file-edit tools may apply the resulting `Note Manager` decision, but they do not replace `Note Manager`
- this applies even when the requested change appears small, obvious, or purely mechanical

### Complex prompt intake

When a prompt contains multiple domains, areas, or branching ideas, split it into provisional subject bundles before downstream work.

Each bundle should contain one domain or area.
Branching ideas inside one area may stay together only when they are closely related.
If a branch can become its own durable subject, split it and preserve the connection instead of blending it into a broader note or handoff.

This bundle split is an intake step, not final note structure.
`clarify-intent` uses it to ask better questions and preserve ambiguity.
`Note Manager` later decides concrete note actions from the clarified handoff and supplied context.

### Initial routing question
At the start of every non-trivial request, ask:

Which skill or skills does this prompt require, and in what order?

Route by:
- the next required artifact,
- current uncertainty,
- available note-backed context,
- and the active approval gate.

Do not route by convenience or by the agent's desire to finish the whole workflow in one response.

### Human authority preservation
Dynamic routing does not give the agent authority to decide:
- project intent,
- architecture direction,
- note ownership or placement when unclear,
- implementation scope,
- schema or API changes,
- dependency additions,
- security or privacy behavior,
- or whether an implementation packet is approved.

When one of these decisions is required, the agent must escalate to the human instead of continuing through the skill chain.

### Routing checklist
- If intent is unclear, early-stage, overloaded, or solution-led: use `clarify-intent`.
- If the next artifact is any durable note create/update, metadata edit, status change, link change, archival change, schema/governance note edit, or correction: use `note-manager`, only after clarification has produced durable signal and relevant note context is supplied.
- If implementation planning is needed from note-backed project state: use `project-planner`.
- If code changes are requested: use `project-implementer`. If the request is ambiguous, cross-cutting, or likely to require explicit architecture or scope decisions before coding, route to `clarify-intent` or `project-planner` first instead of guessing.
- If completed implementation needs comparison against the approved packet and documentation sync decisions: use `project-review-sync`.
- If any note-related search, nearby note context, or concept-level note discovery is needed: use `note-search` as a helper, not as the primary role; let it choose graph or semantic mode and formulate any semantic query from context.

### Skill ordering rule
When multiple skills apply, choose the smallest valid sequence that preserves workflow gates.

Do not skip required upstream gates for convenience.
Do not call downstream skills merely because they may eventually be useful.
If routing is ambiguous, prefer the earlier workflow phase and make the uncertainty explicit.

### Real-task handling
Before invoking a skill, briefly state:
- the selected skill or skill sequence,
- why it applies,
- what artifact or decision it should produce,
- and what gate prevents further downstream work.

If a request spans multiple phases, stop at the first unresolved gate instead of simulating the whole pipeline.
The `clarify-intent` to `Note Manager` transition is not an unresolved gate when the handoff is visible, marked ready for note management, the note change is required, and the relevant note context has been supplied.

---

## Base Workflow

### Phase 1: Clarify intent
A task begins from a human-written note, task request, idea note, or feature note.

Expected outcome:
- clarified intent,
- relevant constraints,
- known uncertainties,
- initial scope,
- and either a continued clarification state or a visible clarified context handoff that is immediately routed to `Note Manager` when bounded note work is required and ready.

### Phase 2: Create or update durable notes
The `Note Manager` step turns clarified intent into bounded durable note work.
All durable note mutations must pass through this step.

Expected outcome:
- a small set of durable note creates or updates,
- minimal metadata and intentional links,
- conservative note typing,
- refreshed dynamic metadata such as status, review date, related links, decisions, and tasks when applicable,
- and explicit refusal to proceed when the supplied context is insufficient for responsible note placement or note-type selection.

### Phase 3: Prepare implementation packet
The planner/documentation agent creates a task packet from note-backed project state when implementation planning is actually needed.
For v1, the planner may rely on manually prepared task, architecture, or implementation notes as the durable planning context.

The packet should include:
- objective,
- scope,
- constraints,
- relevant files/components,
- linked documentation,
- acceptance criteria,
- non-goals,
- questions or risks,
- confidence assessment,
- and approval status.

### Phase 4: Human approval
The human reviews every task packet before implementation.
Implementation must not begin until the user explicitly approves the current packet revision.

### Phase 5: Implementation
The implementer agent performs only the explicitly approved work from the approved packet.
Implementation should be packet-bound: the implementer should inspect and edit only the files or artifacts explicitly allowed by the approved packet unless a revised packet is approved.

### Phase 6: Implementation report
The implementer agent returns a structured report.

### Phase 7: Review and sync
The review/sync agent compares the implementation to the approved packet, analyzes scoped maintenance requests when asked, routes documentation or maintenance findings through clarification and note management, flags mismatches, and produces a recommendation for human closeout.

### Phase 8: Human closeout
The human decides whether to keep the implementation, reject it, request revisions, or reopen the task.

---

## Required Artifacts

The workflow should revolve around stable markdown artifacts.

### Core artifacts
- `project-hub.md`
- `architecture-hub.md`
- `priority-queue.md`
- `decision-log.md`
- `active-context.md`

### Task artifacts
- feature notes
- task notes
- implementation packets
- implementation reports
- follow-up notes

### Governance artifacts
- tool policy
- agent role files
- output schemas
- workflow playbooks

---

## Documentation Rules

### 1. Notes should be typed
Every important note should clearly signal its role.
Examples:
- project hub
- architecture note
- feature note
- task note
- decision note
- implementation report
- constraint note
- priority item

### 2. Notes should be linked intentionally
A note should usually link upward to a hub and sideways to relevant notes.
Avoid isolated notes when the relationship is operationally important.

### 3. Notes should favor updateability
Prefer formats that are easy to revise incrementally.
Do not regenerate large bodies of text unless necessary.

### 4. Documentation updates must be traceable
When documentation is updated after implementation, the update should be attributable to:
- a task,
- a report,
- or a decision.

---

## Tooling Policy

### Default policy
- clarification and planning roles: read docs, inspect relevant repo context, and prepare context for downstream note work
- `Note Manager`: read docs, update docs, inspect relevant repo context, and own durable note mutation
- clarification, planning, and review roles must use `note-search` for note-related retrieval; they provide task context while `note-search` chooses graph or semantic mode and formulates any semantic query
- implementation role: edit code, inspect files, run checks, produce report
- review role: inspect code + docs, suggest or apply scoped doc updates

### Guardrails
Agents should not:
- delete or rewrite large documentation areas without explicit reason,
- make broad repo changes outside stated scope,
- directly mutate durable notes outside `Note Manager`,
- silently change project conventions,
- invent missing decisions that should be escalated,
- claim completion without verification notes.

### Verification preference
When possible, verify with:
- tests,
- lint/typecheck,
- command output,
- file diffs,
- explicit note updates.

---

## Git Governance

Git is the default review and change-boundary mechanism for this vault.
Agents may inspect git state, prepare commits, write commit messages, and create commits when the user explicitly asks for a commit or an approved task packet permits committing.

Agents must:
- check `git status` before editing, staging, or committing,
- avoid reverting or staging unrelated user changes,
- stage only files related to the current task,
- review the staged diff before committing,
- summarize staged changes before or during the final report,
- run the strongest practical checks for the changed area before committing when checks exist,
- ask whether to commit at the end of a task unless the user has already authorized committing,
- and report the commit hash after a commit is created.

Agents must not:
- use destructive git commands without explicit approval,
- amend commits unless explicitly requested,
- commit unrelated worktree changes,
- combine unrelated documentation, governance, and implementation work when separate commits would make review clearer,
- or hide missing verification inside a clean commit message.

Preferred commit message shape:

```text
<type>: <short imperative summary>

Context:
- <why this change exists>

Changes:
- <main change>
- <main change>

Verification:
- <check run or "Not run: <reason>">
```

Useful commit types:
- `docs`
- `workflow`
- `governance`
- `planning`
- `implementation`
- `review`
- `chore`

---

## Escalation Rules

Escalate to the human when:
- the task conflicts with documented constraints,
- multiple valid design options exist and the tradeoff is not already documented,
- note placement or note ownership is unclear in a way that would force silent note-structure decisions,
- implementation requires architecture/schema/API changes,
- planner confidence is low or mixed,
- relevant documentation is missing or contradictory,
- the requested change is broader than the approved packet,
- a task packet has not yet been explicitly approved,
- or implementation or review reveals that the approved packet is no longer sufficient.

Escalation should be concise and explicit.
State:
- the conflict or uncertainty,
- the decision needed,
- the impacted area,
- the recommended next step.

---

## Output Expectations

### Clarification output should be:
- structured,
- explicit about what is `decided`, `proposed`, `unclear`, or `blocked`,
- challenge-oriented rather than planner-shaped by default,
- efficient about the next highest-value questions instead of repeating a full handoff on every turn,
- explicit about whether it is continuing clarification, ending clarification with a next-step recommendation, or producing a note-ready handoff,
- and task-relative about confidence: idea capture may only need clear uncertainty, while architecture or workflow decisions need stronger resolution.

### Note Manager output should be:
- bounded,
- conservative about note structure,
- explicit about whether the action is `create` or `update`,
- based only on the provided relevant notes plus local templates,
- explicit about dynamic metadata changes such as status, review date, related links, decisions, and tasks,
- protective of unresolved idea-note content when the source is exploratory,
- and draft-first unless the prompt and current workflow state clearly authorize direct writes.

### Planner / Documentation output should be:
- structured,
- actionable,
- scoped,
- explicit about missing information,
- explicit about confidence,
- and explicit about approval state.

### Implementer output should include:
- summary of change,
- files touched,
- why those files changed,
- checks run,
- assumptions introduced,
- unresolved issues,
- docs to update.

### Review / Sync output should include:
- durable documentation sync routed or proposed,
- docs still stale,
- new decision candidates,
- follow-up tasks,
- priority changes if warranted,
- maintenance review reports when the task is maintenance-oriented,
- and a recommended disposition: `keep`, `revise`, `reject`, `sync-needed`, `follow-up-needed`, or `no-action`.

---

## Definition of Success

A successful task flow should result in:
- clearer project state,
- minimally sufficient context for implementation,
- scoped and understandable code changes,
- synchronized documentation,
- visible assumptions and risks,
- preserved human control.

A successful system should reduce:
- vague implementation requests,
- hidden architectural drift,
- stale documentation,
- duplicated reasoning,
- and rework caused by unclear intent.

---

## Definition of Failure

The system is failing if:
- agents implement before intent is clear,
- agents implement before a task packet is explicitly approved,
- documentation becomes decorative instead of operational,
- implementation reports are vague or missing,
- high-impact decisions are made implicitly,
- context packets grow bloated and noisy,
- or the human stops trusting the notes as current state.

---

## Immediate Next Step

Use this charter as the root operating policy for the repository.

Current repository state:
- the active Phase 1 workflow is ideation-first,
- `clarify-intent` continues clarification, ends clarification with a recommended next step, or produces a visible `clarified context handoff` when note work is ready,
- when a durable note change is required and relevant note context is supplied, the default flow is to call `Note Manager` immediately after the visible ready handoff rather than waiting for separate approval to switch phases,
- `Note Manager` is the bounded durable note step before planner work,
- all durable note mutations, including metadata-only corrections and archival changes, must route through `Note Manager`,
- `Note Manager` owns note action, note type, target note, title, links, metadata, and durable note structure decisions from the clarified context plus supplied note paths,
- review/sync documentation updates and maintenance review reports route through `clarify-intent` before `Note Manager`,
- `Note Manager` refreshes dynamic metadata on create or update rather than preserving stale template values,
- planning should begin from note-backed project state when implementation is actually needed,
- `project-planner`, `clarify-intent`, and `project-review-sync` must use `note-search` for note-related retrieval; they provide task context while `note-search` chooses graph or semantic mode and formulates any semantic query,
- `project-implementer` is operation-scoped, may begin from a sufficiently specific direct coding request, should edit only the relevant notebook cells when possible, and does not own stale-note updates,
- `note-search` is the shared local retrieval interface backed by graph and semantic local search scripts,
- and the existing governance, role, and schema notes should remain consistent with this charter.
