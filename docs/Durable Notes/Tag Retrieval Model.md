# Tag Retrieval Model

Status: [[Tags/status-active]]
Type: [[design-note]]
Parent:
Related: [[note-search-skill]], [[Local Note Search Script]], [[Status Tag Registry]], [[Hybrid Note Search and Entry Note Workflow]]
Created: 14-05-2026
Last Reviewed: 2026-05-14
Source: hybrid-note-search-v2 implementation report and review-sync tag-model decision
Project Subjects: [[Hybrid Note Search and Entry Note Workflow]], [[Note Search Test Set]]
Tasks: [[packet-hybrid-note-search-v2]]
Reports: [[report-hybrid-note-search-v2]]

---

## Design Scope

This note defines how note-based tags should behave in note retrieval.

## Context

Hybrid note search now combines semantic, BM25-style keyword, graph, and tag-aware signals. Tags need explicit retrieval semantics because this vault treats tags as linked notes with workflow meaning, not as plain text labels.

## Chosen Design

Tags are note links with operational meaning, not plain tokens.

Tag notes should be resolved through the same graph/link-aware note model used for vault links.

Tags should primarily constrain, filter, or facet candidate sets before ranking.

Ranking may still expose tag evidence through `tag_score`, `tag_filter`, and `why` reasons, but tag matches should not behave like BM25 terms.

Status and type tags should remain conservative retrieval signals. They may narrow candidate sets or explain why a note matched, but they should not dominate broad relevance scoring.

## Rationale

This keeps tag behavior aligned with the vault model: tags are notes, links, and operational metadata. It also prevents common workflow tags such as status or type from overpowering content relevance in hybrid search.

## Constraints

- Do not redesign the vault tag system as part of retrieval.
- Do not make tags automatic note-action decisions.
- Do not collapse graph links and tags into one undifferentiated score.
- Do not treat status and type tags like semantic subject tags.

## Technical Shape

Current hybrid note search extracts tags from metadata and wikilinks that resolve under `Tags/`.

The retrieval flow uses tags in three places:

- candidate filtering through `tag_filter`
- conservative tag scoring through `tag_score`
- explanation through `why` reasons such as `tag_match:<tag>`

BM25-style keyword scoring remains separate from tag matching.

## Open Questions

- Which tag categories should become reliable semantic retrieval signals later?
- Should seed-derived tags from entry notes become query expansion inputs?
- What benchmark thresholds should tune tag score weights?
