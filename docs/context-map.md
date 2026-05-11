# Context Map

Last Updated: 2026-05-11

---

## Purpose

Stable project-structure map for the Atlas Workflow System.
Use this file to understand what major files and folders are for.

This file describes structure only. Workflow rules, routing, gates, and loading policy live in `AGENTS.md`.

---

## Project Type

Dev-workflow Atlas source repository.
This repo defines and develops the reusable `dev-workflow` mode.

Mode-specific behavior lives under `modes/dev-workflow/` and syncs into consumer projects through Atlas.

---

## Root Files

| Path | Purpose |
| --- | --- |
| `AGENTS.md` | Runtime contract, local authority, workflow routing, and gates |
| `CLAUDE.md` | Claude-facing runtime instructions generated or maintained alongside local workflow rules |
| `atlas.yaml` | Atlas configuration for this workspace, including mode, managed docs, managed skills, and managed tools |
| `docs/context-map.md` | Stable map of this project's files and folders |
| `docs/active-context.md` | Current workflow state pointer for phase, gate, active subject, and next expected action |

---

## Documentation Folders

| Path | Purpose |
| --- | --- |
| `docs/Durable Notes/` | Settled or active workflow design notes |
| `docs/Idea Backlog/` | Exploratory workflow ideas and unresolved design directions |
| `docs/Main Hubs/` | Lightweight hub notes when a subject needs a local index |
| `docs/Templates/` | Reusable note templates for this workflow vault |
| `docs/Reports/` | Workflow reports and generated or temporary workflow artifacts |
| `docs/Reports/in-flight/` | Active handoffs, packets, and reports that still affect the next workflow step |
| `docs/Tags/` | Tag notes and managed label definitions |
| `docs/Tasks/` | Task notes when task tracking is useful |

---

## Mode Source

| Path | Purpose |
| --- | --- |
| `modes/dev-workflow/` | Canonical reusable mode source |
| `modes/dev-workflow/agents-bridge.md` | Managed `AGENTS.md` bridge content for dev-workflow projects |
| `modes/dev-workflow/docs/` | Managed docs, templates, tags, and starter context files copied into project vaults |
| `modes/dev-workflow/skills/` | Source files for managed Codex skills |
| `modes/dev-workflow/tools/` | Managed workflow tools |
| `modes/dev-workflow/vocabulary.md` | Shared workflow vocabulary and label definitions |

---

## Generated Or Managed Areas

| Path | Purpose |
| --- | --- |
| `docs/.codex-note-search/` | Note-search index/cache files |
| `docs/Reports/in-flight/` | Active workflow artifacts; not durable project knowledge |
| `modes/dev-workflow/docs/` | Source files that Atlas can sync into project docs |
| `modes/dev-workflow/skills/` | Source files that Atlas can sync into installed or project-managed skills |
