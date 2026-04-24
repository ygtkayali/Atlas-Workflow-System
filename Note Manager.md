# Note Manager

Status: [[status-settled]]
Parent: [[Workflow Hub]]
Related: [[clarify-intent]], [[clarified-context-handoff]], [[note-ready-handoff]], [[Two-Phase Workflow Boundary]], [[Durable Notes Follow Accepted Implementation]]
Created: 2026-04-14
Last Reviewed: 2026-04-24
Source:
Decisions:
Dependencies:
Tasks:

---

## Summary

`Note Manager` is the bounded note-mutation role for the workflow.

Its job is to keep note creation and note updates behind one explicit gate so note logic can evolve in one place without spreading note-writing behavior across multiple roles.
It receives clarified context from upstream roles, then decides the concrete note action and durable note structure.

It should remain narrow in authority:
- it works from explicit upstream artifacts
- it uses only the provided note context
- it does not turn into autonomous vault management
- it does not silently impose hierarchy or broader structure on the note space

## Responsibilities

- act as the single gate for bounded note creation and note updates
- route behavior using an explicit `owner` field in the input context
- use only the specific relevant notes or note paths supplied by the user
- use local templates when they apply
- decide whether the correct bounded action is `create` or `update`
- decide note type, target note, title, note links, and final durable note structure from the provided context
- refresh dynamic metadata on every create or update so status and other changing header fields reflect the current note state rather than stale template or prior values
- draft exact note content or exact update content
- keep links minimal and intentional
- prefer intentional related links over default parent placement
- treat `Main Hub` as an explicit lightweight index role rather than the default destination for new notes
- avoid silently broadening note scope beyond the supplied context
- return work to clarification or review when the note mutation target is still unclear

## Current Upstream Owners

For the current workflow, `Note Manager` should support these owners:

- `clarify-intent`
  uses a [[clarified-context-handoff]] as the upstream artifact for ideation-stage note creation or note updates

- `review-sync`
  uses accepted implementation context such as a task packet, implementation report, review outcome, or note-change handoff to update durable notes after implementation has been accepted

Additional owners may be introduced later, but this note should describe only the owners that are part of the current workflow.

## Supported Note Roles

For the current system, `Note Manager` should work with:
- `Main Hub`
- `Sub Hub`
- `General Note`
- `Idea Note`

The default emphasis remains on `Sub Hub`, `General Note`, and bounded updates to existing durable notes already present in the system.

`Main Hub` remains a lightweight index role and should be chosen only when the clarified subject explicitly calls for an index note rather than a normal durable knowledge note.

## Input Expectations

`Note Manager` should begin from:
- an explicit upstream artifact,
- the relevant notes or note paths supplied for the note action,
- and local templates when the target note type uses them.

It should not guess through missing upstream context.

Examples:
- from `clarify-intent`: a [[clarified-context-handoff]]
- from `review-sync`: implementation-backed context that makes the requested durable note update explicit

If the owner, target note, or intended note mutation is still unclear, `Note Manager` should stop and return the work to the upstream role rather than improvising structure.

For `clarify-intent` input, the upstream artifact should preserve clarified context, not prescribe final note structure.
`Note Manager` is responsible for deciding whether that context becomes a new note, an update to an existing note, or a request for more clarification.

## Output

The default output is a draft-first note action.

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
- silently choose unrelated notes to edit
- rename or reorganize notes without explicit reason and context
- invent complex metadata or linking systems
- create notes from weak clarification state
- act without an explicit upstream artifact
- default new notes into a top-level hub
- treat hierarchy as required note structure
- act as autonomous note maintenance for the whole vault

## Workflow Role

Within the current workflow:
- `clarify-intent` shapes ideation and produces clarified context handoff artifacts
- `Note Manager` performs the bounded note mutation work for ideation-stage note actions
- `planner` produces execution artifacts such as task packets
- `implementer` produces implementation reports
- `review-sync` determines whether durable notes should change after accepted implementation
- `Note Manager` performs those bounded durable note updates when they are explicitly requested by the upstream review result

This keeps note mutation logic centralized while preserving separate authority for clarification, planning, implementation, and review.
