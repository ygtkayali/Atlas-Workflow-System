# Implementation Report Schema

Status: [[status-settled]]
Parent: [[Workflow Schemas Hub]]
Related: [[task-packet-schema]], [[implementer-agent]], [[review-agent]]
Created: 2026-04-15
Last Reviewed:
Source:
Decisions:
Dependencies:
Tasks:

---

## Purpose
This schema defines the minimum structure for reporting completed implementation work back into the workflow.

The report exists to make changes explainable, reviewable, and synchronizable with project documentation.
It should preserve clear traceability back to the approved packet or equivalent approved artifact that authorized the implementation.

---

## Required Sections

### 1. Header
- report title
- report type: `implementation-report`
- status
- implementation date
- related approved task packet or equivalent approved artifact
- packet revision when known
- implementer or implementing role if known

### 2. Summary of Change
- what changed
- what outcome was achieved

### 3. Files Touched
- files changed
- concise reason each file changed

### 4. Why These Changes Were Made
- tie implementation choices back to the approved packet or constraint set

### 5. Checks Run
- tests, lint, typecheck, builds, or focused command checks
- result of each check
- limitations when checks were not run

### 6. Outcome Against Acceptance Criteria
- whether acceptance criteria were met, partially met, or blocked
- any notable deviation from the approved packet

### 7. Assumptions Introduced
- new assumptions added during implementation that were not already explicit in the packet

### 8. Unresolved Issues
- remaining gaps
- known limitations
- items that need follow-up or human review

### 9. Documentation Impact
- notes updated
- notes that should be updated next
- stale docs or missing decisions discovered during implementation

---

## Recommended Optional Sections
- diff summary
- rollout or migration notes
- dependency impact
- operational considerations
- follow-up tasks

---

## Reporting Rules

### Be explicit
Do not compress uncertainty into a polished summary.
If verification was partial, say so.
If an assumption was introduced, say so.

### Stay scoped
Report only the implemented work and directly relevant observations.
Do not mix in a broad retrospective unless it materially affects review.

### Preserve traceability
Every report should point back to a request, task, packet, or decision when possible.

---

## Uncertainty Labels
Use these labels when helpful:
- `decided`
- `proposed`
- `unclear`
- `blocked`

Use them especially for assumptions, unresolved issues, and documentation impact.

---

## Report Quality Bar
Before considering the report complete, check:
- Does it explain what changed?
- Does it explain why the touched files changed?
- Does it state the outcome against the acceptance criteria?
- Does it show what was verified?
- Does it surface assumptions and unresolved issues?
- Does it identify documentation impact?
- Is it traceable to the originating packet?

If any answer is no, refine the report before handoff to review.

---

## Minimal Report Template

```md
# <Implementation Report Title>

- Type: implementation-report
- Status: <completed | partial | blocked>
- Related packet: <link or identifier>
- Packet revision: <v1>
- Date: YYYY-MM-DD

## Summary of Change

## Files Touched

## Why These Changes Were Made

## Outcome Against Acceptance Criteria

## Checks Run

## Assumptions Introduced

## Unresolved Issues

## Documentation Impact
```
