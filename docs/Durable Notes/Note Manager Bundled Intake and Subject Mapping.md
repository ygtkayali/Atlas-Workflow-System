# Note Manager Bundled Intake and Subject Mapping

Status: [[Tags/status-draft]]
Type: [[design-note]]
Parent: [[note-manager]]
Related: [[note-manager]], [[Note Manager Write Authorization Model]], [[Note Manager Escalation Routing]], [[clarified-context-handoff]]
Created: 2026-05-15
Last Reviewed: 2026-05-15
Source: modes/dev-workflow/skills/dw-note-manager/SKILL.md
Project Subjects:
Tasks:
Reports:

---

## Design Scope

How Note Manager handles multi-subject inputs. The N:M relationship between clarified subjects and note actions, when a separate manifest is required versus when the upstream proposal table is sufficient as a decision surface, and how approval isolation across bundle rows is maintained.

## Context

Note Manager may receive a bundle of clarified durable subjects or an approved review/sync proposal table with multiple rows. The challenge is allowing intake efficiency — not requiring one sequential approval per row — while still preventing a single approval signal from silently authorizing a set of unrelated note mutations.

The deeper problem is structural: the relationship between upstream subjects and note actions is not one-to-one. One clarified subject may produce zero, one, or many note actions. Multiple subjects may support a single note action when their context is genuinely shared. Forcing a rigid mapping would either produce wrong note structure or require constant clarification.

## Chosen Design

**No separate manifest by default.** For single-subject handoffs, the action header (note action + type + target/title) serves as the manifest. For multi-subject handoffs or proposal tables, the upstream proposal table is the decision surface when each row already includes: target, action, evidence, proposed change, uncertainty, constraints, and route.

**Create a separate manifest only when:**
- upstream rows are mixed or ambiguous,
- one subject may map to several note actions and the mapping is not explicit,
- multiple subjects might collapse into one note action,
- or the user explicitly asks for a manifest before drafting or writing.

**N:M mapping rules:**
- One clarified subject may produce zero, one, or many note actions.
- One note action must target exactly one durable note.
- Multiple subjects may support one note action only when that relationship is explicit in the manifest or proposal table.

**Approval isolation:** Approval for one note action does not extend to any other note action in the same bundle unless the user explicitly approves the batch. When a batch is explicitly approved, Note Manager applies only the approved rows and preserves row boundaries in its report. Rows routed to `clarify-intent`, `defer`, or `reject` are excluded from the write pass.

## Rationale

The proposal table is already a structured decision surface when rows are clear. Creating a parallel manifest duplicates that structure without adding clarity. The overhead of mandatory manifests would make batch operations slower without improving safety when the proposal table already contains all decision fields.

Approval isolation is the more important constraint. The failure mode being avoided is: user says "yes" to a table review, Note Manager reads that as approving all rows. This is especially risky in large batches where a few rows may be clear and others ambiguous. The row-level isolation rule means each row must be individually authorized, and the explicit batch approval signal must be present for a full-batch write pass.

The N:M relationship acknowledges that semantic subject separation (owned by `clarify-intent`) and subject-to-note mapping (owned by Note Manager) are different problems. Note Manager must be free to decide that two related subjects belong in one note, or that one complex subject should produce two notes, without being forced into a one-to-one mapping by the upstream bundle structure.

## Alternatives Considered

**Always produce a manifest**: safer for ambiguous inputs but adds overhead for clear ones. Rejected in favor of using the proposal table as the decision surface by default, with manifest creation triggered only by ambiguity or explicit request.

**One approval covers the batch**: simpler user experience, fewer confirmation steps. Rejected because it makes approval-scope ambiguity invisible and allows one "yes" to silently cover unreviewed rows.

## Constraints

- Provisional subject bundles from complex-prompt intake are input evidence, not final note structure. Note Manager treats them as starting context, not as prescribed note boundaries.
- Branching ideas within a bundle should stay together only when closely related. If a branch can become its own durable subject, split it and preserve the connection.
- Row boundaries must be preserved in the batch-write report. Note Manager must not merge or collapse rows during application.

## Technical Shape

For clear proposal tables, Note Manager applies rows in a single pass when the user explicitly approves the batch. The report lists: row/subject id, target note, action applied, metadata refreshed, evidence basis, skipped rows and why, checks run.

## Impacted Project Subjects

- [[note-manager]] — primary subject
- [[Note Manager Write Authorization Model]] — batch approval isolation is enforced through the same gate model

## Open Questions

## Review Notes
