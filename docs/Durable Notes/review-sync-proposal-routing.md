# Review-Sync Proposal Table Routing

Status: [[Tags/status-draft]]
Type: [[design-note]]
Parent: [[review-agent]]
Related: [[review-agent]], [[review-sync-phase-gates]], [[review-sync-interpretation-fidelity]]
Created: 2026-05-15
Last Reviewed: 2026-05-15
Source: modes/dev-workflow/skills/project-review-sync/SKILL.md
Decisions:
Dependencies:
Tasks:

---

Documentation sync proposals are expressed as compact tables. Each row routes to either `dw-note-manager` (clear rows) or `dw-clarify-intent` (uncertain rows) based on whether Note Manager can apply the change without guessing.

## Design Scope

The routing split governs how documentation sync findings move from the review / sync skill into the note management and clarification pipeline. It applies to both implementation-backed documentation sync and maintenance review findings.

## Chosen Design

Table columns: subject · target or uncertainty · action · evidence · proposed change · uncertainty · constraints · route.

**Clear row** — routes directly to `dw-note-manager` after approval:
- target note is unambiguous
- evidence is bounded and sufficient for the mode, such as implementation-backed sync evidence or maintenance-review note/artifact evidence
- Note Manager can apply the change without guessing

**Uncertain row** — routes to `dw-clarify-intent` first:
- mixed subjects
- unclear target ownership
- weak evidence
- unresolved durable meaning
- any decision that would force Note Manager to guess

`dw-clarify-intent` produces a clarified-context-handoff, which then routes to `dw-note-manager`.

## Rationale

Separating routing by certainty keeps Note Manager bounded to mechanical application and keeps interpretive decisions visible to the human. Routing uncertain rows directly to Note Manager would require it to make untracked interpretive choices about durable note meaning.

## Open Questions
