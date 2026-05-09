<!-- atlas-dev-workflow-bridge:start -->
# Dev Workflow Runtime Contract

## Purpose
This project is configured for the `dev-workflow` Atlas mode.

The workflow uses structured markdown documentation as the control surface for planning, implementation, review, and synchronization.
AI accelerates execution. Humans retain ownership of intent, architecture, prioritization, and irreversible decisions.

## Local Authority
Local project instructions are authoritative.

If project-specific constraints, verification commands, architecture rules, ownership rules, coding conventions, security boundaries, or release practices exist, follow them before reusable workflow guidance.
Those local rules should be recorded in the repo-specific section below or in clearly linked project documentation.

The reusable workflow mode does not override human decisions, project architecture, public APIs, security/privacy constraints, or repo-specific implementation rules.

## Atlas Configuration
The active Atlas configuration lives in:

- `atlas.yaml`

Use it to identify:
- the selected Atlas mode,
- the local workflow docs path,
- managed workflow assets,
- managed skills,
- and managed tools.

By default, workflow documentation lives under:

- `docs/`

If a required workflow or shared skill is missing, stop and report the setup gap.
Run the configured Atlas skill sync before continuing workflow work.

## Core Principles

### Human Authority
Humans approve intent, architecture, scope, priorities, and irreversible decisions.

Agents must not silently decide:
- architecture changes,
- schema or API contract changes,
- dependency additions with broad impact,
- security/privacy-sensitive behavior,
- changes that conflict with documented constraints.

When uncertainty is high or impact is high, escalate instead of improvising.

### Documentation Is Operational State
Markdown documentation is working project state, not passive reference material.

Use documentation to shape tasks, define constraints, record decisions, explain changes, and detect drift between intent and implementation.

### Structured Over Verbose
Prefer compact, structured, updateable notes over long generic prose.

Every artifact should be easy to read, link, update, compare, and reuse in future tasks.

### Explicit Uncertainty
Do not hide uncertainty behind polished output.

Always distinguish between:
- `decided`
- `proposed`
- `unclear`
- `blocked`

If key information is missing, ask, flag, or defer.

### Scoped Context
Do not load or summarize the whole project by default.

Work from the smallest relevant context set:
- active feature or project subject,
- related architecture notes,
- current decisions,
- active task note,
- recent implementation reports,
- relevant constraints.

### Explainable Implementation
Every meaningful implementation step must produce a structured explanation of what changed, why, assumptions introduced, checks run, unresolved issues, and documentation impact.

### Confidence-Based Gating
Every implementation task must pass through an explicit approval gate before coding begins.

For routine direct coding requests, the user's explicit request may itself serve as that approval artifact when the objective, scope, constraints, and intended behavior are clear enough for safe implementation.

Planner output should make confidence visible so the human can decide whether to approve, revise, defer, or reject the packet.
Confidence does not replace approval.

## System Roles

### Human
Owns project intent, priorities, acceptance of major changes, and final decisions.

The human may create or edit notes, approve or reject task packets, request implementation, review reports, and update priorities.

### Planner / Documentation Agent
Owns clarity before execution: refine intent, surface ambiguity, check constraints, and prepare implementation context when planning is needed.

Detailed planning procedure lives in the selected skill.

### Implementer Agent
Owns scoped execution from an approved packet or sufficiently specific direct coding request.

It should keep implementation limited, explainable, and verified. It does not own stale-note updates or durable note synchronization.

Detailed implementation procedure lives in the selected skill.

### Review / Sync Agent
Owns comparison, drift detection, and synchronization routing after implementation or during bounded maintenance review.

It recommends closeout disposition but does not silently normalize mismatches or bypass note-management gates.

Detailed review and synchronization procedure lives in the selected skill.

## Runtime Workflow Router
`AGENTS.md` is the runtime routing authority for dev-workflow projects.
It tells agents which workflow phase comes first, which gate blocks the next phase, and where detailed behavior lives.

The installed skill `SKILL.md` files own in-role procedure.
Do not duplicate full skill instructions here.
Use this file to choose the skill and gate; then follow that skill's own instructions.

### Skill Routing Table

| Situation | Skill | Required output or gate |
| --- | --- | --- |
| Early-stage idea, ambiguous request, overloaded prompt, or solution-led request | `dw-clarify-intent` | Continued clarification, next-step recommendation, or visible `ready_for_note_manager` handoff |
| Durable note create/update, metadata edit, status change, link change, archival change, schema/governance edit, or correction | `dw-note-manager` | Draft first unless direct-write authorization is clear; durable write only after the note-manager gate is satisfied |
| Note-backed implementation planning need | `project-planner` | Scoped implementation packet with explicit approval state |
| Approved packet or sufficiently specific direct coding request | `project-implementer` | Operation-scoped change plus implementation report |
| Verification before closeout for implementation-like changes | `implementation-verifier` | Verification result, durable tests when appropriate, and explicit remaining risk |
| Completed implementation review, documentation-sync routing, or bounded maintenance review | `project-review-sync` | Review or maintenance report with disposition |
| Note-related retrieval needed by clarification, planning, review, or other workflow roles | shared `note-search` helper | Default note search/retrieval tool for dev-workflow; candidate note paths or local context capsule; caller supplies task context and `note-search` chooses retrieval mode |

### Routing Rules
- Ask which skill or skills the prompt requires, and in what order, before non-trivial work.
- Choose the smallest valid sequence that preserves the gates.
- If note-related retrieval is needed, use `note-search` as the default search/retrieval tool for dev-workflow; do not manually perform broad vault discovery.
- If a prompt spans multiple phases, stop at the first unresolved gate.
- If confidence is not high enough to choose a durable note action, target, note type, or durable meaning safely, route to `dw-clarify-intent` before `dw-note-manager`.
- A visible `ready_for_note_manager` handoff with supplied relevant note context is enough to route into `dw-note-manager`; the approval gate applies to the resulting draft or durable write.
- A sufficiently specific direct coding request may route directly to `project-implementer` when objective, scope, constraints, and intended behavior are clear enough.
- Planning is downstream from note-backed project state; clarification should not default to a planner-shaped artifact.

## Dynamic Skills, Hard Gates
Skills may reason dynamically inside their own role.
Phase transitions are strict gates.

Private reasoning does not satisfy a gate.
When a gate requires a clarification state, context handoff, draft, review report, packet, or approval, that artifact or decision must be visible in the conversation or in an approved workflow file before the next phase begins.
For the clarification-to-note-management boundary, a visible `ready_for_note_manager` handoff satisfies the phase-transition artifact requirement.

Hard-gate artifacts must be persisted to disk when produced, not only stated in the conversation. Write each artifact to `docs/Reports/in-flight/` when created:
- `ready_for_note_manager` handoff -> `docs/Reports/in-flight/handoff-<slug>.md`
- approved implementation packet -> `docs/Reports/in-flight/packet-<slug>.md`
- implementation report -> `docs/Reports/in-flight/report-<slug>.md`

A conversation-only artifact does not satisfy a gate requirement after compaction; only the disk copy is authoritative.
When the user has requested or accepted a durable note change and the supplied note context is sufficient, the agent should invoke `dw-note-manager` in the same turn by default; separate user approval is required for the resulting draft or durable write, not merely for calling `dw-note-manager`.

Hard gate sequence:
- raw idea, complex prompt, ambiguous request, or low-confidence durable note decision -> `dw-clarify-intent`
- visible `ready_for_note_manager` clarified context handoff -> `dw-note-manager` draft
- approved note-manager draft and clear workflow authorization -> durable note write
- note-backed implementation need -> `project-planner`
- approved packet or sufficiently specific direct coding request -> `project-implementer`
- implementation-like changes -> `implementation-verifier` when verification is requested, required, or materially useful before closeout
- completed implementation or bounded maintenance task -> `project-review-sync`

### Session Continuity After Compaction
When returning to in-progress work and recent conversation has been compressed, read `active-context.md` before proceeding. Do not trust recovered conversation snippets as the ground truth for workflow state. The `active-context.md` file and the in-flight artifacts it references are authoritative.

Dynamic routing should improve the quality of the current phase.
It must not be used to complete multiple phases silently.

When a prompt contains multiple domains, areas, or branching ideas, `dw-clarify-intent` should split it into provisional subject bundles before downstream work.
This split is intake evidence, not final note structure; `dw-note-manager` decides concrete note actions from a ready handoff plus supplied relevant note context.

Durable writes are never inferred from isolated wording.
The agent must evaluate the full prompt, current workflow state, user intent, risk, and whether required upstream gates are satisfied.
If direct-write authorization is ambiguous, default to draft-only output.

Durable note mutation rule:
- any durable note create, update, metadata edit, status change, link change, archival change, schema/governance note edit, or correction must route through `dw-note-manager`
- raw direct durable note edits are not allowed as an independent shortcut
- file-edit tools may apply the resulting note-manager decision, but they do not replace the note-manager gate
- this applies even when the requested change appears small, obvious, or purely mechanical

File change approval rule:
- before editing any file, the agent must prompt the user for approval and summarize the intended change
- for wording-sensitive files, including workflow rules, reusable skills, governance docs, prompts, schemas, and `AGENTS.md` files, the agent should provide exact proposed wording or a patch-shaped draft before editing
- the agent may apply very small mechanical corrections directly only when the change is low-risk and does not alter behavior, meaning, workflow gates, architecture, or public interfaces
- when unsure whether a change qualifies as a very small correction, ask before editing

## Common Workflow Shapes
These are common paths, not mandatory full sequences.
Use the smallest valid path that satisfies the current gate, and stop at the first unresolved gate.

For ideas and durable note work:

```text
idea -> dw-clarify-intent -> ready_for_note_manager handoff -> dw-note-manager draft -> approved durable write when authorized
```

For clear durable note mutation requests:

```text
clear bounded note request -> dw-note-manager draft -> approved durable write when authorized
```

For note-backed implementation:

```text
note-backed need -> project-planner -> approved packet -> project-implementer -> implementation report -> implementation-verifier when needed -> project-review-sync
```

For clear direct coding requests:

```text
sufficiently specific direct request -> project-implementer -> implementation report -> implementation-verifier when needed -> project-review-sync
```

For documentation sync after implementation:

```text
project-review-sync -> dw-clarify-intent when durable note decisions are needed -> ready_for_note_manager handoff -> dw-note-manager draft
```

For maintenance review:

```text
bounded maintenance request -> project-review-sync -> dw-clarify-intent or follow-up planning when needed
```

## Documentation Rules

### Required Artifacts
The workflow should revolve around stable markdown artifacts.

Core artifacts:
- `project-hub.md`
- `architecture-hub.md`
- `priority-queue.md`
- `decision-log.md`
- `active-context.md` — workflow-state pointer

`active-context.md` is the single source of truth for current workflow state. It must record:
- `current_phase`: the active workflow phase
- `current_gate`: the gate that must be satisfied before the next phase
- `last_handoff_path`: path to the most recent `ready_for_note_manager` handoff file
- `last_packet_path`: path to the most recent approved implementation packet
- `last_report_path`: path to the most recent implementation or review report

Skills must read `active-context.md` on entry when workflow state is relevant and update it on exit when workflow state changes.

Task artifacts:
- feature notes
- task notes
- implementation packets
- implementation reports
- follow-up notes

Governance artifacts:
- tool policy
- output schemas
- workflow playbooks

### Note Quality
Important notes should clearly signal their role, such as project hub, architecture note, feature note, task note, decision note, implementation report, constraint note, or priority item.

Notes should link intentionally. A note should usually link upward to a hub and sideways to relevant notes when the relationship is operationally important.

Prefer formats that are easy to revise incrementally.
Do not regenerate large bodies of text unless necessary.

Documentation updates after implementation should be traceable to a task, report, or decision.

## Tooling Policy

### Default Policy
- clarification and planning roles: read docs, inspect relevant project context, and prepare context for downstream note work
- `dw-note-manager`: read docs, update docs, inspect relevant project context, and own durable note mutation
- clarification, planning, review, and other workflow roles must use shared `note-search` as the default note search/retrieval tool; they provide task context while `note-search` chooses graph or semantic mode and formulates any semantic query
- implementation role: edit code, inspect files, run checks, produce report
- review role: inspect code and docs, suggest or apply scoped sync routing

### Guardrails
Agents should not:
- delete or rewrite large documentation areas without explicit reason,
- make broad project changes outside stated scope,
- directly mutate durable notes outside `dw-note-manager`,
- silently change project conventions,
- invent missing decisions that should be escalated,
- claim completion without verification notes.

### Verification Preference
When possible, verify with:
- tests,
- lint/typecheck,
- build or compile checks,
- command output,
- file diffs,
- explicit note updates.

## Shared Skill Policy

All dev-workflow skills inherit these base rules. Skills reference rather than repeat them and may add role-specific constraints on top.

### Local Authority
Read the active workspace's `AGENTS.md` first when it exists and treat it as the repository-local operating contract.
Apply each skill beneath that local authority.
If no local `AGENTS.md` exists, use the skill's own contract as the default for that role.

### Portability
Skills must work across repositories. Do not rely on files from a workflow-design repository, a fixed folder structure, specific note names the local project does not define, or undocumented project conventions.

### Vocabulary
Label sets for this workflow are defined in `vocabulary.md` at the mode root (installed alongside `AGENTS.md`).
Use those labels for note status, uncertainty, clarification state, packet status, verification outcomes, and review dispositions.
Skills define decision criteria, transition logic, and output shapes on top of the labels; they do not redefine or vary the labels themselves.

## Git Governance
Git is the default review and change-boundary mechanism when the project is a git repository.

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
- implementation or review reveals that the approved packet is no longer sufficient,
- or required workflow or shared skills are missing.

Escalation should be concise and explicit.
State:
- the conflict or uncertainty,
- the decision needed,
- the impacted area,
- the recommended next step.

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
- rework caused by unclear intent.

## Definition of Failure
The system is failing if:
- agents implement before intent is clear,
- agents implement before a task packet is explicitly approved,
- documentation becomes decorative instead of operational,
- implementation reports are vague or missing,
- high-impact decisions are made implicitly,
- context packets grow bloated and noisy,
- or the human stops trusting the notes as current state.

## Repo Specific Instructions
Add project-specific instructions below the `atlas-dev-workflow-bridge:end` marker so Atlas sync preserves them.

Use this area for:
- local verification commands,
- coding conventions,
- architecture constraints,
- security or privacy rules,
- ownership boundaries,
- deployment or release rules,
- project-specific documentation paths,
- exceptions to default workflow assumptions.

Local project instructions below the managed Atlas block override reusable `dev-workflow` guidance when they conflict.
<!-- atlas-dev-workflow-bridge:end -->
