# Main Vault Note Structure and Agent Context

Status: [[status-draft]]
Parent: [[Idea Hub]]
Related: [[Workflow Hub]], [[Note Manager]]
Created: 05-05-2026

---

## Idea

The main vault should keep durable notes inside a full notes folder regardless of note type, so the main directory stays clean.

This differs from the current Project Planning Workflow vault, where workflow notes currently live near the root and templates point Idea Notes to `[[Idea Hub]]`.

## Questions

- Should the main vault's `AGENTS.md` define a folder policy where all durable notes live under a full notes folder?
- Should note type affect metadata and structure only, while folder placement remains fixed?
- How should agents distinguish between full notes, fleeting notes, and source material notes without turning folders into a rigid hierarchy?
- Should `Note Manager` in the main vault own the exact folder path for new notes?
- How much of this should be inherited from the Project Planning Workflow rules versus overridden locally?

## Current Thinking

- Folder placement and note type should be separate concepts.
- A full notes folder can keep the main directory clean without forcing hierarchical knowledge structure.
- The main vault likely needs a local `AGENTS.md` that adapts this workflow's principles to its own folder model.

## Open Decisions

- The exact full notes folder name.
- Whether existing full notes should be moved during an alignment pass.
- Whether folder moves require a separate maintenance review before `Note Manager` applies changes.

