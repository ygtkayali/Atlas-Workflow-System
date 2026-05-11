# Obsidian CLI Automation for Vault Workflows

Status: [[Tags/status-draft]]
Type: [[idea-note]]
Related: [[note-search-skill]]
Created: 05-05-2026
Last Reviewed: 2026-05-07
Priority:[[priority-mid]] 

---

## Idea

There may be an Obsidian CLI tool that can help automate parts of vault work, especially vault loading, note discovery, or operational handoffs between agents and the vault.

This should be explored as an idea before changing the workflow or depending on the tool.

## Questions

- What Obsidian CLI tool exists, and what operations does it actually support?
- Can it safely help with vault loading, note creation, metadata updates, link maintenance, or search?
- Would using it improve the current bounded `note-search` and `Note Manager` flow, or would it introduce too much hidden behavior?
- Does it respect the local-first, deterministic, approval-gated workflow?
- Should CLI automation be allowed only as an implementation detail after `Note Manager` has decided the note action?

## Current Thinking

- CLI automation may be useful for mechanical operations, but it should not replace workflow gates.
- The safest first use would be read-only inspection or deterministic file operations after an explicit note action is decided.
- Any tool dependency should be evaluated before being added to agent instructions.
- Obsidian CLI integration is deferred for Atlas V2.
- The first Atlas build should use plain filesystem markdown operations for initialization, health checks, sync, and managed workflow assets.
- Obsidian-specific automation can be researched later as a separate tool integration question.

## Open Decisions

- Whether to research the available Obsidian CLI options.
- Whether the main vault needs CLI-specific rules in `AGENTS.md`.
- Whether this workflow should keep plain filesystem markdown operations as the default path after Atlas V2.
