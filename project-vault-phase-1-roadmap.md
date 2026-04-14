# Phase 1 Roadmap: Ideation-First Project Vault Workflow

Status: draft
Parent: [[Workflow Hub]]
Related: [[Idea Hub]], [[note-ready-handoff]]
Created:
Last Reviewed:
Source:
Decisions:
Dependencies:
Tasks:

---

## Summary

Build this repository as the `project-vault` subsystem of the broader personal knowledge system.

Phase 1 now focuses first on proving the ideation side of the system on real work before optimizing the full implementation pipeline.

The immediate workflow target is:
`idea -> clarify-intent -> note creation`

The implementation pipeline still matters, but in this phase it should remain a lighter, note-driven second stage:
`notes -> planning -> approval -> implementation -> review/sync`

This phase should optimize for:
- stronger idea clarification before durable notes are created
- selective note creation instead of broad capture
- practical use on real projects before retrieval and governance are optimized
- preserving human control over scope, note quality, and workflow direction

## Product Definition For This Phase

The Phase 1 system should be defined as:

A personal, note-centered project workflow that helps move from rough idea to clarified understanding, then into durable notes, and only later into implementation support.

For this phase, the system is responsible for:
- helping shape rough ideas before they become project notes
- exposing ambiguity, assumptions, and missing decisions early
- creating or updating a small set of meaningful durable notes from clarified ideas
- using those notes as source material for later planning and implementation work
- preserving explicit human approval before implementation begins

For this phase, the system is not responsible for:
- advanced retrieval or indexing behavior
- automated note maintenance behind the scenes
- complex metadata or link-enforcement systems
- broad canonical graph design across many note types
- full redesign of planning, implementation, and review artifacts in the same pass
- autonomous note creation from ordinary conversation

## Two-Part Workflow

### 1. Ideation

This is the primary Phase 1 focus.

The ideation workflow is:
`idea -> clarify-intent -> note creation`

The goal of ideation is to strengthen understanding enough that only confident, durable project knowledge gets promoted into notes.

Expected behavior:
- `clarify-intent` challenges weak assumptions, surfaces ambiguity, and helps the user reason through the idea
- ideation can continue for multiple rounds without forcing note creation
- note creation only happens when there is enough confident material to justify a durable note

### 2. Implementation

This remains part of the system, but only at a high level for now.

The implementation workflow is:
`notes -> planning -> approval -> implementation -> review/sync`

The key rule is:
planning should take project notes as input, not rely on the current planner-oriented clarification brief as the default handoff.

Detailed redesign of planner packets, implementer inputs, and review/sync outputs is deferred until the ideation loop has been proven on real use.

## Primary User Stories

- `New project idea`
  I start with a rough project idea. The system should help me articulate the goal, expose ambiguity, ask clarification questions, and challenge weak assumptions before any durable note is created.

- `Iterative idea refinement`
  I have an early direction, but it still feels weak. The system should help me improve it through repeated clarification rounds until the surviving ideas are strong enough to become notes.

- `Selective note creation`
  I do not want a note for everything I say. The system should create or update notes only for ideas that are clear enough, durable enough, and important enough to matter later.

- `Simple v1 note taking`
  I want the first version of note creation to stay simple. It should work with the existing templates and avoid complex retrieval, indexing, or automatic graph management.

- `Notes as implementation input`
  Once I understand the system well enough, I want later planning and implementation work to start from notes rather than from a clarification brief alone.

## V1 Note Model

Phase 1 v1 should use four working note roles:

- `Main Hub`
  Main hubs are lightweight index notes at the basic entry level of the vault.
  They should remain mostly empty, should not act as the main hierarchical center of the system, and should usually be referenced only by sub hubs rather than directly carrying broad note-link lists.

- `Sub Hub`
  Sub hubs hold broader context for a bounded area and act as the real organizing layer of the vault.
  A sub hub may contain or reference other sub hubs when the context justifies deeper grouping.

- `General Note`
  General notes are the main unit of knowledge and evolution in the vault.
  They should hold the substantive information, expose useful connections, and improve over time as understanding changes.
  A general note is allowed to evolve into a sub hub later when the surrounding context expands enough to require a broader organizing note.

- `Idea Note`
  Idea notes capture feature ideas, directions, or other not-yet-actualized subjects.
  They preserve potential work that has not yet been implemented or turned into stable project knowledge.

The main operational emphasis should be on `Sub Hub` and `General Note`.
`Main Hub` exists as a lightweight index role, not as the primary knowledge structure.

This v1 should prefer a minimal usable structure over a large note taxonomy.
If the system works in practice, note types and note architecture can be expanded later.

## Clarify-Intent Output For V1

`clarify-intent` should continue to act as an ideation and challenge loop, not as a planner.

Its successful output for this workflow should be a `note-ready handoff`, not a planning brief by default.

The note-ready handoff should capture:
- the surviving idea summary
- confident decisions worth preserving
- unresolved questions that still matter
- boundaries or non-goals made clear during clarification
- candidate note actions such as `create idea note`, `create general note`, `update existing note`, or `consider sub hub`

The handoff exists to help the note-creation skill decide whether durable note work is justified.
It is not approval for implementation and it is not a substitute for later planning artifacts.

## V1 Note-Creation Skill Behavior

The first version of note creation should stay intentionally narrow.

It should:
- work from the provided note context rather than broad vault discovery
- support `Main Hub`, `Sub Hub`, `General Note`, and `Idea Note` decisions
- create a new note when the clarified idea clearly deserves one
- propose updating an existing note when the clarified idea clearly belongs there
- ask the minimum questions needed to understand where the note belongs in the local note structure
- keep note bodies meaningful instead of producing placeholder capture
- treat `Main Hub` as a lightweight index role,
- treat `Sub Hub` as the broader context layer,
- treat `General Note` as the primary evolving knowledge unit,
- and treat `Idea Note` as not-yet-actualized work or direction

It should not:
- create notes from weak or ambiguous clarification state
- make silent decisions about unclear note placement
- treat main hubs as dense hierarchical content notes
- try to solve advanced retrieval, ranking, indexing, or backlink management
- enforce a large metadata or linking system in v1
- create notes for everything discussed in ideation

If the idea is still too weak or the target note is ambiguous, the skill should refuse to create or update notes and send the work back to `clarify-intent`.

## Note Creation And Update Timing

The intended v1 timing is:

1. Start with ideation.
2. Stay in clarification until durable signal exists.
3. Produce a note-ready handoff.
4. Let note creation decide whether to create a new note or update an existing one.
5. Return to clarification if confidence or note placement is still weak.

This keeps durable notes selective and avoids polluting the vault with low-confidence summaries.

## Implementation Phase Direction

After the ideation loop is working, the second part of the system should support implementation from notes.

That later phase should follow these rules:
- planning reads notes as the source material for implementation preparation
- planning produces bounded execution artifacts only when implementation is actually needed
- implementation still requires explicit human approval before coding begins
- review/sync should reflect implementation results back into the notes when project understanding changes

Phase 1 does not need the detailed planner, implementer, and review redesign yet.
It only needs the workflow direction to be explicit so later work does not keep assuming a planner-brief-first model.

## Explicitly Deferred Work

Do not optimize these yet:
- retrieval and context-generation skills
- complex metadata schemas
- strict link and backlink governance
- automated stale-note detection
- review queues for note maintenance
- canonical graph architecture across many specialized note classes
- deep note-maintenance hooks and background behaviors
- detailed implementation-packet and implementation-report redesign tied to the new note model

These are useful later, but they should follow proof that the simpler ideation and note-creation loop works on real projects.

## Acceptance Criteria For This Plan

The Phase 1 design is complete when:
- the repo clearly defines Phase 1 as ideation-first
- the first active workflow is `idea -> clarify-intent -> note creation`
- the note-creation v1 scope reflects the vault's working note roles
- main hubs are treated as lightweight entry indexes rather than the primary hierarchy
- sub hubs are treated as the primary context layer
- general notes are treated as the primary evolving knowledge unit
- idea notes are treated as not-yet-actualized work
- `clarify-intent` is defined as producing a note-ready handoff rather than a planning brief by default
- ambiguous or weak note creation routes back to clarification
- the later implementation phase is clearly note-driven at a high level
- advanced retrieval, indexing, metadata, and governance work are explicitly deferred

## Test Cases And Validation Scenarios

Validate the design against these scenarios:
- a rough idea stays in clarification for multiple rounds before any note is created
- a clarified idea becomes an `Idea Note` using the existing template
- a clarified concept with durable project value becomes a `General Note`
- a broad topic with multiple related notes becomes a `Sub Hub`
- a lightweight top-level index stays a `Main Hub` rather than absorbing operational detail
- a broader project area becomes a `Sub Hub` when an organizing note is clearly justified
- a clarified request updates an existing note instead of creating an obvious duplicate
- an expanding `General Note` is converted into a `Sub Hub` when the surrounding context now requires it
- an ambiguous `create a note` request is refused and sent back to clarification
- later planning is described as consuming notes rather than the planning brief as default input

## Assumptions And Defaults

- Updated direction overrides older roadmap language where they conflict.
- This repository should prove the ideation and note-creation loop before optimizing the rest of the system.
- The current templates are sufficient for v1 note creation, with `Main Hub` using the hub-style structure as a lightweight index role.
- Selective note creation is more important than broad note coverage in v1.
- Human approval remains required before implementation begins.
- Later planning, implementation, and review still belong in the system, but only as a note-driven second stage for now.
