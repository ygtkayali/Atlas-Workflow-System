# Project Planning Workflow

A documentation-centered workflow for building software with AI assistance.

This project treats markdown documentation as the control surface for AI-assisted work. Instead of asking an agent to jump straight from a vague request into code, the workflow makes intent, constraints, planning, implementation, review, and documentation sync visible as durable project state.

## What This Project Is For

This repository is for teams or solo developers who want AI coding assistance without losing control of project direction.

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

The workflow is organized around a small set of agent roles and local tools:

- `clarify-intent` turns rough ideas, ambiguous requests, or review/sync proposals into clarified context.
- `Note Manager.md` owns durable note create/update decisions after clarification.
- `planner-agent.md` prepares scoped implementation packets from note-backed project state.
- `implementer-agent.md` performs bounded code changes and returns implementation reports.
- `review-agent.md` compares implementation results to the approved packet and routes documentation sync.
- `tools/local_note_search.py` retrieves nearby linked notes from a known seed note without broad vault search.
- `Note Search Skill.md` is the shared retrieval interface for graph search and Codex-local semantic search.

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
- `Main Hubs/` - compact entry points into the note graph.
- `Full Notes/` - durable project notes that are not top-level governance files.
- `Templates/` - starter templates for new notes.
- `Tags/` and `Status Tag Registry.md` - status tags and their intended meanings.
- `clarify-intent.md`, `Note Manager.md`, `planner-agent.md`, `implementer-agent.md`, `review-agent.md` - role contracts.
- `clarified-context-handoff.md`, `note-ready-handoff.md`, `task-packet-schema.md`, `implementation-report-schema.md` - reusable workflow schemas.
- `Two-Phase Workflow Boundary.md` and `Durable Notes Follow Accepted Implementation.md` - core workflow decisions.
- `tool-policy.md` - tool-use expectations and boundaries.
- `tools/local_note_search.py` - deterministic local note-neighborhood retrieval helper.
- `Note Search Skill.md` - durable contract for routing known-seed graph search and concept-level semantic search.

Private idea notes, speculative future-development notes, and local Obsidian workspace state are intentionally excluded from v1.

## Basic Setup

1. Clone the repository.
2. Open the folder in a markdown editor or Obsidian if you want wiki-link navigation.
3. Read `AGENTS.md` first. It is the root operating policy.
4. Read `Main Hubs/Workflow Hub.md` for the compact note index.
5. Use `Templates/` when creating new project notes.

No package installation is required for the markdown workflow itself.

The bundled search helper uses only the Python standard library and can be run with Python 3:

```bash
python3 tools/local_note_search.py \
  --vault-root . \
  --seed-path "Note Manager.md" \
  --format json
```

Semantic note search is not bundled as a repo-owned script yet.
It currently depends on the Codex-local helper at `/home/yigit-kayali/.codex/tools/local_note_semantic_search.py`, the installed `note-search` skill, the `base-ml` conda environment, and the vault-local `.codex-note-search/` cache.
This keeps the semantic tool as a local installed dependency instead of creating a second script copy to synchronize.

## Operating Rules

- Humans own intent, architecture, priority, and irreversible decisions.
- Agents must expose uncertainty instead of silently resolving high-impact choices.
- Durable note creation, metadata changes, link changes, archival changes, and corrections route through `Note Manager`.
- Implementation begins only from an approved task packet or a sufficiently specific direct coding request.
- Implementation reports must state what changed, why, checks run, assumptions, unresolved issues, and review/sync follow-up.

## Recommended First Read

1. `AGENTS.md`
2. `Main Hubs/Workflow Hub.md`
3. `Two-Phase Workflow Boundary.md`
4. `Note Manager.md`
5. `clarify-intent.md`
6. `planner-agent.md`
7. `implementer-agent.md`
8. `review-agent.md`
9. `task-packet-schema.md`
10. `implementation-report-schema.md`
