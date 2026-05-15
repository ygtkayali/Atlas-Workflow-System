# Review / Sync Agent

Status: [[Tags/status-settled]]
Type: [[design-note]]
Parent:
Related: [[planner-agent]], [[implementer-agent]], [[clarify-intent]], [[clarified-context-handoff]], [[note-manager]], [[Durable Notes Follow Accepted Implementation]]
Created:
Last Reviewed: 2026-05-15
Source: [[LLM Wiki Lossy Compression and Integrity Risks]]
Runtime: modes/dev-workflow/skills/project-review-sync/SKILL.md
Decisions: Review/sync should validate durable note output against the handoff's `Interpretation Basis`. Review/sync phase changes are gated; implementation review, documentation sync analysis, Note Manager handoff, durable write, and task-lane closeout must not run as one automatic chain. Documentation sync should use compact proposal tables; clear rows can route directly to Note Manager and uncertain rows to clarify-intent.
Dependencies:
Tasks: `docs/In-flight/report-technical-project-documentation-governance.md`, `docs/In-flight/report-review-sync-note-manager-compression-path.md`

---

The review / sync skill is the post-implementation and maintenance analysis layer for the dev-workflow mode. It compares implementation output against approved plans, routes documentation synchronization through proposal tables, and runs bounded maintenance inspections — all behind explicit phase gates that prevent any review from silently escalating into a note mutation or artifact cleanup.

## Design Notes

- [[review-sync-mode-dispatch]] — Mode Detection and Dispatch
- [[review-sync-phase-gates]] — Phase Gate Model
- [[review-sync-scope-cap]] — Scope Cap
- [[review-sync-proposal-routing]] — Proposal Table Routing
- [[review-sync-interpretation-fidelity]] — Interpretation Fidelity Check
