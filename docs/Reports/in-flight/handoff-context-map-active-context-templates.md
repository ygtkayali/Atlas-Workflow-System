# Context Map And Active Context Template Handoff

- Type: clarified-context-handoff
- Status: ready_for_note_manager
- Related to: dev-workflow template simplification
- Created: 2026-05-11

## Clarified Subject / Subjects

### Subject 1: context-map.md Template

A stable project-structure context file that helps agents assemble the smallest useful starting context for a project.

It should explain where important files live, which files are authoritative for which purposes, what metadata exists, and which files should be read first for common task types.

It should not track current workflow state, project decisions, or priorities.

### Subject 2: active-context.md Template

A lightweight current-state file that explains the active workflow state for the current project or conversation thread.

It should identify the current phase, current gate, active subject, authoritative artifacts, next expected action, and stale or blocked state.

It should not become a backlog, decision log, project hub, or general memory dump.

## Interpretation Basis

Origin type: user prompt and live workflow design discussion.

Original user intent:

- User does not think priority-queue.md or decision-log.md are needed as required core artifacts.
- User sees decision rationale as better captured in idea notes or the Interpretation Basis section of clarified handoffs.
- User sees priority as better represented through metadata or tags such as high/mid/low.
- User considers active-context.md the important runtime state file.
- User wants a project hub or something similar that explains project structure and metadata so initial context creation is easier.
- User then requested the first concrete step: create template shapes for context-map.md and active-context.md.

Relevant context used:

- Current AGENTS.md still lists project-hub.md, architecture-hub.md, priority-queue.md, decision-log.md, and active-context.md as core artifacts.
- Current active-context.md role is over-specified as "single source of truth" for workflow state.
- Current decision-log.md and priority-queue.md roles are under-specified and likely stale-prone.
- Existing docs folder has docs/Templates/, making reusable templates a plausible target area, but target placement is for Note Manager to decide.

Intent to preserve:

- Simplify required workflow files.
- Reduce AI-maintained stale state.
- Keep only state surfaces that provide clear operational value.
- Separate stable project context from changing active workflow state.

User intent versus agent inference:

- User intent: create shapes/templates for context-map.md and active-context.md.
- User intent: do this through clarify-intent first.
- Agent inference: context-map.md should replace much of the practical value previously expected from project-hub.md.
- Agent inference: active-context.md should be narrowed rather than removed.
- Agent inference: priority-queue.md and decision-log.md should be removed from required core artifacts later, but not in this handoff step.

Validation target:

- Downstream Note Manager should preserve the distinction between stable context map and volatile active context.
- It should not reintroduce decision-log or priority-queue responsibilities into either template.
- It should draft templates, not apply broader AGENTS.md cleanup yet.

## User Goal

Create reusable template shapes for each project so agents can start with better context while avoiding stale workflow files.

The immediate goal is not to update all workflow docs yet. It is to define the two replacement template shapes clearly enough that they can later be synced into dev-workflow assets and referenced by AGENTS.md.

## Decided

- context-map.md and active-context.md are distinct files with distinct purposes.
- context-map.md is stable project structure/context guidance.
- active-context.md is current workflow state and gate guidance.
- decision-log.md should not be required for this simplified model.
- priority-queue.md should not be required for this simplified model.
- Prioritization can be represented through metadata or tags.
- Decision rationale can live in idea notes, accepted artifacts, or Interpretation Basis sections rather than a global log.
- The next durable work should draft template shapes for the two files only.

## Unclear / Blocked

- Whether context-map.md should also be created in modes/dev-workflow/ as a starter file for new projects is not yet decided.
- Whether active-context.md should be manually maintained, generated, or semi-generated is not fully decided.

## Boundaries / Non-goals

- Do not clean AGENTS.md in this step.
- Do not update skills in this step.
- Do not remove decision-log.md or priority-queue.md references in this step.
- Do not create a full event lifecycle or state automation system yet.
- Do not make context-map.md a project narrative, backlog, or decision register.
- Do not make active-context.md a comprehensive project memory.
