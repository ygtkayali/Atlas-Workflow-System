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
The active Atlas configuration lives in `atlas.yaml`.

## Core Principles

- Human Authority: Humans approve intent, architecture, scope, priorities, and irreversible decisions.
- Agents must not silently decide:
	- architecture changes,
	- schema or API contract changes,
	- dependency additions with broad impact,
	- security/privacy-sensitive behavior,
	- changes that conflict with documented constraints.
- Documentation is operational workflow state, not passive reference.
- Prefer compact, structured, updateable notes over long generic prose.
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

Start from the operational entry points:
- `context-map.md` for project structure, authoritative docs, and recommended context paths,
- `docs/In-flight/` for active task lanes, gates, reports, and next actions.

Read only the relevant in-flight artifacts, not the whole folder by default.

If more note context is needed, use `note-search` from a known seed note, task subject, or semantic query instead of broad manual vault discovery.

Then load the smallest useful supporting context:
- active feature or project subject,
- related architecture notes,
- current decisions,
- active task note,
- recent implementation reports,
- relevant constraints.

Stop once the current phase has enough context to proceed safely.

### Confidence-Based Gating
Every implementation task must pass through an explicit approval gate before coding begins.

For routine direct coding requests, the user's explicit request may itself serve as that approval artifact when the objective, scope, constraints, and intended behavior are clear enough for safe implementation.

Planner output should make confidence visible so the human can decide whether to approve, revise, defer, or reject the packet.
	Confidence does not replace approval.

## Runtime Workflow Router

`AGENTS.md` is the runtime routing authority for dev-workflow projects.
Use it to choose the first workflow phase, then follow the selected skill's `SKILL.md` for detailed procedure.

## Skill Router

| Situation | Skill |
| --- | --- |
| Ambiguous, overloaded, early-stage, or solution-led request | `dw-clarify-intent` |
| Read docs. create/update notes, metadata edit, status/link/archive/schema/governance change, or correction.  | `dw-note-manager` |
| Note-backed implementation planning | `project-planner` |
| Approved packet or clear direct coding request | `project-implementer` |
| Verification before closeout | `implementation-verifier` |
| Completed implementation review, documentation-sync routing, or bounded maintenance review | `project-review-sync` |
| Note retrieval needed by any workflow role | shared `note-search` helper |

### Routing Rules

- Choose the smallest valid skill sequence and stop at the first unresolved gate.
- Use `note-search` for note-related retrieval instead of broad manual vault discovery.
- A sufficiently specific direct coding request may route directly to `project-implementer` when objective, scope, constraints, and intended behavior are clear enough.
- If confidence is not high enough to choose a durable note action, target, note type, or durable meaning safely, route to `dw-clarify-intent` before `dw-note-manager`.
- Durable note mutations must route through `dw-note-manager`. File-edit tools may apply an approved note-manager decision, but they do not replace that gate.

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

### Vocabulary
Label sets for this workflow are defined in `docs/vocabulary.md` in the workflow vault.
Use those labels for note status, uncertainty, clarification state, packet status, verification outcomes, and review dispositions.
Skills define decision criteria, transition logic, and output shapes on top of the labels; they do not redefine or vary the labels themselves.

## Git Governance

When the project is a git repository, use git as the change boundary.

Before staging, committing, or making broad edits:
- check `git status`,
- preserve unrelated user changes,
- and keep the task's changes separate from unrelated work.

Agents may create commits only when the user explicitly asks for a commit or an approved task packet authorizes it.

Before committing:
- stage only files related to the current task,
- review the staged diff,
- run the strongest practical checks for the changed area,
- and summarize what is being committed.

Agents must not use destructive git commands, amend commits, revert unrelated work, or hide missing verification without explicit approval.

After committing, report the commit hash.

Preferred commit message shape:

```text
<type>: <short imperative summary>

Context:
- <why this change exists>

Changes:
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
## Escalation
  - Escalate when a task conflicts with documented constraints, requires architecture/schema/API/security decisions, lacks enough confidence to choose the next gate, exceeds approved scope, or depends on missing/contradictory documentation.
  - State the uncertainty, decision needed, impacted area, and recommended next step.
## Repo Specific Instructions
- Add project-specific instructions below the `atlas-dev-workflow-bridge:end` marker so Atlas sync preserves them.
- Local project instructions below the managed Atlas block override reusable `dev-workflow` guidance when they conflict.
<!-- atlas-dev-workflow-bridge:end -->

# Repo Specific Instructions
This repository is the Atlas Workflow System repository. It contains multiple reusable modes under `modes/`. This checkout itself is initialized as a `dev-workflow` project for development of the Atlas Workflow System. Use the root `atlas.yaml` to confirm the active mode for this repo.
## Where work belongs
Repo-specific plans, notes, implementation packets, reports, and project context belong under this repo's `docs/` vault. Mode-specific changes belong under the relevant `modes/<mode>/` source when they affect reusable mode behavior, including: - persistent folder structures, - managed files, - reusable rules, - reusable templates, - starter notes, - managed tags, - mode-specific skills, - mode-specific tools. Do not maintain reusable mode behavior in both a project copy and the mode source. Change the relevant `modes/<mode>/` source, then use Atlas sync in the project where that mode is used. For this repository's own workflow, the active mode is currently `dev-workflow`. When changing reusable behavior for that mode, update `modes/dev-workflow/` and sync it into this repo rather than manually maintaining both places.

## Operating policy 
Use the managed Atlas bridge above as the root operating policy for this repository. For runtime routing, start from the bridge's `Runtime Workflow Router`, preserve the hard gates, and then follow the selected skill's `SKILL.md` for detailed procedure.