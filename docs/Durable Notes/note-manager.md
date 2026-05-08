# Note Manager

Status: [[Tags/status-settled]]
Parent:
Related: [[clarify-intent]], [[clarified-context-handoff]], [[Two-Phase Workflow Boundary]], [[Durable Notes Follow Accepted Implementation]], [[Main Vault Note Structure and Agent Context]], [[Tags/idea-note]], [[Tags/feature-subject-note]], [[Tags/design-note]]
Created: 2026-04-14
Last Reviewed: 2026-05-08
Source: [[LLM Wiki Lossy Compression and Integrity Risks]]
Decisions: `Note Manager` must consume and preserve the handoff's `Interpretation Basis`, especially original input, when drafting or updating durable notes. It must prefer the local note-type tag model when creating or updating dev-workflow notes.
Dependencies:
Tasks:

---

## Summary

`Note Manager` is the bounded note-mutation role for the workflow.

Its job is to keep note creation and note updates behind one explicit gate so note logic can evolve in one place without spreading note-writing behavior across multiple roles.
It receives clarified context from upstream roles, then decides the concrete note action and durable note structure.
Every durable note mutation must pass through `Note Manager`.
Raw direct note edits are not allowed as an independent shortcut, even for metadata-only edits, status changes, link changes, archival changes, schema/governance note edits, or small corrections.

It should remain narrow in authority:
- it works from explicit upstream artifacts
- it uses only the provided note context
- it may consume search results supplied by upstream roles, including semantic `note-search` context capsules
- it does not turn into autonomous vault management
- it does not silently impose hierarchy or broader structure on the note space
- it treats folders as human readability aids, while note governance comes from metadata, tags, links, backlinks, and explicit relationships

## Responsibilities

- act as the single gate for bounded note creation and note updates
- own every durable note mutation, including metadata-only updates and corrections
- route behavior using an explicit `owner` field in the input context
- use only the specific relevant notes or note paths supplied by the user
- consume supplied `note-search` context capsules as upstream context when they are provided
- use local templates when they apply
- decide whether the correct bounded action is `create` or `update`
- decide note type, target note, title, note links, and final durable note structure from the provided context
- use local note-type tags when the project provides them, especially `[[idea-note]]`, `[[feature-subject-note]]`, and `[[design-note]]`
- choose folder placement only from the provided context, local folder policy, or local `AGENTS.md`, treating folder placement as readability rather than governance
- refresh dynamic metadata on every create or update so status and other changing header fields reflect the current note state rather than stale template or prior values
- evaluate context drift on every update, especially whether `Status` should move between `[[status-draft]]`, `[[status-active]]`, `[[status-pending]]`, `[[status-settled]]`, and `[[status-archived]]`
- draft exact note content or exact update content
- preserve the handoff's `Interpretation Basis` in the draft or update when it affects intent, tone, uncertainty, or traceability
- preserve the original input or upstream artifact especially when the clarified context handoff exists only as transient conversation state, using a link, excerpt, concise basis note, or intentional redaction as appropriate
- preserve the question-based nature of `[[idea-note]]` content when the handoff is exploratory
- preserve local design-choice trails inside `[[feature-subject-note]]` notes instead of moving every decision into a separate design note
- keep links minimal and intentional
- prefer intentional related links over default parent placement
- treat `Main Hub` as an explicit lightweight index role rather than the default destination for new notes
- avoid silently broadening note scope beyond the supplied context
- return work to clarification or review when the note mutation target is still unclear
- default to draft-only output when durable-write authorization is ambiguous in the prompt and workflow state

## Current Upstream Owners

For the current workflow, `Note Manager` should support these owners:

- `clarify-intent`
  uses a [[clarified-context-handoff]] as the upstream artifact for ideation-stage note creation or note updates

- `review-sync`
  routes accepted implementation context through `clarify-intent` first, then uses the resulting [[clarified-context-handoff]] for durable note updates

Additional owners may be introduced later, but this note should describe only the owners that are part of the current workflow.

## Supported Note Roles

For the current system, `Note Manager` should work with:
- `Main Hub`
- `Sub Hub`
- `[[idea-note]]`
- `[[feature-subject-note]]`
- `[[design-note]]`
- `General Note` as a fallback when the local typed model does not fit

The default emphasis remains on bounded updates to existing durable notes and on the local note-type tags used by the dev-workflow documentation system.

`Main Hub` remains a lightweight index role and should be chosen only when the clarified subject explicitly calls for an index note rather than a normal durable knowledge note.

`[[idea-note]]` preserves live thinking.
When the source handoff is exploratory, unresolved questions, tensions, candidate options, branching thoughts, assumptions to test, and unresolved decisions are first-class note content.
`Note Manager` must not convert them into recommendations, policy, or settled direction unless the handoff explicitly marks those points as decided.

`[[feature-subject-note]]` is the normal promotion target for an idea that becomes active or settled project knowledge.
It should preserve the local thought process for one feature, workflow behavior, implementation concept, or action area, including discovered design choices, technical details, implementation notes, open questions, and related tasks or reports.

`[[design-note]]` is for coherent design areas or cross-cutting system behavior.
It should be used when the design spans multiple feature subject notes, constrains future work, or should explain how a related feature set works from one place.
A design note does not replace the design-choice trail inside the relevant feature subject notes.

## Vault Folder Handling

`Note Manager` should treat vault folders as a readability layer for the human, not as the main governance model for the note system.

The primary governance model is:
- note metadata
- status tags
- intentional links
- backlinks when relevant
- explicit one-way or two-way note relationships

Folder placement and note type are separate concepts.
A note's operational meaning should come from its role, metadata, links, and supplied context, not from its folder alone.

When a vault has a local folder policy, `Note Manager` should follow it only as a placement/readability rule.
For the current dev-workflow structure, the base folders are:
- `Idea Backlog` for `[[idea-note]]` notes and early capture
- `Durable Notes` for active or settled project knowledge such as `[[feature-subject-note]]` and `[[design-note]]` notes
- `Tasks` for implementation packets and task-facing workflow artifacts
- `Reports` for implementation, verification, and review/sync reports
- `Tags` for note-based tags
- `Main Hubs` for hub notes
- `Templates` for note and artifact templates

Project-specific folders may be valid when the project type benefits from them, such as `Tests`, `Features`, or `Reports`.
Those folders should be proposed or constrained by the project's local `AGENTS.md` or supplied project context.

`Note Manager` should not create domain hierarchy folders such as `Backend notes` just to group related subjects.
Domain grouping should be handled through links, tags, hubs, and backlinks unless the user or local project policy explicitly approves a readability folder for that project type.

## Input Expectations

`Note Manager` should begin from:
- an explicit upstream artifact,
- the relevant notes or note paths supplied for the note action,
- and local templates when the target note type uses them.

It should not guess through missing upstream context.

Examples:
- from `clarify-intent`: a [[clarified-context-handoff]]
- from `review-sync`: a [[clarified-context-handoff]] produced by `clarify-intent` from implementation-backed review context

If the owner sends raw implementation context, review output, or a note-change proposal that has not passed through `clarify-intent`, `Note Manager` should route that input to `clarify-intent` first.
If the owner, target note, or intended note mutation is still unclear after clarification, `Note Manager` should stop and return the work to the upstream role rather than improvising structure.

For `clarify-intent` input, the upstream artifact should preserve clarified context, not prescribe final note structure.
`Note Manager` is responsible for deciding whether that context becomes a new note, an update to an existing note, or a request for more clarification.
When the handoff contains an `Interpretation Basis`, `Note Manager` should use it as source basis for the note action and preserve the parts needed to validate intent later.
At minimum, it should not discard original input, tone or stance, user-intent versus agent-inference boundaries, open ambiguity, or things not to imply when those fields affect the durable note's meaning.
When `clarify-intent` produces a visible `ready_for_note_manager` handoff for a required note change and the relevant note context is supplied, `Note Manager` should be called by default without waiting for separate phase-switch approval.
The required approval gate is the `Note Manager` draft or durable-write decision.

If the user or another role asks for a note edit directly, `Note Manager` should treat that as a note-mutation request and take ownership of the update.
It should not allow the agent to bypass this role by describing the change as a small patch, metadata fix, typo correction, schema adjustment, or governance edit.

## Bundled Intake

`Note Manager` may receive a bundle of clarified durable subjects from upstream context.

A bundle is allowed for intake efficiency, but it must not collapse note-action approval.
Before drafting note content from a bundle, `Note Manager` must produce a subject-to-note action manifest.

If the upstream artifact contains provisional subject bundles from complex-prompt intake, `Note Manager` should treat them as input evidence rather than final note structure.
Each bundle should contain one domain or area; branching ideas should remain together only when they are closely related.
If a branch can become its own durable subject, split it and preserve the connection instead of blending it into a broader note action.

The manifest should include one row per proposed note action:
- subject id or subject label
- target note, if known
- action: `create`, `update`, `defer`, or `return-to-clarification`
- why this note is the right target
- source basis from the clarified context
- interpretation basis that must be preserved or validated
- relevant context for this note action
- excluded or non-applicable context when separation matters
- status: `ready`, `needs_clarification`, or `deferred`

The relationship between clarified subjects and note actions is not one-to-one:
- one clarified subject may produce zero, one, or many note actions
- one note action must target exactly one durable note
- multiple subjects may support one note action only when that relationship is explicit in the manifest

`clarify-intent` owns semantic subject separation.
`Note Manager` owns subject-to-note mapping, note action choice, target note choice, note type, metadata, links, and final draft structure.

Only manifest rows marked `ready` may become note drafts.
Each resulting note draft must be presented and approved separately before writing.
Approval for one note action does not approve any other note action in the same bundle.

If `Note Manager` cannot map a clarified subject to note actions without mixing unrelated context, guessing target notes, or relying on raw implementation evidence, it must return that subject to clarification instead of drafting.

## Dynamic Metadata Rules

`Note Manager` must refresh dynamic metadata for every durable note mutation.

At minimum, it should evaluate:
- `Status`
- `Type`
- `Last Reviewed`
- `Related`
- `Parent`
- `Tasks`
- `Decisions`

Status should come from the approved status registry:
- `[[status-draft]]`
- `[[status-active]]`
- `[[status-pending]]`
- `[[status-settled]]`
- `[[status-archived]]`

Status drift must be handled explicitly:
- if a note becomes historical, legacy, deprecated, replaced, or no longer part of active working context, evaluate `[[status-archived]]`
- if a note becomes active and reliable after being worked through, evaluate `[[status-settled]]`
- if an idea note is promoted out of draft/backlog and is now active working context but not yet settled, evaluate `[[status-active]]`
- if a note is still forming, evaluate `[[status-draft]]`
- if a note remains relevant but deferred, evaluate `[[status-pending]]`

The final check for any note update must include:
- does `Status` match the current body and role of the note?
- does `Last Reviewed` reflect the current review date when the note was meaningfully evaluated?
- do `Related` and `Parent` links still describe the note's current role?
- does `Type` match the note's current role when the local project uses note-type tags?
- did the update introduce stale `Tasks` or `Decisions` metadata?

## Output

The default output is a draft-first note action.
Direct durable writes require satisfied upstream gates and clear authorization from the full prompt and current workflow state.
Durable writes should not be inferred from isolated wording.
If authorization is ambiguous, remain draft-only.

When the action is `create`, it should provide:
- note action
- note type
- proposed title
- proposed related links
- proposed parent link only when explicitly justified by the provided context
- refreshed dynamic metadata appropriate for the new note state
- full draft note body

When the action is `update`, it should provide:
- note action
- target note
- why that note is the correct target
- refreshed dynamic metadata appropriate for the updated note state
- exact updated content or patch-shaped replacement text

Future merge or relink behavior may be added later, but it is not required as part of the current baseline output.

## Boundaries

`Note Manager` should not:
- search the vault broadly
- run semantic search as its own discovery step
- silently choose unrelated notes to edit
- allow raw direct durable note updates outside `Note Manager`
- convert unresolved ideas into recommendations, policy, decisions, or settled direction unless the handoff explicitly marks those points as decided
- rename or reorganize notes without explicit reason and context
- invent complex metadata or linking systems
- create notes from weak clarification state
- act without an explicit upstream artifact
- default new notes into a top-level hub
- treat hierarchy as required note structure
- infer note meaning, ownership, or governance from folders alone
- create domain hierarchy folders when links, tags, hubs, or backlinks are the intended structure
- act as autonomous note maintenance for the whole vault

## Workflow Role

Within the current workflow:
- `clarify-intent` shapes ideation and produces clarified context handoff artifacts
- `Note Manager` performs the bounded note mutation work for ideation-stage note actions
- `planner` produces execution artifacts such as task packets
- `implementer` produces implementation reports
- `review-sync` determines whether durable notes should change after accepted implementation
- `review-sync` sends implementation-backed note-sync context through `clarify-intent`
- `Note Manager` performs bounded durable note updates from the resulting clarified context handoff

This keeps note mutation logic centralized while preserving separate authority for clarification, planning, implementation, and review.
