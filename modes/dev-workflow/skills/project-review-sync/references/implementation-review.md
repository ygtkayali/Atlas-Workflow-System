# Implementation Review

Compare implementation against the approved packet and decide whether documentation sync should be proposed.

## Steps

1. Extract acceptance criteria, scope, and constraints from the approved packet.
2. Read the implementation report and verification notes.
3. Compare implementation against the approved packet.
4. Identify matches, mismatches, missing checks, and newly introduced assumptions.
5. For durable note changes from a clarified context handoff, run the **Interpretation Fidelity Check** (see SKILL.md).
6. Decide whether documentation sync analysis should be proposed.
7. Create or propose follow-up task context for unresolved issues.
8. Recommend `keep`, `revise`, or `reject`. If `reject`, produce a follow-up task or re-clarification context — never a silent revert.
9. If documentation sync may be needed, output a gate confirmation and stop.

## Checklist

- scope drift from the approved packet
- unapproved behavior changes
- missing or weak verification for material-risk changes
- broken traceability between task, implementation, and docs
- newly implied decisions that were never recorded
- interpretation fidelity drift
- follow-up work that should be queued rather than folded into the original task

## Disposition

`keep` | `revise` | `reject`

`reject` produces a follow-up task or re-clarification context. Never a silent revert or normalized state change.

## Output

- matches and mismatches against the approved packet
- missing or weak verification findings
- gate confirmation for doc sync analysis when durable knowledge may need sync
- follow-up tasks and decision candidates
- disposition: `keep` / `revise` / `reject`

## Final Check

- Was implementation compared to the approved packet?
- Are mismatches explicit?
- Was doc sync only proposed, not run automatically?
- Are follow-up tasks separated from completed work?
- Has any unapproved change been escalated instead of normalized?
- If `reject`, is there a follow-up task or re-clarification context?
