# Documentation Sync Analysis

Inspect accepted implementation evidence for durable-knowledge impact. Produce a compact sync proposal table.

Use only after accepted implementation evidence exists and the user has approved moving from implementation review, or when the user directly requests this mode for bounded accepted implementation.

## Steps

1. Read the accepted review disposition, approved packet, implementation report, and relevant diff.
2. Identify implementation-backed facts, decisions, behavior changes, or settled ideas that may need durable documentation.
3. Separate each proposed sync subject. One row per subject — do not bundle unrelated note changes.
4. For each subject, distinguish `decided`, `proposed`, `unclear`, and `blocked`.
5. Run the **Interpretation Fidelity Check** (see SKILL.md) when the subject came from a clarified context handoff.
6. Produce a compact Documentation Sync Proposal Table (see below).
7. Route clear rows to `dw-note-manager` after user approval. Route only uncertain rows to `dw-clarify-intent`.
8. If no sync is needed, say so explicitly and propose whether task-lane closeout should be considered next.

## Checklist

- accepted implementation facts that changed durable project knowledge
- idea notes that became promotion candidates (promotion is not automatic)
- stale or missing project subject, design, decision, or workflow-state documentation
- multiple subjects that should remain separate
- unclear note target ownership that should go through clarification
- any proposed action that would require Note Manager rather than review/sync

## Documentation Sync Proposal Table

| subject | target note or uncertainty | action | evidence | proposed change | uncertainty | constraints | route |
|---|---|---|---|---|---|---|---|
| durable subject | note path or unclear target | `create`/`update`/`defer`/`reject` | packet/report/diff evidence | brief description of note change | `decided`/`proposed`/`unclear`/`blocked` | what must not happen | `note-manager`/`clarify-intent`/`defer`/`reject` |

Route rules:
- `note-manager` — target, action, evidence, durable meaning, and constraints are all clear.
- `clarify-intent` — subject boundaries mixed, target ownership unclear, evidence weak, or durable meaning unresolved.
- `defer` — subject is valid but should not be handled in this pass.
- `reject` — proposed sync would be misleading, out of scope, or not durable knowledge.

Approval prompt should let the user approve, revise, defer, or reject rows individually or as a batch.

## Disposition

`sync-needed` | `no-sync-needed` | `clarification-needed`

`sync-needed` — produce the proposal table and wait for approval before routing rows.
`no-sync-needed` — may propose task-lane closeout as next phase, but must stop before closeout.
`clarification-needed` — route the uncertainty through `dw-clarify-intent` before Note Manager.

## Output

- accepted implementation evidence inspected
- documentation-sync subjects identified
- one compact Documentation Sync Proposal Table
- uncertainty labels per subject
- proposed next action per row
- disposition

## Final Check

- Was the phase explicitly approved or directly requested for bounded accepted evidence?
- Was the Interpretation Fidelity Check run for any clarified context handoff?
- Are recommendations traceable?
- Does the proposal table route only uncertain rows to `dw-clarify-intent`?
- Did output stop before Note Manager routing or durable write unless separately approved?
