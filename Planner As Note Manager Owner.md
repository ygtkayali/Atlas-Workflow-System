# Planner Produces Planning Context, Not Durable Notes

Status: [[status-settled]]
Parent: [[Idea Hub]]
Related: [[Note Manager]], [[planner-agent]], [[clarify-intent]], [[clarified-context-handoff]], [[Two-Phase Workflow Boundary]]
Created: 15-04-2026
Last Reviewed: 2026-04-24
Source:
Decisions:
Dependencies:
Tasks:

---

## Summary

The planner should not become a direct `Note Manager` owner.

The settled direction is that planner may evolve in its planning role by improving context gathering, reasoning, scope analysis, contradiction detection, and task packet preparation.
It may identify documentation gaps and propose that note work is needed, but it should not directly create or update durable notes.

Durable note creation and updates should continue through:

`clarify-intent -> clarified context handoff -> Note Manager`

This keeps planner focused on planning reasoning while keeping durable note mutation centralized.

## Current Decision

The earlier idea of `Planner As Note Manager Owner` is superseded.

Planner should not send explicit note actions directly to `Note Manager`.
Instead, when planning exposes a documentation gap that must become durable note state, planner should route the relevant planning context through `clarify-intent`.

`clarify-intent` separates durable subjects and preserves the relevant decisions, evidence, uncertainty, and boundaries.
`Note Manager` then decides whether to create, update, defer, or return the work to clarification.

## Task Packets And Reports

Task packets and implementation reports are workflow artifacts, not durable notes.

Planner may produce task packet artifacts directly.
Implementer may produce implementation report artifacts directly.

These artifacts can later become evidence for durable note synchronization, but their creation does not itself require `Note Manager`.
If a task packet or implementation report implies a durable note update, that update must still route through `clarify-intent -> Note Manager`.

## Planner Responsibilities

Planner may:
- gather bounded planning context
- compare relevant notes
- detect stale, missing, or contradictory documentation
- reason about scope, constraints, risks, and implementation readiness
- prepare task packets
- identify planning-stage documentation gaps
- recommend that durable note work is needed before implementation

Planner must not:
- create or update durable notes directly
- choose final durable note targets
- draft final durable note content
- use task packet preparation as a shortcut around `Note Manager`
- treat speculative planning conclusions as durable project truth

## When Planner Should Route To Clarification

Planner should route planning-stage documentation gaps to `clarify-intent` when:
- durable note-backed planning context is missing, stale, or contradictory
- the gap blocks safe task packet creation
- the human has approved a pre-implementation structural or documentation decision
- a planning discovery needs to become durable project knowledge
- the planner can state the documentation-sync subject without deciding note structure

Planner should not route ordinary small tasks or speculative planning ideas into durable note mutation by default.

## Reasoning

This model preserves the useful part of the old idea without giving planner note-mutation authority.

Planner can become better at planning through stronger context handling and reasoning.
`clarify-intent` remains responsible for durable subject clarification.
`Note Manager` remains responsible for note action mapping, metadata, links, structure, drafting, and approval gates.

This avoids both failure modes:
- planner becoming too weak to handle real planning complexity
- planner quietly turning into a durable note editor
