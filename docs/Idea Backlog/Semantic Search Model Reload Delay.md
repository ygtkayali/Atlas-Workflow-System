# Semantic Search Model Reload Delay

Status: [[Tags/status-settled]]
Type: [[idea-note]]
Related: [[note-search-skill]]
Created: 05-05-2026
Last Reviewed: 2026-05-12
Priority: [[priority-low]]

---

## Summary

The semantic note-search tool originally reloaded the embedding model on every CLI invocation.

The note embedding cache already avoided re-embedding unchanged files, but it did not avoid model-load latency because each query started a new Python process.

This note is now settled for the current workflow mode: semantic search uses an auto-start warm socket path so repeated queries for the same Atlas project can reuse the loaded model.

## Original Observation

The first run on `Special Image Of My Brain` indexed 412 notes in about 43 seconds.

A cached rerun avoided note re-embedding with `updated: 0`, but still took about 18 seconds because model loading remained part of query execution.

## Current Behavior

Semantic search now supports a lazy auto-start Unix socket mode:

- `--auto-socket` checks for a vault/model-specific socket service.
- If the socket service is already running, the query uses it.
- If no responsive socket exists, the command starts the socket service on demand and waits for it to become ready.
- The first auto-started query still pays the model-load cost.
- Later queries for the same `vault_root` and model reuse the warm service.
- `--no-socket` preserves explicit cold one-off search.
- Manual `--serve-socket` remains available for debugging or explicit long-lived sessions.

The `note-search` skill defaults semantic discovery to this auto-start warm socket path, so normal callers no longer need to manually set up the socket.

## Boundaries

The reliable CLI baseline remains available.

This settlement does not add:

- Codex or Atlas startup preloading,
- a global semantic-search broker,
- idle-timeout or stop commands,
- multi-vault registry behavior,
- or changes to semantic ranking and graph expansion.

## Future Possible Step

A stronger long-term design may be a single local semantic-search broker:

- one process keeps the embedding model loaded globally,
- each request supplies the target `vault_root`,
- the broker refreshes that vault's index as needed,
- the broker handles the query and returns results,
- and lifecycle commands such as `status`, `stop`, cleanup, and idle timeout live in one place.

This would avoid one warm model process per Atlas project and could reduce socket/process pile-up risk.

The broker idea is lower priority now because the current auto-start socket path removes the immediate manual setup pain while preserving the existing CLI fallback.

## Remaining Questions

- Should auto-started socket services gain an explicit idle timeout?
- Should there be a `status` or `cleanup` command for stale socket files?
- Should the future broker replace per-vault socket services or only coordinate them?
