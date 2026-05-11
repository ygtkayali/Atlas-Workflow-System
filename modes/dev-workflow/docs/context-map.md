# Context Map

Last Updated: YYYY-MM-DD

---

## Purpose

Stable project-structure map for this project.
Use this file to understand what major files and folders are for.

This file describes structure only. Workflow rules, routing, gates, and loading policy belong in `AGENTS.md`.

When this file is copied into a project, replace the example rows with that project's real files and folders. Keep it short enough to read at the start of a session.

---

## Project Type

Briefly state what kind of project this is and what the repository or vault owns.

Example:

```text
Web application repository for <product>.
```

---

## Root Files

| Path | Purpose |
| --- | --- |
| `AGENTS.md` | Runtime contract, local authority, workflow routing, and gates |
| `atlas.yaml` | Atlas configuration for this workspace, when Atlas is used |
| `docs/context-map.md` | Stable map of this project's files and folders |
| `docs/active-context.md` | Current workflow state pointer for phase, gate, active subject, and next expected action |

---

## Project Folders

| Path | Purpose |
| --- | --- |
| `docs/` | Project documentation and workflow artifacts |
| `docs/Reports/in-flight/` | Active handoffs, packets, and reports that still affect the next workflow step |
| `<source-folder>/` | Main implementation source, if applicable |
| `<test-folder>/` | Tests, checks, or verification fixtures, if applicable |

---

## Documentation Areas

| Path | Purpose |
| --- | --- |
| `docs/Durable Notes/` | Settled or active project notes, if used |
| `docs/Idea Backlog/` | Exploratory ideas and unresolved directions, if used |
| `docs/Templates/` | Reusable note or workflow templates, if used |
| `docs/Tags/` | Tag notes and managed label definitions, if used |
| `docs/Tasks/` | Task notes, if used |

---

## Generated Or Managed Areas

| Path | Purpose |
| --- | --- |
| `docs/.codex-note-search/` | Note-search index/cache files, if present |
| `docs/Reports/in-flight/` | Active workflow artifacts; not durable project knowledge |
| `<generated-folder>/` | Generated files, build outputs, or synced assets, if applicable |
