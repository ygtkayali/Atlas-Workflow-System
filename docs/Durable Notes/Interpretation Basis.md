# Interpretation Basis

Status: [[Tags/status-draft]]
Type: [[design-note]]
Parent: [[clarify-intent]]
Related: [[Two-Phase Clarification Architecture]], [[Clarify Intent Output Modes]], [[clarified-context-handoff]], [[clarify-intent]]
Created: 2026-05-15
Last Reviewed: 2026-05-15
Decisions: Required in full-depth clarification and for any review/sync context. May be omitted in light-depth only when the origin is a direct user prompt with no upstream artifact or hidden context. User-intent claims and agent-inference claims must be separated explicitly.
Source: modes/dev-workflow/skills/dw-clarify-intent/SKILL.md
Dependencies:
Tasks:

---

## Design

`Interpretation Basis` is a structured field in the clarified-context handoff that records how the input was understood and what constraints that understanding carries forward. It exists so downstream skills can validate the handoff against the original intent rather than treating the clarified output as ground truth.

## Fields

The full Interpretation Basis preserves:
- **origin type** — where the input came from (direct user prompt, upstream artifact, review/sync context, etc.)
- **original input or artifact** — the source as received, not as interpreted
- **relevant context used** — what additional context shaped the interpretation
- **interpreted intent** — what the skill understood the user to be asking for
- **tone or stance to preserve** — how downstream output should be oriented
- **user-intent claims** — what the user stated
- **agent-inference claims** — what the skill inferred, explicitly marked as inference
- **open ambiguity** — what remains unresolved and must be preserved, not smoothed over
- **things not to imply** — constraints on how downstream work should frame the subject
- **validation target** — what a reviewer would check to confirm the handoff is correct

Separating user-intent claims from agent-inference claims is the field that prevents the skill from laundering its own assumptions into the handoff as settled facts.

## Depth-Conditional Requirement

Required in full-depth clarification. In light-depth, may be omitted only when all of these hold:
- the origin is a direct user prompt,
- no hidden context, source material, or upstream artifact is being interpreted.

The moment any upstream artifact or hidden context is involved, Interpretation Basis is required regardless of declared depth.

## Review/Sync Context

When clarifying implementation-backed review/sync context, the basis must explicitly separate implementation facts from review proposals. This prevents a proposal from being presented as an established fact when it carries agent inference.

## Long-Session Re-Validation

Before producing a handoff after a long or compacted conversation, the skill re-reads the original triggering input and verifies the handoff still matches in goal, scope, tone, and uncertainty. Drift introduced during the clarification loop is flagged rather than normalized. This anchors the Interpretation Basis to the actual origin rather than to a gradually shifted version accumulated through the loop.

## Design Rationale

Handoffs without a preserved interpretation basis tend to collapse ambiguity into apparent resolution. A downstream skill receiving that handoff has no way to know which parts were settled by the user and which were inferred during clarification. The Interpretation Basis makes that boundary explicit and auditable.
