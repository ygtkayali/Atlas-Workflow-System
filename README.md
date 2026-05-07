# Atlas Workflow System

Atlas is a local workflow system for installing, initializing, checking, and synchronizing documentation-centered AI workflows.

This repository contains the Atlas CLI source, shared workflow assets, and the first concrete mode: `dev-workflow`. The earlier Project Planning Workflow now acts as the source basis for that mode rather than the whole system identity.

## What This Project Is For

This repository is for teams or solo developers who want AI coding assistance without losing control of project direction, and who want reusable workflow setup across projects.

It provides a practical operating model where:

- humans own intent, architecture, priorities, and irreversible decisions;
- project notes capture current context, constraints, decisions, and tasks;
- agents work from compact, relevant context instead of broad repo summaries;
- implementation begins only from an approved packet or a sufficiently specific direct coding request;
- completed work returns a structured report; and
- review routes any documentation changes back through clarification and note management.

The result is a loop between human intent, project documentation, implementation work, and review.

## Problem It Solves

AI coding workflows can become unreliable when agents infer too much from loose prompts, silently change scope, or leave documentation behind after implementation.

This project addresses those failure modes by making the workflow explicit:

- unclear ideas go through clarification before they become durable project state;
- durable note changes go through `Note Manager`;
- implementation planning starts from note-backed context;
- coding work stays scoped to an approved packet or clear direct request;
- implementation reports explain what changed and what remains unresolved;
- review/sync identifies stale documentation, mismatches, and follow-up work.

The goal is not to add bureaucracy. The goal is to prevent hidden design drift, stale notes, bloated context, and unclear handoffs.

## Tools And Roles

The `dev-workflow` mode is organized around a small set of agent roles and local tools:

- `clarify-intent` turns rough ideas, ambiguous requests, or review/sync proposals into clarified context.
- `Full notes/note-manager.md` owns durable note create/update decisions after clarification.
- `Full notes/planner-agent.md` prepares scoped implementation packets from note-backed project state.
- `Full notes/implementer-agent.md` performs bounded code changes and returns implementation reports.
- `Full notes/review-agent.md` compares implementation results to the approved packet and routes documentation sync.
- `shared/tools/local_note-search.py` retrieves nearby linked notes from a known seed note without broad vault search.
- `Full notes/note-search-skill.md` is the shared retrieval interface for graph search and Codex-local semantic search.

These roles are intentionally gated. A downstream role should not silently absorb work that belongs to an earlier phase.

## Workflow Summary

The current v1 idea-to-note path is:

```text
idea -> clarify-intent -> visible clarified context handoff -> Note Manager draft
```

When a durable note change is required and the handoff is ready, the default is to invoke `Note Manager` immediately after the visible handoff. Approval is required for the resulting draft or durable write, not merely for the phase switch.

Implementation planning remains downstream and should begin from note-backed project state:

```text
notes or clear direct request -> planner -> task packet -> approval -> implementer -> implementation report -> review/sync
```

Post-implementation documentation synchronization routes through:

```text
review/sync -> clarify-intent -> visible clarified context handoff -> Note Manager draft
```

## Repository Structure

- `AGENTS.md` - root operating charter for agents working in this repository.
- `atlas` and `tools/atlas.py` - local Atlas CLI entry point and command implementation.
- `modes/dev-workflow/` - first mode manifest, starter assets, templates, and mode skill sources.
- `shared/` - shared skills and tools reused across modes.
- `Main Hubs/` - compact entry points into the note graph.
- `Fleeting notes/` - idea notes and early capture.
- `Full notes/` - durable project notes that are not hubs, templates, tags, or fleeting notes.
- `Templates/` - starter templates for new notes.
- `Tags/` and `Full notes/Status Tag Registry.md` - status tags and their intended meanings.
- `Full notes/clarify-intent.md`, `Full notes/note-manager.md`, `Full notes/planner-agent.md`, `Full notes/implementer-agent.md`, `Full notes/review-agent.md` - role contracts.
- `Full notes/clarified-context-handoff.md`, `Full notes/note-ready-handoff.md`, `Full notes/task-packet-schema.md`, `Full notes/implementation-report-schema.md` - reusable workflow schemas.
- `Full notes/Two-Phase Workflow Boundary.md` and `Full notes/Durable Notes Follow Accepted Implementation.md` - core workflow decisions.
- `Full notes/tool-policy.md` - tool-use expectations and boundaries.
- `shared/tools/local_note-search.py` - deterministic local note-neighborhood retrieval helper source.
- `Full notes/note-search-skill.md` - durable contract for routing known-seed graph search and concept-level semantic search.

Idea notes and early capture belong in `Fleeting notes/`.
Local Obsidian workspace state remains excluded from v1.

## Basic Setup

1. Clone the repository.
2. Open the folder in a markdown editor or Obsidian if you want wiki-link navigation.
3. Read `AGENTS.md` first. It is the root operating policy.
4. Read `Main Hubs/Workflow Hub.md` for the compact note index.
5. Use `Templates/` when creating new project notes.

No package installation is required for the markdown workflow itself.

## Atlas CLI

Run Atlas directly from this checkout:

```bash
./atlas --help
```

To make `atlas` available outside this directory, create a one-time user-local symlink:

```bash
ln -s "$(pwd)/atlas" ~/.local/bin/atlas
```

`~/.local/bin` must be on your `PATH`. After the symlink is created, use `atlas` from any project directory:

```bash
atlas --help
atlas mode list
```

If the symlink already exists and points to an old checkout, replace it:

```bash
rm ~/.local/bin/atlas
ln -s "$(pwd)/atlas" ~/.local/bin/atlas
```

### Common Commands

Inspect available modes:

```bash
atlas mode list
```

Initialize a project with the development workflow:

```bash
atlas init --mode dev-workflow .
```

Check a project's Atlas setup:

```bash
atlas health check .
```

Synchronize project-local managed assets:

```bash
atlas sync .
```

Synchronize globally installed skills and shared tools for the current project's mode:

```bash
atlas sync skills
```

You can also call the explicit skills subcommand:

```bash
atlas skills sync --mode dev-workflow
```

Project initialization and project sync do not install global skills automatically. Run skill sync separately when shared skills or tools change.

The bundled search helper uses only the Python standard library and can be run with Python 3:

```bash
python3 shared/tools/local_note-search.py \
  --vault-root . \
  --seed-path "Full notes/note-manager.md" \
  --format json
```

Semantic note search has a repo-local helper copy for this vault.
It currently depends on the shared source helper at `shared/tools/local_note_semantic_search.py`, the installed/deployed helper at `~/.codex/tools/local_note_semantic_search.py`, the installed `note-search` skill, the configured conda environment, and the vault-local `.codex-note-search/` cache.
The shared semantic helper source is intentional; keep it synchronized with the installed helper when behavior changes.

Atlas mode assets use lowercase hyphenated skill IDs such as `dw-clarify-intent`, `dw-note-manager`, `project-planner`, and shared `note-search`. Run `./atlas health check .` to inspect local drift and `./atlas skills sync --mode dev-workflow` to review the global skill sync plan.

## Operating Rules

- Humans own intent, architecture, priority, and irreversible decisions.
- Agents must expose uncertainty instead of silently resolving high-impact choices.
- Durable note creation, metadata changes, link changes, archival changes, and corrections route through `Note Manager`.
- Implementation begins only from an approved task packet or a sufficiently specific direct coding request.
- Implementation reports must state what changed, why, checks run, assumptions, unresolved issues, and review/sync follow-up.

## Recommended First Read

1. `AGENTS.md`
2. `Main Hubs/Workflow Hub.md`
3. `Full notes/Two-Phase Workflow Boundary.md`
4. `Full notes/note-manager.md`
5. `Full notes/clarify-intent.md`
6. `Full notes/planner-agent.md`
7. `Full notes/implementer-agent.md`
8. `Full notes/review-agent.md`
9. `Full notes/task-packet-schema.md`
10. `Full notes/implementation-report-schema.md`
