---
name: note-search
description: Use when bounded note retrieval is needed — graph search from a known seed note, or semantic search from a concept — without broad vault reads.
---

# Note Search

Use this skill when you need a bounded, reusable note-retrieval step from a local markdown vault.

Use it for:
- graph search from a known seed note,
- semantic search from a concept, question, or rough description,
- and context capsules that reduce broad manual note reads.

This skill is the stable interface layer for note retrieval.
It does not implement graph traversal, embedding, or ranking itself.
It calls the local retrieval scripts resolved from platform config.

## Tool Path Resolution

Before calling either script, resolve `tools_root` from `platforms.yaml`:

1. Read `platforms.yaml` from the atlas source checkout.
2. Identify the current platform: `codex` when running under Codex, `claude` when running under Claude Code.
3. Read `tools_root` for that platform entry.
4. Use `<tools_root>/local_note_search.py` for graph search and `<tools_root>/local_note_semantic_search.py` for semantic search.

Never hardcode `~/.codex/tools/` or any platform-specific prefix directly in calls.

In an Atlas workflow source checkout, skill-related tool sources live under `shared/tools/`; those sources should stay synchronized with the installed helpers when behavior changes.

## vault_root Resolution

When `vault_root` is not supplied by the caller:

1. Read `atlas.yaml` from the repository root.
2. Use `vault.path` as the vault root, resolved relative to the repository root.

## Responsibilities

Do:
- use this skill as the single retrieval interface,
- choose graph search when a known seed note path or title is supplied,
- choose semantic search when the prompt asks whether something exists, asks for similar notes, or provides only a concept without a seed note,
- request JSON output for automation or follow-on reasoning,
- return candidate note paths or a semantic context capsule from the script result,
- let calling skills consume retrieval results rather than reimplementing separate context search behavior,
- keep the calling surface stable even if the scripts evolve later.

Do not:
- reimplement note-graph traversal in the skill,
- reimplement semantic ranking or embedding in the skill,
- silently broaden retrieval beyond the script contracts,
- modify notes automatically,
- treat debug output as normal retrieval output unless diagnostics are needed,
- let caller skills bypass this skill with ad hoc manual note discovery when semantic search is the better fit.

## Required Inputs

Provide:
- either `seed_path`, `seed_title`, or `query`

`vault_root` is optional; resolve from `atlas.yaml` when not supplied.

Optional controls:
- `limit` (default: 10)
- `max_hops`
- `sparse_threshold`
- `debug`
- `expand_graph`
- `no_refresh`

## Routing Rules

Use graph search when:
- a specific seed note path is known,
- a specific seed note title is known,
- nearby direct links or backlinks are the target.

Use semantic search when:
- the user asks whether a topic already exists in the vault,
- the user asks what similar notes exist,
- the prompt gives only a concept, question, or rough subject,
- a role needs a bounded context capsule before deciding which notes to read.

Fallback rule: if graph search by title returns no match, fall back to a semantic query using that title as the query string rather than failing.

Prefer semantic search over manual `rg` or broad file scanning for concept-level note discovery.
Manual text search remains acceptable for exact strings, filenames, or implementation code checks.

## Graph Call Pattern

```bash
python3 <tools_root>/local_note_search.py \
  --vault-root "<vault-root>" \
  --seed-path "<note-path>" \
  --format json
```

When only the note title is known:

```bash
python3 <tools_root>/local_note_search.py \
  --vault-root "<vault-root>" \
  --seed-title "<note-title>" \
  --format json
```

Use debug mode only when scoring, hop reasons, or unresolved-link diagnostics are needed:

```bash
python3 <tools_root>/local_note_search.py \
  --vault-root "<vault-root>" \
  --seed-path "<note-path>" \
  --format json \
  --debug
```

## Semantic Call Pattern

Default to the auto-start warm socket path for semantic search.

**Warm auto-start (default):** use this for normal semantic discovery. It reuses an existing vault/model socket service, or starts one on demand before running the query.

```bash
conda run --no-capture-output -n base-ml \
  python <tools_root>/local_note_semantic_search.py \
  --vault-root "<vault-root>" \
  --query "<query>" \
  --expand-graph \
  --auto-socket \
  --format json
```

**Cold fallback:** use when auto-start fails and the caller explicitly accepts model-load latency for a one-off query.

```bash
conda run --no-capture-output -n base-ml \
  python <tools_root>/local_note_semantic_search.py \
  --vault-root "<vault-root>" \
  --query "<query>" \
  --expand-graph \
  --no-socket \
  --format json
```

Manual service startup remains available for debugging or explicit long-lived sessions, but normal callers should not require it:

```bash
conda run --no-capture-output -n base-ml \
  python <tools_root>/local_note_semantic_search.py \
  --vault-root "<vault-root>" \
  --serve-socket
```

Semantic search uses `sentence-transformers/all-MiniLM-L6-v2` and stores a vault-local cache at `.codex-note-search/`.

### Refresh behavior

Refresh is the default: each query checks for changed files and updates the index before searching.
Use `--no-refresh` only when the caller explicitly wants to skip index updates for speed.

### Result size

Default limit is 10 results. If results would exceed roughly 4 000 tokens of context, truncate to the top results that fit rather than returning the full set. Surface the truncation count to the caller.

## Output Handling

Graph search returns `seed_path` and `candidates`.
Semantic search returns `read_first` (primary bounded context set) and optionally `graph_expansion` (adjacent context).

Treat `read_first` as the primary set. `graph_expansion` is optional.

If the script returns an `error`, treat retrieval as failed and surface the reason directly rather than guessing.

## Current Boundary

This skill wraps only the local graph and semantic scripts.

It should not claim support for:
- tag-based retrieval
- BM25
- autonomous context selection beyond the script output

If those are added later, update this skill so callers can keep using the same interface.
