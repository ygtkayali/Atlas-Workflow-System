#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")


@dataclass(frozen=True)
class ResolutionResult:
    raw: str
    cleaned: str
    resolved_path: str | None
    reason: str
    candidates: tuple[str, ...] = ()


def normalize_key(value: str) -> str:
    normalized = value.strip().replace("\\", "/")
    if normalized.endswith(".md"):
        normalized = normalized[:-3]
    normalized = normalized.strip("/")
    return normalized.casefold()


def parse_wikilinks(markdown: str) -> list[str]:
    return WIKILINK_RE.findall(markdown)


def clean_link_target(raw_target: str) -> str:
    cleaned = raw_target.split("|", 1)[0]
    cleaned = cleaned.split("#", 1)[0]
    cleaned = cleaned.split("^", 1)[0]
    return cleaned.strip()


def discover_markdown_files(vault_root: Path) -> list[Path]:
    files: list[Path] = []
    for path in vault_root.rglob("*.md"):
        rel_parts = path.relative_to(vault_root).parts
        if any(part.startswith(".") for part in rel_parts):
            continue
        files.append(path)
    files.sort(key=lambda path: path.relative_to(vault_root).as_posix().casefold())
    return files


def build_indexes(vault_root: Path) -> tuple[dict[str, str], dict[str, list[str]]]:
    path_index: dict[str, str] = {}
    title_index: dict[str, list[str]] = defaultdict(list)

    for path in discover_markdown_files(vault_root):
        rel_path = path.relative_to(vault_root).as_posix()
        path_index[normalize_key(rel_path)] = rel_path
        title_index[normalize_key(path.stem)].append(rel_path)

    for title, candidates in title_index.items():
        title_index[title] = sorted(candidates, key=str.casefold)

    return path_index, title_index


def resolve_target(
    target: str,
    path_index: dict[str, str],
    title_index: dict[str, list[str]],
) -> ResolutionResult:
    cleaned = clean_link_target(target)
    if not cleaned:
        return ResolutionResult(raw=target, cleaned=cleaned, resolved_path=None, reason="empty_target")

    normalized = normalize_key(cleaned)

    if "/" in cleaned:
        resolved = path_index.get(normalized)
        if resolved:
            return ResolutionResult(raw=target, cleaned=cleaned, resolved_path=resolved, reason="resolved_by_path")
        return ResolutionResult(raw=target, cleaned=cleaned, resolved_path=None, reason="unresolved_path")

    direct_path = path_index.get(normalized)
    if direct_path:
        return ResolutionResult(raw=target, cleaned=cleaned, resolved_path=direct_path, reason="resolved_by_path")

    title_matches = title_index.get(normalized, [])
    if len(title_matches) == 1:
        return ResolutionResult(
            raw=target,
            cleaned=cleaned,
            resolved_path=title_matches[0],
            reason="resolved_by_title",
        )
    if len(title_matches) > 1:
        return ResolutionResult(
            raw=target,
            cleaned=cleaned,
            resolved_path=None,
            reason="ambiguous_title",
            candidates=tuple(title_matches),
        )
    return ResolutionResult(raw=target, cleaned=cleaned, resolved_path=None, reason="unresolved_title")


def resolve_seed(
    seed_path: str | None,
    seed_title: str | None,
    path_index: dict[str, str],
    title_index: dict[str, list[str]],
) -> tuple[str | None, str | None]:
    if seed_path:
        resolution = resolve_target(seed_path, path_index, title_index)
        if resolution.resolved_path:
            return resolution.resolved_path, None
        if resolution.reason == "ambiguous_title":
            joined = ", ".join(resolution.candidates)
            return None, f"Seed path is ambiguous: {seed_path} -> {joined}"
        return None, f"Seed path could not be resolved: {seed_path}"

    if seed_title:
        matches = title_index.get(normalize_key(seed_title), [])
        if len(matches) == 1:
            return matches[0], None
        if len(matches) > 1:
            joined = ", ".join(matches)
            return None, f"Seed title is ambiguous: {seed_title} -> {joined}"
        return None, f"Seed title could not be resolved: {seed_title}"

    return None, "Provide either --seed-path or --seed-title."


def build_graph(
    vault_root: Path,
    path_index: dict[str, str],
    title_index: dict[str, list[str]],
) -> tuple[dict[str, set[str]], dict[str, set[str]], dict[str, list[ResolutionResult]]]:
    outgoing: dict[str, set[str]] = defaultdict(set)
    incoming: dict[str, set[str]] = defaultdict(set)
    unresolved_links: dict[str, list[ResolutionResult]] = defaultdict(list)

    for rel_path in sorted(path_index.values(), key=str.casefold):
        source_path = vault_root / rel_path
        text = source_path.read_text(encoding="utf-8")
        for raw_link in parse_wikilinks(text):
            resolution = resolve_target(raw_link, path_index, title_index)
            if resolution.resolved_path is None:
                unresolved_links[rel_path].append(resolution)
                continue
            if resolution.resolved_path == rel_path:
                continue
            if resolution.resolved_path in outgoing[rel_path]:
                continue
            outgoing[rel_path].add(resolution.resolved_path)
            incoming[resolution.resolved_path].add(rel_path)

    for rel_path in path_index.values():
        outgoing.setdefault(rel_path, set())
        incoming.setdefault(rel_path, set())

    return outgoing, incoming, unresolved_links


def rank_candidates(
    seed_path: str,
    outgoing: dict[str, set[str]],
    incoming: dict[str, set[str]],
    max_hops: int,
    sparse_threshold: int,
) -> list[dict[str, object]]:
    scores: dict[str, int] = defaultdict(int)
    reasons: dict[str, set[str]] = defaultdict(set)

    direct_neighbors = sorted((outgoing[seed_path] | incoming[seed_path]) - {seed_path}, key=str.casefold)

    for candidate in direct_neighbors:
        if candidate in outgoing[seed_path]:
            scores[candidate] += 100
            reasons[candidate].add("outgoing_link")
        if candidate in incoming[seed_path]:
            scores[candidate] += 100
            reasons[candidate].add("backlink")

    if max_hops >= 2 and len(direct_neighbors) < sparse_threshold:
        for neighbor in direct_neighbors:
            second_hop = (outgoing[neighbor] | incoming[neighbor]) - {seed_path}
            for candidate in second_hop:
                if candidate in direct_neighbors:
                    continue
                scores[candidate] += 10
                reasons[candidate].add(f"two_hop_via:{neighbor}")

    ranked: list[dict[str, object]] = []
    for candidate, score in scores.items():
        ranked.append(
            {
                "path": candidate,
                "score": score,
                "reasons": sorted(reasons[candidate]),
            }
        )

    ranked.sort(key=lambda item: (-int(item["score"]), str(item["path"]).casefold()))
    return ranked


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Return candidate related note paths from an Obsidian-style markdown vault."
    )
    parser.add_argument("--vault-root", required=True, help="Absolute or relative path to the vault root.")
    parser.add_argument("--seed-path", help="Seed note path or resolvable note identifier.")
    parser.add_argument("--seed-title", help="Seed note title when path is not known.")
    parser.add_argument("--limit", type=int, default=10, help="Maximum number of candidate paths to return.")
    parser.add_argument(
        "--max-hops",
        type=int,
        choices=(1, 2),
        default=2,
        help="Graph expansion depth. Default keeps 1-hop retrieval with optional 2-hop fallback.",
    )
    parser.add_argument(
        "--sparse-threshold",
        type=int,
        default=5,
        help="Trigger 2-hop fallback when the direct neighborhood has fewer candidates than this value.",
    )
    parser.add_argument(
        "--format",
        choices=("json", "text"),
        default="json",
        help="Output format. JSON is recommended for skills and automation.",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Include scores, reasons, and unresolved-link counts in the output.",
    )
    return parser.parse_args()


def emit_error(message: str, output_format: str) -> int:
    if output_format == "json":
        print(json.dumps({"error": message}, indent=2))
    else:
        print(f"error: {message}", file=sys.stderr)
    return 1


def main() -> int:
    args = parse_args()
    vault_root = Path(args.vault_root).expanduser().resolve()

    if not vault_root.exists() or not vault_root.is_dir():
        return emit_error(f"Vault root does not exist or is not a directory: {vault_root}", args.format)

    path_index, title_index = build_indexes(vault_root)
    seed_path, error = resolve_seed(args.seed_path, args.seed_title, path_index, title_index)
    if error:
        return emit_error(error, args.format)
    assert seed_path is not None

    outgoing, incoming, unresolved_links = build_graph(vault_root, path_index, title_index)
    ranked = rank_candidates(
        seed_path=seed_path,
        outgoing=outgoing,
        incoming=incoming,
        max_hops=args.max_hops,
        sparse_threshold=max(args.sparse_threshold, 0),
    )
    limited = ranked[: max(args.limit, 0)]

    if args.format == "text":
        for item in limited:
            print(item["path"])
        return 0

    if args.debug:
        payload = {
            "seed_path": seed_path,
            "config": {
                "limit": args.limit,
                "max_hops": args.max_hops,
                "sparse_threshold": args.sparse_threshold,
            },
            "candidates": limited,
            "unresolved_link_count": sum(len(items) for items in unresolved_links.values()),
        }
    else:
        payload = {
            "seed_path": seed_path,
            "candidates": [item["path"] for item in limited],
        }

    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
