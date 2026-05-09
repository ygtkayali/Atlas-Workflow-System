# Context Proposal Artifact

A context proposal artifact is produced by `project-review-sync` and consumed by `dw-clarify-intent`. It carries implementation-backed documentation-sync context for a single subject note or documentation area so that clarification can produce a clarified-context-handoff before `note-manager` acts.

One artifact per documentation-sync subject.

## Required Fields

| Field | Type | Description |
|---|---|---|
| `subject` | string | The note title or documentation area this proposal concerns |
| `trigger` | string | What in the diff, report, or packet triggered this proposal |
| `intent` | string | What documentation change is proposed and why |
| `source_evidence` | string | Quoted or referenced excerpt from the packet, report, or diff that supports the proposed change |
| `open_questions` | list | Questions that must be resolved in clarification before note mutation |
| `constraints` | list | What the note change must not do (scope limits, tone, traceability requirements) |

## Optional Fields

| Field | Type | Description |
|---|---|---|
| `related_notes` | list | Other notes that should reflect this change or that constrain it |
| `interpretation_drift` | list | Fidelity flags raised during the Interpretation Fidelity Check, if applicable |

## Usage Notes

- Keep `source_evidence` explicit — `dw-clarify-intent` must be able to trace the proposal back to the implementation without re-reading the full report.
- If `open_questions` is empty, clarification may proceed but should still confirm before note mutation.
- `interpretation_drift` entries must describe: the original claim, the current note state, and the specific issue (polarity flip, generalization, or silent resolution).
- Do not embed resolved decisions in the artifact — those belong in the clarified-context-handoff that `dw-clarify-intent` produces.
