# Context Map

Last Updated: 15-05-2026

---

## Purpose

Stable project-structure map for the Atlas Workflow System repository.
Use this file to understand what major files, folders, source assets, and workflow documentation areas are for before loading deeper context.

This file describes structure only. Workflow rules, routing, gates, and loading policy belong in `AGENTS.md`.

Keep this file current when file paths, file names, folder roles, managed asset locations, or other structure-significant content changes.

---

## Project Type

Local workflow-system repository for Atlas. It owns the Atlas CLI, reusable workflow modes, managed skills and tools, project sync behavior, tests, and this repository's own `dev-workflow` documentation vault.

---

## Root Files

| Path                  | Purpose                                                                                                        |
| --------------------- | -------------------------------------------------------------------------------------------------------------- |
| `AGENTS.md`           | Codex runtime contract, local authority, workflow routing, gates, git governance, and repo-specific rules       |
| `CLAUDE.md`           | Claude-facing runtime contract managed from the same reusable bridge when that platform is synced               |
| `README.md`           | Human-facing overview, setup notes, common Atlas commands, and repository orientation                           |
| `atlas`               | Executable wrapper for the local Atlas CLI                                                                      |
| `atlas.yaml`          | Active Atlas configuration for this repository; currently `dev-workflow` with `docs/` as the vault              |
| `platforms.yaml`      | Platform registry mapping agent files, skill install roots, and tool install roots                             |
| `docs/context-map.md` | This project-specific structure map and recommended orientation entry point                                     |

---

## Project Folders

| Path                  | Purpose                                                                                                   |
| --------------------- | --------------------------------------------------------------------------------------------------------- |
| `tools/`              | Atlas CLI implementation source; `tools/atlas.py` contains mode, init, health, sync, and skill-sync logic |
| `modes/dev-workflow/` | Reusable `dev-workflow` mode source: manifest, managed bridge, starter docs, tags, templates, and skills |
| `shared/`             | Shared skills and tools reused across modes, including note-search helpers                                |
| `tests/`              | Unit tests and benchmark/test helpers for Atlas sync and note-search behavior                             |
| `docs/`               | This repository's own workflow vault, project notes, task lanes, templates, tags, and context map         |

---

## Documentation Areas

| Path                    | Purpose                                                           |
| ----------------------- | ----------------------------------------------------------------- |
| `docs/Durable Notes/`   | Active and settled workflow-system design notes and role contracts |
| `docs/Idea Backlog/`    | Exploratory ideas and unresolved directions                       |
| `docs/In-flight/`       | Active task lanes, handoffs, packets, reports, gates, and next actions |
| `docs/Main Hubs/`       | Lightweight index hubs for workflow schema and note navigation    |
| `docs/Templates/`       | Local copies of reusable note and workflow templates              |
| `docs/Tags/`            | Tag notes and managed label definitions                           |
| `docs/Archieved/Tasks/` | Distilled closeout summaries and archived workflow task artifacts |
| `docs/Archieved/Notes/` | Archived notes retained for historical reference                  |

---

## Generated Or Managed Areas

| Path                       | Purpose                                                                                           |
| -------------------------- | ------------------------------------------------------------------------------------------------- |
| `docs/.codex-note-search/` | Note-search index/cache files, if present                                                         |
| `docs/In-flight/`          | Active workflow artifacts; primary open workflow state and not durable project knowledge          |
| `docs/Archieved/`          | Historical material retained after closeout                                                       |
| `modes/dev-workflow/docs/` | Source assets copied into project vaults by Atlas init/sync; update here for reusable starter docs |
| `modes/dev-workflow/skills/` | Source skill definitions for the `dev-workflow` mode; sync globally with `atlas sync skills`     |
| `shared/tools/`            | Source tool implementations for cross-mode helper scripts                                          |
