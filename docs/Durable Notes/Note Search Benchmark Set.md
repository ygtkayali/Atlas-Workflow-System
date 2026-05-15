# Note Search Benchmark Set

Status: [[Tags/status-settled]]
Type: [[feature-subject-note]]
Related: [[Hybrid Note Search and Entry Note Workflow]], [[note-search-skill]], [[Tag Retrieval Model]]
Created: 14-05-2026
Last Reviewed: 2026-05-15
Source: [[report-note-search-benchmark-expansion]]
Priority: [[docs/Tags/priority-high|priority-high]]

---

## Summary

A real-vault benchmark set for the `note-search` skill that compares keyword,
semantic, and hybrid retrieval across five query categories with per-mode rank
thresholds and expected-result rationale.

The benchmark lives in `tests/note_search_benchmark.py`.

## Benchmark Categories

1. **Note Manager connection discovery** — tests whether graph-adjacent and
   tag-linked notes surface for connection-oriented queries.
2. **Hybrid note search implementation artifacts** — tests retrieval of
   implementation notes from a known feature area.
3. **Tag/status-oriented retrieval** — tests whether tag and status notes
   behave as candidate filters rather than raw BM25 terms.
4. **Priority/task retrieval** — tests whether priority-tagged and
   task-linked notes rank appropriately for task-oriented queries.
5. **Rough concept discovery** — tests non-exact prompt retrieval where no
   precise term match exists.

Expected results include a rationale and per-mode rank thresholds.
`Tag Retrieval Model.md` is intentionally included or excluded with explicit
rationale in relevant expected sets.

## Design Decisions

- Rank thresholds start conservative and reflect current accepted behavior,
  not future scoring targets.
- Keyword mode is not expected to satisfy semantic or contextual queries;
  those are accepted as semantic/hybrid mode expectations.
- `Tag Retrieval Model.md` is an intentional expected result for tag and
  hybrid-search queries.
- `note-manager.md` is a semantic-mode expectation for the broad connection
  query but not a hybrid-mode pass/fail expectation until score tuning
  improves that case.
- Benchmark failures are retrieval feedback, not necessarily test failures,
  unless a strict threshold is intentionally defined.

## Known Scoring Gaps

- Hybrid ranking does not currently surface `note-manager.md` in the top 8
  for `note manager connections tags note search`.
- This is a scoring-quality follow-up, not a benchmark definition failure.
- Rank thresholds may need adjustment as future durable-note additions
  change the vault surface.

## Open Questions

- What benchmark evidence should tune tag score weights and determine which
  tag categories are reliable semantic retrieval signals? See
  [[Tag Retrieval Model]].
- Should seed-derived tags from entry notes become query expansion inputs?
- At what point should rank thresholds be tightened beyond conservative
  baseline values?
