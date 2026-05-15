# Implementer Verification and Report

Status: [[Tags/status-draft]]
Type: [[design-note]]
Parent: [[implementer-agent]]
Related: [[implementer-agent]], [[implementation-report-schema]], [[review-agent]]
Created: 2026-05-15
Last Reviewed: 2026-05-15
Source: modes/dev-workflow/skills/project-implementer/SKILL.md
Decisions:
Dependencies:
Tasks:

---

The implementer's output has two parts: verification of the change and a structured implementation report. Both are required. Together they make the work reviewable and handoff-safe.

## Verification

The implementer must run the strongest practical verification available for the changed area. "Practical" means: if tests exist, run them; if lint or typecheck exists, run it; if there is a build step, run it. Manual validation is the fallback when automation is unavailable, not a first-choice substitute.

**Failed tests are not a silent fix opportunity.** When a test in the approved artifact or planner output fails after the change, the correct behavior is to report the failure with a diagnosis and pause for user direction. A failing test may indicate a problem with the implementation, a problem with the test, or a problem with the plan — the implementer cannot determine which one unilaterally.

**Partial verification must be declared.** Presenting incomplete verification as full confidence is prohibited. If certain checks could not be run, that is stated explicitly in the report.

## The Implementation Report

The report is the implementer's only documentation artifact unless the approved artifact explicitly authorizes another workflow output. This is deliberate: durable note creation and documentation synchronization happen after review, through the clarify-intent → note-manager path. The implementer does not write to the vault.

**Minimum report structure:**
- Summary of change
- Files touched and why each changed
- Checks run (or why they were not)
- Assumptions introduced
- Unresolved issues
- Review/sync follow-up signals

## Why Review/Sync Signals Are Not Note Actions

The implementer may identify stale docs, missing decisions, or architectural follow-up during implementation. These are reported as signals in the implementation report — not acted on directly. Acting on them during implementation would cross the approval boundary between implementation and documentation governance. The signals surface the follow-up need; the human decides whether and how to act.

## Report as Handoff Surface

The implementation report is what makes the work legible to the next step in the workflow (review, sync, or human re-engagement). A report that hides assumptions or omits unresolved issues is not a complete handoff — it just defers the cost until review.
