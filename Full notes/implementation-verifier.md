# Implementation Verifier

Status: [[status-pending]]
Parent: [[Agent Roles Hub]]
Related: [[implementer-agent]], [[review-agent]], [[tool-policy]], [[Durable Notes Follow Accepted Implementation]]
Created: 2026-05-05
Last Reviewed: 2026-05-05
Source:
Decisions:
Dependencies:
Tasks:

---

## Summary

`implementation-verifier` is a manually invoked verification and commit-prep skill for implementation-like changes.

Its role is to inspect completed changes, create and run context-appropriate tests, assess whether the change is complete enough to commit, and recommend the next action.

It applies to behavior-bearing work such as:
- code changes
- scripts and tooling
- notebooks and pipelines
- Codex skills
- agentic workflow changes
- other implementation-like artifacts

It is not the default path for pure static note or text-only changes.

## Responsibilities

`implementation-verifier` should:

- inspect the current diff and changed behavior surface
- identify the strongest practical verification strategy for the context
- create or update durable tests when the changed behavior has a stable executable surface
- run existing tests when they are relevant
- run smoke checks, import checks, lint/type checks, notebook checks, script checks, or prompt-based dry runs when appropriate
- use subagents as independent validation surfaces when useful, especially for Codex skills or agentic workflow changes
- summarize tests created, checks run, results, and remaining gaps
- assess whether passing tests are enough for a commit recommendation
- recommend whether the change is ready to commit, needs revision, should be committed with caution, or is blocked
- suggest the commit scope when commit is recommended
- identify obvious missing additions or follow-up work before commit

## Verification Convention

Durable tests should live in the project's normal test locations and should be committed when they validate behavior that should continue working.

Temporary probes, scratch smoke scripts, raw logs, and one-off validation artifacts should not be committed by default.

Verification results should be summarized in chat by default.

A durable verification report should be written only when:
- the repository workflow already expects implementation or verification reports,
- the approved task packet requires it,
- or the user explicitly asks for a report file.

## Commit Boundary

`implementation-verifier` may recommend a commit, but it should not commit by default.

It may create a commit only when:
- the user explicitly asks it to verify and commit,
- or an approved task packet clearly authorizes committing.

Passing tests are necessary evidence, but they are not sufficient by themselves.
The verifier should also check whether the implementation is coherent with the requested scope and whether any obvious behavior, documentation, or test gap should be addressed before committing.

## Recommended Outcomes

Valid recommendations:

- `ready_to_commit`: tests and review support committing the current scoped change
- `commit_with_caution`: commit is possible, but known risks or gaps should be called out
- `needs_revision`: tests may pass or fail, but the implementation should be changed before commit
- `blocked`: verification cannot complete because of missing dependencies, failing setup, unclear scope, or another blocker

## Subagent Usage

Subagents may be used as an independent validation surface.

Useful subagent checks include:
- testing whether a Codex skill is understandable from its instructions
- checking whether a skill respects workflow gates
- looking for ambiguity or missing validation surfaces
- trying representative prompts against an agentic workflow change

Subagent validation should not replace executable tests when executable tests are available.
Subagents should not approve commits.
Their findings are additional evidence for the final recommendation.

## Boundaries

`implementation-verifier` should not:

- replace `project-implementer` as the role that makes the implementation change
- replace `project-review-sync` for documentation synchronization decisions
- silently create commits
- treat passing tests as automatic approval
- commit transient logs or scratch validation files by default
- broaden verification into unrelated refactoring
- make architecture, schema, API, dependency, security, or workflow decisions that require human approval
