# Tool Policy

Status: [[Tags/status-settled]]
Parent:
Related: [[planner-agent]], [[implementer-agent]], [[review-agent]]
Created:
Last Reviewed:
Source:
Decisions:
Dependencies:
Tasks:

---

## Purpose
This note defines how tool policy should be placed within the workflow.

It is not the primary source of truth for role behavior.
Role-specific tool boundaries, verification expectations, and escalation rules should live in the corresponding role notes and workflow skills.

Project-wide governance may still live in:
- `AGENTS.md`,
- a project bootstrap template,
- or a local project-specific `tool-policy.md` when the repository needs extra operational rules.

---

## Placement Rules

### Keep in `AGENTS.md` or project bootstrap files
- project-wide governance goals,
- global approval rules,
- instruction priority,
- and any repository-wide constraints that apply to every role.

### Keep in role notes and role skills
- role tool boundaries,
- role-specific verification expectations,
- role-specific escalation triggers,
- and role-specific output requirements.

### Keep in a local project `tool-policy.md` only when needed
Use a project-local `tool-policy.md` for rules that are:
- more operational than architectural,
- more specific than the generic workflow charter,
- and shared across multiple roles in that one repository.

Examples:
- which verification commands are preferred in that repo,
- which environments require human approval,
- which directories or systems are considered sensitive,
- and which tool classes are disallowed locally.

## Portability Guidance
To keep the workflow portable across projects:
- do not rely on this file as the only source of role behavior,
- let local `AGENTS.md` tighten or extend project-wide policy,
- keep role-specific rules with the corresponding role artifacts,
- and use project-local policy files only for repository-specific operational constraints.
