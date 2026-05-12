# Dev Workflow Vocabulary

Canonical label sets for the dev-workflow skill chain. Skills reference this file rather than redefining labels inline. Skills may define decision criteria, transition logic, and output shapes on top of these labels but must not redefine the labels themselves inconsistently.

## Note Status Tags

For tag definitions and usage rules, see `docs/Durable Notes/Status Tag Registry.md`.

Approved tags: `[[status-draft]]` · `[[status-active]]` · `[[status-pending]]` · `[[status-settled]]` · `[[status-archived]]`

## Uncertainty Labels

Used in planning and clarification to classify key information.

| Label | Meaning |
|---|---|
| `decided` | Documented and settled; no open question |
| `proposed` | A recommendation exists but is not yet confirmed |
| `unclear` | Insufficient information to settle |
| `blocked` | Depends on a missing decision or external input |

## Clarification State Labels

Used by `dw-clarify-intent` to represent the current state of an idea or request.

| Label | Meaning |
|---|---|
| `draft` | Clarification state captured but rough or incomplete |
| `needs_clarification` | High-impact uncertainty or missing decision would force downstream guesswork |
| `ready_for_note_manager` | Core subject, goals, scope, constraints, and major tradeoffs are clear enough for `Note Manager` to act without silent decision-making |
| `partial_clarification` | Iteration cap reached; some subjects settled, others blocked; user direction needed |

## Packet Status Labels

Used by `project-planner` for implementation packet approval state.

| Label | Meaning |
|---|---|
| `draft` | Planning incomplete; not ready for review |
| `approval_pending` | Ready for human review; implementation must not begin |
| `approved` | Human has explicitly approved this exact revision |
| `blocked` | An unresolved issue prevents safe implementation |

## Task Lane Status Labels

Used by workflow artifacts in `docs/In-flight/` to show where a serialized task lane sits in the artifact lifecycle.

These labels are artifact status values, not durable note status tags.

| Label | Meaning |
|---|---|
| `intake` | A handoff exists, but downstream planning, note management, or implementation has not settled the next execution step |
| `planned` | An implementation packet or equivalent execution artifact exists, but implementation has not completed |
| `in_progress` | Implementation or review work is actively underway |
| `settled` | Work has reached a stable checkpoint and is eligible for review/sync closeout |
| `closed` | Review/sync has completed closeout and produced the required archive or disposition |
| `blocked` | The lane cannot continue without a human decision, missing input, or follow-up task |

## Task Lane Closeout Recommendation Labels

Used by `project-review-sync` when reviewing settled workflow task lanes.

| Label | Meaning |
|---|---|
| `archive-ready` | A settled lane can be summarized and closed after any required cleanup approval |
| `retain-in-flight` | A lane should remain in `docs/In-flight/` because it is unsettled, blocked, or still affects current work |
| `follow-up-needed` | Closeout found a missing decision, stale durable note, implementation gap, or other issue requiring follow-up |

## Verification Outcome Labels

Used by `implementation-verifier` for commit recommendations.

| Label | Meaning |
|---|---|
| `ready_to_commit` | Tests and review support committing the current scoped change |
| `commit_with_caution` | Commit is possible, but known risks or gaps should be called out |
| `needs_revision` | Tests may pass or fail, but implementation should change before commit |
| `blocked` | Verification cannot complete due to missing dependencies, failing setup, unclear scope, or another blocker |

## Review Disposition Labels

Used by `project-review-sync`.

**Implementation review:** `keep` · `revise` · `reject`

| Label | Meaning |
|---|---|
| `keep` | Implementation matches the approved packet; no revision needed |
| `revise` | Implementation needs changes before closeout |
| `reject` | Does not meet the approved packet; requires a follow-up task or re-clarification — never a silent revert |

**Maintenance review:** `sync-needed` · `follow-up-needed` · `no-action`

| Label | Meaning |
|---|---|
| `sync-needed` | Durable notes or artifacts need updates |
| `follow-up-needed` | A task or decision gap needs routing |
| `no-action` | Nothing requires update |
