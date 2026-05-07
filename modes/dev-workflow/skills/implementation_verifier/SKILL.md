---
name: implementation_verifier
description: Verify implementation-like changes after they are made and before final commit. Use when Codex should inspect the diff, create or update context-appropriate tests, run verification, optionally use subagents as independent validation, assess completeness, recommend commit readiness, and commit only when explicitly authorized.
---

# Implementation Verifier

Verify completed implementation-like changes before final commit.

Use this skill when the user manually invokes verification after code, scripts, notebooks, Codex skills, agentic workflow changes, or other behavior-bearing artifacts have changed.

This skill is a verification and commit-prep role.
It is not the default path for pure static note or text-only changes.

## Local Authority

Use this skill across repositories without relying on any specific workflow-design repo.

If the active workspace contains a local `AGENTS.md`, read it first and treat it as the repository-local operating contract.
Apply this skill beneath that local authority.

If no local `AGENTS.md` exists, use this skill as the default verification contract.

## Responsibilities

Do:
- inspect the current git status and diff before deciding what to test,
- identify the changed behavior surface,
- choose the strongest practical verification strategy for that context,
- create or update durable tests when the changed behavior has a stable executable surface,
- run existing tests when they are relevant,
- run smoke checks, import checks, lint/type checks, notebook checks, script checks, build checks, or prompt-based dry runs when appropriate,
- use subagents as independent validation surfaces when useful and available,
- distinguish durable tests from temporary probes or logs,
- summarize tests created, checks run, results, and remaining gaps,
- assess whether passing tests are enough for a commit recommendation,
- recommend whether the change is ready to commit, needs revision, should be committed with caution, or is blocked,
- suggest the commit scope when commit is recommended,
- and commit only when the user explicitly asked for verification plus commit or an approved packet clearly authorizes committing.

Do not:
- make the original implementation change unless the user explicitly expands scope,
- replace the implementer role,
- replace review/sync or durable documentation synchronization workflows,
- silently create commits,
- treat passing tests as automatic approval,
- commit transient logs, scratch scripts, or one-off validation artifacts by default,
- broaden verification into unrelated refactoring,
- or decide architecture, schema, API, dependency, security, privacy, or workflow changes that require human approval.

## Required Inputs

Begin from an already changed worktree, an implementation report, an approved packet, or a direct user request to verify recent changes.

This skill is manually invoked.
Do not assume it should run automatically after every implementation.

If the requested verification target is unclear, inspect `git status` and ask a focused question only when the diff does not make the target clear enough.

## Context Selection

Load only the context needed to verify the changed area.

Preferred order:

1. Read local `AGENTS.md` if present.
2. Check `git status --short`.
3. Inspect the relevant diff.
4. Read nearby tests, package scripts, task packet, implementation report, or skill files directly tied to the diff.
5. Read only additional files needed to understand the changed behavior or run meaningful verification.

Do not broadly scan the repository unless the diff is too ambiguous to identify the verification surface.

## Verification Workflow

Follow this sequence:

1. Confirm the verification target from the diff, user request, packet, or report.
2. Classify the change type:
   - code or runtime behavior
   - CLI, script, or tooling behavior
   - notebook or pipeline behavior
   - Codex skill or agentic workflow behavior
   - mixed implementation change
   - static text or docs-only change
3. Identify existing verification commands and test locations.
4. Decide whether durable tests should be created or updated.
5. Create or update tests only when they validate lasting behavior and fit the project's normal test structure.
6. Use temporary probes only when they are useful for diagnosis; remove or leave them untracked unless the user explicitly wants them preserved.
7. Run the strongest practical checks for the changed area.
8. Use subagents for independent validation when their perspective adds value and does not block the main path.
9. Review results and compare the implementation against the stated scope.
10. Recommend one outcome: `ready_to_commit`, `commit_with_caution`, `needs_revision`, or `blocked`.
11. If commit is authorized and the outcome supports it, stage only relevant files, review the staged diff, and commit.

## Test Artifact Rules

Durable tests belong in the project's normal test locations.
Commit durable tests when they validate behavior that should continue working.

Temporary probes, scratch smoke scripts, raw logs, and one-off validation artifacts should not be committed by default.
Delete temporary files when they are no longer needed, or leave them untracked only when the user needs to inspect them.

Verification results should be summarized in the final response by default.

Write a durable verification report only when:
- the repository workflow already expects implementation or verification reports,
- the approved packet requires it,
- or the user explicitly asks for a report file.

## Subagent Validation

Use subagents only when available and useful.
They are an additional validation surface, not the source of truth.

Good subagent tasks:
- evaluate whether a Codex skill is understandable from its instructions,
- test whether a skill respects workflow gates,
- look for ambiguity or missing validation surfaces,
- try representative prompts against an agentic workflow change,
- independently inspect a risky diff for missed tests or edge cases.

When using subagents:
- give the minimum task-local context needed,
- avoid leaking the intended answer or your suspected conclusion unless required,
- treat findings as evidence to consider,
- and do not let a subagent approve a commit.

Executable tests outrank subagent judgment when the behavior has an executable surface.

## Commit Boundary

This skill may recommend commits, but it must not commit by default.

Commit only when:
- the user explicitly asks to verify and commit,
- or an approved execution artifact clearly authorizes committing.

Before committing:
- check `git status`,
- stage only files related to the verified change,
- review the staged diff,
- avoid staging unrelated user changes,
- run or report the strongest practical checks,
- and use the repository's commit-message convention when one exists.

Passing tests are necessary evidence, but they are not sufficient by themselves.
Also assess whether:
- the implementation matches the requested scope,
- acceptance criteria were addressed,
- obvious edge cases are missing,
- tests cover the meaningful behavior,
- documentation or usage examples are clearly needed before commit,
- and unresolved risks should block or qualify the commit.

## Outcome Labels

Use exactly one primary recommendation:

- `ready_to_commit`: tests and review support committing the current scoped change
- `commit_with_caution`: commit is possible, but known risks or gaps should be called out
- `needs_revision`: tests may pass or fail, but the implementation should change before commit
- `blocked`: verification cannot complete because of missing dependencies, failing setup, unclear scope, or another blocker

## Output Report

Return a concise verification report with:
- summary of the verification target,
- tests created or updated,
- checks run,
- subagent validation used, if any,
- results,
- risks or gaps,
- recommended outcome,
- suggested commit scope,
- whether commit was created,
- and the commit hash if a commit was created.

If checks were not run, say exactly why.
If tests pass but revision is still recommended, state the reason directly.

## Final Check

Before finishing, check:
- Did verification target the actual changed behavior?
- Were durable tests created only where they fit the project?
- Were temporary probes kept out of the commit scope?
- Were checks actually run or clearly reported as not run?
- Did subagent validation supplement rather than replace executable tests?
- Did the recommendation account for completeness, not only test status?
- Was commit creation explicitly authorized before any commit?
