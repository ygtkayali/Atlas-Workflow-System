# Clarification Depth Model

Status: [[Tags/status-draft]]
Type: [[design-note]]
Parent: [[clarify-intent]]
Related: [[Two-Phase Clarification Architecture]], [[Interpretation Basis]], [[clarify-intent]]
Created: 2026-05-15
Last Reviewed: 2026-05-15
Decisions: Light depth may omit Interpretation Basis when the origin is a direct user prompt with no upstream artifact or hidden context. Full depth is required for any high-impact area. Escalation from light to full is not optional once a high-impact area surfaces.
Source: modes/dev-workflow/skills/dw-clarify-intent/SKILL.md
Dependencies:
Tasks:

---

## Design

`dw-clarify-intent` commits to a depth level before the clarification loop begins. Choosing depth upfront prevents the skill from over-clarifying narrow requests or under-clarifying high-impact ones.

## Depth Levels

**Light** applies to low-impact, narrow, or already-mostly-clear requests:
- restate the goal in 2–4 lines,
- ask at most two high-value questions,
- end clarification or produce a compact handoff.

`Interpretation Basis` may be omitted when the origin is the direct user prompt with no hidden context, source material, or upstream artifact being interpreted.

**Full** applies when the request touches any high-impact area or involves a multi-domain bundle. The full guided loop runs with full `Interpretation Basis` in any produced handoff.

## Escalation Rule

Start light. Escalate to full the moment a high-impact area surfaces. The escalation is not optional.

## High-Impact Taxonomy

These areas require full depth and bias toward `needs_clarification` until resolved:
- architecture or pipeline shape
- schema, API contract, or public interface
- new dependency with broad reach
- security, privacy, or auth behavior
- workflow gates, ownership boundaries, or note governance
- conflicts with documented constraints

Minor wording, presentation choices, and low-impact implementation details are not high-impact.

## Design Rationale

A single depth forces a tradeoff: always-light is too shallow for high-stakes decisions; always-full creates unnecessary friction for simple requests. The two-level model with an escalation rule keeps the default fast without removing the safety net.
