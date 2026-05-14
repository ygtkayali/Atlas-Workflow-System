from __future__ import annotations

import argparse
import json
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SEARCH_TOOL = REPO_ROOT / "shared" / "tools" / "local_note_semantic_search.py"
VAULT_ROOT = REPO_ROOT / "docs"


@dataclass(frozen=True)
class ExpectedNote:
    path: str
    rationale: str
    max_rank_by_mode: dict[str, int | None] = field(default_factory=dict)

    def max_rank_for(self, mode: str) -> int | None:
        return self.max_rank_by_mode.get(mode)


def expect(
    path: str,
    rationale: str,
    *,
    keyword: int | None = None,
    semantic: int | None = None,
    hybrid: int | None = None,
) -> ExpectedNote:
    return ExpectedNote(
        path=path,
        rationale=rationale,
        max_rank_by_mode={
            "keyword": keyword,
            "semantic": semantic,
            "hybrid": hybrid,
        },
    )


@dataclass(frozen=True)
class QueryCase:
    category: str
    query: str
    expected: tuple[ExpectedNote, ...]


QUERY_CASES = (
    QueryCase(
        category="note_manager_connection_discovery",
        query="note manager connections tags note search",
        expected=(
            expect(
                "Idea Backlog/Hybrid Note Search and Entry Note Workflow.md",
                "Primary idea note for hybrid note-search connection behavior.",
                keyword=3,
                semantic=3,
                hybrid=3,
            ),
            expect(
                "Durable Notes/Tag Retrieval Model.md",
                "New design note that should be intentionally visible for tag/search queries.",
                keyword=8,
                semantic=4,
                hybrid=8,
            ),
            expect(
                "Durable Notes/note-search-skill.md",
                "Stable caller interface for note retrieval.",
                keyword=6,
                semantic=6,
                hybrid=8,
            ),
            expect(
                "Durable Notes/note-manager.md",
                "Connection target for Note Manager search-context usage; semantic mode currently carries this conceptual relationship.",
                semantic=8,
            ),
            expect(
                "Durable Notes/Status Tag Registry.md",
                "Important tag-governance context; keyword mode may miss it without semantic context.",
                semantic=8,
                hybrid=8,
            ),
        ),
    ),
    QueryCase(
        category="hybrid_search_implementation_artifacts",
        query="hybrid note search BM25 tags",
        expected=(
            expect(
                "Durable Notes/Tag Retrieval Model.md",
                "Tag behavior became a first-class durable model after hybrid search review.",
                keyword=3,
                semantic=3,
                hybrid=3,
            ),
            expect(
                "In-flight/packet-hybrid-note-search-v2.md",
                "Primary implementation packet for the hybrid scoring work.",
                keyword=3,
                semantic=4,
                hybrid=4,
            ),
            expect(
                "Idea Backlog/Hybrid Note Search and Entry Note Workflow.md",
                "Originating idea note for the hybrid-search direction.",
                keyword=5,
                semantic=5,
                hybrid=5,
            ),
            expect(
                "Durable Notes/note-search-skill.md",
                "Caller interface updated for hybrid, keyword, and score fields.",
                keyword=6,
                semantic=6,
                hybrid=6,
            ),
            expect(
                "Durable Notes/Local Note Search Script.md",
                "Boundary note that separates graph search from semantic/hybrid query discovery.",
                semantic=8,
                hybrid=8,
            ),
        ),
    ),
    QueryCase(
        category="tag_status_retrieval",
        query="status-settled",
        expected=(
            expect(
                "Tags/status-settled.md",
                "Exact status tag note should be the strongest result.",
                keyword=1,
                semantic=1,
                hybrid=1,
            ),
            expect(
                "Durable Notes/Status Tag Registry.md",
                "Registry explains the status tag set.",
                keyword=3,
                semantic=3,
                hybrid=3,
            ),
        ),
    ),
    QueryCase(
        category="priority_task_retrieval",
        query="high priority next task",
        expected=(
            expect(
                "Tags/priority-high.md",
                "Exact priority tag note should be present when semantic or hybrid query behavior targets high priority.",
                hybrid=5,
            ),
            expect(
                "Idea Backlog/Hybrid Note Search and Entry Note Workflow.md",
                "High-priority current note-search direction should remain visible.",
                keyword=8,
                semantic=8,
                hybrid=8,
            ),
            expect(
                "Idea Backlog/Note Search Test Set.md",
                "High-priority benchmark/test-set idea should be discoverable for task planning.",
                keyword=8,
                semantic=8,
                hybrid=8,
            ),
        ),
    ),
    QueryCase(
        category="rough_concept_discovery",
        query="bounded context capsule from entry notes",
        expected=(
            expect(
                "Idea Backlog/Hybrid Note Search and Entry Note Workflow.md",
                "Owns the two-step entry-note to bounded-context search workflow.",
                keyword=4,
                semantic=3,
                hybrid=3,
            ),
            expect(
                "Durable Notes/note-search-skill.md",
                "Defines the bounded context capsule interface for callers.",
                keyword=8,
                semantic=8,
                hybrid=8,
            ),
        ),
    ),
)


def run_search(query: str, mode: str, limit: int) -> list[str]:
    result = subprocess.run(
        [
            sys.executable,
            str(SEARCH_TOOL),
            "--vault-root",
            str(VAULT_ROOT),
            "--query",
            query,
            "--search-mode",
            mode,
            "--format",
            "json",
            "--limit",
            str(limit),
            "--no-socket",
        ],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
        check=True,
    )
    payload = json.loads(result.stdout)
    return [item["path"] for item in payload.get("read_first", [])]


def evaluate_case(case: QueryCase, mode: str, limit: int) -> dict[str, object]:
    results = run_search(case.query, mode, limit)
    expected_notes = [note for note in case.expected if note.max_rank_for(mode) is not None]
    ranks = {
        note.path: (results.index(note.path) + 1 if note.path in results else None)
        for note in expected_notes
    }
    thresholds = {note.path: note.max_rank_for(mode) for note in expected_notes}
    rationale = {note.path: note.rationale for note in expected_notes}
    passed = {
        note.path: (ranks[note.path] is not None and ranks[note.path] <= int(thresholds[note.path]))
        for note in expected_notes
    }
    hits = sum(passed.values())
    return {
        "category": case.category,
        "query": case.query,
        "mode": mode,
        "hits": hits,
        "expected_count": len(expected_notes),
        "ranks": ranks,
        "thresholds": thresholds,
        "passed": passed,
        "rationale": rationale,
        "top_results": results,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Evaluate note-search ranking on a small real-vault benchmark.")
    parser.add_argument("--modes", nargs="+", choices=("keyword", "semantic", "hybrid"), default=["keyword"])
    parser.add_argument("--limit", type=int, default=8)
    args = parser.parse_args()

    all_results = [evaluate_case(case, mode, args.limit) for mode in args.modes for case in QUERY_CASES]
    print(json.dumps({"limit": args.limit, "results": all_results}, indent=2))

    missing = [
        result
        for result in all_results
        if int(result["hits"]) < int(result["expected_count"])
    ]
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
