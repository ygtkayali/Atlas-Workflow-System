#!/usr/bin/env python3

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import socket
import stat
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from tempfile import gettempdir
from typing import Any


DEFAULT_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
INDEX_DIR_NAME = ".codex-note-search"
MANIFEST_NAME = "manifest.json"
EMBEDDINGS_NAME = "embeddings.npy"

WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.DOTALL)
LEXICAL_STOPWORDS = {
    "about",
    "after",
    "all",
    "and",
    "are",
    "but",
    "can",
    "does",
    "for",
    "from",
    "has",
    "have",
    "how",
    "into",
    "not",
    "that",
    "the",
    "this",
    "what",
    "when",
    "where",
    "with",
}


@dataclass(frozen=True)
class NoteDocument:
    path: str
    text: str
    file_hash: str
    embedding_text_hash: str
    mtime_ns: int
    size: int
    title: str
    headings: tuple[str, ...]
    links: tuple[str, ...]


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def normalize_key(value: str) -> str:
    normalized = value.strip().replace("\\", "/")
    if normalized.endswith(".md"):
        normalized = normalized[:-3]
    normalized = normalized.strip("/")
    return normalized.casefold()


def clean_link_target(raw_target: str) -> str:
    cleaned = raw_target.split("|", 1)[0]
    cleaned = cleaned.split("#", 1)[0]
    cleaned = cleaned.split("^", 1)[0]
    return cleaned.strip()


def parse_wikilinks(markdown: str) -> list[str]:
    return WIKILINK_RE.findall(markdown)


def discover_markdown_files(vault_root: Path) -> list[Path]:
    files: list[Path] = []
    for path in vault_root.rglob("*.md"):
        rel_parts = path.relative_to(vault_root).parts
        if any(part.startswith(".") for part in rel_parts):
            continue
        files.append(path)
    files.sort(key=lambda item: item.relative_to(vault_root).as_posix().casefold())
    return files


def split_frontmatter(markdown: str) -> tuple[dict[str, str], str]:
    match = FRONTMATTER_RE.match(markdown)
    if not match:
        return {}, markdown

    metadata: dict[str, str] = {}
    raw_frontmatter = match.group(1)
    for line in raw_frontmatter.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip()
    return metadata, markdown[match.end() :]


def extract_headings(markdown: str, limit: int = 12) -> list[str]:
    headings: list[str] = []
    for line in markdown.splitlines():
        match = HEADING_RE.match(line)
        if match:
            headings.append(match.group(2).strip())
        if len(headings) >= limit:
            break
    return headings


def extract_body_excerpt(markdown: str, max_chars: int) -> str:
    lines: list[str] = []
    in_code_block = False
    for raw_line in markdown.splitlines():
        line = raw_line.strip()
        if line.startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block or not line:
            continue
        if line.startswith("#"):
            continue
        lines.append(line)
        if sum(len(item) + 1 for item in lines) >= max_chars:
            break
    excerpt = "\n".join(lines)
    return excerpt[:max_chars].strip()


def build_note_document(vault_root: Path, path: Path, max_body_chars: int) -> NoteDocument:
    rel_path = path.relative_to(vault_root).as_posix()
    raw_text = path.read_text(encoding="utf-8")
    stat = path.stat()
    metadata, body = split_frontmatter(raw_text)
    headings = extract_headings(body)
    links = tuple(clean_link_target(link) for link in parse_wikilinks(raw_text) if clean_link_target(link))
    title = path.stem

    semantic_parts = [
        f"Title: {title}",
        f"Path: {rel_path}",
    ]
    for key in ("Status", "Parent", "Related", "Decisions", "Tasks"):
        value = metadata.get(key)
        if value:
            semantic_parts.append(f"{key}: {value}")
    if headings:
        semantic_parts.append("Headings:\n" + "\n".join(f"- {heading}" for heading in headings))
    excerpt = extract_body_excerpt(body, max_chars=max_body_chars)
    if excerpt:
        semantic_parts.append("Body excerpt:\n" + excerpt)

    embedding_text = "\n\n".join(semantic_parts).strip()
    return NoteDocument(
        path=rel_path,
        text=embedding_text,
        file_hash=sha256_text(raw_text),
        embedding_text_hash=sha256_text(embedding_text),
        mtime_ns=stat.st_mtime_ns,
        size=stat.st_size,
        title=title,
        headings=tuple(headings),
        links=links,
    )


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def import_numpy() -> Any:
    try:
        import numpy as np
    except ImportError as exc:
        raise RuntimeError("Missing dependency: numpy. Install numpy before using semantic note search.") from exc
    return np


def import_sentence_transformer() -> Any:
    try:
        from sentence_transformers import SentenceTransformer
    except ImportError as exc:
        raise RuntimeError(
            "Missing dependency: sentence-transformers. Install it with `pip install sentence-transformers` "
            "or run this script in an environment where it is available."
        ) from exc
    return SentenceTransformer


def load_model(model_name: str) -> Any:
    sentence_transformer = import_sentence_transformer()
    return sentence_transformer(model_name)


def encode_texts(model: Any, texts: list[str]) -> Any:
    return model.encode(texts, normalize_embeddings=True, show_progress_bar=False)


def read_index(vault_root: Path) -> tuple[Path, dict[str, Any], Any | None]:
    np = import_numpy()
    index_dir = vault_root / INDEX_DIR_NAME
    manifest_path = index_dir / MANIFEST_NAME
    embeddings_path = index_dir / EMBEDDINGS_NAME
    manifest = load_json(
        manifest_path,
        {
            "version": 1,
            "created_at": utc_now(),
            "updated_at": None,
            "model": None,
            "notes": {},
        },
    )
    embeddings = np.load(embeddings_path) if embeddings_path.exists() else None
    return index_dir, manifest, embeddings


def note_needs_embedding(entry: dict[str, Any] | None, note: NoteDocument, model_name: str) -> str | None:
    if entry is None:
        return "missing"
    if entry.get("embedding_model") != model_name:
        return "model_stale"
    if entry.get("embedding_text_hash") != note.embedding_text_hash:
        return "stale"
    if entry.get("status") == "error":
        return "error"
    return None


def build_or_refresh_index(
    vault_root: Path,
    model_name: str,
    reindex: str,
    max_body_chars: int,
    model: Any | None = None,
) -> tuple[dict[str, Any], Any, dict[str, int]]:
    np = import_numpy()
    index_dir, manifest, existing_embeddings = read_index(vault_root)
    index_dir.mkdir(parents=True, exist_ok=True)

    note_paths = discover_markdown_files(vault_root)
    documents = [build_note_document(vault_root, path, max_body_chars=max_body_chars) for path in note_paths]
    by_path = {document.path: document for document in documents}
    old_notes: dict[str, dict[str, Any]] = manifest.get("notes", {})

    previous_vectors: dict[str, Any] = {}
    if existing_embeddings is not None:
        for path, entry in old_notes.items():
            row = entry.get("row")
            if isinstance(row, int) and 0 <= row < len(existing_embeddings):
                previous_vectors[path] = existing_embeddings[row]

    refresh_reasons: dict[str, str] = {}
    for document in documents:
        entry = old_notes.get(document.path)
        reason = "forced" if reindex == "all" else note_needs_embedding(entry, document, model_name)
        if reason:
            refresh_reasons[document.path] = reason

    if refresh_reasons:
        active_model = model if model is not None else load_model(model_name)
        refresh_paths = sorted(refresh_reasons, key=str.casefold)
        vectors = encode_texts(active_model, [by_path[path].text for path in refresh_paths])
        for path, vector in zip(refresh_paths, vectors):
            previous_vectors[path] = vector

    new_notes: dict[str, dict[str, Any]] = {}
    vectors_in_order: list[Any] = []
    for row, document in enumerate(sorted(documents, key=lambda item: item.path.casefold())):
        vector = previous_vectors.get(document.path)
        if vector is None:
            # This can happen when --no-refresh is used through search_index without first building.
            continue
        vectors_in_order.append(vector)
        old_entry = old_notes.get(document.path, {})
        new_notes[document.path] = {
            "path": document.path,
            "mtime_ns": document.mtime_ns,
            "size": document.size,
            "file_hash": document.file_hash,
            "embedding_text_hash": document.embedding_text_hash,
            "embedding_model": model_name,
            "row": row,
            "status": "fresh",
            "indexed_at": utc_now() if document.path in refresh_reasons else old_entry.get("indexed_at", utc_now()),
            "title": document.title,
            "headings": list(document.headings),
        }

    if vectors_in_order:
        embedding_matrix = np.vstack(vectors_in_order)
    else:
        embedding_matrix = np.empty((0, 0), dtype="float32")

    manifest = {
        "version": 1,
        "created_at": manifest.get("created_at", utc_now()),
        "updated_at": utc_now(),
        "model": model_name,
        "notes": new_notes,
    }
    save_json(index_dir / MANIFEST_NAME, manifest)
    np.save(index_dir / EMBEDDINGS_NAME, embedding_matrix)

    status_counts = Counter({"fresh": len(new_notes), "updated": len(refresh_reasons)})
    deleted_count = len(set(old_notes) - set(by_path))
    if deleted_count:
        status_counts["deleted"] = deleted_count
    return manifest, embedding_matrix, dict(status_counts)


def load_existing_index(vault_root: Path, model_name: str) -> tuple[dict[str, Any], Any]:
    _, manifest, embeddings = read_index(vault_root)
    if embeddings is None or not manifest.get("notes"):
        raise RuntimeError("Semantic note index does not exist yet. Run without --no-refresh or use --reindex changed-only.")
    if manifest.get("model") != model_name:
        raise RuntimeError("Semantic note index was built with a different model. Re-run without --no-refresh.")
    return manifest, embeddings


def lexical_boost(query: str, entry: dict[str, Any]) -> tuple[float, list[str]]:
    query_terms = {
        term
        for term in re.findall(r"[a-zA-Z0-9_]+", query.casefold())
        if len(term) >= 3 and term not in LEXICAL_STOPWORDS
    }
    if not query_terms:
        return 0.0, []
    haystack_parts = [entry.get("title", ""), entry.get("path", "")]
    haystack_parts.extend(entry.get("headings", []))
    haystack = " ".join(haystack_parts).casefold()
    hits = sorted(term for term in query_terms if term in haystack)
    if not hits:
        return 0.0, []
    return min(0.08, 0.02 * len(hits)), [f"lexical_match:{term}" for term in hits[:4]]


def build_graph(vault_root: Path) -> tuple[dict[str, set[str]], dict[str, set[str]]]:
    markdown_files = discover_markdown_files(vault_root)
    path_index = {normalize_key(path.relative_to(vault_root).as_posix()): path.relative_to(vault_root).as_posix() for path in markdown_files}
    title_index: dict[str, list[str]] = defaultdict(list)
    for path in markdown_files:
        title_index[normalize_key(path.stem)].append(path.relative_to(vault_root).as_posix())

    outgoing: dict[str, set[str]] = defaultdict(set)
    incoming: dict[str, set[str]] = defaultdict(set)
    for path in markdown_files:
        rel_path = path.relative_to(vault_root).as_posix()
        text = path.read_text(encoding="utf-8")
        for raw_link in parse_wikilinks(text):
            cleaned = clean_link_target(raw_link)
            normalized = normalize_key(cleaned)
            resolved = path_index.get(normalized)
            if resolved is None and "/" not in cleaned:
                matches = title_index.get(normalized, [])
                if len(matches) == 1:
                    resolved = matches[0]
            if resolved and resolved != rel_path:
                outgoing[rel_path].add(resolved)
                incoming[resolved].add(rel_path)
    return outgoing, incoming


def semantic_search(
    vault_root: Path,
    query: str,
    model_name: str,
    limit: int,
    context_limit: int,
    expand_graph: bool,
    no_refresh: bool,
    max_body_chars: int,
) -> dict[str, Any]:
    np = import_numpy()
    if no_refresh:
        manifest, embeddings = load_existing_index(vault_root, model_name)
        index_status = {"fresh": len(manifest.get("notes", {})), "updated": 0}
    else:
        manifest, embeddings, index_status = build_or_refresh_index(
            vault_root=vault_root,
            model_name=model_name,
            reindex="changed-only",
            max_body_chars=max_body_chars,
        )

    model = load_model(model_name)
    return semantic_search_prepared(
        vault_root=vault_root,
        query=query,
        model_name=model_name,
        limit=limit,
        context_limit=context_limit,
        expand_graph=expand_graph,
        manifest=manifest,
        embeddings=embeddings,
        model=model,
        index_status=index_status,
    )


def semantic_search_prepared(
    vault_root: Path,
    query: str,
    model_name: str,
    limit: int,
    context_limit: int,
    expand_graph: bool,
    manifest: dict[str, Any],
    embeddings: Any,
    model: Any,
    index_status: dict[str, int],
) -> dict[str, Any]:
    if len(embeddings) == 0:
        return {
            "query": query,
            "mode": "semantic_context",
            "index_status": index_status,
            "read_first": [],
            "graph_expansion": [],
            "warnings": ["semantic index is empty"],
        }

    query_vector = encode_texts(model, [query])[0]
    similarities = embeddings @ query_vector

    notes_by_row = sorted(manifest["notes"].values(), key=lambda item: int(item["row"]))
    candidates: list[dict[str, Any]] = []
    for row, entry in enumerate(notes_by_row):
        semantic_score = float(similarities[row])
        boost, boost_reasons = lexical_boost(query, entry)
        score = semantic_score + boost
        reasons = ["semantic_match"]
        reasons.extend(boost_reasons)
        candidates.append(
            {
                "path": entry["path"],
                "score": round(score, 4),
                "semantic_score": round(semantic_score, 4),
                "why": reasons,
            }
        )
    candidates.sort(key=lambda item: (-float(item["score"]), str(item["path"]).casefold()))
    read_first = candidates[: max(limit, 0)]

    graph_expansion: list[dict[str, Any]] = []
    if expand_graph and read_first:
        outgoing, incoming = build_graph(vault_root)
        seen = {item["path"] for item in read_first}
        for hit in read_first[: max(context_limit, 0)]:
            path = hit["path"]
            neighbors = sorted((outgoing[path] | incoming[path]) - seen, key=str.casefold)
            for neighbor in neighbors:
                reasons = []
                if neighbor in outgoing[path]:
                    reasons.append(f"linked_from_top_hit:{path}")
                if neighbor in incoming[path]:
                    reasons.append(f"backlinks_to_top_hit:{path}")
                graph_expansion.append({"path": neighbor, "why": reasons})
                seen.add(neighbor)
                if len(graph_expansion) >= context_limit:
                    break
            if len(graph_expansion) >= context_limit:
                break

    return {
        "query": query,
        "mode": "semantic_context",
        "model": model_name,
        "index_status": index_status,
        "read_first": read_first,
        "graph_expansion": graph_expansion,
        "warnings": [],
    }


def default_socket_path(vault_root: Path, model_name: str) -> Path:
    key = sha256_text(f"{vault_root.as_posix()}\n{model_name}")[:16]
    return Path(gettempdir()) / f"codex-note-semantic-search-{key}.sock"


def resolve_socket_path(vault_root: Path, model_name: str, socket_path: str | None) -> Path:
    if socket_path:
        return Path(socket_path).expanduser()
    env_socket = os.environ.get("CODEX_NOTE_SEARCH_SOCKET")
    if env_socket:
        return Path(env_socket).expanduser()
    return default_socket_path(vault_root, model_name)


def socket_available(socket_path: Path) -> bool:
    return socket_path.exists() and stat_is_socket(socket_path)


def stat_is_socket(path: Path) -> bool:
    try:
        return stat.S_ISSOCK(path.stat().st_mode)
    except OSError:
        return False


def request_socket_search(socket_path: Path, request: dict[str, Any], timeout: float) -> dict[str, Any]:
    try:
        with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as client:
            client.settimeout(timeout)
            client.connect(socket_path.as_posix())
            client.sendall(json.dumps(request).encode("utf-8") + b"\n")
            chunks: list[bytes] = []
            while True:
                chunk = client.recv(65536)
                if not chunk:
                    break
                chunks.append(chunk)
    except OSError as exc:
        raise RuntimeError(f"semantic search socket request failed: {exc}") from exc

    raw_response = b"".join(chunks).decode("utf-8").strip()
    if not raw_response:
        raise RuntimeError("semantic search socket returned an empty response")
    response = json.loads(raw_response)
    if "error" in response:
        raise RuntimeError(str(response["error"]))
    return response


def serve_socket(
    vault_root: Path,
    socket_path: Path,
    model_name: str,
    no_refresh: bool,
    max_body_chars: int,
) -> int:
    if socket_path.exists():
        if socket_available(socket_path):
            socket_path.unlink()
        else:
            return emit_error(f"Socket path exists and is not a socket: {socket_path}", "text")

    if no_refresh:
        manifest, embeddings = load_existing_index(vault_root, model_name)
        index_status = {"fresh": len(manifest.get("notes", {})), "updated": 0}
    else:
        manifest, embeddings, index_status = build_or_refresh_index(
            vault_root=vault_root,
            model_name=model_name,
            reindex="changed-only",
            max_body_chars=max(max_body_chars, 0),
        )
    model = load_model(model_name)

    socket_path.parent.mkdir(parents=True, exist_ok=True)
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as server:
        server.bind(socket_path.as_posix())
        server.listen(16)
        print(
            json.dumps(
                {
                    "mode": "serve_socket",
                    "socket": socket_path.as_posix(),
                    "vault_root": vault_root.as_posix(),
                    "model": model_name,
                    "index_status": index_status,
                },
                indent=2,
            ),
            file=sys.stderr,
            flush=True,
        )
        try:
            while True:
                connection, _address = server.accept()
                with connection:
                    request_bytes = connection.recv(65536)
                    try:
                        request = json.loads(request_bytes.decode("utf-8"))
                        query = str(request.get("query", "")).strip()
                        if not query:
                            raise RuntimeError("request missing query")
                        manifest, embeddings, index_status = build_or_refresh_index(
                            vault_root=vault_root,
                            model_name=model_name,
                            reindex="changed-only",
                            max_body_chars=max(max_body_chars, 0),
                            model=model,
                        )
                        payload = semantic_search_prepared(
                            vault_root=vault_root,
                            query=query,
                            model_name=model_name,
                            limit=int(request.get("limit", 10)),
                            context_limit=int(request.get("context_limit", 5)),
                            expand_graph=bool(request.get("expand_graph", False)),
                            manifest=manifest,
                            embeddings=embeddings,
                            model=model,
                            index_status=index_status,
                        )
                    except Exception as exc:  # Keep the service alive on malformed requests.
                        payload = {"error": str(exc)}
                    connection.sendall(json.dumps(payload).encode("utf-8") + b"\n")
        finally:
            try:
                socket_path.unlink()
            except OSError:
                pass
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Semantic query search for a local markdown note vault.")
    parser.add_argument("--vault-root", required=True, help="Absolute or relative path to the vault root.")
    parser.add_argument("--query", help="Concept or question to search for.")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"SentenceTransformer model. Default: {DEFAULT_MODEL}.")
    parser.add_argument("--limit", type=int, default=10, help="Maximum semantic matches to return.")
    parser.add_argument("--context-limit", type=int, default=5, help="Maximum graph-expanded context notes to return.")
    parser.add_argument("--expand-graph", action="store_true", help="Add graph neighbors around top semantic hits.")
    parser.add_argument("--no-refresh", action="store_true", help="Use the existing index without refreshing stale notes.")
    parser.add_argument("--serve-socket", action="store_true", help="Run a long-lived Unix socket service with the model loaded.")
    parser.add_argument("--socket", help="Unix socket path for service mode or client queries. Defaults to a vault/model-specific path in /tmp.")
    parser.add_argument("--no-socket", action="store_true", help="Skip the warm socket client path and run the query in this process.")
    parser.add_argument("--require-socket", action="store_true", help="Fail instead of falling back to cold in-process search when no socket service is available.")
    parser.add_argument("--socket-timeout", type=float, default=5.0, help="Seconds to wait for a semantic search socket response.")
    parser.add_argument("--max-body-chars", type=int, default=2500, help="Maximum body excerpt chars to embed per note.")
    parser.add_argument(
        "--reindex",
        choices=("all", "changed-only"),
        help="Refresh the semantic index and exit unless --query is also supplied.",
    )
    parser.add_argument("--format", choices=("json", "text"), default="json")
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

    try:
        socket_path = resolve_socket_path(vault_root, args.model, args.socket)
        if args.serve_socket:
            return serve_socket(
                vault_root=vault_root,
                socket_path=socket_path,
                model_name=args.model,
                no_refresh=args.no_refresh,
                max_body_chars=max(args.max_body_chars, 0),
            )

        if args.reindex:
            manifest, _embeddings, index_status = build_or_refresh_index(
                vault_root=vault_root,
                model_name=args.model,
                reindex=args.reindex,
                max_body_chars=max(args.max_body_chars, 0),
            )
            payload: dict[str, Any] = {
                "mode": "reindex",
                "model": args.model,
                "index_status": index_status,
                "note_count": len(manifest.get("notes", {})),
            }
            if not args.query:
                print(json.dumps(payload, indent=2) if args.format == "json" else payload)
                return 0

        if not args.query:
            return emit_error("Provide --query or --reindex.", args.format)

        if not args.no_socket and not args.reindex and socket_available(socket_path):
            payload = request_socket_search(
                socket_path=socket_path,
                request={
                    "query": args.query,
                    "limit": args.limit,
                    "context_limit": args.context_limit,
                    "expand_graph": args.expand_graph,
                },
                timeout=max(args.socket_timeout, 0.1),
            )
            if args.format == "text":
                for item in payload.get("read_first", []):
                    print(item["path"])
                return 0
            print(json.dumps(payload, indent=2))
            return 0

        if not args.no_socket and not args.reindex and (args.require_socket or args.socket or os.environ.get("CODEX_NOTE_SEARCH_SOCKET")):
            return emit_error(f"Semantic search socket is not available: {socket_path}", args.format)

        payload = semantic_search(
            vault_root=vault_root,
            query=args.query,
            model_name=args.model,
            limit=args.limit,
            context_limit=args.context_limit,
            expand_graph=args.expand_graph,
            no_refresh=args.no_refresh,
            max_body_chars=max(args.max_body_chars, 0),
        )
    except RuntimeError as exc:
        return emit_error(str(exc), args.format)

    if args.format == "text":
        for item in payload.get("read_first", []):
            print(item["path"])
        return 0

    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
