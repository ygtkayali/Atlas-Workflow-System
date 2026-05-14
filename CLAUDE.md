<!-- atlas-dev-workflow-bridge:start -->
# Dev Workflow Runtime Contract

## Purpose
This project uses the `dev-workflow` Atlas mode.
Structured markdown documentation is the control surface for planning, implementation, review, and synchronization.
AI accelerates execution. Humans retain ownership of intent, architecture, prioritization, and irreversible decisions.

## Local Authority
Project-specific constraints override reusable workflow guidance.
Record local rules below the `atlas-dev-workflow-bridge:end` marker.

## Atlas Configuration
Active config: `atlas.yaml`

## Core Principles
- Humans approve intent, architecture, scope, priorities, and irreversible decisions.
- Agents must not silently decide architecture changes, schema/API contract changes, broad-impact dependency additions, security/privacy-sensitive behavior, or changes conflicting with documented constraints.
- Documentation is operational state, not passive reference.
- Prefer compact, structured, updateable notes over long generic prose.

### Explicit Uncertainty
Distinguish between: `decided`, `proposed`, `unclear`, `blocked`.
If key information is missing, ask, flag, or defer.

## Runtime Routing
`AGENTS.md` is the routing authority. The skill router table and routing constraints are injected per-message by the `route-inject` hook.

Entry points: `context-map.md` (structure), `docs/In-flight/` (active work).

## Commit Message Shape
```
<type>: <short imperative summary>

Context:
- <why this change exists>

Changes:
- <main change>

Verification:
- <check run or "Not run: <reason>">
```
Types: `docs`, `workflow`, `governance`, `planning`, `implementation`, `review`, `chore`

## Escalation
Escalate when a task conflicts with constraints, requires architecture/schema/API/security decisions, lacks confidence to choose the next gate, exceeds approved scope, or depends on missing/contradictory docs.
State: uncertainty, decision needed, impacted area, recommended next step.

## Vocabulary
Labels defined in `docs/vocabulary.md`. Skills define logic on top of labels; they do not redefine them.

## Repo Specific Instructions
- Add project-specific instructions below the `atlas-dev-workflow-bridge:end` marker so Atlas sync preserves them.
- Local project instructions below the managed Atlas block override reusable `dev-workflow` guidance when they conflict.
<!-- atlas-dev-workflow-bridge:end -->

## Claude Code: Workflow State Gate

Hooks in `.claude/hooks/` gate writes and turn-end via `.claude/workflow-state.json`. Set required fields before acting; reset to defaults after the skill's work is done.

- **`docs/` writes** (`dw-note-manager`): set `active_skill: "dw-note-manager"`
- **Implementation writes** (`project-implementer`): set `active_skill: "project-implementer"`, `gate_status: "approved"`, `approved_scope: ["<paths>"]`
- **Verification** (`implementation-verifier`): set `verification_required: true`; set `verification_done: true` when checks pass
- **Review-sync** (`project-review-sync`): set `phase: "review-sync"`, `review_subphase: "<current>"`; set `review_subphase: "complete"` to release stop-gate

Defaults: `phase: "none"`, `active_skill: "none"`, `gate_status: "none"`, `approved_scope: []`, `verification_required: false`, `verification_done: false`
