# Note Search Benchmark Expansion

- Type: task-packet
- Status: approval_pending
- Task ID: note-search-benchmark-expansion
- Task Status: planned
- Related to: [[Note Search Test Set]], [[Hybrid Note Search and Entry Note Workflow]], [[Tag Retrieval Model]], [[note-search-skill]]
- Revision: v1
- Created: 2026-05-14

## Objective

Expand the note-search benchmark so hybrid, semantic, and keyword retrieval quality can be evaluated with a broader and more current real-vault test set.

This follows the hybrid search maintenance review finding that `Tag Retrieval Model.md` now ranks prominently and the current benchmark expected sets do not yet capture that durable note or clear rank expectations.

## Scope

In scope:

- Update `tests/note_search_benchmark.py` to include a broader set of real-vault query cases.
- Add expected useful notes for the new `Tag Retrieval Model.md` where it is a relevant result.
- Add expected-rank or maximum-rank thresholds where a note's position matters, instead of only checking presence in the top N.
- Keep separate reporting for `keyword`, `semantic`, and `hybrid` modes.
- Preserve benchmark output that explains ranks and top results for tuning feedback.
- Update `docs/Idea Backlog/Note Search Test Set.md` only if the benchmark intent or test categories need to be recorded.
- Optionally add or adjust unit tests in `tests/test_note_search.py` only for benchmark helper behavior, not search scoring behavior.

## Non-goals

- Do not tune scoring weights in this packet.
- Do not change retrieval semantics, tag filtering, BM25 scoring, graph scoring, or semantic ranking.
- Do not add LLM reranking.
- Do not add new dependencies.
- Do not require network access for keyword-mode benchmark execution.
- Do not close or archive the `hybrid-note-search-v2` lane.
- Do not change durable note status tags unless routed separately through Note Manager.

## Relevant Context

Read first:

- [tests/note_search_benchmark.py](/home/yigit-kayali/Atlas%20Workflow%20System/tests/note_search_benchmark.py)
- [docs/Idea Backlog/Note Search Test Set.md](/home/yigit-kayali/Atlas%20Workflow%20System/docs/Idea%20Backlog/Note%20Search%20Test%20Set.md)
- [docs/Durable Notes/Tag Retrieval Model.md](/home/yigit-kayali/Atlas%20Workflow%20System/docs/Durable%20Notes/Tag%20Retrieval%20Model.md)
- [docs/In-flight/report-hybrid-note-search-v2.md](/home/yigit-kayali/Atlas%20Workflow%20System/docs/In-flight/report-hybrid-note-search-v2.md)
- [shared/tools/local_note_semantic_search.py](/home/yigit-kayali/Atlas%20Workflow%20System/shared/tools/local_note_semantic_search.py) for CLI behavior only

Useful current maintenance evidence:

- Keyword benchmark currently misses `Durable Notes/Status Tag Registry.md` for `note manager connections tags note search` at limit 8.
- Semantic and hybrid benchmark modes currently pass for the small existing set.
- `Durable Notes/Tag Retrieval Model.md` now appears near the top for hybrid/tag search queries and should be treated intentionally.

## Allowed Implementation Area

Editable:

- `tests/note_search_benchmark.py`
- `tests/test_note_search.py` only for benchmark helper or output-shape tests
- `docs/Idea Backlog/Note Search Test Set.md`
- `docs/In-flight/packet-note-search-benchmark-expansion.md` if the packet needs a revision before approval

Read-only unless separately approved:

- `shared/tools/local_note_semantic_search.py`
- `shared/skills/note-search/SKILL.md`
- `docs/Durable Notes/Tag Retrieval Model.md`
- `docs/Durable Notes/note-search-skill.md`
- `docs/In-flight/report-hybrid-note-search-v2.md`
- `docs/In-flight/packet-hybrid-note-search-v2.md`

Discovery beyond the listed files should stay narrow and only support benchmark-case selection.

## Constraints

- Keep benchmark logic deterministic and local.
- Keep keyword-mode benchmark runnable with plain `python3`.
- Keep semantic and hybrid benchmark execution compatible with the existing `base-ml` conda path.
- Treat benchmark failures as ranking feedback, not necessarily unit-test failures, unless a strict threshold is intentionally defined.
- Make expected results explicit enough that future score tuning has a stable target.
- Preserve tag semantics from [[Tag Retrieval Model]]: tags are linked operational notes, candidate filters/facets before ranking, and separate from BM25 term matching.
- Do not let benchmark fixture updates silently redefine search behavior.

## Acceptance Criteria

- Benchmark includes at least five real-vault query cases covering:
  - Note Manager connection discovery
  - hybrid note search implementation artifacts
  - tag/status-oriented retrieval
  - priority/task retrieval
  - rough concept discovery from a non-exact prompt
- `Tag Retrieval Model.md` is intentionally included or explicitly excluded in relevant expected sets with a short rationale in code comments or result metadata.
- Benchmark can express maximum acceptable rank for specific expected notes where rank matters.
- Benchmark output still includes query, mode, hit count, expected count, ranks, and top results.
- Keyword, semantic, and hybrid modes can still be run independently with the existing `--modes` flag.
- Existing unit tests continue to pass.

## Verification Expectations

Run:

```bash
python3 -m py_compile shared/tools/local_note_search.py shared/tools/local_note_semantic_search.py tests/note_search_benchmark.py tests/test_note_search.py
python3 -m unittest discover -s tests -v
python3 tests/note_search_benchmark.py --modes keyword --limit 8
conda run --no-capture-output -n base-ml python tests/note_search_benchmark.py --modes semantic hybrid --limit 8
git diff --check -- tests/note_search_benchmark.py tests/test_note_search.py "docs/Idea Backlog/Note Search Test Set.md"
```

If the keyword benchmark intentionally remains nonzero because keyword cannot satisfy a semantic expectation, report the specific failed expectation and explain whether that is accepted benchmark feedback or a candidate search-quality follow-up.

## Risks / Open Questions

- Unclear: exact rank thresholds for each expected note. Start with conservative thresholds and explain any strict thresholds in the benchmark data.
- Risk: benchmark expected sets can become brittle as durable notes change. Prefer query categories and explicit rationale over opaque expected lists.
- Risk: adding `Tag Retrieval Model.md` to expected sets may mask other retrieval regressions if the benchmark only checks total hits. Preserve per-note rank reporting.
- Risk: semantic/hybrid checks require `base-ml`; if unavailable, keyword checks should still run and the limitation should be reported.

## Assumptions

- The current hybrid search behavior is accepted enough for benchmark expansion; this packet does not revisit scoring implementation.
- The maintenance review finding about `Tag Retrieval Model.md` is valid and should be reflected in benchmark expectations.
- The benchmark is allowed to be partly diagnostic rather than a pure pass/fail unit test.

## Confidence Assessment

Confidence: medium.

The objective, files, and non-goals are clear. Confidence is not high because rank thresholds need empirical judgment from actual query outputs and may require one implementation pass to calibrate without overfitting.

## Approval Status

Approval status: approval_pending.

Implementation must not begin until this packet revision is explicitly approved.
