# Status Tag Registry

Status: [[status-settled]]
Parent:
Related: [[Tag Notes Instead Of Hierarchical Hubs]], [[Note Manager]], [[Local Note Search Script]]
Created: 15-04-2026
Last Reviewed:
Source: note-manager draft from clarified lifecycle/status discussion
Decisions:
- v1 status tags are `[[status-draft]]`, `[[status-pending]]`, `[[status-settled]]`, `[[status-archived]]`
- status tags express note state only
- a note should usually have one primary status tag
Dependencies:
Tasks:

---

## Summary

This note defines the v1 status tag set for notes.

The goal is to keep note state simple, reusable, and easy to maintain while supporting retrieval and future local note search.

Status tags are a classification layer for note state only. They do not replace note type, priority, or future workflow tags.

## Details

Approved v1 status tags:

- `[[status-draft]]`
- `[[status-pending]]`
- `[[status-settled]]`
- `[[status-archived]]`

Definitions:

- `[[status-draft]]`
  The note is still forming. It is incomplete, exploratory, or not ready to rely on yet.

- `[[status-pending]]`
  The note is relevant but not yet worked through enough. It remains in the queue for later attention.

- `[[status-settled]]`
  The note has already been worked through enough for now. It is not on the queue, not archived, and still relevant.

- `[[status-archived]]`
  The note is kept for history or reference and is no longer part of active working context.

Usage rules:

- A note should usually have one primary status tag.
- Status tags should come from the approved registry only.
- Status tags answer only one question: what is the current state of this note?
- Status tags should not encode priority, implementation readiness, or note type.
- Agents may reuse approved status tags but should not invent new status tags without approval.

Examples:

- a vague new concept note usually starts as `[[status-draft]]`
- a note about something that should be revisited later is usually `[[status-pending]]`
- a note that has been worked through and remains useful is usually `[[status-settled]]`
- an old note retained mainly for history is usually `[[status-archived]]`

## Open Questions

- Should every durable note be expected to carry one status tag, or can some notes omit status temporarily?
- Should lightweight hub or index notes follow the same status rule, or use a lighter convention?
- Should future retrieval tags such as implementation-related tags be governed in a separate registry note?
