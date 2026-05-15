# Note Search Benchmark Expansion

- Type: task-archive-summary
- Status: closed
- Task ID: note-search-benchmark-expansion
- Date: 2026-05-15

## Original Intent

Expand the real-vault note-search benchmark from three presence-only query
cases to five categorized query cases with per-mode rank thresholds and
expected-result rationale.

Driver: maintenance review finding that `Tag Retrieval Model.md` now ranks
prominently in hybrid/tag queries but was not captured in the benchmark
expected sets.

## Work Done

- Expanded `tests/note_search_benchmark.py` with five benchmark categories,
  structured expected notes with rationale, and per-mode rank thresholds.
- Treated `Tag Retrieval Model.md` as an intentional expected result for
  relevant tag and hybrid-search queries.
- Updated `docs/Idea Backlog/Note Search Test Set.md` to record benchmark
  categories and tag-model treatment (now archived as
  `docs/Archieved/Notes/Note Search Test Set.md`).
- Created `docs/Durable Notes/Note Search Benchmark Set.md` as the settled
  durable record of benchmark categories and design decisions.

## Important Decisions

- Rank thresholds start conservative and reflect current accepted behavior,
  not desired future improvements.
- Keyword mode is not expected to satisfy semantic or contextual queries.
- `Tag Retrieval Model.md` is an intentional expected result for tag and
  hybrid queries.
- `note-manager.md` is a semantic-mode expectation for the broad connection
  query but not a hybrid-mode pass/fail expectation until score tuning
  improves that case.
- Benchmark failures are retrieval feedback, not necessarily test failures,
  unless a strict threshold is intentionally defined.

## Final Files

- `tests/note_search_benchmark.py`
- `docs/Durable Notes/Note Search Benchmark Set.md`
- `docs/Archieved/Notes/Note Search Test Set.md`

## Verification

- `python3 -m py_compile` — passed
- `python3 -m unittest discover -s tests -v` — 6 tests passed
- `python3 tests/note_search_benchmark.py --modes keyword --limit 8` — passed
- `conda run --no-capture-output -n base-ml python tests/note_search_benchmark.py --modes semantic hybrid --limit 8` — passed
- `git diff --check` — passed

## Reusable Pattern

Benchmark categories with explicit rationale are more durable than opaque
expected lists — they let future score tuning know why a note should rank,
not just that it should appear.

## Remaining Risk Or Follow-up

- Hybrid ranking still does not surface `note-manager.md` in the top 8 for
  `note manager connections tags note search`; scoring-quality follow-up,
  not a benchmark definition failure.
- Rank thresholds may need adjustment as future durable-note additions
  change the vault surface.
- Packet was never recorded as formally approved; implementation proceeded
  from prior conversation context. No conformance impact; record-keeping gap
  only.
