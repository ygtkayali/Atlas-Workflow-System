# Context Map

Last Updated: {{date:DD-MM-YYYY}}

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

| Path                  | Purpose                                                                                                  |
| --------------------- | -------------------------------------------------------------------------------------------------------- |
| `AGENTS.md`           | Runtime contract, local authority, workflow routing, and gates                                           |
| `atlas.yaml`          | Atlas configuration for this workspace, when Atlas is used                                               |
| `docs/context-map.md` | Stable map of this project's files and folders                                                           |
| `docs/In-flight/`     | Current workflow state folder for active task lanes, handoffs, packets, reports, gates, and next actions |

---

## Project Folders

| Path               | Purpose                                                                                          |
| ------------------ | ------------------------------------------------------------------------------------------------ |
| `docs/`            | Project documentation and workflow artifacts                                                     |
| `docs/In-flight/`  | Active handoffs, packets, reports, and review artifacts that still affect the next workflow step |
| `<source-folder>/` | Main implementation source, if applicable                                                        |
| `<test-folder>/`   | Tests, checks, or verification fixtures, if applicable                                           |

---

## Documentation Areas

| Path                    | Purpose                                                           |
| ----------------------- | ----------------------------------------------------------------- |
| `docs/Durable Notes/`   | Settled or active project notes, if used                          |
| `docs/Idea Backlog/`    | Exploratory ideas and unresolved directions, if used              |
| `docs/Templates/`       | Reusable note or workflow templates, if used                      |
| `docs/Tags/`            | Tag notes and managed label definitions, if used                  |
| `docs/Archieved/Tasks/` | Distilled closeout summaries and archived workflow task artifacts |
| `docs/Archieved/Notes/` | Archived notes retained for historical reference                  |

---

## Generated Or Managed Areas

| Path                       | Purpose                                                                                  |
| -------------------------- | ---------------------------------------------------------------------------------------- |
| `docs/.codex-note-search/` | Note-search index/cache files, if present                                                |
| `docs/In-flight/`          | Active workflow artifacts; primary open workflow state and not durable project knowledge |
| `docs/Archieved/`          | Historical material retained after closeout                                              |
| `<generated-folder>/`      | Generated files, build outputs, or synced assets, if applicable                          |
