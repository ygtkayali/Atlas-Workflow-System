# Workflow CLI Tooling System

Status: [[status-draft]]
Parent: [[Idea Hub]]
Related: [[Workflow Hub]], [[Agent Roles Hub]], [[Workflow Mode Skill Governance]]
Created: 2026-05-06
Last Reviewed: 2026-05-07

---

## Idea

`atlas` is the local CLI and product layer for installing, initializing, checking, and synchronizing mode-based workflow systems.

It should support long-term work, learning, reading, knowledge tracking, project execution, and future knowledge-base maintenance through modes.

The CLI should make workflow setup reproducible without forcing every project to manually copy skills, templates, starter files, or `AGENTS.md` instructions.

## Current Direction

- V2 should start as a local CLI or local command surface, not as a PyPI release.
- PyPI plus `pipx` should be deferred until the local mode system proves useful.
- The CLI should behave as an installer, initializer, health checker, and synchronizer rather than as the workflow brain itself.
- The CLI should install skills, tools, templates, and necessary local files so Codex can use the selected workflow.
- The first mode should be `dev-workflow`.
- Mode manifests should use YAML.
- Mode manifests should be allowed to define mode-specific templates, starter notes, artifact folders, and human-facing vault folder names.
- Local project `AGENTS.md` files should remain authoritative for project-specific rules.
- The workflow system's canonical `AGENTS.md` should remain the authority for workflow decisions.
- Existing local `AGENTS.md` files should not be replaced automatically.
- If a local `AGENTS.md` already exists, the CLI should either leave it unchanged or add a clearly marked bridge only when explicitly allowed.
- Mode behavior belongs in a separate mode-governance note rather than being fully defined inside the CLI note.

## Version Scope

### V2: Local `atlas` Tooling

V2 should provide enough local tooling to make the first `dev-workflow` mode usable in real directories.

The local version should include:

- listing available local modes
- initializing the `dev-workflow` mode in a project or vault
- installing or synchronizing mode-specific skills locally
- checking expected files, skills, templates, and tools
- reporting drift without silently overwriting local project rules

The local version should prioritize reviewable behavior over distribution polish.

### V3: Distribution And Mode Maturity

V3 can revisit public packaging after the local workflow is stable.

V3 may include:

- PyPI and `pipx` distribution
- stronger update/version handling
- mode tests or evaluation checks
- additional modes beyond `dev-workflow`
- generated skill or overlay tooling if local duplication becomes costly

## Possible CLI Commands

```bash
atlas mode list
atlas init --mode dev-workflow .
atlas skills install --mode dev-workflow
atlas skills sync --mode dev-workflow
atlas health check .
```

`doctor` should not be the user-facing term.
Use `health check` for setup and drift inspection.

`update` should remain deferred until local versioning and managed-file policy are clearer.

## Manifest Format

Mode manifests should use YAML.

The initial `manifest.yaml` should likely include:

- mode name
- mode purpose
- active skills
- disabled skills
- required files
- templates
- starter notes
- vault folder names
- artifact folders
- tools
- gates
- default artifacts
- health checks

The manifest should define what `atlas` can inspect, initialize, install, and synchronize for a mode.
It should not override local project authority.

For `dev-workflow`, the mode manifest should probably use a clearer name than `Fleeting notes/` for draft implementation ideas, such as `Idea Backlog/`.
That name better matches notes that are waiting to be refined, planned, promoted to durable project documentation, implemented, or discarded.

## Setup Responsibilities

- install mode-specific Codex skills
- initialize project or vault starter files
- check whether expected files and skills exist
- detect stale or missing workflow assets
- protect existing local `AGENTS.md` files
- provide explicit update or sync commands instead of hidden mutation
- support both technical project setup and non-technical vault setup
- read mode behavior from YAML manifests where possible

## Project And Vault Setup

For a technical project, the CLI could set up a workflow-aware project directory without taking over repo-specific rules.

For a vault, the CLI could create or update the note-taking frame with templates, hubs, starter notes, and selected skills.

For an existing vault, the CLI could load or synchronize skills and check expected files without replacing the local project contract.

## Useful External Pattern

Graphify shows a useful two-layer setup pattern:

- global or user-level skill installation
- per-project Codex setup through local files

This workflow should copy the shape but be more conservative around `AGENTS.md`.

## Open Questions

- Should global skill installation be separate from project or vault initialization?
- Should CLI-managed state live in a config file, marker note, `.codex` file, or a generated metadata file?
- Should updates be version-aware through package metadata, installed file hashes, or explicit managed-block markers?
- Should `health check` only report drift or also offer fixes?
- How much should the CLI know about mode internals versus delegating to mode manifests?
- Which commands are necessary for the first local `dev-workflow` mode, and which can wait for V3?
- Should the first local command surface be a small script before becoming a packaged CLI?
- Should `skills install` and `skills sync` remain separate commands or become one command with options?
- Should `atlas health check` inspect only the current directory or accept both path and mode arguments?

## Tensions

- Setup should be easy without hiding durable workflow decisions.
- Local project authority must remain clear even when the CLI installs shared workflow assets.
- The CLI should be useful early without becoming a fragile installer that overwrites user edits.
- Versioned updates are useful, but update behavior must be reviewable and reversible.

## Next Possible Step

Define the first `dev-workflow` `manifest.yaml`, then use it to drive local `atlas` mode listing, initialization, skill install/sync, and health checks.
