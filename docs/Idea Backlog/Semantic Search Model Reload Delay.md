# Semantic Search Model Reload Delay

Status: [[Tags/status-draft]]
Type: [[idea-note]]
Related: [[note-search-skill]]
Created: 05-05-2026
Priority:[[priority-high]] 

---

## Summary

The semantic note-search script currently reloads the embedding model every time the command is run.

The note embedding cache avoids re-embedding unchanged files, but it does not avoid model-load latency because each CLI invocation starts a new Python process.

## Current Observation

The first run on `Special Image Of My Brain` indexed 412 notes in about 43 seconds.

A cached rerun avoided note re-embedding with `updated: 0`, but still took about 18 seconds because model loading remained part of query execution.

## Candidate Directions

- Keep the current CLI as the simple reliable baseline.
- Add a long-running stdin mode that loads the model once and accepts repeated queries line by line.
- Add a small local daemon or server that keeps the model loaded and receives search requests through localhost or a Unix socket.
- Add a client wrapper that talks to the daemon while preserving the current command-line interface for fallback.
- Consider preloading the service when Codex starts only after the long-running mode proves useful.

## Questions

- Is model-load latency painful enough in real use to justify a persistent process?
- Should the first improvement be `--serve-stdin` rather than a daemon?
- How should a long-running process handle multiple vault roots?
- Should it keep one model loaded and multiple vault indexes cached?
- What shutdown and stale-index behavior should be expected?

## Boundary

This is an optimization idea, not a required change for semantic search v1.
The current CLI remains the reliable baseline.
