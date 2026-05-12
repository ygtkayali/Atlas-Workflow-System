# Implementation Report: Atlas Platform Backfill

## Summary
- Updated Atlas project config generation so `atlas.platforms` is always written to project `atlas.yaml`.
- `atlas init` uses explicit `--platform` values when creating or backfilling an existing config.
- `atlas sync` preserves existing project platforms and backfills source defaults when the field is missing or empty.

## Files Touched
- `tools/atlas.py`

## Why
- Projects should not need a local `platforms.yaml`.
- Project `atlas.yaml` should still record which platform names Atlas should target.
- Missing `atlas.platforms` made platform targeting implicit and confusing.

## Checks Run
- `python3 -m compileall tools/atlas.py`
- Temporary `atlas init ... --platform codex,claude` check confirmed new configs include both platforms.
- Temporary `atlas sync ...` check confirmed missing platforms are backfilled from defaults.
- Temporary `atlas sync ...` check confirmed existing `codex, claude` platforms are preserved.
- Temporary `atlas init ... --platform codex,claude` check confirmed an existing config without platforms is backfilled from the explicit init platforms.

## Assumptions Introduced
- Empty `atlas.platforms: []` is treated the same as missing platforms and backfilled.
- `atlas sync` should use source default platforms when a project has no explicit platform list.

## Unresolved Issues
- No durable automated test suite exists for the Atlas CLI behavior; verification used compile and temporary CLI smoke checks.

## Review / Sync Follow-up
- Consider adding durable CLI tests for `init` and `sync` platform config behavior.
