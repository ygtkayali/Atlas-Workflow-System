# Note Manager

Status: [[Tags/status-settled]]
Type: [[design-note]]
Runtime: modes/dev-workflow/skills/dw-note-manager/SKILL.md
Parent:
Related: [[clarify-intent]], [[clarified-context-handoff]], [[Two-Phase Workflow Boundary]], [[Durable Notes Follow Accepted Implementation]], [[Main Vault Note Structure and Agent Context]], [[Tags/idea-note]], [[Tags/feature-subject-note]], [[Tags/design-note]], [[Note Manager Write Authorization Model]], [[Note Manager Bundled Intake and Subject Mapping]], [[Note Manager Note-Type Selection and Promotion Lifecycle]], [[Note Manager Escalation Routing]]
Created: 2026-04-14
Last Reviewed: 2026-05-15
Source: [[LLM Wiki Lossy Compression and Integrity Risks]]
Decisions: `Note Manager` must consume and preserve the handoff's `Interpretation Basis`, especially original input, when drafting or updating durable notes. It must prefer the local note-type tag model when creating or updating dev-workflow notes. Note Manager action confirmation and durable-write confirmation are separate gates. Approved compact proposal tables can authorize direct bounded batch writes.
Dependencies:
Tasks: `docs/In-flight/report-technical-project-documentation-governance.md`, `docs/In-flight/report-review-sync-note-manager-compression-path.md`

---

`Note Manager` is the bounded note-mutation role for the workflow. It exists to keep all durable note creation and updates behind one explicit gate — so note logic evolves in one place rather than spreading across roles — and to ensure every mutation comes from a clear upstream artifact and explicit write authorization rather than from conversational drift.

## Design Notes

- [[Note Manager Write Authorization Model]] — two-gate design, four write signals, draft-first default
- [[Note Manager Bundled Intake and Subject Mapping]] — N:M subject-to-note mapping, manifest policy, approval isolation
- [[Note Manager Note-Type Selection and Promotion Lifecycle]] — type role boundaries, promotion as status + type + folder
- [[Note Manager Escalation Routing]] — decision confidence threshold, when to act vs. route, raw input boundary
