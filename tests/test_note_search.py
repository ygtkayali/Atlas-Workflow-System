from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
GRAPH_SEARCH = REPO_ROOT / "shared" / "tools" / "local_note_search.py"
SEMANTIC_SEARCH = REPO_ROOT / "shared" / "tools" / "local_note_semantic_search.py"


def write_note(vault: Path, relative_path: str, text: str) -> None:
    path = vault / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


class NoteSearchTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.vault = Path(self.tempdir.name)
        self._build_vault()

    def tearDown(self) -> None:
        self.tempdir.cleanup()

    def _build_vault(self) -> None:
        write_note(
            self.vault,
            "Core Search.md",
            """
            # Core Search

            Related: [[Hybrid Search]]

            Graph retrieval should find direct outgoing links.
            """,
        )
        write_note(
            self.vault,
            "Hybrid Search.md",
            """
            # Hybrid Search

            Hybrid BM25 ranking score fusion combines keyword, graph, and tag signals.
            """,
        )
        write_note(
            self.vault,
            "Backlink Source.md",
            """
            # Backlink Source

            This note points back to [[Core Search]].
            """,
        )
        write_note(
            self.vault,
            "Tagged Idea.md",
            """
            # Tagged Idea

            Type: [[Tags/idea-note]]

            This describes a workflow idea with tag-guided retrieval.
            """,
        )
        write_note(
            self.vault,
            "Tags/idea-note.md",
            """
            # idea-note

            Idea note tag.
            """,
        )
        write_note(
            self.vault,
            "Distractor.md",
            """
            # Distractor

            This unrelated document talks about deployment chores.
            """,
        )
        write_note(
            self.vault,
            "Archived Result.md",
            """
            # Archived Result

            Status: [[Tags/status-archived]]

            Hybrid BM25 ranking score fusion should not surface archived notes by default.
            """,
        )
        write_note(
            self.vault,
            "High Priority Task.md",
            """
            # High Priority Task

            Priority: [[Tags/priority-high]]

            This task describes next task selection for note search.
            """,
        )
        write_note(
            self.vault,
            "Low Priority Task.md",
            """
            # Low Priority Task

            Priority: [[Tags/priority-low]]

            This task also describes next task selection for note search.
            """,
        )
        write_note(
            self.vault,
            "Tags/status-archived.md",
            """
            # status-archived
            """,
        )
        write_note(
            self.vault,
            "Tags/priority-high.md",
            """
            # priority-high
            """,
        )
        write_note(
            self.vault,
            "Tags/priority-low.md",
            """
            # priority-low
            """,
        )

    def run_json(self, *args: str) -> dict:
        result = subprocess.run(
            [sys.executable, *args],
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
            check=True,
        )
        return json.loads(result.stdout)

    def test_graph_search_returns_outgoing_links_and_backlinks(self) -> None:
        payload = self.run_json(
            str(GRAPH_SEARCH),
            "--vault-root",
            str(self.vault),
            "--seed-path",
            "Core Search.md",
            "--format",
            "json",
            "--debug",
        )

        candidates = {item["path"]: item["reasons"] for item in payload["candidates"]}
        self.assertIn("Hybrid Search.md", candidates)
        self.assertIn("outgoing_link", candidates["Hybrid Search.md"])
        self.assertIn("Backlink Source.md", candidates)
        self.assertIn("backlink", candidates["Backlink Source.md"])

    def test_keyword_search_ranks_exact_term_note_first(self) -> None:
        payload = self.run_json(
            str(SEMANTIC_SEARCH),
            "--vault-root",
            str(self.vault),
            "--query",
            "hybrid bm25 score fusion",
            "--search-mode",
            "keyword",
            "--format",
            "json",
            "--limit",
            "3",
        )

        first = payload["read_first"][0]
        self.assertEqual(first["path"], "Hybrid Search.md")
        self.assertEqual(first["semantic_score"], 0.0)
        self.assertGreater(first["keyword_score"], 0.0)
        self.assertTrue(any(reason.startswith("keyword_match:") for reason in first["why"]))
        paths = [item["path"] for item in payload["read_first"]]
        self.assertNotIn("Archived Result.md", paths)

    def test_keyword_search_uses_tags_as_candidate_filters(self) -> None:
        payload = self.run_json(
            str(SEMANTIC_SEARCH),
            "--vault-root",
            str(self.vault),
            "--query",
            "high priority next task",
            "--search-mode",
            "keyword",
            "--format",
            "json",
            "--limit",
            "5",
        )

        paths = [item["path"] for item in payload["read_first"]]
        self.assertIn("High Priority Task.md", paths)
        self.assertNotIn("Low Priority Task.md", paths)
        self.assertEqual(payload["tag_filter"]["include_tags"], ["priority-high"])

    def test_archived_filter_is_canceled_when_archived_is_targeted(self) -> None:
        payload = self.run_json(
            str(SEMANTIC_SEARCH),
            "--vault-root",
            str(self.vault),
            "--query",
            "archived hybrid bm25",
            "--search-mode",
            "keyword",
            "--format",
            "json",
            "--limit",
            "5",
        )

        paths = [item["path"] for item in payload["read_first"]]
        self.assertIn("Archived Result.md", paths)
        self.assertEqual(payload["tag_filter"]["include_tags"], ["status-archived"])
        self.assertEqual(payload["tag_filter"]["exclude_tags"], [])

    def test_keyword_search_exposes_tag_score_for_note_based_tags(self) -> None:
        payload = self.run_json(
            str(SEMANTIC_SEARCH),
            "--vault-root",
            str(self.vault),
            "--query",
            "idea-note workflow retrieval",
            "--search-mode",
            "keyword",
            "--format",
            "json",
            "--limit",
            "5",
        )

        tagged = next(item for item in payload["read_first"] if item["path"] == "Tagged Idea.md")
        self.assertGreater(tagged["tag_score"], 0.0)
        self.assertTrue(any(reason.startswith("tag_match:idea-note") for reason in tagged["why"]))

    def test_keyword_text_mode_prints_paths_only(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                str(SEMANTIC_SEARCH),
                "--vault-root",
                str(self.vault),
                "--query",
                "hybrid bm25",
                "--search-mode",
                "keyword",
                "--format",
                "text",
                "--limit",
                "2",
            ],
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
            check=True,
        )

        lines = [line for line in result.stdout.splitlines() if line]
        self.assertEqual(lines[0], "Hybrid Search.md")
        self.assertTrue(all(not line.startswith("{") for line in lines))


if __name__ == "__main__":
    unittest.main()
