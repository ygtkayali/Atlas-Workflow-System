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

- **`docs/` writes** (`dw-note-manager`): set `active_skill: "dw-note-manager"`, then invoke the skill
- **Implementation writes** (`project-implementer`): set `active_skill: "project-implementer"`, `gate_status: "approved"`, `approved_scope: ["<paths>"]`, then invoke the skill
- **Verification** (`implementation-verifier`): set `active_skill: "implementation-verifier"`, `verification_required: true`, then invoke the skill; set `verification_done: true` when checks pass
- **Review-sync** (`project-review-sync`): set `phase: "review-sync"`, `review_subphase: "<current subphase name>"`; before stopping to show a proposal and await user input, set `review_subphase: "awaiting_approval"`; set `review_subphase: "complete"` when the full review is done. The stop-gate allows exit only on `awaiting_approval` or `complete` — any other named subphase is treated as abandoned in-progress work and is blocked.

**Timestamp requirement**: whenever writing non-default state, include `"state_set_at": "<ISO-8601 UTC timestamp>"` (e.g. `2026-05-15T14:32:00Z`). session-start.sh uses this to detect stale state from previous sessions. Without it, the hook falls back to file mtime, which is less reliable.

Defaults: `phase: "none"`, `active_skill: "none"`, `gate_status: "none"`, `approved_scope: []`, `verification_required: false`, `verification_done: false`, `state_set_at: null`

Active in-flight work items are tracked via `docs/In-flight/` artifacts, not a field in workflow-state.json.
