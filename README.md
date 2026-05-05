# Project Planning Workflow

A documentation-centered workflow for using AI assistants on software projects.

The project treats markdown documentation as operational state: intent is clarified, durable notes are updated deliberately, implementation is planned and approved, code changes are reported, and review routes any documentation sync back through clarification and note management.

## What This Repository Contains

- `AGENTS.md` - root operating charter for agents working in this repository.
- `clarify-intent.md`, `Note Manager.md`, `planner-agent.md`, `implementer-agent.md`, `review-agent.md` - role contracts for the workflow.
- `task-packet-schema.md`, `implementation-report-schema.md`, `clarified-context-handoff.md`, `note-ready-handoff.md` - reusable artifact schemas.
- `Two-Phase Workflow Boundary.md` and `Durable Notes Follow Accepted Implementation.md` - core workflow decisions.
- `Templates/` - starter markdown templates for new notes.
- `Tags/` and `Status Tag Registry.md` - note-state tags used by the workflow.
- `tools/local_note_search.py` - local graph-based note retrieval helper used by the note-search workflow.

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

## Workflow Summary

The current v1 path is:

```text
idea -> clarify-intent -> clarified context handoff -> Note Manager
```

Implementation planning remains downstream and should begin from note-backed project state:

```text
notes or direct request -> planner -> task packet -> approval -> implementer -> implementation report -> review/sync
```

Post-implementation documentation synchronization routes through:

```text
review/sync -> clarify-intent -> clarified context handoff -> Note Manager
```

## Operating Rules

- Humans own intent, architecture, priority, and irreversible decisions.
- Agents must expose uncertainty instead of silently resolving high-impact choices.
- Durable note creation, metadata changes, link changes, archival changes, and corrections route through `Note Manager`.
- Implementation begins only from an approved task packet or a sufficiently specific direct coding request.
- Implementation reports must state what changed, why, checks run, assumptions, unresolved issues, and review/sync follow-up.

## Recommended First Read

1. `AGENTS.md`
2. `Two-Phase Workflow Boundary.md`
3. `Note Manager.md`
4. `planner-agent.md`
5. `implementer-agent.md`
6. `review-agent.md`
7. `task-packet-schema.md`
8. `implementation-report-schema.md`
