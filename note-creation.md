# Note Creation

Status: draft
Parent: [[Workflow Hub]]
Related: [[clarify-intent]], [[note-ready-handoff]], [[project-vault-phase-1-roadmap]]
Created: 2026-04-14
Last Reviewed:
Source:
Decisions:
Dependencies:
Tasks:

---

## Summary

`note-creation` is the bounded durable note step that follows clarification in Phase 1.

Its job is to turn a stable clarified subject into a draft note create or update action without turning into broad vault management.

## Responsibilities

- begin from a [[note-ready-handoff]]
- use only the specific relevant notes or note paths supplied by the user
- use local templates when they apply
- decide whether the correct action is `create` or `update`
- draft exact note content or exact update content
- keep links minimal and intentional
- return work to clarification when durable subject, note type, or note placement is still unclear

## Supported Note Roles

For v1, this skill works with:
- `Main Hub`
- `Sub Hub`
- `General Note`
- `Idea Note`

The default emphasis is on `Sub Hub` and `General Note`, with `Main Hub` remaining a lightweight index role.

## Output

The default output is a draft-first note action.

When the action is `create`, it should provide:
- note action
- note type
- proposed title
- proposed parent or related links
- full draft note body

When the action is `update`, it should provide:
- note action
- target note
- why that note is the correct target
- exact updated content or patch-shaped replacement text

## Boundaries

`note-creation` should not:
- search the vault broadly
- silently choose unrelated notes to edit
- rename or reorganize notes
- invent complex metadata or linking systems
- create notes from weak clarification state
