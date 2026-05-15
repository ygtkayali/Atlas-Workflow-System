---
name: note-search
description: >
  MANDATORY retrieval interface for any markdown vault note lookup.
  Use this skill — never grep, ls, find, or manual directory listing — whenever:
  a note path, title, or topic is mentioned; the user asks what notes exist on a subject;
  a role needs context before reading or editing notes; a concept needs to be discovered
  in the vault; backlinks or linked notes are needed; or any search over the vault is required.
  Skipping this skill and using grep/ls/find instead causes catastrophic context bloat in
  large vaults. Even a simple "do I have notes on X?" MUST go through this skill.
---

# Note Search

## STOP

Never use `ls`, `find`, `grep`, or manual directory listing to discover or retrieve notes.

These commands return raw filesystem output. In a large vault they can return hundreds of file paths and bloat context.
This skill exists to replace them.

The only acceptable exceptions:
- checking whether a specific known file path exists with `test -f`
- searching for an exact code string or implementation detail inside a file that is already open

Everything else goes through this skill.

## Quick-Start Decision Table

| Situation | Mode | Script |
| --- | --- | --- |
| You have a seed note path or title | graph | `local_note_search.py` |
| You have a concept, topic, or question | hybrid | `local_note_semantic_search.py --search-mode hybrid` |
| You want BM25-style keyword match without model load | keyword | `local_note_semantic_search.py --search-mode keyword` |
| Caller explicitly needs pure semantic scoring | semantic | `local_note_semantic_search.py --search-mode semantic` |
| Graph search by title returned nothing | fallback to hybrid using that title as the query | |

Default to hybrid for concept-level discovery.
Use graph only when a concrete seed note is known.

## Step 1: Resolve Paths Before Every Call

### `vault_root`

If `vault_root` is not supplied by the caller:

1. Read `atlas.yaml` from the repository root.
2. Use `vault.path`, resolved relative to the repository root.

### `tools_root`

Resolve installed tool paths from both project config and Atlas platform config:

1. Read `atlas.yaml` from the repository root.
2. Read `atlas.platforms`.
3. Determine the target platform:
   - if `atlas.platforms` has exactly one entry, use that platform
   - if `atlas.platforms` has multiple entries and the current runtime platform is one of them, use the current runtime platform
   - if the current runtime platform is not listed, or the target platform cannot be determined safely, stop and surface the mismatch instead of guessing
4. Read `platforms.yaml` from the Atlas source checkout.
5. Read `tools_root` for the chosen platform entry.
6. Use `<tools_root>/local_note_search.py` for graph search and `<tools_root>/local_note_semantic_search.py` for hybrid, semantic, and keyword search.

Never hardcode `~/.codex/tools/`, `~/.claude/tools/`, `shared/tools/`, or any other platform-specific prefix directly in skill calls.

## Step 2: Call The Right Script

### Graph Search

Use when a seed note path or title is known.

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

Optional graph controls:
- `--limit`
- `--max-hops`
- `--sparse-threshold`
- `--debug`

### Hybrid Search

Default for concept discovery.

Warm auto-start path:

```bash
conda run --no-capture-output -n base-ml \
  python <tools_root>/local_note_semantic_search.py \
  --vault-root "<vault-root>" \
  --query "<query>" \
  --search-mode hybrid \
  --expand-graph \
  --auto-socket \
  --format json
```

Cold fallback when one-off latency is acceptable:

```bash
conda run --no-capture-output -n base-ml \
  python <tools_root>/local_note_semantic_search.py \
  --vault-root "<vault-root>" \
  --query "<query>" \
  --search-mode hybrid \
  --expand-graph \
  --no-socket \
  --format json
```

### Keyword Search

Use when the caller wants local BM25-style retrieval without model load.

```bash
python <tools_root>/local_note_semantic_search.py \
  --vault-root "<vault-root>" \
  --query "<query>" \
  --search-mode keyword \
  --expand-graph \
  --format json
```

### Semantic-Only Search

Use only when the caller explicitly wants pure semantic scoring behavior.

```bash
conda run --no-capture-output -n base-ml \
  python <tools_root>/local_note_semantic_search.py \
  --vault-root "<vault-root>" \
  --query "<query>" \
  --search-mode semantic \
  --expand-graph \
  --auto-socket \
  --format json
```

Optional semantic-script controls:
- `--limit`
- `--context-limit`
- `--no-refresh`
- `--socket`
- `--socket-timeout`
- `--socket-start-timeout`
- `--max-body-chars`

Manual `--serve-socket` is for debugging only.
Normal callers should use `--auto-socket`.

## Step 3: Handle The Output

### Graph Results

Fields:
- `seed_path`
- `candidates`

### Hybrid, Semantic, And Keyword Results

Primary fields:
- `read_first`
- `graph_expansion`

Score components when available:
- `semantic_score`
- `keyword_score`
- `graph_score`
- `tag_score`
- `score`
- `why`

Rules:
- treat `read_first` as the primary candidate set
- treat `graph_expansion` as supplemental adjacent context
- if results would exceed roughly 4,000 tokens of context, truncate to the top-fitting results and surface that truncation
- if the script returns an `error`, surface it directly and do not guess
- treat tags as filters and facets rather than plain keyword matches

### Fallback Rule

If graph search by title returns no match, rerun as a hybrid query using that title as the query string.
Do not fail at the graph step.

## Operational Notes

- Refresh is on by default. Use `--no-refresh` only when the caller explicitly wants speed over freshness.
- Result limits come from the script defaults unless the caller passes `--limit`.
- Hybrid and semantic search use `sentence-transformers/all-MiniLM-L6-v2` and a vault-local cache at `.codex-note-search/`.
- Keyword mode uses local markdown parsing and BM25-style scoring only.
- This skill does not modify notes. It returns candidate paths and bounded context for the caller to use.

## Boundaries

This skill is the stable retrieval interface.
It does not implement graph traversal, embedding, or ranking itself.

Caller skills should:
- use this skill as the single note-retrieval interface
- consume returned candidate paths or context capsules
- avoid reimplementing separate discovery logic

Caller skills should not:
- bypass this skill with ad hoc manual vault discovery
- broaden retrieval beyond the script contracts
- treat retrieval output as permission to mutate notes
