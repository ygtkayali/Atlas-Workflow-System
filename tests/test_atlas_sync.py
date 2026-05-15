from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from tools import atlas


def write_file(root: Path, relative_path: str, text: str) -> None:
    path = root / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


class AtlasSyncTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)

    def tearDown(self) -> None:
        self.tempdir.cleanup()

    def test_source_files_differ_detects_stale_target_file(self) -> None:
        source = self.root / "source"
        target = self.root / "target"
        write_file(source, "SKILL.md", "current\n")
        write_file(target, "SKILL.md", "current\n")
        write_file(target, "removed.md", "stale\n")

        self.assertTrue(atlas.source_files_differ(source, target))

    def test_skill_sync_plan_updates_when_target_has_stale_file(self) -> None:
        write_file(self.root, "source/skills/example/SKILL.md", "current\n")
        write_file(self.root, "installed/example/SKILL.md", "current\n")
        write_file(self.root, "installed/example/removed.md", "stale\n")
        manifest = {
            "source_assets": {"root": str(self.root / "source")},
            "managed_skills": {
                "items": [{"id": "example", "source": "skills/example"}],
            },
        }
        platform_cfg = {"skills_root": str(self.root / "installed")}

        actions, skipped = atlas.skill_sync_plan(
            "test",
            self.root / "source" / "manifest.yaml",
            manifest,
            "test-platform",
            platform_cfg,
        )

        self.assertEqual(skipped, [])
        self.assertEqual(len(actions), 1)
        self.assertEqual(actions[0]["kind"], "copy_tree")
        self.assertIn("update changed files", actions[0]["detail"])

    def test_copy_tree_payload_removes_stale_target_file(self) -> None:
        source = self.root / "source"
        target = self.root / "target"
        write_file(source, "SKILL.md", "current\n")
        write_file(source, "references/current.md", "current reference\n")
        write_file(target, "SKILL.md", "old\n")
        write_file(target, "references/removed.md", "stale reference\n")

        atlas.copy_tree_payload(source, target)

        self.assertEqual((target / "SKILL.md").read_text(encoding="utf-8"), "current\n")
        self.assertEqual(
            (target / "references/current.md").read_text(encoding="utf-8"),
            "current reference\n",
        )
        self.assertFalse((target / "references/removed.md").exists())

    def test_copy_tree_payload_ignores_gitkeep_as_payload(self) -> None:
        source = self.root / "source"
        target = self.root / "target"
        write_file(source, "SKILL.md", "current\n")
        write_file(target, "SKILL.md", "current\n")
        write_file(target, ".gitkeep", "")

        atlas.copy_tree_payload(source, target)

        self.assertTrue((target / ".gitkeep").exists())
        self.assertFalse(atlas.source_files_differ(source, target))


if __name__ == "__main__":
    unittest.main()
