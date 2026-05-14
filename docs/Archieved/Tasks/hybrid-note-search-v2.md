# Hybrid Note Search V2

- Type: task-archive-summary
- Status: closed
- Task ID: hybrid-note-search-v2
- Date: 2026-05-14

## Original Intent

Improve the existing `note-search` system without introducing a separate discovery tool.

The lane focused on adding hybrid retrieval behavior that combines semantic, BM25-style keyword, graph, and tag-aware signals while preserving the existing local and socket-based search workflow.

## Work Done

- Added `--search-mode hybrid`, `semantic`, and `keyword` behavior to `shared/tools/local_note_semantic_search.py`.
- Added separate `semantic_score`, `keyword_score`, `graph_score`, `tag_score`, final `score`, and `why` output fields.
- Added tag extraction, conservative tag scoring, and tag-based candidate filtering.
- Preserved graph search as a separate known-seed tool and clarified the graph-vs-semantic/hybrid boundary in durable notes.
- Updated the shared `note-search` skill and the repo durable note-search contract for hybrid and keyword retrieval.
- Added a first benchmark/testing layer for note-search behavior.
- Added the durable `Tag Retrieval Model` note and updated related note-search documents during review/sync.

## Important Decisions

- Hybrid search is the default concept-discovery path; semantic-only remains available explicitly.
- Tags are linked operational notes, not plain keyword tokens.
- Tags should primarily constrain or facet candidate sets before ranking.
- Tag evidence remains visible in scoring output, but tag matches should not behave like BM25 terms.
- Status and type tags remain conservative retrieval signals rather than broad relevance boosts.

## Final Files

- `shared/tools/local_note_semantic_search.py`
- `shared/skills/note-search/SKILL.md`
- `docs/Durable Notes/note-search-skill.md`
- `docs/Durable Notes/Local Note Search Script.md`
- `docs/Durable Notes/Tag Retrieval Model.md`
- `docs/Idea Backlog/Hybrid Note Search and Entry Note Workflow.md`
- `tests/test_note_search.py`
- `tests/note_search_benchmark.py`
- `modes/dev-workflow/agents-bridge.md`
- `AGENTS.md`
- `CLAUDE.md`

## Verification

- `python3 -m py_compile shared/tools/local_note_search.py shared/tools/local_note_semantic_search.py`
- `python3 -m unittest discover -s tests -v`
- `python3 shared/tools/local_note_search.py --vault-root docs --seed-path "Durable Notes/note-search-skill.md" --format json --debug`
- `python3 shared/tools/local_note_semantic_search.py --vault-root docs --query "hybrid note search BM25 tags" --search-mode keyword --expand-graph --format json`
- `conda run --no-capture-output -n base-ml python shared/tools/local_note_semantic_search.py --vault-root docs --query "hybrid note search BM25 tags" --search-mode hybrid --expand-graph --no-socket --format json`
- `python3 tests/note_search_benchmark.py --modes keyword --limit 8`
- `conda run --no-capture-output -n base-ml python tests/note_search_benchmark.py --modes semantic hybrid --limit 8`
- `git diff --check`

## Reusable Pattern

For bounded note discovery, keep human-authored entry notes as the first context layer and use hybrid note-search as the retrieval layer behind them.

Separate graph-neighborhood retrieval from concept discovery, and expose score components so later tuning can be evidence-driven instead of opaque.

## Remaining Risk Or Follow-up

- Hybrid ranking still does not surface `note-manager.md` strongly enough for the broad `note manager connections tags note search` query.
- Score weights are still first-pass defaults and not benchmark-tuned.
- Seed-derived tag expansion remains deferred.
- In-flight packet/report artifacts for this lane still need a separate cleanup decision if you want them moved or deleted.
