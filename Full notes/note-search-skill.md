# Note Search Skill

Status: [[status-settled]]
Parent: [[Agent Roles Hub]]
Related: [[Local Note Search Script]], [[Semantic Search Model Reload Delay]]
Created: 18-04-2026
Last Reviewed: 2026-05-06
Source:
Decisions:
Dependencies:
Tasks:

---

## Summary

`Note Search Skill` is the shared note-retrieval interface intended for reuse across other Codex skills.

Its current role is to provide one stable skill entry point for:
- graph search from a known seed note
- semantic search from a concept, question, or rough description
- bounded context capsules that reduce broad manual note reads

## Details

This skill does not implement retrieval logic itself.

Instead, it wraps local retrieval scripts:

- graph search: `tools/local_note_search.py` or `/home/yigit-kayali/.codex/tools/local_note_search.py`
- semantic search: `tools/local_note_semantic_search.py` and `/home/yigit-kayali/.codex/tools/local_note_semantic_search.py`

Current expectations:
- accept the retrieval need from another skill
- choose graph search when a known seed note path or title is supplied
- choose semantic search when the prompt asks whether something exists, asks for similar notes, or provides only a concept without a seed note
- call the appropriate local script
- return candidate note paths or a semantic context capsule from the script result
- let calling skills consume retrieval results instead of reimplementing separate context search behavior
- keep the calling surface stable even if the underlying search behavior evolves later

This note should treat the skill as the interface layer, while the scripts remain the retrieval engines.

That separation supports:
- easier maintenance
- one controlled integration point for other skills
- easier future upgrades to search behavior without rewriting every caller

## Boundaries

The current version of `Note Search Skill` should not:
- own ranking or graph traversal logic directly
- own embedding or semantic-ranking logic directly
- broaden into a general autonomous context-selection system
- modify notes automatically
- let caller skills bypass it with ad hoc manual note discovery when semantic search is the better fit

## Current Dependency

The current skill depends on:

- `tools/local_note_search.py`
- `/home/yigit-kayali/.codex/tools/local_note_search.py`
- `tools/local_note_semantic_search.py`
- `/home/yigit-kayali/.codex/tools/local_note_semantic_search.py`

Graph search is path or title seeded.
Semantic search uses `sentence-transformers/all-MiniLM-L6-v2` through the `base-ml` conda environment and stores a vault-local cache at `.codex-note-search/`.

If the script interface changes later, the skill should absorb that change so other skills can continue using one stable search entry point.

## Ownership Boundary

Repo-owned:
- `tools/local_note_search.py`
- `tools/local_note_semantic_search.py`
- durable notes that define graph and semantic search routing expectations

Codex-local owned:
- `/home/yigit-kayali/.codex/tools/local_note_semantic_search.py`
- `/home/yigit-kayali/.codex/skills/note-search/SKILL.md`

When semantic search behavior changes, update the installed skill and update repo notes only when the workflow contract changes.
The repo-local semantic script copy is intentional; keep it synchronized with the installed helper when behavior changes.

## Routing Rules

Use graph search when:
- a specific seed note path is known
- a specific seed note title is known
- nearby direct links or backlinks are the target

Use semantic search when:
- the user asks whether a topic already exists in the vault
- the user asks what similar notes exist
- the prompt gives only a concept, question, or rough subject
- a role needs a bounded context capsule before deciding which notes to read

Prefer semantic search over manual `rg` or broad file scanning for concept-level note discovery.
Manual text search remains acceptable for exact strings, filenames, or implementation code checks.

## Semantic Usage

Use this command pattern for semantic discovery:

```bash
conda run --no-capture-output -n base-ml python /home/yigit-kayali/.codex/tools/local_note_semantic_search.py --vault-root "<vault-root>" --query "<query>" --expand-graph --format json
```

Use `--no-refresh` only when the caller explicitly wants to avoid checking changed files:

```bash
conda run --no-capture-output -n base-ml python /home/yigit-kayali/.codex/tools/local_note_semantic_search.py --vault-root "<vault-root>" --query "<query>" --no-refresh --format json
```

Semantic output may include:
- `read_first`
- `graph_expansion`
- `index_status`
- `score`
- `semantic_score`
- `why`

Calling skills should treat `read_first` as the primary bounded context set and `graph_expansion` as optional adjacent context.

## Open Questions

- Should the semantic script gain a long-running mode or local server to avoid repeated model-load latency?
- Should semantic results be benchmarked against a fixed set of real vault queries?
- Should query routing eventually support multi-vault search through a registry while keeping per-vault indexes as the default?
