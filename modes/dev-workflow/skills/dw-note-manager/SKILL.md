---
name: dw-note-manager
description: Manage bounded note create/update work from a clarified context handoff plus user-supplied relevant notes. Use when Codex needs to decide, draft, or apply a bounded note action after clarification, especially in note-centered workflows that want explicit confirmation, template-based notes, and no autonomous vault retrieval or reorganization.
---

# Note Manager

Perform bounded note-mutation work from clarified input without turning into a vault-management system.

Use this skill after clarification has produced durable signal and the user has supplied the relevant notes or note paths needed for the change.
Do not use it as the first step for a note-action request; route the work through clarification at least once before this skill acts.
Any durable note mutation must use this skill, including metadata-only fixes, status changes, schema/governance note edits, link changes, small corrections in durable notes, and archival changes.
Do not make raw direct durable note updates outside `Note Manager`.

## Local Authority

If the active workspace contains a local `AGENTS.md`, read it first and treat it as the repository-local operating contract.
Apply this skill beneath that local authority.

If no local `AGENTS.md` exists, use the user request, the clarified context handoff, and the provided notes as the operating context.

## Responsibilities

Do:
- read the clarified context handoff,
- route behavior using an explicit `owner` field in the input context when the local workflow provides one,
- read only the specific relevant notes the user provides,
- consume supplied `note-search` context capsules as upstream context when provided,
- read the local note templates when they exist,
- decide whether the bounded action is `create` or `update`,
- decide note type, target note, title, links, and final durable note structure from the provided context,
- use the local note-type tags when the project provides them, especially `[[idea-note]]`, `[[feature-subject-note]]`, and `[[design-note]]`,
- choose folder placement only from the provided context, local folder policy, or local `AGENTS.md`, treating folder placement as readability rather than governance,
- refresh dynamic metadata on every create or update so status and other changing header fields reflect the current note state rather than stale template or prior values,
- evaluate context drift on every update, including whether status should become `[[status-draft]]`, `[[status-active]]`, `[[status-pending]]`, `[[status-settled]]`, or `[[status-archived]]`,
- draft exact note content or exact update content,
- keep note bodies meaningful and durable,
- consume and preserve the handoff's `Interpretation Basis` when it affects intent, tone, uncertainty, or traceability,
- preserve the original input or upstream artifact especially when the clarified context handoff exists only as transient conversation state, using a link, excerpt, concise basis note, or intentional redaction as appropriate,
- preserve the question-based nature of `[[idea-note]]` content when the handoff is exploratory,
- preserve local design-choice trails inside `[[feature-subject-note]]` notes instead of moving every decision into a separate design note,
- use the minimum useful links needed for the provided context,
- prefer intentional related links over default parent placement,
- split or group subjects conservatively using the v1 note rules,
- produce a subject-to-note action manifest before drafting when the clarified context contains multiple durable subjects,
- treat `Main Hub` as an explicit lightweight index role rather than the default destination for new notes,
- and wait for confirmation before writing unless the prompt and current workflow state clearly authorize direct writes.

Do not:
- search the vault broadly for related notes,
- run semantic search as its own discovery step,
- silently choose unrelated notes to edit,
- allow raw direct durable note updates outside this role,
- rename, move, or reorganize notes,
- invent a richer metadata or linking system,
- act without at least one prior clarification pass,
- create notes from weak clarification state,
- convert unresolved ideas into recommendations, policy, decisions, or settled direction unless the handoff explicitly marks those points as decided,
- default new notes into a top-level hub,
- treat hierarchy as required note structure,
- infer note meaning, ownership, or governance from folders alone,
- create domain hierarchy folders when links, tags, hubs, or backlinks are the intended structure,
- or preserve every conversational detail just because it was discussed.

## Required Inputs

Begin from:
- an explicit upstream artifact such as a clarified context handoff,
- the relevant notes or note paths supplied by the user,
- and the local templates when the project uses them.

If any of these are missing, do not guess through the gap.

Escalate back to clarification when:
- the request has not yet passed through clarification at least once,
- the upstream input is raw review-sync output, implementation context, or another note-change proposal that has not been clarified,
- the durable subject is still weak,
- the supplied context is insufficient to choose a note type responsibly,
- the requested update depends on notes that were not provided,
- or the correct note action cannot be determined without broader vault discovery.

## Context Selection

Load context in layers and stop when it is sufficient.

Preferred order:

1. Read the local `AGENTS.md` if it exists.
2. Read the clarified context handoff.
3. Read the specific note files or note paths supplied by the user.
   Supplied context may include a semantic `note-search` context capsule, but `Note Manager` should not run search as its own discovery step.
4. Read the local note templates that match the chosen or strongly indicated note type.
5. Read [references/v1-note-rules.md](references/v1-note-rules.md) when note splitting, grouping, or type selection needs a closer pass, especially when choosing between hub roles and local note-type tags.

Avoid broad repository scans. This skill should shape a bounded note action, not discover the whole vault.

When `dw-clarify-intent` produces a visible `ready_for_note_manager` handoff for a required note change and the relevant note context is supplied, proceed into this workflow by default without waiting for separate phase-switch approval. The approval gate applies to the resulting draft or durable-write decision.

## Workflow

Follow this sequence:

1. Identify the durable subject from the clarified context handoff.
2. Confirm that the current request has already passed through clarification at least once.
3. Confirm the candidate action: `create` or `update`.
4. Choose and justify the note type, preferring local note-type tags such as `[[idea-note]]`, `[[feature-subject-note]]`, or `[[design-note]]` when they exist.
5. Read only the provided notes needed for the action.
6. Decide whether the subject belongs in one note or a small obvious set of notes.
   If the handoff contains provisional subject bundles, use them as input evidence rather than final note structure.
7. Refresh dynamic metadata fields for the current note state instead of preserving stale template or previously copied values.
8. Draft the exact note content or exact update content.
9. Make the minimum useful related links from the provided context and use parent placement only when explicitly justified.
10. Present the draft and wait for confirmation before writing.

If any step depends on unprovided context or unclear structure, stop and escalate instead of improvising.
If the input did not pass through `dw-clarify-intent`, route it there first and wait for a clarified context handoff before drafting note content.

## Bundled Intake

`Note Manager` may receive a bundle of clarified durable subjects from upstream context.

A bundle is allowed for intake efficiency, but it must not collapse note-action approval.
Before drafting note content from a bundle, `Note Manager` must produce a subject-to-note action manifest.

If the upstream artifact contains provisional subject bundles from complex-prompt intake, treat them as input evidence rather than final note structure.
Each bundle should contain one domain or area; branching ideas should remain together only when they are closely related.
If a branch can become its own durable subject, split it and preserve the connection instead of blending it into a broader note action.

The manifest should include one row per proposed note action:
- subject id or subject label,
- target note, if known,
- action: `create`, `update`, `defer`, or `return-to-clarification`,
- why this note is the right target,
- source basis from the clarified context,
- interpretation basis that must be preserved or validated,
- relevant context for this note action,
- excluded or non-applicable context when separation matters,
- status: `ready`, `needs_clarification`, or `deferred`.

The relationship between clarified subjects and note actions is not one-to-one:
- one clarified subject may produce zero, one, or many note actions,
- one note action must target exactly one durable note,
- multiple subjects may support one note action only when that relationship is explicit in the manifest.

`dw-clarify-intent` owns semantic subject separation.
`Note Manager` owns subject-to-note mapping, note action choice, target note choice, note type, metadata, links, and final draft structure.
When a handoff includes `Interpretation Basis`, use it as source basis for the note action and preserve the parts needed to validate intent later.
Do not discard original input, tone or stance, user-intent versus agent-inference boundaries, open ambiguity, or things not to imply when those fields affect the durable note's meaning.

Only manifest rows marked `ready` may become note drafts.
Each resulting note draft must be presented and approved separately before writing.
Approval for one note action does not approve any other note action in the same bundle.

If `Note Manager` cannot map a clarified subject to note actions without mixing unrelated context, guessing target notes, or relying on raw implementation evidence, return that subject to clarification instead of drafting.

## Dynamic Metadata Rules

Refresh dynamic metadata for every durable note mutation.

At minimum, evaluate:
- `Status`,
- `Type`,
- `Last Reviewed`,
- `Related`,
- `Parent`,
- `Tasks`,
- and `Decisions`.

Use only approved status tags:
- `[[status-draft]]`,
- `[[status-active]]`,
- `[[status-pending]]`,
- `[[status-settled]]`,
- `[[status-archived]]`.

Status drift must be handled explicitly:
- use or evaluate `[[status-archived]]` when a note becomes historical, legacy, deprecated, replaced, or no longer part of active working context,
- use or evaluate `[[status-settled]]` when a note has been worked through and remains active reliable context,
- use or evaluate `[[status-active]]` when an idea note has been promoted out of draft/backlog and is now active working context but not yet settled,
- use or evaluate `[[status-draft]]` when a note is still forming,
- use or evaluate `[[status-pending]]` when a note remains relevant but deferred.

Do not preserve stale metadata just because the body edit is small.

## Note-Type Selection

Prefer the local dev-workflow note-type tags when they exist:
- `[[idea-note]]` for draft ideas, future plans, exploratory questions, and possible directions that are not yet active durable project subjects. These notes usually live in `docs/Idea Backlog/` and should not depend on a separate idea hub.
- `[[feature-subject-note]]` for promoted project subjects that started as ideas and are now active or settled project knowledge. Use this for one feature, workflow behavior, implementation concept, or action area. Preserve the subject's own design choices, technical details, implementation notes, open questions, and related tasks or reports in the note.
- `[[design-note]]` for coherent design areas or cross-cutting system behavior. Use this when the design spans multiple feature subject notes, constrains future work, or should explain how a related feature set works from one place.

Keep this structural role available:
- `Main Hub` only for a lightweight top-level index role. It should stay mostly empty, should not become the primary hierarchical center of the vault, and should usually link to stable workflow entry points rather than broadly across the note graph.

Do not use `General Note` as a normal fallback in `dev-workflow`.
The `[[feature-subject-note]]` template is the default durable subject template for notes that would previously have been generic durable notes.

Do not expose `Sub Hub` as a normal note-creation path in `dev-workflow`.
When a related subject set needs one shared explanation, prefer a `[[design-note]]`; its links to related subject notes provide the natural organizing layer.

`[[idea-note]]` content should preserve live thinking.
When the source handoff is exploratory, use questions, tensions, candidate options, assumptions to test, branching thoughts, and unresolved decisions as first-class content.
Do not smooth these into recommendations or settled direction unless the handoff explicitly marks them as decided.

When promoting an idea, prefer creating or updating a `[[feature-subject-note]]` rather than a `[[design-note]]`.
Use a `[[design-note]]` later when an active or settled feature set needs a broader design explanation.
A design note does not replace the local `Design Choices` or equivalent decision trail inside the feature subject notes.

Do not use `Sub Hub` as a generic wrapper for every small topic cluster.
Do not promote a note to `Main Hub` just because it is high-level.
If a future project truly needs a hub-like note beyond the starter main hubs, escalate instead of silently creating a sub hub.

## Vault Folder Handling

Treat vault folders as a readability layer for the human, not as the main governance model for the note system.

The primary governance model is:
- note metadata,
- status tags,
- intentional links,
- backlinks when relevant,
- and explicit one-way or two-way note relationships.

Folder placement and note type are separate concepts.
A note's operational meaning should come from its role, metadata, links, and supplied context, not from its folder alone.

When a vault has a local folder policy, follow it only as a placement/readability rule.
For the current dev-workflow structure, the base folders are:
- `Idea Backlog` for `[[idea-note]]` notes and early capture,
- `Durable Notes` for active or settled project knowledge such as `[[feature-subject-note]]` and `[[design-note]]` notes,
- `Tasks` for implementation packets and task-facing workflow artifacts,
- `Reports` for implementation, verification, and review/sync reports,
- `Tags` for note-based tags,
- `Main Hubs` for hub notes,
- and `Templates` for note and artifact templates.

Project-specific folders may be valid when the project type benefits from them, such as `Tests`, `Features`, or `Reports`.
Those folders should be proposed or constrained by the project's local `AGENTS.md` or supplied project context.

Do not create domain hierarchy folders such as `Backend notes` just to group related subjects.
Domain grouping should be handled through links, tags, hubs, and backlinks unless the user or local project policy explicitly approves a readability folder for that project type.

## Output Contract

Default output should be a draft-first note action.
Direct durable writes require both satisfied upstream gates and clear authorization from the prompt and current workflow state.
If write authorization is ambiguous, produce draft-only output.

When the action is `create`, provide:
- note action,
- note type,
- proposed title,
- proposed related links from the provided context,
- proposed parent link only when explicitly justified by the provided context,
- refreshed dynamic metadata appropriate for the new note state,
- and the full draft note body.

When the action is `update`, provide:
- note action,
- target note,
- why this note is the correct target,
- refreshed dynamic metadata appropriate for the updated note state,
- and the exact proposed updated content or patch-shaped replacement text.

If the request should return to clarification, state:
- the blocking ambiguity,
- why `Note Manager` would be guesswork,
- and the minimum clarification needed next.

## Output Style

Keep outputs:
- bounded,
- explicit,
- conservative about structure,
- and clear about what is drafted versus what is already decided.

Do not hide uncertainty inside polished note prose.
Do not silently expand a local note edit into vault maintenance.

## Final Check

Before finishing, check:
- Is the subject durable enough to merit a note?
- Is the note type justified?
- Is the action clearly `create` or `update`?
- Is the draft based only on provided context plus local templates?
- If this is an `Idea Note`, did I preserve unresolved questions instead of converting them into conclusions?
- If the handoff was complex, did I avoid treating provisional subject bundles as final note structure without evaluation?
- Were dynamic metadata fields refreshed so status and other changing headers are current rather than stale?
- Does `Status` match the current body and role of the note, especially for legacy or archived notes?
- Do `Last Reviewed`, `Related`, `Parent`, `Tasks`, and `Decisions` still match the updated note?
- Are links minimal and intentional?
- Would this note still be useful beyond the current chat?
- Should this be one note, or a small obvious set of notes?
- Is any durable write clearly authorized by the prompt and workflow state, or should the output remain draft-only?

If any answer is no, refine the draft or return the work to clarification.
