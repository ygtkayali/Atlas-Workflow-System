# Implementer Agent

Status: [[Tags/status-settled]]
Type: [[design-note]]
Parent:
Related: [[planner-agent]], [[review-agent]], [[modes/dev-workflow/skills/project-implementer/references/implementation-report-schema]], [[clarify-intent]], [[note-manager]]
Runtime: modes/dev-workflow/skills/project-implementer/SKILL.md
Created:
Last Reviewed: 2026-05-15
Source:
Decisions:
Dependencies:
Tasks:

---

The project implementer skill performs scoped implementation work from an explicitly approved artifact. It exists to separate the act of executing code changes from the act of deciding scope, architecture, and intent — keeping approval authority with the human while the agent executes bounded work and reports what happened. The skill is designed so that its outputs are legible and auditable: what changed, why, what was verified, and what remains open.

## Design Notes

- [[implementer-approval-gate]] — Why approval is the entry condition and what counts as sufficient approval
- [[implementer-context-loading]] — The minimum-context policy and why discovery beyond the artifact boundary is prohibited
- [[implementer-escalation-threshold]] — The two-tier model for mid-implementation decisions and why partial hiding is prohibited
- [[implementer-verification-and-report]] — Verification expectations, failed-test handling, and the implementation report as the only output artifact
