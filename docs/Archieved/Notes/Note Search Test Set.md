# Note Search Test Set

Status: [[Tags/status-archived]]
Type: [[feature-subject-note]]
Related: [[note-search-skill]], [[Hybrid Note Search and Entry Note Workflow]], [[Tag Retrieval Model]]
Successor: [[Note Search Benchmark Set]]
Created: 14-05-2026
Last Reviewed: 2026-05-15
Priority: [[docs/Tags/priority-high|priority-high]] 
Source: [[report-note-search-benchmark-expansion]]
Tasks: [[packet-note-search-benchmark-expansion]]
Reports: [[report-note-search-benchmark-expansion]]

---

## Summary

Maintain a small real-vault benchmark set for the `note-search` skill.

The test set should compare keyword, semantic, and hybrid search results across a few real vault queries. It should record expected useful notes, noisy results, and ranking issues so hybrid scoring can be tuned with evidence instead of guesswork.

The first benchmark implementation lives in `tests/note_search_benchmark.py`.

## Current Test Categories

The first benchmark should cover:

- Note Manager connection discovery
- hybrid note search implementation artifacts
- tag/status-oriented retrieval
- priority/task retrieval
- rough concept discovery from a non-exact prompt

Expected results should include a short rationale and rank thresholds where position matters.
[[Tag Retrieval Model]] should be treated intentionally in tag and hybrid-search benchmark cases because it is now a relevant durable result, not incidental noise.

## Current Follow-up Signal

Hybrid ranking does not currently surface `note-manager.md` in the top 8 for `note manager connections tags note search`.
Treat that as a scoring-quality follow-up, not a benchmark definition failure.
