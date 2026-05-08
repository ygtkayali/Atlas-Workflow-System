# Workflow Hub

Status: [[Tags/status-settled]]
Parent:
Related: [[modes/dev-workflow/docs/Main Hubs/Agent Roles Hub]], [[modes/dev-workflow/docs/Main Hubs/Workflow Schemas Hub]], [[modes/dev-workflow/docs/Tags/idea-note]]
Created: 2026-04-14
Last Reviewed: 2026-05-08
Scope: Local entry point for the dev-workflow operating loop.

## Overview

This hub explains the reusable workflow installed by Atlas for development projects.

`AGENTS.md` remains the local operating contract for agents. `atlas.yaml` records the selected Atlas mode and the local docs path. This hub is the first note-graph entry point for understanding the workflow after a project has been initialized.

## Workflow Loops

For ideas and durable note work:

```text
idea -> dw-clarify-intent -> clarified context handoff -> dw-note-manager draft
```

For implementation:

```text
note-backed need or clear direct request -> project-planner when needed -> approved packet or clear direct request -> project-implementer -> implementation report -> project-review-sync
```

For documentation sync after implementation:

```text
project-review-sync -> dw-clarify-intent -> clarified context handoff -> dw-note-manager draft
```

## Start Here

- [[modes/dev-workflow/docs/Main Hubs/Agent Roles Hub]] explains which installed skill owns each phase.
- [[modes/dev-workflow/docs/Main Hubs/Workflow Schemas Hub]] explains the core handoff, packet, and report artifacts.
- `docs/Idea Backlog/` stores captured ideas, future plans, and questions before they become durable project state.
- [[modes/dev-workflow/docs/Tags/idea-note]] marks notes that are still idea-shaped rather than active feature subjects or design notes.

## Local Project Growth

As the project develops, add project-specific durable notes under `docs/Durable Notes/`, task packets under `docs/Tasks/`, and implementation or review reports under `docs/Reports/`.

Keep local project constraints in the project `AGENTS.md` when they affect agent behavior.
