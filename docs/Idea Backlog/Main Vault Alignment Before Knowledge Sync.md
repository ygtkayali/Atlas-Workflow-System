# Main Vault Alignment Before Knowledge Sync

Status: [[Tags/status-draft]]
Type: [[idea-note]]
Related: [[note-manager]]
Created: 05-05-2026
Priority: [[priority-low]] 

---

## Idea

The main vault may need an alignment pass before agents move project learnings, research outputs, or other extracted knowledge into it.

The concern is that the main vault's current state differs from this workflow vault enough that agents may produce awkward or inconsistent note output unless they receive better local operating context first.

## Questions

- How much of the main vault state should an instantiated agent receive before durable knowledge sync begins?
- Should an agent receive the full list of tag names upfront, or should tag use be handled through a smaller tag policy, tag registry, or retrieval step?
- What is the minimum context needed for `Note Manager` to select tags responsibly without loading too much of the vault?
- Should tag selection be an explicit `Note Manager` responsibility in the main vault, or should it be constrained by a separate main-vault `AGENTS.md` rule?
- What alignment is required before learned information from external project vaults or source material is moved into the main vault?

## Current Thinking

- Passing every tag name to every agent may be noisy and brittle.
- A more efficient approach may be to define tag-use rules in the main vault's `AGENTS.md`, then provide only the relevant tag subset or registry path when a task needs tagging.
- Knowledge sync should probably produce clarified context first, then route durable note changes through `Note Manager`.

## Open Decisions

- Whether the main vault should have a dedicated tag registry note.
- Whether agents should use broad tag lists, bounded tag subsets, or only explicit user-provided tags.
- Whether knowledge sync should wait until the main vault has its own note-placement and tag-selection rules.
