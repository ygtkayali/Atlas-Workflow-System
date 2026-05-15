# Technical Project Documentation Governance

Status: [[Tags/status-settled]]
Type: [[design-note]]
Parent:
Related: [[Dev Workflow Documentation Model]], [[note-manager]], [[review-agent]], [[Workflow Artifact Lifecycle and Closeout]], [[Two-Phase Workflow Boundary]], [[Durable Notes Follow Accepted Implementation]]
Created: 2026-05-13
Last Reviewed: 2026-05-15
Source: promoted from `docs/Idea Backlog/Technical Project Documentation Governance.md`
Project Subjects: technical documentation governance, project-review-sync phases, Note Manager confirmation gates, documentation sync analysis
Tasks: `docs/Archieved/Tasks/technical-project-documentation-governance.md`
Reports:

---

## Design Scope

Governance rules for technical project documentation in `dev-workflow`: what a technical project must document, how `Project Subject` and `Design Note` differ, how transient task artifacts become durable knowledge, and how `project-review-sync` and `dw-note-manager` are gated to prevent silent action.

## Context

Documentation lacked clarity on which note type to use for a given subject. Review/sync was silently combining implementation review, documentation sync analysis, in-flight cleanup, artifact summarization, and documentation proposals into one continuous flow. Neither review/sync nor Note Manager had explicit gates preventing them from executing durable changes without user confirmation.

## Chosen Design

**Note types:**
- `Project Subject` is the default durable note for one active technical area (feature, workflow behavior, module, tool, integration, or implementation concept).
- `Design Note` is for cross-cutting design, reusable behavior, architecture constraints, or decisions affecting multiple subjects. Every accepted idea does not automatically become a design note.
- Keep the documentation type set small.

**Transient artifacts:**
- Task packets and implementation reports are workflow evidence, not durable knowledge notes.
- Durable note creation or update must go through `dw-note-manager`.
- Post-implementation review identifies whether accepted implementation created durable knowledge.
- Idea notes become promotion candidates when accepted implementation settles or materially advances them.

**Confirmation gates:**
- `project-review-sync` may analyze and propose; it may not execute durable action without confirmation.
- `dw-note-manager` may decide or draft proposed note actions; it may not write until approved.
- Action confirmation is required before draft preparation; write confirmation is required before durable mutation.
- Confirmation is also required before artifact cleanup, archiving, deletion, movement, or idea promotion.

**Hard phase gates in `project-review-sync`:**
- Implementation review, documentation sync analysis, and artifact closeout are separate jobs.
- Each phase produces a proposal and stops. No phase automatically enters the next.
- Gated sequence:

```
implementation report
-> implementation review        (propose disposition, stop)
-> user confirms next phase
-> documentation sync analysis  (propose sync subjects, stop)
-> user confirms Note Manager handoff
-> Note Manager manifest or draft
-> user confirms durable write
-> user confirms artifact closeout
-> archive summary / cleanup
```

## Rationale

Review/sync was overloaded. Separating it into gated phases ensures the user retains approval authority at each boundary and prevents silently combined flows from making irreversible changes without awareness.

Keeping note types narrow prevents documentation sprawl and maintains a clear distinction between local technical state (Project Subject) and broader constraints and rationale (Design Note).

## Alternatives Considered

- Making every accepted idea become a design note — rejected; keeps type set small and preserves the intended boundary.
- Documentation sync analysis as a fully separate skill — deferred; currently a named mode under `project-review-sync`.
- Task-lane closeout as a separate tool — deferred; currently a named mode under `project-review-sync`.
- A single continuous review/sync flow — rejected; this is what caused the overload problem.

## Constraints

- Neither `project-review-sync` nor `dw-note-manager` may execute durable actions without confirmation.
- Implementation review, documentation sync analysis, and artifact closeout are separate gated phases.
- Durable note mutation is owned exclusively by `dw-note-manager`.
- Task packets, reports, handoffs, context proposals, manifests, and drafts are workflow evidence and do not become durable notes by themselves.

## Technical Shape

- `project-review-sync` operates in explicit modes: `implementation-review`, `documentation-sync-analysis`, `task-lane-closeout`. Each mode stops and returns a proposal.
- `dw-note-manager` distinguishes action confirmation (before draft preparation) from write confirmation (before durable mutation).
- Compact sync proposal tables: clear rows may go directly to Note Manager; uncertain rows route to `dw-clarify-intent`.
- Project Subject and Design Note templates were sharpened to enforce the note-type boundary at authoring time.

## Impacted Project Subjects

- `project-review-sync` — phase gate structure and explicit modes
- `dw-note-manager` — two-stage confirmation (action vs. write)
- `docs/Templates/Design Note Template.md` and `docs/Templates/Project Subject Template.md` — sharpened templates
- `docs/Durable Notes/Workflow Artifact Lifecycle and Closeout.md` — transient artifact policy
- `docs/Durable Notes/Dev Workflow Documentation Model.md` — documentation type and governance model

## Open Questions

- Should documentation sync review be a required closeout phase or only triggered when durable knowledge changed?
- Should idea promotion become a first-class `dw-note-manager` action?
- Should documentation sync analysis or task-lane closeout eventually become separate skills/tools?
- Should confirmation prompt shapes be standardized as a reusable template in mode source?
- What is the long-term archive policy for consumed raw workflow artifacts?

## Review Notes

Core implementation completed 2026-05-14. Task archived at `docs/Archieved/Tasks/technical-project-documentation-governance.md`. Open questions above are governance follow-up, not blockers to settling this design.
