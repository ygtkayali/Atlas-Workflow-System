# Workflow Schemas Hub

Status: [[Tags/status-settled]]
Parent:
Related:
Created: 2026-04-14
Last Reviewed: 2026-05-08
Scope: Local index for core dev-workflow artifact shapes.

## Overview

This hub summarizes the main workflow artifacts used by the installed skills.

These summaries are intentionally compact. Add project-specific packet, report, and decision examples as the project develops.

## Core Artifacts

- `clarified context handoff`: visible output from `dw-clarify-intent` when an idea or sync proposal is ready for note management.
- `note-manager draft`: bounded create/update proposal from `dw-note-manager`; durable writes still require clear authorization.
- `task packet`: implementation planning artifact with objective, scope, constraints, acceptance criteria, risks, confidence, and approval state.
- `implementation report`: post-change summary with files touched, why they changed, checks run, assumptions, unresolved issues, and review/sync follow-up.
- `review/sync report`: comparison against scope plus recommended disposition such as `keep`, `revise`, `reject`, `sync-needed`, `follow-up-needed`, or `no-action`.

## Storage

- Put task packets in `docs/Tasks/`.
- Put implementation and review reports in `docs/Reports/`.
- Put reusable project knowledge in `docs/Durable Notes/`.
- Put early ideas in `docs/Idea Backlog/` until they are clarified.
