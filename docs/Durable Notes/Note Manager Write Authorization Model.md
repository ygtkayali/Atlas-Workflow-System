# Note Manager Write Authorization Model

Status: [[Tags/status-draft]]
Type: [[design-note]]
Parent: [[note-manager]]
Related: [[note-manager]], [[Note Manager Bundled Intake and Subject Mapping]], [[Note Manager Escalation Routing]], [[clarified-context-handoff]]
Created: 2026-05-15
Last Reviewed: 2026-05-15
Source: modes/dev-workflow/skills/dw-note-manager/SKILL.md
Project Subjects:
Tasks:
Reports:

---

## Design Scope

Note Manager's write model separates two decisions that are easy to conflate: approving a proposed note action and authorizing a durable write. This note captures why they are separate gates, what signals constitute explicit write authorization, and why the default is always draft-first.

## Context

Note Manager is the single gate for all durable note mutations. The workflow routes note proposals through it from multiple upstream sources: clarified context handoffs from `clarify-intent`, compact proposal tables from `review-sync`, and direct user requests. Each source can reach Note Manager at different states of confirmation — a review proposal may be well-structured but not yet approved for writing; a batch approval may cover some rows but not others.

The risk is silent mutation: a well-formed proposal being treated as a write instruction because the user said "yes" somewhere in the exchange without explicitly authorizing the write.

## Chosen Design

Two distinct gates:

**Gate 1 — Action confirmation**: approves preparing or applying a specific note action (create, update, defer, return to clarification). This gate is satisfied when the user approves a proposed action or the prompt clearly authorizes the action.

**Gate 2 — Durable-write confirmation**: approves applying a prepared draft, patch, or approved proposal-table row to the vault. This gate requires one of four explicit signals:

1. The user message contains a direct write directive ("apply", "write", "commit", or equivalent).
2. The upstream handoff contains `direct_write: true`.
3. An approved execution packet explicitly authorizes the write.
4. The user approves a review/sync proposal table for Note Manager writing.

Anything outside these four signals produces draft-only output.

Action approval does not imply durable-write approval unless the approval explicitly says to apply or write. Durable-write approval for one note action does not extend to other note actions in the same bundle unless the user explicitly approves the batch.

## Rationale

Action confidence and write intent are different decisions. A user reviewing a proposed note action may say "yes, that's the right action" while still wanting to see the draft before it lands in the vault. Collapsing the two gates into one makes that distinction invisible and turns every action approval into a silent write trigger.

This is especially consequential for batch operations. When a review/sync proposal table contains ten rows and the user approves the table, Note Manager must not read that as approving all ten writes in one pass unless the approval is explicit about that scope. The four-signal model forces that explicitness at the moment of write.

The draft-first default is the safety position: when authorization is ambiguous, producing a draft costs little. Applying a write that wasn't intended costs more to undo.

## Alternatives Considered

**Single gate (action approval = write approval)**: reduces friction, avoids the second confirmation step. Rejected because it makes silent writes too easy, especially in batch contexts or when Note Manager receives a compact proposal table that looks ready but hasn't been explicitly confirmed for writing.

**Implicit write from context**: inferring write intent from conversational tone ("sounds good", "perfect", "do it"). Rejected because tone-based inference is unreliable and produces inconsistent behavior across similar exchanges. The four explicit signals are intentionally narrow.

## Constraints

- Note Manager must not infer write authorization from isolated wording or conversational approval.
- Durable-write approval for one row in a batch does not extend to other rows.
- The draft-first default cannot be bypassed by the skill itself — only by one of the four signals.

## Technical Shape

The write-authorization check is the final step before any file mutation. Small-edit mode patches (metadata-only or single-line changes) follow the same two-gate model.

## Impacted Project Subjects

- [[note-manager]] — primary subject
- [[Note Manager Bundled Intake and Subject Mapping]] — batch approval isolation is the downstream application of this model

## Open Questions

## Review Notes
