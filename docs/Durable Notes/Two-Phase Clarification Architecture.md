# Two-Phase Clarification Architecture

Status: [[Tags/status-draft]]
Type: [[design-note]]
Parent: [[clarify-intent]]
Related: [[Clarification Depth Model]], [[Clarify Intent Output Modes]], [[Interpretation Basis]], [[clarify-intent]]
Created: 2026-05-15
Last Reviewed: 2026-05-15
Decisions: Phase 2 introduces no new decisions. Handoffs are written as approval-pending artifacts under docs/In-flight/. A produced handoff does not grant implicit permission to continue into implementation or note mutation in the same turn.
Source: modes/dev-workflow/skills/dw-clarify-intent/SKILL.md
Dependencies:
Tasks:

---

## Design

The skill separates its work into two distinct phases. Phase 1 is a conversational loop; Phase 2 is handoff synthesis. Keeping them separate prevents synthesis pressure from closing off questions that should stay open longer.

## Phase 1: Clarification Loop

Phase 1 is interactive. The skill asks, challenges, and updates the clarification state. It does not synthesize a full handoff unless the user explicitly asks or the state is clearly ready.

Loop steps:
1. Capture the idea as the user currently states it.
2. Restate goal, problem shape, and proposed direction separately.
3. Split into subject bundles when the prompt is multi-domain.
4. Identify ambiguity, hidden assumptions, missing decisions, and inconsistencies — distinguish high-impact from minor.
5. Ask the highest-value questions; challenge weak directions with concrete tradeoffs.
6. Update the clarification state (decided / proposed / unclear / blocked).
7. Continue, end, hand off, or mark `partial_clarification`.

### Iteration Cap

After three full loop iterations on the same subject without reaching `ready_for_note_manager`, the loop stops. A `partial_clarification` summary is produced listing what is settled, what is blocking, and explicit options (defer / narrow scope / escalate / abandon). The user then directs the next move. The cap exists to surface subjects that need a human decision to progress.

### Escalation Conditions

These keep work in Phase 1 regardless of iteration count:
- conflicting goals that cannot be resolved through clarification,
- scope that cannot be narrowed without a human choice,
- high-impact uncertainty still present,
- source-of-truth, ownership, or note placement unclear,
- the request would force note-manager or the planner to guess key intent.

## Phase 2: Handoff Creation

Phase 2 synthesizes. It records what was clarified, what remains proposed, what is unclear, and what is blocked. It does not introduce new decisions.

The handoff is written as an approval-pending artifact under `docs/In-flight/` — a reviewable workflow gate, not a hidden internal state. A produced handoff does not grant implicit permission to continue into implementation or durable note mutation in the same turn.

### Long-Session Re-Validation

Before producing a handoff after a long or compacted conversation:
- re-read the original triggering input,
- verify the handoff still matches in goal, scope, tone, and uncertainty,
- flag any drift rather than normalizing it.

## Design Rationale

Synthesis pressure — the pull toward producing a polished output — tends to normalize unresolved uncertainty. Keeping phases distinct means Phase 1 stays genuinely exploratory and Phase 2 only records what Phase 1 actually settled.
