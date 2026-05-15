# Interpretation Fidelity Check

Status: [[Tags/status-draft]]
Type: [[design-note]]
Parent: [[review-agent]]
Related: [[review-agent]], [[review-sync-proposal-routing]], [[clarify-intent]]
Created: 2026-05-15
Last Reviewed: 2026-05-15
Source: modes/dev-workflow/skills/project-review-sync/SKILL.md
Decisions:
Dependencies:
Tasks:

---

When a note change traces back to a clarified context handoff, review / sync checks whether the resulting note preserves the original input faithfully. Each failure mode is surfaced as an explicit flag, not normalized.

## Design Scope

The interpretation fidelity check is a sub-step within Implementation Review and Documentation Sync Analysis. It applies only when the note change being reviewed came through the `clarify-intent → Note Manager` path.

## Chosen Design

Three failure modes:
1. **Polarity flip** — uncertainty in the handoff became certainty in the note
2. **Generalization** — a specific claim became vague
3. **Silent resolution** — an open question was closed without a recorded decision

Steps:
1. Load the original handoff or prompt.
2. Diff against the current or proposed note change.
3. Flag each failure mode explicitly.

Each flag is surfaced separately. None are folded into a summary finding.

## Rationale

Lossy compression between a clarified context handoff and the resulting durable note is hard to detect after the fact. Once a polarity flip or silent resolution is written into a settled note, it erodes the traceability the entire workflow depends on. The check must be explicit and per-failure-mode so nothing gets normalized away.

## Open Questions
