# Subject Bundle Splitting

Status: [[Tags/status-draft]]
Type: [[design-note]]
Parent: [[clarify-intent]]
Related: [[Two-Phase Clarification Architecture]], [[clarify-intent]]
Created: 2026-05-15
Last Reviewed: 2026-05-15
Decisions: The split axis is semantic subject, not target note or note action. Bundle split is intake evidence only; note-manager owns subject-to-note mapping.
Source: modes/dev-workflow/skills/dw-clarify-intent/SKILL.md
Dependencies:
Tasks:

---

## Design

When a clarification prompt contains multiple domains, areas, or branching ideas, `dw-clarify-intent` splits it into provisional subject bundles before downstream work begins. This keeps subjects traceable through the workflow without forcing premature decisions about note structure.

## Bundle Shape

Each bundle uses this fixed shape:
- `id` — stable short label
- `label` — human-readable subject name
- `summary` — 1–2 line description
- `scope` — what is in / out for this bundle
- `why-distinct` — why this should not collapse into a neighboring bundle

One bundle holds one domain or area. Branches inside a bundle stay together only when closely related. If a branch can become its own durable subject, it should be split and the connection preserved rather than blended into a broader bundle.

## Split Axis: Semantic Subject

The split axis is semantic subject — one coherent area of meaning. It is not:
- target note (which note will record this)
- note action (create vs. update)
- note type (idea-note vs. design-note)

Splitting by note action or target note at this stage pre-decides structure that belongs to note-manager, and likely misaligns subjects that span more than one note or map to zero note actions.

## Intake Evidence, Not Final Structure

The bundle split is intake evidence, not final note structure. `note-manager` owns subject-to-note mapping: deciding how many notes a subject produces, which notes are the right targets, and whether two subjects should merge into one note action. The bundle split gives note-manager traceable input; it does not bind note-manager's decisions.

## Design Rationale

Without this boundary, the clarification step implicitly decides note structure by grouping subjects around target notes — collapsing two distinct decisions ("what is this about?" and "where does it go?") into one. Keeping them separate lets note-manager apply its placement rules without inheriting structuring choices made during a phase not designed for that.
