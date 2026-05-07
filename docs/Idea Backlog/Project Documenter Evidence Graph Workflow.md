# Project Documenter Evidence Graph Workflow

Status: [[Tags/status-draft]]
Parent: [[Main Hubs/Idea Hub]]
Related: [[note-search-skill]], [[Local Note Search Script]], [[note-manager]], [[LLM Wiki Lossy Compression and Integrity Risks]], [[Main Hubs/Workflow Hub]]
Created: 07-05-2026
Last Reviewed: 2026-05-07

---

## Idea

Create a documentation workflow for already existing projects that can scale to large repos and multi-source systems without turning human review into hundreds of isolated note approvals.

The core approach is to separate evidence extraction from durable note creation:

1. A deterministic graph tool builds a shallow whole-project evidence graph.
2. A workflow skill interprets that graph into a documentation map and batch review.
3. The human approves documentation batches, not every extracted fact.
4. Note-ready handoffs are generated only for the selected batch.
5. Durable notes still route through [[note-manager]].

## Proposed Tool And Skill Split

The deterministic tool should own evidence extraction and graph construction.

Possible tool:

```text
~/.codex/tools/project_doc_graph.py
```

Tool responsibilities:
- scan local project sources
- respect ignore rules
- extract files, docs, configs, imports, schemas, APIs, entrypoints
- produce `source-inventory.json`
- produce `evidence-graph.json`
- attach file paths, line refs, source snapshot, and confidence labels
- produce cluster and graph metrics

The workflow skill should own documentation routing and human-facing decisions.

Possible skill:

```text
~/.codex/skills/project-documenter/SKILL.md
```

Skill responsibilities:
- decide when to run the graph tool
- interpret the evidence graph into `documentation-map.md`
- recommend breadth-first or depth-first documentation batches
- prepare `batch-review.md`
- generate note-ready handoffs only for approved batches
- route durable note changes through [[note-manager]]

## Documentation Creation Logic

Use two passes:

```text
one shallow whole-project evidence pass
many small documentation passes
```

The whole-project evidence pass should answer:
- what exists
- where it is
- what connects to what
- which areas look central
- what documentation already exists
- where gaps, conflicts, stale areas, or risky inferred claims may exist

It should not decide:
- final architecture intent
- complete behavior explanations
- whether inferred behavior is intentional
- final durable note structure
- which documentation claims are settled

## Batch Review Logic

The split should happen at the documentation map or batch review layer, not inside the raw evidence graph.

Default strategy:
- start breadth-first until there is a stable top-level system map
- switch depth-first when a cluster is high-value, high-risk, central, stale, conflicting, or immediately relevant to planned work
- create boundary and map notes before detailed behavior notes
- avoid deep settled claims before enough evidence exists

Batch review should let the human choose:
- approve batch
- revise batch
- switch breadth/depth
- inspect cluster
- defer ambiguous area
- request clarification
- route selected handoffs to [[note-manager]]

## Graphify Reference

Graphify is a useful reference for the extraction and graph-building side of this idea, especially:
- staged extraction pipelines
- graph nodes and edges with source evidence
- confidence labels such as extracted, inferred, or ambiguous
- ignore rules
- secure input handling
- graph/report outputs

This idea should not imply adopting Graphify wholesale. The useful pattern is the deterministic evidence layer, not replacing this vault's approval-gated note workflow.

## Traceability Requirements

Each generated note handoff should preserve:

```text
source snapshot
source class: code, existing-doc, config, external-spec, or user-supplied
exact evidence paths and line refs where possible
claim type: observed, inferred, ambiguous, or contradicted
confidence: high, mixed, or low
stale risk
human decision needed
```

The graph should support documentation claims without pretending that extracted links equal architectural intent.

## Security Requirements

Default v1 should be local-only.

Security boundaries:
- do not execute project code
- respect `.gitignore` and a project-documenter ignore file
- exclude secret-looking files and environment files by default
- sanitize graph and report labels
- cap file and source sizes
- require explicit opt-in for URLs, PDFs, videos, tickets, or remote docs
- treat inferred relationships as provisional
- never let the tool or skill write durable notes directly

## Open Questions

- What should the final skill name be?
- Where should generated graph artifacts live?
- Should this be installed globally first or prototyped inside this workflow vault?
- What should the v1 graph schema contain?
- Should Graphify be used only as design inspiration, wrapped, or forked?
- Should v1 support only code, docs, and config, or include external sources from the beginning?
- What is the smallest useful batch-review format?

## V1 Constraint

Start narrow:

```text
local repo only
code/docs/config only
shallow whole-project graph
documentation-map and batch-review outputs
selected-batch handoffs only
no durable note writes
```
