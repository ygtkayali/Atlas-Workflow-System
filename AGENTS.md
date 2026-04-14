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
- reading the approved task packet,
- inspecting code and relevant files,
- making scoped changes,
- running checks,
- producing a structured implementation report.

This role should optimize for correct, limited execution.
It should not redefine project goals or silently rewrite architecture.
It must not begin from an unapproved packet or an informal request alone.

### Review / Sync Agent
Responsible for:
- comparing implementation results to the task packet,
- updating or proposing documentation updates,
- surfacing mismatches,
- suggesting follow-up tasks,
- marking stale notes or decision gaps,
- and recommending whether the implementation should be kept, revised, or rejected.

---

## Active Skill State

### `clarify-intent`
Use `clarify-intent` for early-stage ideas and ambiguous requests before durable note creation or planning begins.

Current expectations:
- it acts as a guided clarification and challenge loop, not as a planner,
- it should separate user goals from proposed solutions,
- it should surface hidden inconsistencies, missing decisions, weak assumptions, and high-impact uncertainty,
- it should keep work in clarification when note creation or planning would still require guesswork,
- and its default successful output for this repository is a `note-ready handoff`, not a planning brief by default.

### `note-creation`
Use `note-creation` after clarification has produced durable signal and the user has supplied the relevant note paths or notes needed for the change.

Current expectations:
- it performs bounded note `create` or `update` work only,
- it should use the local templates when they apply,
- it should read only the provided relevant notes and avoid broad vault discovery,
- it should work conservatively with `Idea Note`, `General Note`, and `Sub Hub`,
- it should draft first and wait for confirmation before writing unless the user explicitly asks for direct writes,
- and it should return work to `clarify-intent` when the durable subject, note type, or target placement is still unclear.

### Downstream implication
Planning is no longer the default direct output of clarification.

The active workflow is:
`idea -> clarify-intent -> note-ready handoff -> note-creation`

Planning remains downstream, but it should consume note-backed project state rather than relying on a planner-oriented clarification artifact by default.

---

## Base Workflow

### Phase 1: Clarify intent
A task begins from a human-written note, task request, idea note, or feature note.

Expected outcome:
- clarified intent,
- relevant constraints,
- known uncertainties,
- initial scope,
- and either a continued clarification state or a note-ready handoff.

### Phase 2: Create or update durable notes
The note-creation step turns clarified intent into bounded durable note work.

Expected outcome:
- a small set of durable note creates or updates,
- minimal metadata and intentional links,
- conservative note typing,
- and explicit refusal to proceed when note placement or note type is still unclear.

### Phase 3: Prepare implementation packet
The planner/documentation agent creates a task packet from note-backed project state when implementation planning is actually needed.

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

### Phase 6: Implementation report
The implementer agent returns a structured report.

### Phase 7: Review and sync
The review/sync agent compares the implementation to the approved packet, updates or proposes documentation changes, flags mismatches, and produces a recommendation for human closeout.

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
- clarification, note-creation, and planning roles: read docs, update docs, inspect relevant repo context
- implementation role: edit code, inspect files, run checks, produce report
- review role: inspect code + docs, suggest or apply scoped doc updates

### Guardrails
Agents should not:
- delete or rewrite large documentation areas without explicit reason,
- make broad repo changes outside stated scope,
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
- and explicit about whether the next step is more clarification, note creation, or planning.

### Note-creation output should be:
- bounded,
- conservative about note structure,
- explicit about whether the action is `create` or `update`,
- based only on the provided relevant notes plus local templates,
- and draft-first unless the user explicitly requests direct writes.

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
- docs updated,
- docs still stale,
- new decision candidates,
- follow-up tasks,
- priority changes if warranted,
- and a recommended disposition: `keep`, `revise`, or `reject`.

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
- `clarify-intent` produces a `note-ready handoff` by default when clarification succeeds,
- `note-creation` is the bounded durable note step before planner work,
- planning should begin from note-backed project state when implementation is actually needed,
- and the existing governance, role, and schema notes should remain consistent with this charter.
