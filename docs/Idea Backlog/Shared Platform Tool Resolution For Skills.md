# Shared Platform Tool Resolution For Skills

Status: [[Tags/status-draft]]
Type: [[idea-note]]
Related: [[note-search-skill]], [[Local Note Search Script]], [[Tool Policy]]
Created: 2026-05-15
Last Reviewed: 2026-05-15
Priority: [[docs/Tags/priority-mid|priority-mid]]

---

## Idea

Atlas skills and tool wrappers should separate platform-specific dependency details from skill behavior more cleanly.

The current pattern still leaks platform assumptions into some skill guidance and command examples. A visible example is the Codex-local dependency in semantic note-search command patterns such as `~/.codex/tools/local_note_semantic_search.py`.

The system may need one shared script or resolution layer that can generalize tool lookup for all skills instead of repeating platform-aware command construction inside each skill.

## Why This Matters

Mode behavior should stay portable across supported platforms.

When a skill embeds platform-specific paths directly:

- the skill becomes harder to reuse under another platform
- repo notes and installed skills can drift in different directions
- shared tooling changes require edits in many places
- it becomes less clear whether the source of truth is the skill text, the repo tool source, or the installed helper path

This is especially visible for shared tooling such as note search, where the skill is supposed to be the stable interface and the scripts are supposed to be the implementation layer.

## Current Problem Shape

There are at least three layers involved:

- reusable skill behavior
- platform-specific installed tool locations
- repo-owned tool source under `shared/tools/`

The current setup already has `platforms.yaml`, which helps resolve `tools_root`, but that logic still depends on each skill following the pattern correctly.

If one skill hardcodes a Codex path or documents one platform more strongly than the others, the portability boundary weakens.

## Candidate Direction

Introduce one shared script or small tool-resolution entry point that all skills can call when they need a platform-managed helper.

Possible shape:

- skills call one stable resolver command
- the resolver reads `platforms.yaml`
- the resolver returns or executes the correct tool path for the current platform
- the actual tool implementation remains in repo-owned source and installed helper copies

That would make the skill contract simpler:

- skills describe *which tool capability* they need
- the resolver handles *where that tool lives on this platform*

## Example Trigger

`note-search` is a useful concrete example because it already needs both graph and semantic helper resolution.

The problem is not only the runtime command. It is also the duplication pressure between:

- `modes/.../skills/.../SKILL.md`
- durable notes that describe the tool contract
- installed helper locations such as Codex-local tool paths

## Boundaries

This idea does not yet decide:

- whether the shared resolver should be a Python script, shell wrapper, or Atlas CLI subcommand
- whether the resolver should only return paths or should also execute tools
- whether all shared tools should be installed to platform-local homes or always routed through repo copies
- whether skill docs should keep example commands or reduce them to capability-level references

It also should not turn into a broad tool plugin system unless repeated real cases justify that expansion.

## Open Questions

- Should the generalization target be only path resolution, or also environment resolution such as `conda run -n base-ml`?
- Should Atlas expose one official helper-invocation pattern for every shared tool?
- Should durable notes like [[note-search-skill]] stop documenting platform-local example paths once the resolver exists?
- Which current skills besides `note-search` already leak platform assumptions in a way that should be migrated first?
