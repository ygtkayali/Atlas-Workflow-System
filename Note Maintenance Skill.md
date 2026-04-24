# Note Maintenance Skill

Status: [[status-pending]]
Parent: [[Idea Hub]]
Related: [[Local Note Search Script]]
Created: 14-04-2026

## Summary

Create a dedicated note maintenance skill for existing notes. This skill is separate from `note-manager`: `note-manager` remains focused on a single note and its immediate context, while note maintenance may operate across a much broader note space and therefore must prioritize efficiency.

## Details

The skill is intended for cleaning and restructuring existing notes when the user provides a maintenance task. It should support broader vault maintenance work without forcing manual review of the entire vault.

This skill is expected to become more important as vault size grows, but it is not yet decided whether it belongs in v1. That timing should remain open until later iterations make the need and impact clearer.

The skill should default to an analyze-first approach.

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

This boundary must be defined explicitly later. It should not be guessed or normalized implicitly, because vault-wide maintenance can easily turn into unauthorized structural reorganization.

## Open Questions

- Does this skill belong in v1, or should it remain a later-phase capability?
- What exact maintenance actions are safe for scoped direct application?
- What exact restructuring actions must always stay proposal-only?
- What scope controls should be required for each task, such as whole vault, note-type subset, folder, or explicit file list?
- How should findings outside the requested task scope be handled?
