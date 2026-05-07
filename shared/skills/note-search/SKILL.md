---
name: note-search
description: Retrieve bounded note context from a local markdown vault by routing known-seed requests to graph search and concept-level discovery requests to semantic embedding search. Use when Codex needs nearby notes, similar notes, or a query-first context capsule without broad vault reads.
---

# Note Search

Use this skill when you need a bounded, reusable note-retrieval step from a local markdown vault.

Use it for:
- graph search from a known seed note,
- semantic search from a concept, question, or rough description,
- and context capsules that reduce broad manual note reads.

This skill is the stable interface layer for note retrieval.
It does not implement graph traversal, embedding, or ranking itself.
It calls the local retrieval scripts:

- graph search: `/home/yigit-kayali/.codex/tools/local_note-search.py`
- semantic search: `/home/yigit-kayali/.codex/tools/local_note_semantic_search.py`

In an Atlas workflow source checkout, skill-related tool sources live under `shared/tools/`; those sources should stay synchronized with the installed helpers when behavior changes.

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
- `vault_root`
- either `seed_path`, `seed_title`, or `query`

Optional controls:
- `limit`
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

Prefer semantic search over manual `rg` or broad file scanning for concept-level note discovery.
Manual text search remains acceptable for exact strings, filenames, or implementation code checks.

## Graph Call Pattern

Use JSON by default.

```bash
python3 /home/yigit-kayali/.codex/tools/local_note-search.py \
  --vault-root "<vault-root>" \
  --seed-path "<note-path>" \
  --format json
```

When only the note title is known:

```bash
python3 /home/yigit-kayali/.codex/tools/local_note-search.py \
  --vault-root "<vault-root>" \
  --seed-title "<note-title>" \
  --format json
```

Use debug mode only when you need scoring, hop reasons, or unresolved-link diagnostics:

```bash
python3 /home/yigit-kayali/.codex/tools/local_note-search.py \
  --vault-root "<vault-root>" \
  --seed-path "<note-path>" \
  --format json \
  --debug
```

## Semantic Call Pattern

When a warm semantic search service is running, use the fast socket client with plain `python3`:

```bash
python3 /home/yigit-kayali/.codex/tools/local_note_semantic_search.py --vault-root "<vault-root>" --query "<query>" --expand-graph --require-socket --format json
```

Start the warm service in a separate terminal when repeated semantic queries are expected:

```bash
conda run --no-capture-output -n base-ml python /home/yigit-kayali/.codex/tools/local_note_semantic_search.py --vault-root "<vault-root>" --serve-socket --no-refresh
```

Use cold semantic discovery through the `base-ml` conda environment when no service is running:

```bash
conda run --no-capture-output -n base-ml python /home/yigit-kayali/.codex/tools/local_note_semantic_search.py --vault-root "<vault-root>" --query "<query>" --expand-graph --format json
```

Use `--no-refresh` only when the caller explicitly wants to avoid checking changed files:

```bash
conda run --no-capture-output -n base-ml python /home/yigit-kayali/.codex/tools/local_note_semantic_search.py --vault-root "<vault-root>" --query "<query>" --no-refresh --format json
```

Semantic search uses `sentence-transformers/all-MiniLM-L6-v2` and stores a vault-local cache at `.codex-note-search/`.

## Output Handling

Graph JSON output:
- `seed_path`
- `candidates`

Debug JSON output may also include:
- scored candidate objects with `path`, `score`, and `reasons`
- `unresolved_link_count`

Semantic JSON output may include:
- `read_first`
- `graph_expansion`
- `index_status`
- `score`
- `semantic_score`
- `why`

Treat `read_first` as the primary bounded context set and `graph_expansion` as optional adjacent context.

If the script returns an `error`, treat retrieval as failed and surface the reason directly rather than guessing.

## Current Boundary

This skill wraps only the local graph and semantic scripts.

It should not claim support for:
- tag-based retrieval
- BM25
- autonomous context selection beyond the script output

If those are added later, update this skill so callers can keep using the same interface.
