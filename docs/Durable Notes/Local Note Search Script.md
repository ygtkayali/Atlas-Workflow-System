# Local Note Search Script

Status: [[Tags/status-settled]]
Parent:
Related: [[note-search-skill]]
Created: 14-04-2026
Last Reviewed: 2026-05-07

## Summary

Create a reusable local script that agents can call with a known seed note to retrieve candidate related note paths without reading the entire vault.

The Atlas source repository includes the graph script source at `shared/tools/local_note_search.py`.
The semantic and hybrid-search companion lives at `~/.codex/tools/local_note_semantic_search.py` when installed and is routed through [[note-search-skill]] rather than replacing this graph script.

## Current V1 Intent

The first version should stay narrow, deterministic, and easy to debug.

V1 should:
- accept a known seed note
- return candidate note paths
- use note-graph relationships as the retrieval basis
- avoid free-text interpretation
- avoid automatic note changes

## Retrieval Approach

Primary retrieval should come from the local note graph.

For this note, `backlinks` means other notes that link to the seed note.

Initial retrieval behavior:
- use direct backlinks for the seed note
- use direct links from the seed note when available
- use 1-hop retrieval by default
- allow bounded 2-hop fallback only when 1-hop results are too sparse
- compute backlinks from parsed links in the vault rather than relying on Obsidian UI state

## V1 Boundaries

Initial use case:
- call the script for a new note to find nearby candidate notes that may be relevant for linking

Secondary use case:
- rerun the script after substantial note changes when metadata or surrounding relationships may need review

- local script
- reusable by agents
- deterministic behavior
- returns candidate note paths only
- no free-text input
- no tag-based expansion in the initial version
- no tag-based filtering in the initial version
- does not decide which links should actually be added
- does not modify notes automatically

## Usage

```bash
python3 shared/tools/local_note_search.py \
  --vault-root . \
  --seed-path "Full notes/note-manager.md" \
  --format json
```

## Why Tags Are Deferred

Tags may become useful later, especially in a larger knowledge base with mature content-related tags.

They are excluded from the initial version because:
- current tags may reflect workflow state rather than subject relevance
- status-like tags can produce noisy candidates
- technical project documentation may rely more on explicit links than tags
- tag usage needs separate design once the vault has clearer semantic tagging patterns

## Initial Evaluation Approach

Quality should be checked with a small manual benchmark rather than broad assumptions.

Initial evaluation:
- choose a small set of seed notes
- define the expected relevant neighboring notes for each
- inspect top results for missed context and noise
- compare 1-hop only against 1-hop plus 2-hop fallback behavior

## Deferred Work

- semantic/content tag support
- tag-role separation such as operational tags vs semantic tags
- strict mode in addition to expanded mode
- richer ranking or explanation layers

The script should support the documentation-centered workflow by reducing unnecessary vault-wide reading while still giving agents enough nearby context to make linking decisions.
Semantic, BM25-style keyword, tag-aware, and hybrid query discovery is handled by the separate semantic/hybrid script through [[note-search-skill]].
Keep this graph script focused on known-seed graph neighborhoods.

## Open Questions

- Should the canonical input be note path only, or should title lookup normalize to path first?
- What exact threshold should trigger 2-hop fallback?
- What candidate cap should stop expansion before result bloat?
- Should backlinks and direct outgoing links be weighted equally?
