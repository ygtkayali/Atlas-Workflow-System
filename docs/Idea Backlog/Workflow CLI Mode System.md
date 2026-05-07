# Workflow CLI Tooling System

Status: [[Tags/status-draft]]
Parent: [[Main Hubs/Idea Hub]]
Related: [[Main Hubs/Workflow Hub]], [[Main Hubs/Agent Roles Hub]], [[Workflow Mode Skill Governance]]
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
- Project root should contain `atlas.yaml`.
- `atlas.yaml` should record active mode, Atlas or mode version, documentation vault name and path, managed files, managed skills, and managed tools.
- Managed assets are Atlas-created or Atlas-installed workflow assets, not every note in the project vault.
- Global skill sync should be separate from project initialization.
- `atlas skills sync --mode dev-workflow` should be the single user-facing command for installing missing skills and updating outdated skills.
- `atlas health check .` should be report-only.
- `atlas sync` may apply project-local file or tool updates only after explicit approval.
- V2 sync approval should apply to the whole proposed sync run, not per-file partial approval.
- Partial approval can be reconsidered later if sync plans become too large.
- Obsidian CLI integration is deferred for V2.
- Local project `AGENTS.md` files should remain authoritative for project-specific rules.
- The workflow system's canonical `AGENTS.md` should remain the authority for workflow decisions.
- Existing local `AGENTS.md` files should not be replaced automatically.
- If a local `AGENTS.md` already exists, the CLI should either leave it unchanged or add a clearly marked bridge only when explicitly allowed.
- Mode behavior belongs in a separate mode-governance note rather than being fully defined inside the CLI note.

## Current Implementation Snapshot

The first local Atlas scaffold exists in this repository:

- `./atlas` and `tools/atlas.py` provide the local command surface.
- `modes/dev-workflow/manifest.yaml` defines the first mode.
- `shared/manifest.yaml` defines shared assets such as `note-search` and the note-search tools.
- mode skill sources use lowercase hyphenated ids such as `dw-clarify-intent`, `dw-note-manager`, `project-planner`, and `project-implementer`.

`./atlas health check .` is report-only and currently surfaces missing project-local setup and missing hyphen-named global skills when those assets have not been synced yet.
`./atlas skills sync --mode dev-workflow` remains the explicit command for reviewing and applying global skill installation.

## Version Scope

### V2: Local `atlas` Tooling

V2 should provide enough local tooling to make the first `dev-workflow` mode usable in real directories.

The local version should include:

- listing available local modes
- initializing the `dev-workflow` mode in a project or vault
- synchronizing mode-specific global skills through a separate command
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
atlas health check .
atlas sync
atlas skills sync --mode dev-workflow
```

`doctor` should not be the user-facing term.
Use `health check` for setup and drift inspection.

`update` should remain deferred until local versioning needs are clearer.

`atlas init --mode dev-workflow .` should initialize project-local setup only.
It should create or update `atlas.yaml` and initialize docs vault assets, but it should not install global skills implicitly.

`atlas health check .` should read `atlas.yaml`, inspect the configured vault path, compare managed files, tools, and global skills against expected mode versions, and report missing, outdated, or inconsistent assets without mutating anything.

`atlas sync` should show a proposed project-local file or tool update plan, ask for explicit approval, and apply the whole approved sync run.

`atlas skills sync --mode dev-workflow` should install missing global mode skills, update outdated global mode skills, leave matching skills unchanged, and ask for explicit approval before applying changes.

## Manifest Format

Mode manifests should use YAML.

The initial `manifest.yaml` should likely include:

- mode name
- mode version
- mode description
- default vault name and path
- expected folders
- managed files
- managed skills
- managed tools
- vault folder names
- artifact folders
- gates
- default artifacts
- health checks
- sync policy

The manifest should define what `atlas` can inspect, initialize, install, and synchronize for a mode.
It should not override local project authority.

For `dev-workflow`, the mode manifest should use `Idea Backlog/` instead of `Fleeting notes/` for draft implementation ideas.
That name better matches notes that are waiting to be refined, planned, promoted to durable project documentation, implemented, or discarded.

The project-local `atlas.yaml` should use this initial shape:

```yaml
atlas:
  mode: dev-workflow
  version: 0.1

vault:
  name: "docs"
  path: "docs"

managed_files: []
managed_skills: []
managed_tools: []
```

The mode manifest should stay operational: files, folders, tools, skills, versions, checks, and sync policy.
Workflow philosophy belongs in `AGENTS.md` and skill files.

## Setup Responsibilities

- synchronize mode-specific Codex skills through a separate global skill command
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

- Should later updates become version-aware through package metadata, installed file hashes, or explicit managed-block markers?
- How much should the CLI know about mode internals versus delegating to mode manifests?
- Which existing commands need hardening after real-project trial?
- When should the local script-style command surface become a packaged CLI, if ever?
- Should `atlas health check` inspect only the current directory or accept both path and mode arguments?

## Tensions

- Setup should be easy without hiding durable workflow decisions.
- Local project authority must remain clear even when the CLI installs shared workflow assets.
- The CLI should be useful early without becoming a fragile installer that overwrites user edits.
- Versioned updates are useful, but update behavior must be reviewable and reversible.

## Next Possible Step

Use the scaffolded `dev-workflow` manifest to trial local `atlas` initialization, health checks, and explicit skill sync in a real project before expanding the mode catalog or packaging surface.
