# Note Maintenance Skill

Status: [[status-archived]]
Parent: [[Idea Hub]]
Related: [[Local Note Search Script]], [[review-agent]]
Created: 14-04-2026
Last Reviewed: 2026-04-25

## Summary

This separate maintenance-skill direction has been archived. The current direction is to merge bounded maintenance review into [[review-agent]] instead of creating a separate maintenance skill.

`note-manager` remains focused on bounded durable note mutation from clarified context and supplied notes. Maintenance review now belongs to review/sync as an analysis and routing responsibility, not as direct note mutation authority.

## Archive Note

The current direction is that `project-review-sync` remains the named skill and acts as the analysis and routing layer for both implementation review and bounded maintenance review tasks.

Maintenance review produces a structured report, usually in conversation rather than as a durable file by default. That report is routed through `clarify-intent -> Note Manager` when durable note decisions or note mutations are needed.

## Details

The earlier idea was to create a dedicated skill for cleaning and restructuring existing notes when the user provides a maintenance task. It would support broader vault maintenance work without forcing manual review of the entire vault.

That separate-skill direction is no longer active for now. Broader vault maintenance still needs governance, but the review/sync role is the better middle layer because it can analyze state, produce findings, and route the result to clarification and note management without taking direct ownership of durable note changes.

The merged review direction keeps the analyze-first approach.

Current operating model:
- analysis/report mode for broader, riskier, or more ambiguous maintenance tasks
- scoped apply mode for simple, explicit maintenance actions

Possible examples of simple scoped maintenance include:
- adding required metadata to a known note subset
- normalizing known note aspects for a specific file type or note type

The skill may be supported by tools where needed for performance, especially when broader vault inspection would otherwise become too expensive.

A critical unresolved decision remains:
- the exact allowed action types
- which actions may be auto-applied
- which actions must remain proposal-only

This boundary is handled by keeping review as analysis and routing only. Durable note changes still go through `clarify-intent -> Note Manager`, because vault-wide maintenance can easily turn into unauthorized structural reorganization.

## Open Questions

- Does this skill belong in v1, or should it remain a later-phase capability?
- What exact maintenance actions are safe for scoped direct application?
- What exact restructuring actions must always stay proposal-only?
- What scope controls should be required for each task, such as whole vault, note-type subset, folder, or explicit file list?
- How should findings outside the requested task scope be handled?
