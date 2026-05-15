# Hybrid Note Search and Entry Note Workflow

Status: [[Tags/status-settled]]
Type: [[feature-subject-note]]
Related: [[note-search-skill]], [[Local Note Search Script]], [[Main Vault Note Structure and Agent Context]], [[context-map]], [[Tag Retrieval Model]] [[hybrid-note-search-v2]] [[Note Search Benchmark Set]]
Created: 14-05-2026
Last Reviewed: 2026-05-15
Priority: [[docs/Tags/priority-high|priority-high]] 

---

## Summary

Improve the current `note-search` system before creating a separate discovery tool.

The direction is a two-step search workflow:

1. Read the known entry notes first.
2. Use `note-search` from that bounded context to find related notes, connections, and supporting context.

This keeps the workflow grounded in explicit entry notes while still allowing search to improve context quality and reduce broad vault reading.

## Current Direction

The current priority is to strengthen the existing `note-search` interface and tools.

The first improvement should be a hybrid search system that can combine:

- graph search from known notes
- semantic search from concepts or rough queries
- keyword or BM25-style retrieval
- tag-aware signals when tags are useful for retrieval
- reranking or score fusion that explains why a note was returned

The goal is not to make `note-search` an autonomous vault manager.
The goal is to make it a better bounded retrieval layer for workflow roles that already need context.

## Two-Step Workflow

Entry notes should remain the first context layer when they exist.

Useful entry notes may include:

- `context-map.md` for project structure, important files, and stable entry paths
- feature or project subject notes
- hub notes
- supplied task notes or implementation artifacts
- local workflow notes that define current constraints

After reading the relevant entry notes, the agent can call `note-search` with a better seed:

- a seed note path when graph context is needed
- a concept query when similar notes are needed
- terms extracted from the entry note when keyword search would help
- tags from the entry note when tags are meaningful retrieval signals

This should reduce repetitive broad reading while preserving human-authored entry points as the first source of context.

Tag retrieval mechanics are now partly settled in [[Tag Retrieval Model]].
Tags should be treated as linked operational notes that constrain or facet candidate sets before ranking, not as plain BM25 terms.

## Context Map Role

`context-map.md` may become more useful as a search entry field over time.

As it evolves to include important files, docs, folders, entry notes, and task-specific routing hints, it can help agents choose better initial seeds for `note-search`.

This makes the workflow:

```text
prompt -> entry note/context-map -> note-search -> bounded context capsule -> role-specific work
```

The context map should not need to become a search engine itself.
It should provide stable project orientation and good starting points.

## Note Manager Connection Support

The upgraded search layer may improve `Note Manager` quality by finding likely related notes and connection candidates without requiring broad manual vault reads.

The safer boundary is:

- upstream workflow roles or the runtime routing layer use `note-search`
- `Note Manager` consumes supplied search context capsules
- `Note Manager` still decides the note action, target note, links, and final draft from bounded input

This preserves the current note mutation boundary while allowing search quality to improve linking and context selection.

## Discovery Tool Boundary

A separate discovery tool may still be useful later.

For now, the initial discovery idea is lower priority because entry notes already exist and can serve as the first context layer.

The next step should improve the current `note-search` system first. A separate discovery tool should be considered only if the hybrid search layer cannot cleanly support broader vault exploration needs.

## Open Questions

- What benchmark queries should be used to compare graph-only, semantic-only, BM25-only, and hybrid results?
- Which tag categories are reliable semantic retrieval signals, and what benchmark evidence should tune their weights? The basic retrieval model is decided in [[Tag Retrieval Model]], but reliability and weighting remain open.
- Should reranking start as deterministic score fusion before any LLM-based reranking is considered?
- What should a bounded context capsule include so downstream roles can trust the result without reading too much?
