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
