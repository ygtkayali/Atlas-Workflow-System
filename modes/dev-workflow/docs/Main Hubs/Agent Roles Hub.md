# Agent Roles Hub

Status: [[Tags/status-settled]]
Parent: [[modes/dev-workflow/docs/Main Hubs/Workflow Hub]]
Related: [[modes/dev-workflow/docs/Main Hubs/Workflow Schemas Hub]]
Created: 2026-04-14
Last Reviewed: 2026-05-07
Scope: Local index for dev-workflow agent roles and installed skills.

## Overview

This hub maps workflow phases to the installed `dev-workflow` skills.

Use the project `AGENTS.md` and `atlas.yaml` first. Then use these skills according to the current phase and the user's request.

## Roles

- `dw-clarify-intent` handles ambiguous ideas, unclear requests, and documentation-sync proposals before durable note work.
- `dw-note-manager` handles bounded durable note create/update drafts after clarification.
- `note-search` retrieves bounded local note context for clarification, planning, and review roles.
- `project-planner` creates implementation packets from note-backed project state when planning is needed.
- `project-implementer` performs scoped coding work from an approved packet or sufficiently clear direct request.
- `implementation-verifier` checks implementation-like changes before final closeout when deeper verification is useful.
- `project-review-sync` compares implementation results to scope, identifies stale documentation, and routes sync work.

## Boundaries

Durable note mutation should route through `dw-note-manager` when the workflow requires it.

Broad or ambiguous implementation should not start directly from vague intent. Clarify or plan first.

Human decisions remain authoritative for architecture, scope, security, public interfaces, and irreversible changes.
