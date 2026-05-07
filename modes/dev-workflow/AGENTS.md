<!-- atlas-dev-workflow-bridge:start -->
# Dev Workflow Project Bridge

This project is configured for the `dev-workflow` Atlas mode.

## Local Authority

Local project instructions are authoritative.

If this project later adds project-specific constraints, verification commands, architecture rules, ownership rules, or coding conventions, record them in this `AGENTS.md`. Those local rules override reusable `dev-workflow` guidance when they conflict.

The reusable workflow mode does not override human decisions, project architecture, public APIs, security/privacy constraints, or repo-specific implementation rules.

## Atlas Configuration

The active Atlas configuration lives in:

- `atlas.yaml`

Use it to identify:

- the selected Atlas mode,
- the local workflow docs path,
- managed workflow assets,
- managed skills,
- and managed tools.

By default, workflow documentation lives under:

- `docs/`

Start with:

- `docs/Main Hubs/Workflow Hub.md`
- `docs/Main Hubs/Agent Roles Hub.md`
- `docs/Main Hubs/Workflow Schemas Hub.md`

## Skill Routing

Use the installed `dev-workflow` skills for workflow phases:

- `dw-clarify-intent` for ambiguous ideas, early-stage requests, and unclear durable note intent.
- `dw-note-manager` for durable note create/update work after clarification.
- `note-search` for bounded note retrieval when workflow roles need note context.
- `project-planner` for implementation packets from note-backed project state.
- `project-implementer` for scoped coding work from an approved packet or sufficiently clear direct request.
- `implementation-verifier` for verification before final closeout when implementation-like changes were made.
- `project-review-sync` for implementation review, documentation sync routing, and bounded maintenance review.

Do not mutate durable notes directly when the workflow requires `dw-note-manager`.

Do not begin broad implementation work from vague intent. Clarify or plan first.

## Default Workflow

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

## Git And Verification

Before editing, inspect the relevant files and current git state.

Do not overwrite unrelated user changes.

Run the strongest practical checks for the changed area. If checks cannot be run, report that explicitly.

Do not commit unless the user explicitly asks for a commit.
<!-- atlas-dev-workflow-bridge:end -->
