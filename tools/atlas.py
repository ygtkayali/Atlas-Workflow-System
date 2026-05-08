#!/usr/bin/env python3
"""Minimal local Atlas command surface."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path
from typing import Any

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
MODES_ROOT = REPO_ROOT / "modes"
SHARED_ROOT = REPO_ROOT / "shared"
SHARED_MANIFEST_PATH = SHARED_ROOT / "manifest.yaml"


Action = dict[str, Any]


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a YAML mapping")
    return data


def mode_manifest_paths() -> list[Path]:
    if not MODES_ROOT.exists():
        return []
    return sorted(MODES_ROOT.glob("*/manifest.yaml"))


def load_mode_manifest(mode: str) -> tuple[Path, dict[str, Any]]:
    manifest_path = MODES_ROOT / mode / "manifest.yaml"
    if not manifest_path.exists():
        raise FileNotFoundError(f"Unknown mode: {mode}")
    return manifest_path, load_yaml(manifest_path)


def load_shared_manifest() -> tuple[Path, dict[str, Any]] | None:
    if not SHARED_MANIFEST_PATH.exists():
        return None
    return SHARED_MANIFEST_PATH, load_yaml(SHARED_MANIFEST_PATH)


def manifest_mode_name(manifest: dict[str, Any], fallback: str) -> str:
    mode = manifest.get("mode", {})
    if isinstance(mode, dict):
        return str(mode.get("name") or fallback)
    return fallback


def manifest_mode_version(manifest: dict[str, Any]) -> str:
    mode = manifest.get("mode", {})
    if isinstance(mode, dict):
        return str(mode.get("version") or "unknown")
    return "unknown"


def manifest_mode_description(manifest: dict[str, Any]) -> str:
    mode = manifest.get("mode", {})
    if isinstance(mode, dict):
        return str(mode.get("description") or "")
    return ""


def command_mode_list(_args: argparse.Namespace) -> int:
    manifests = mode_manifest_paths()
    if not manifests:
        print("No modes found.")
        return 1

    for manifest_path in manifests:
        manifest = load_yaml(manifest_path)
        fallback = manifest_path.parent.name
        name = manifest_mode_name(manifest, fallback)
        version = manifest_mode_version(manifest)
        description = manifest_mode_description(manifest)
        suffix = f" - {description}" if description else ""
        print(f"{name} {version}{suffix}")
    return 0


def project_atlas_config_path(project_root: Path) -> Path:
    return project_root / "atlas.yaml"


def read_project_mode(project_root: Path) -> str | None:
    config_path = project_atlas_config_path(project_root)
    if not config_path.exists():
        return None
    config = load_yaml(config_path)
    atlas = config.get("atlas", {})
    if not isinstance(atlas, dict):
        raise ValueError(f"{config_path} has no atlas mapping")
    mode = atlas.get("mode")
    return str(mode) if mode else None


def default_mode() -> str:
    manifests = mode_manifest_paths()
    if len(manifests) == 1:
        return manifests[0].parent.name
    return "dev-workflow"


def vault_path_for_project(project_root: Path, manifest: dict[str, Any]) -> Path:
    config_path = project_atlas_config_path(project_root)
    if config_path.exists():
        config = load_yaml(config_path)
        vault = config.get("vault", {})
        if isinstance(vault, dict) and vault.get("path"):
            return project_root / str(vault["path"])

    vault = manifest.get("vault", {})
    if isinstance(vault, dict) and vault.get("default_path"):
        return project_root / str(vault["default_path"])
    return project_root / "docs"


def manifest_vault_folders(manifest: dict[str, Any]) -> list[str]:
    vault = manifest.get("vault", {})
    if not isinstance(vault, dict):
        return []
    folders = vault.get("folders", [])
    if not isinstance(folders, list):
        return []

    paths: list[str] = []
    for folder in folders:
        if isinstance(folder, dict) and folder.get("path"):
            paths.append(str(folder["path"]))
    return paths


def expand_user_path(path_text: str) -> Path:
    return Path(path_text).expanduser()


def print_check(status: str, label: str, detail: str = "") -> None:
    suffix = f" - {detail}" if detail else ""
    print(f"{status}: {label}{suffix}")


def has_payload(path: Path) -> bool:
    if not path.exists():
        return False
    if path.is_file():
        return path.name != ".gitkeep"
    return any(child.name != ".gitkeep" for child in path.rglob("*") if child.is_file())


def relative_to_repo(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def approve_or_cancel(prompt: str) -> bool:
    try:
        response = input(f"{prompt} Type yes to continue: ").strip()
    except EOFError:
        return False
    return response == "yes"


def copy_file(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def file_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def marked_block_bounds(text: str, begin_marker: str, end_marker: str) -> tuple[int, int] | None:
    begin = text.find(begin_marker)
    if begin == -1:
        return None
    end = text.find(end_marker, begin)
    if end == -1:
        return None
    return begin, end + len(end_marker)


def prepended_file_content(source: Path, target: Path) -> str | None:
    source_text = file_text(source).strip() + "\n"
    target_text = file_text(target)
    if target_text.startswith(source_text):
        return None

    begin_marker = "<!-- atlas-dev-workflow-bridge:start -->"
    end_marker = "<!-- atlas-dev-workflow-bridge:end -->"
    existing_bridge = marked_block_bounds(target_text, begin_marker, end_marker)
    if existing_bridge:
        begin, end = existing_bridge
        target_text = target_text[:begin] + target_text[end:]

    remaining = target_text.lstrip("\n")
    if remaining:
        return f"{source_text}\n{remaining}"
    return source_text


def prepend_file(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    if not target.exists():
        copy_file(source, target)
        return

    content = prepended_file_content(source, target)
    if content is not None:
        target.write_text(content, encoding="utf-8")


def cleaned_marked_block_content(target: Path) -> str | None:
    if not target.exists():
        return None

    begin_marker = "<!-- atlas-dev-workflow-bridge:start -->"
    end_marker = "<!-- atlas-dev-workflow-bridge:end -->"
    target_text = file_text(target)
    existing_bridge = marked_block_bounds(target_text, begin_marker, end_marker)
    if not existing_bridge:
        return None

    begin, end = existing_bridge
    return (target_text[:begin] + target_text[end:]).lstrip("\n")


def clean_marked_block(target: Path) -> None:
    content = cleaned_marked_block_content(target)
    if content is not None:
        target.write_text(content, encoding="utf-8")


def copy_tree_payload(source: Path, target: Path) -> None:
    for source_file in source.rglob("*"):
        if not source_file.is_file() or source_file.name == ".gitkeep":
            continue
        relative = source_file.relative_to(source)
        copy_file(source_file, target / relative)


def source_files_differ(source: Path, target: Path) -> bool:
    for source_file in source.rglob("*"):
        if not source_file.is_file() or source_file.name == ".gitkeep":
            continue
        target_file = target / source_file.relative_to(source)
        if not target_file.exists():
            return True
        if source_file.read_bytes() != target_file.read_bytes():
            return True
    return False


def print_plan(title: str, actions: list[Action], skipped: list[Action]) -> None:
    print(title)
    if not actions and not skipped:
        print("No changes needed.")
        return

    if actions:
        print("Proposed changes:")
        for action in actions:
            detail = action.get("detail", "")
            suffix = f" - {detail}" if detail else ""
            print(f"- {action['kind']}: {action['target']}{suffix}")

    if skipped:
        print("Skipped:")
        for action in skipped:
            detail = action.get("detail", "")
            suffix = f" - {detail}" if detail else ""
            print(f"- {action['kind']}: {action['target']}{suffix}")


def apply_action(action: Action) -> None:
    kind = action["kind"]
    target = Path(action["target"])

    if kind == "create_folder":
        target.mkdir(parents=True, exist_ok=True)
    elif kind == "copy_file":
        copy_file(Path(action["source"]), target)
    elif kind == "prepend_file":
        prepend_file(Path(action["source"]), target)
    elif kind == "clean_marked_block":
        clean_marked_block(target)
    elif kind == "copy_tree":
        copy_tree_payload(Path(action["source"]), target)
    elif kind == "write_atlas_config":
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(yaml.safe_dump(action["content"], sort_keys=False), encoding="utf-8")
    else:
        raise ValueError(f"Unknown sync action kind: {kind}")


def source_asset_root(manifest_path: Path, manifest: dict[str, Any]) -> Path:
    source_assets = manifest.get("source_assets", {})
    if isinstance(source_assets, dict) and source_assets.get("root"):
        root = Path(str(source_assets["root"]))
        if not root.is_absolute():
            return REPO_ROOT / root
        return root
    return manifest_path.parent


def check_source_asset_folders(manifest_path: Path, manifest: dict[str, Any], keys: tuple[str, ...]) -> int:
    failures = 0
    source_assets = manifest.get("source_assets", {})
    if not isinstance(source_assets, dict):
        return failures
    root = source_asset_root(manifest_path, manifest)
    for key in keys:
        relative = source_assets.get(key)
        if not relative:
            continue
        asset_path = root / str(relative)
        if asset_path.exists():
            print_check("ok", f"source asset folder {key}", relative_to_repo(asset_path))
        else:
            print_check("error", f"source asset folder {key}", relative_to_repo(asset_path))
            failures += 1
    return failures


def check_installed_assets(manifest: dict[str, Any], section: str, label: str) -> int:
    warnings = 0
    managed = manifest.get(section, {})
    if not isinstance(managed, dict):
        return warnings
    for item in managed.get("items", []):
        if not isinstance(item, dict):
            continue
        installed_path = item.get("installed_path")
        asset_id = item.get("id", installed_path)
        if not installed_path:
            continue
        if expand_user_path(str(installed_path)).exists():
            print_check("ok", f"{label} {asset_id}", str(installed_path))
        else:
            print_check("warning", f"{label} {asset_id}", f"missing: {installed_path}")
            warnings += 1
    return warnings


def command_health_check(args: argparse.Namespace) -> int:
    project_root = Path(args.path).resolve()
    mode = read_project_mode(project_root) or default_mode()
    manifest_path, manifest = load_mode_manifest(mode)

    failures = 0
    warnings = 0

    print(f"Atlas health check: {project_root}")
    print(f"Mode: {manifest_mode_name(manifest, mode)} {manifest_mode_version(manifest)}")

    if manifest_path.exists():
        print_check("ok", "manifest", str(manifest_path.relative_to(REPO_ROOT)))
    else:
        print_check("error", "manifest", str(manifest_path))
        failures += 1

    failures += check_source_asset_folders(manifest_path, manifest, ("templates", "starter_notes", "tags", "skills", "tools"))

    shared_manifest = load_shared_manifest()
    if shared_manifest:
        shared_manifest_path, shared = shared_manifest
        print_check("ok", "shared manifest", relative_to_repo(shared_manifest_path))
        failures += check_source_asset_folders(shared_manifest_path, shared, ("skills", "tools"))
    else:
        print_check("warning", "shared manifest", "missing")
        warnings += 1

    config_path = project_atlas_config_path(project_root)
    if config_path.exists():
        print_check("ok", "project atlas.yaml", str(config_path))
    else:
        print_check("warning", "project atlas.yaml", "missing")
        warnings += 1

    agents_path = project_root / "AGENTS.md"
    if agents_path.exists():
        print_check("ok", "local AGENTS.md", "exists and may receive the managed bridge")
    else:
        print_check("warning", "local AGENTS.md", "missing")
        warnings += 1

    vault_root = vault_path_for_project(project_root, manifest)
    if vault_root.exists():
        print_check("ok", "vault root", str(vault_root))
    else:
        print_check("warning", "vault root", f"missing: {vault_root}")
        warnings += 1

    for folder in manifest_vault_folders(manifest):
        folder_path = vault_root / folder
        if folder_path.exists():
            print_check("ok", f"vault folder {folder}", str(folder_path))
        else:
            print_check("warning", f"vault folder {folder}", f"missing: {folder_path}")
            warnings += 1

    if shared_manifest:
        _, shared = shared_manifest
        warnings += check_installed_assets(shared, "managed_skills", "shared skill")
        warnings += check_installed_assets(shared, "managed_tools", "shared tool")

    warnings += check_installed_assets(manifest, "managed_skills", "skill")
    warnings += check_installed_assets(manifest, "managed_tools", "tool")

    sync_actions, sync_skipped = project_sync_plan(project_root, mode, manifest_path, manifest)
    for action in sync_actions:
        detail = action.get("detail", "")
        sync_detail = f"{action['kind']}: {action['target']}"
        if detail:
            sync_detail = f"{sync_detail} - {detail}"
        print_check("warning", "project sync drift", sync_detail)
        warnings += 1
    for action in sync_skipped:
        detail = action.get("detail", "")
        sync_detail = f"{action['kind']}: {action['target']}"
        if detail:
            sync_detail = f"{sync_detail} - {detail}"
        print_check("warning", "project sync skipped", sync_detail)
        warnings += 1

    print(f"Summary: {failures} error(s), {warnings} warning(s)")
    return 1 if failures else 0


def atlas_config_for_mode(manifest: dict[str, Any], mode: str) -> dict[str, Any]:
    vault = manifest.get("vault", {})
    managed_skills = manifest.get("managed_skills", {})
    managed_tools = manifest.get("managed_tools", {})
    managed_files = manifest.get("managed_files", [])
    managed_tags = manifest.get("managed_tags", [])
    skill_items = managed_skills.get("items", []) if isinstance(managed_skills, dict) else []
    tool_items = managed_tools.get("items", []) if isinstance(managed_tools, dict) else []
    shared_manifest = load_shared_manifest()
    shared_skill_items: list[dict[str, Any]] = []
    shared_tool_items: list[dict[str, Any]] = []
    if shared_manifest:
        _, shared = shared_manifest
        shared_skills = shared.get("managed_skills", {})
        shared_tools = shared.get("managed_tools", {})
        if isinstance(shared_skills, dict):
            shared_skill_items = [
                item for item in shared_skills.get("items", [])
                if isinstance(item, dict)
            ]
        if isinstance(shared_tools, dict):
            shared_tool_items = [
                item for item in shared_tools.get("items", [])
                if isinstance(item, dict)
            ]

    return {
        "atlas": {
            "mode": manifest_mode_name(manifest, mode),
            "version": manifest_mode_version(manifest),
        },
        "vault": {
            "name": vault.get("default_name", "docs") if isinstance(vault, dict) else "docs",
            "path": vault.get("default_path", "docs") if isinstance(vault, dict) else "docs",
        },
        "managed_files": [item.get("id") for item in managed_files if isinstance(item, dict)],
        "managed_tags": [item.get("id") for item in managed_tags if isinstance(item, dict)],
        "managed_skills": [
            item.get("id")
            for item in [*shared_skill_items, *skill_items]
            if isinstance(item, dict)
        ],
        "managed_tools": [
            item.get("id")
            for item in [*shared_tool_items, *tool_items]
            if isinstance(item, dict)
        ],
    }


def configured_item_ids(project_root: Path, section: str) -> set[str] | None:
    config_path = project_atlas_config_path(project_root)
    if not config_path.exists():
        return None
    config = load_yaml(config_path)
    values = config.get(section)
    if not isinstance(values, list):
        return None
    return {str(value) for value in values if value is not None}


def copy_managed_vault_files(manifest: dict[str, Any], mode_root: Path, vault_root: Path, created: list[Path], kept: list[Path]) -> None:
    for section, base_target in (
        ("managed_templates", vault_root),
        ("managed_starter_notes", vault_root),
        ("managed_tags", vault_root),
    ):
        items = manifest.get(section, [])
        if not isinstance(items, list):
            continue
        for item in items:
            if not isinstance(item, dict) or not item.get("source") or not item.get("target"):
                continue
            source = mode_root / str(item["source"])
            target = base_target / str(item["target"])
            if target.exists():
                kept.append(target)
            elif source.is_file() and has_payload(source):
                copy_file(source, target)
                created.append(target)


def command_init(args: argparse.Namespace) -> int:
    project_root = Path(args.path).resolve()
    project_root.mkdir(parents=True, exist_ok=True)
    manifest_path, manifest = load_mode_manifest(args.mode)
    mode_root = manifest_path.parent

    created: list[Path] = []
    updated: list[Path] = []
    kept: list[Path] = []

    config_path = project_atlas_config_path(project_root)
    if config_path.exists():
        kept.append(config_path)
    else:
        config = atlas_config_for_mode(manifest, args.mode)
        config_path.write_text(yaml.safe_dump(config, sort_keys=False), encoding="utf-8")
        created.append(config_path)

    vault_root = vault_path_for_project(project_root, manifest)
    if vault_root.exists():
        kept.append(vault_root)
    else:
        vault_root.mkdir(parents=True)
        created.append(vault_root)

    for folder in manifest_vault_folders(manifest):
        folder_path = vault_root / folder
        if folder_path.exists():
            kept.append(folder_path)
        else:
            folder_path.mkdir(parents=True)
            created.append(folder_path)

    managed_files = manifest.get("managed_files", [])
    if isinstance(managed_files, list):
        for item in managed_files:
            if not isinstance(item, dict) or not item.get("source") or not item.get("target"):
                continue
            source = mode_root / str(item["source"])
            target = project_root / str(item["target"])
            sync_mode = str(item.get("sync") or "")
            if target in created or target in kept:
                continue
            if target.exists():
                if sync_mode == "prepend_to_existing" and source.is_file() and has_payload(source):
                    content = prepended_file_content(source, target)
                    if content is not None:
                        target.write_text(content, encoding="utf-8")
                        updated.append(target)
                    else:
                        kept.append(target)
                else:
                    kept.append(target)
                continue
            if has_payload(source):
                if source.is_file():
                    copy_file(source, target)
                else:
                    copy_tree_payload(source, target)
                created.append(target)

    copy_managed_vault_files(manifest, mode_root, vault_root, created, kept)

    print(f"Initialized mode {manifest_mode_name(manifest, args.mode)} from {manifest_path.relative_to(REPO_ROOT)}")
    for path in created:
        print_check("created", str(path))
    for path in updated:
        print_check("updated", str(path), "prepended managed bridge")
    for path in kept:
        print_check("kept", str(path), "already exists")
    return 0


def project_sync_plan(project_root: Path, mode: str, manifest_path: Path, manifest: dict[str, Any]) -> tuple[list[Action], list[Action]]:
    actions: list[Action] = []
    skipped: list[Action] = []
    mode_root = manifest_path.parent

    config_path = project_atlas_config_path(project_root)
    if not config_path.exists():
        actions.append({
            "kind": "write_atlas_config",
            "target": str(config_path),
            "content": atlas_config_for_mode(manifest, mode),
            "detail": "create missing atlas.yaml",
        })

    vault_root = vault_path_for_project(project_root, manifest)
    if not vault_root.exists():
        actions.append({
            "kind": "create_folder",
            "target": str(vault_root),
            "detail": "create vault root",
        })

    for folder in manifest_vault_folders(manifest):
        folder_path = vault_root / folder
        if not folder_path.exists():
            actions.append({
                "kind": "create_folder",
                "target": str(folder_path),
                "detail": "create vault folder",
            })

    managed_files = manifest.get("managed_files", [])
    configured_files = configured_item_ids(project_root, "managed_files")
    if isinstance(managed_files, list):
        for item in managed_files:
            if not isinstance(item, dict) or not item.get("source") or not item.get("target"):
                continue
            item_id = str(item.get("id") or "")
            source = mode_root / str(item["source"])
            target = project_root / str(item["target"])
            sync_mode = str(item.get("sync") or "")
            if configured_files is not None and item_id not in configured_files:
                if sync_mode == "prepend_to_existing" and cleaned_marked_block_content(target) is not None:
                    actions.append({
                        "kind": "clean_marked_block",
                        "target": str(target),
                        "detail": f"remove unmanaged bridge for {item_id}",
                    })
                continue
            if target.exists() and sync_mode != "prepend_to_existing":
                continue
            if has_payload(source):
                if target.exists() and sync_mode == "prepend_to_existing":
                    if source.is_file() and prepended_file_content(source, target) is not None:
                        actions.append({
                            "kind": "prepend_file",
                            "source": str(source),
                            "target": str(target),
                            "detail": f"prepend/update bridge from {relative_to_repo(source)}",
                        })
                    continue
                actions.append({
                    "kind": "copy_file" if source.is_file() else "copy_tree",
                    "source": str(source),
                    "target": str(target),
                    "detail": f"from {relative_to_repo(source)}",
                })
            else:
                skipped.append({
                    "kind": "missing_source",
                    "target": str(target),
                    "detail": f"source not populated: {relative_to_repo(source)}",
                })

    for section, base_target in (
        ("managed_templates", vault_root),
        ("managed_starter_notes", vault_root),
        ("managed_tags", vault_root),
    ):
        items = manifest.get(section, [])
        if not isinstance(items, list):
            continue
        for item in items:
            if not isinstance(item, dict) or not item.get("source") or not item.get("target"):
                continue
            source = mode_root / str(item["source"])
            target = base_target / str(item["target"])
            if source.is_file() and has_payload(source):
                if target.exists():
                    if source.read_bytes() != target.read_bytes():
                        actions.append({
                            "kind": "copy_file",
                            "source": str(source),
                            "target": str(target),
                            "detail": f"update changed managed asset from {relative_to_repo(source)}",
                        })
                    continue
                actions.append({
                    "kind": "copy_file",
                    "source": str(source),
                    "target": str(target),
                    "detail": f"from {relative_to_repo(source)}",
                })
            else:
                skipped.append({
                    "kind": "missing_source",
                    "target": str(target),
                    "detail": f"source not populated: {relative_to_repo(source)}",
                })

    managed_tools = manifest.get("managed_tools", {})
    if isinstance(managed_tools, dict):
        for item in managed_tools.get("items", []):
            if not isinstance(item, dict) or not item.get("source") or not item.get("project_path"):
                continue
            source = mode_root / str(item["source"])
            target = project_root / str(item["project_path"])
            if source.is_file() and has_payload(source):
                if target.exists():
                    if source.read_bytes() != target.read_bytes():
                        actions.append({
                            "kind": "copy_file",
                            "source": str(source),
                            "target": str(target),
                            "detail": f"update changed tool from {relative_to_repo(source)}",
                        })
                    continue
                actions.append({
                    "kind": "copy_file",
                    "source": str(source),
                    "target": str(target),
                    "detail": f"from {relative_to_repo(source)}",
                })
            else:
                skipped.append({
                    "kind": "missing_source",
                    "target": str(target),
                    "detail": f"source not populated: {relative_to_repo(source)}",
                })

    return actions, skipped


def command_sync(args: argparse.Namespace) -> int:
    if args.path == "skills":
        project_mode = read_project_mode(Path.cwd()) or default_mode()
        return command_skills_sync(argparse.Namespace(mode=project_mode))

    project_root = Path(args.path).resolve()
    mode = read_project_mode(project_root)
    if not mode:
        raise ValueError(f"{project_atlas_config_path(project_root)} is missing. Run atlas init first.")
    manifest_path, manifest = load_mode_manifest(mode)
    actions, skipped = project_sync_plan(project_root, mode, manifest_path, manifest)

    print_plan(f"Atlas project sync plan: {project_root}", actions, skipped)
    if not actions:
        return 0
    if not approve_or_cancel("Apply the full project sync plan?"):
        print("Cancelled.")
        return 1
    for action in actions:
        apply_action(action)
    print(f"Applied {len(actions)} project sync action(s).")
    return 0


def skill_sync_plan(mode: str, manifest_path: Path, manifest: dict[str, Any]) -> tuple[list[Action], list[Action]]:
    actions: list[Action] = []
    skipped: list[Action] = []
    mode_root = source_asset_root(manifest_path, manifest)
    managed_skills = manifest.get("managed_skills", {})
    if not isinstance(managed_skills, dict):
        return actions, skipped

    for item in managed_skills.get("items", []):
        if not isinstance(item, dict) or not item.get("source") or not item.get("installed_path"):
            continue
        source = mode_root / str(item["source"])
        target = expand_user_path(str(item["installed_path"]))
        skill_id = item.get("id", source.name)

        if not has_payload(source):
            skipped.append({
                "kind": "missing_source",
                "target": str(target),
                "detail": f"skill {skill_id} source not populated: {relative_to_repo(source)}",
            })
            continue

        if not target.exists():
            actions.append({
                "kind": "copy_tree",
                "source": str(source),
                "target": str(target),
                "detail": f"install missing skill {skill_id}",
            })
        elif source_files_differ(source, target):
            actions.append({
                "kind": "copy_tree",
                "source": str(source),
                "target": str(target),
                "detail": f"update changed files for skill {skill_id}",
            })

    return actions, skipped


def tool_sync_plan(manifest_path: Path, manifest: dict[str, Any]) -> tuple[list[Action], list[Action]]:
    actions: list[Action] = []
    skipped: list[Action] = []
    root = source_asset_root(manifest_path, manifest)
    managed_tools = manifest.get("managed_tools", {})
    if not isinstance(managed_tools, dict):
        return actions, skipped

    for item in managed_tools.get("items", []):
        if not isinstance(item, dict) or not item.get("source") or not item.get("installed_path"):
            continue
        source = root / str(item["source"])
        target = expand_user_path(str(item["installed_path"]))
        tool_id = item.get("id", source.name)

        if not source.is_file() or not has_payload(source):
            skipped.append({
                "kind": "missing_source",
                "target": str(target),
                "detail": f"tool {tool_id} source not populated: {relative_to_repo(source)}",
            })
            continue

        if not target.exists():
            actions.append({
                "kind": "copy_file",
                "source": str(source),
                "target": str(target),
                "detail": f"install missing tool {tool_id}",
            })
        elif source.read_bytes() != target.read_bytes():
            actions.append({
                "kind": "copy_file",
                "source": str(source),
                "target": str(target),
                "detail": f"update changed tool {tool_id}",
            })

    return actions, skipped


def command_skills_sync(args: argparse.Namespace) -> int:
    manifest_path, manifest = load_mode_manifest(args.mode)
    actions: list[Action] = []
    skipped: list[Action] = []

    shared_manifest = load_shared_manifest()
    if shared_manifest:
        shared_manifest_path, shared = shared_manifest
        shared_actions, shared_skipped = skill_sync_plan("shared", shared_manifest_path, shared)
        shared_tool_actions, shared_tool_skipped = tool_sync_plan(shared_manifest_path, shared)
        actions.extend(shared_actions)
        actions.extend(shared_tool_actions)
        skipped.extend(shared_skipped)
        skipped.extend(shared_tool_skipped)

    mode_actions, mode_skipped = skill_sync_plan(args.mode, manifest_path, manifest)
    actions.extend(mode_actions)
    skipped.extend(mode_skipped)

    print_plan(f"Atlas skill sync plan: {args.mode}", actions, skipped)
    if not actions:
        return 0
    if not approve_or_cancel("Apply the full skill sync plan?"):
        print("Cancelled.")
        return 1
    for action in actions:
        apply_action(action)
    print(f"Applied {len(actions)} skill sync action(s).")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="atlas")
    subparsers = parser.add_subparsers(dest="command", required=True)

    mode_parser = subparsers.add_parser("mode", help="Inspect available modes")
    mode_subparsers = mode_parser.add_subparsers(dest="mode_command", required=True)
    mode_list = mode_subparsers.add_parser("list", help="List available modes")
    mode_list.set_defaults(func=command_mode_list)

    health_parser = subparsers.add_parser("health", help="Inspect setup health")
    health_subparsers = health_parser.add_subparsers(dest="health_command", required=True)
    health_check = health_subparsers.add_parser("check", help="Check a project path")
    health_check.add_argument("path")
    health_check.set_defaults(func=command_health_check)

    init_parser = subparsers.add_parser("init", help="Initialize a project for a mode")
    init_parser.add_argument("--mode", required=True)
    init_parser.add_argument("path")
    init_parser.set_defaults(func=command_init)

    sync_parser = subparsers.add_parser("sync", help="Synchronize project-local managed assets")
    sync_parser.add_argument("path", nargs="?", default=".")
    sync_parser.set_defaults(func=command_sync)

    skills_parser = subparsers.add_parser("skills", help="Synchronize global skills")
    skills_subparsers = skills_parser.add_subparsers(dest="skills_command", required=True)
    skills_sync = skills_subparsers.add_parser("sync", help="Synchronize skills for a mode")
    skills_sync.add_argument("--mode", required=True)
    skills_sync.set_defaults(func=command_skills_sync)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return int(args.func(args))
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
