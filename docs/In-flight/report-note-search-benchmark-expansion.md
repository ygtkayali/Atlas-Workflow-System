# Note Search Benchmark Expansion Implementation Report

- Type: implementation-report
- Status: completed
- Task ID: note-search-benchmark-expansion
- Task Status: settled
- Related artifact: [[packet-note-search-benchmark-expansion]]
- Packet revision: v1
- Date: 2026-05-14

## Summary of Change

Expanded the real-vault note-search benchmark from three presence-only query cases to five categorized query cases with per-mode rank thresholds and expected-result rationale.

The benchmark now treats `Durable Notes/Tag Retrieval Model.md` as an intentional expected result for relevant tag and hybrid-search queries.

## Files Touched

- `tests/note_search_benchmark.py`
  - Added structured expected notes with rationale and per-mode maximum ranks.
  - Added benchmark categories for connection discovery, implementation artifacts, tag/status retrieval, priority/task retrieval, and rough concept discovery.
  - Extended output with thresholds, per-note pass state, rationale, and category.
- `docs/Idea Backlog/Note Search Test Set.md`
  - Recorded the benchmark categories and the expectation that `Tag Retrieval Model` should be handled intentionally.
- `docs/In-flight/report-note-search-benchmark-expansion.md`
  - Added this implementation report for the approved packet.

## Why These Changes Were Made

The approved packet requested a broader benchmark that can evaluate keyword, semantic, and hybrid retrieval quality with stable expected notes and rank thresholds.

The prior benchmark only checked whether expected notes appeared within the top limit. That made it harder to distinguish acceptable ranking shifts from real retrieval regressions, especially after `Tag Retrieval Model.md` became a relevant search result.

## Outcome Against Acceptance Criteria

- Met: benchmark includes five real-vault query cases covering all requested categories.
- Met: `Tag Retrieval Model.md` is intentionally included in relevant expected sets with rationale.
- Met: benchmark can express maximum acceptable ranks per mode and expected note.
- Met: output still includes query, mode, hit count, expected count, ranks, and top results.
- Met: keyword, semantic, and hybrid modes can still be run independently with `--modes`.
- Met: existing unit tests continue to pass.

## Checks Run

- Passed: `python3 -m py_compile shared/tools/local_note_search.py shared/tools/local_note_semantic_search.py tests/note_search_benchmark.py tests/test_note_search.py`
- Passed: `python3 -m unittest discover -s tests -v`
  - Ran 6 tests.
- Passed: `python3 tests/note_search_benchmark.py --modes keyword --limit 8`
- Passed: `conda run --no-capture-output -n base-ml python tests/note_search_benchmark.py --modes semantic hybrid --limit 8`
- Passed: `git diff --check -- tests/note_search_benchmark.py tests/test_note_search.py "docs/Idea Backlog/Note Search Test Set.md"`

During verification, initial benchmark thresholds exposed two aspirational expectations rather than stable current behavior:

- keyword mode does not reliably surface broad conceptual connection targets such as `note-manager.md`
- hybrid mode does not currently surface `note-manager.md` in the top 8 for `note manager connections tags note search`

The benchmark was calibrated to current accepted behavior and leaves those as search-quality follow-up signals rather than pass/fail expectations.

## Assumptions Introduced

- Decided: keyword mode should not be expected to retrieve `Status Tag Registry.md` for the broad `note manager connections tags note search` query because the maintenance review already identified that as semantic/contextual rather than exact-term behavior.
- Decided: rank thresholds should start conservative and reflect current accepted behavior, not desired future scoring improvements.
- Decided: `note-manager.md` should be a semantic-mode expectation for the broad connection query, but not a hybrid-mode pass/fail expectation until score tuning improves that query.

## Unresolved Issues

- Score tuning remains out of scope.
- Rank thresholds may need adjustment after future durable-note additions change the vault surface.
- Hybrid ranking still does not surface `note-manager.md` in the top 8 for `note manager connections tags note search`; this remains a candidate scoring-quality follow-up.

## Review / Sync Follow-up

- Review should evaluate whether the benchmark category list should become durable guidance beyond the current idea note.
