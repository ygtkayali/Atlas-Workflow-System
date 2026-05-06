# Workflow Mode Skill Governance

Status: [[status-draft]]
Parent: [[Idea Hub]]
Related: [[Workflow CLI Mode System|Workflow CLI Tooling System]], [[Workflow Hub]], [[Agent Roles Hub]]
Created: 2026-05-06
Last Reviewed: 2026-05-06

---

## Idea

The workflow system should support modes that select and tune only the skills needed for a specific kind of work.

This would let the current Project Planning Workflow become one mode while other modes can develop their own skill expectations without overloading the same skill files.

## Current Direction

- V2 should introduce the local mode system.
- Project Planning Workflow should become a mode, not the entire system.
- The first mode should be the current PPW workflow, tuned for technical projects.
- Modes should expose selective skills rather than requiring every user to understand every role.
- Reading mode should not need planning, implementation, implementation verification, or implementation review skills.
- Technical-project or project-planning mode can include planner, implementer, verifier, and review skills.
- Skills can be tuned differently per mode when their identity or behavior meaningfully changes.
- V3 should focus on mode refinement, additional modes, and mode tests after the first local mode proves useful.

## Why This Matters

Some skills have matured through repeated use, especially `clarify-intent` and `note-manager`.

Other skills, such as planner, implementer, and implementation verifier, are less tested because they have not been exercised much on real technical projects.

Keeping all expectations inside one universal skill set makes skill tuning harder. Modes give each workflow a smaller surface area to refine.

## Candidate Modes

- `project-planning`
- `technical-project`
- `reading`
- `book-analysis`
- `article-analysis`
- `research-brief`
- `maintenance-review`

## Version Scope

### V2: Local PPW Mode System

V2 should bring most of the mode-system direction forward, but keep it local.

V2 should:

- define the first concrete PPW mode
- tune that mode for technical-project planning and implementation workflows
- decide whether `ppw`, `project-planning`, and `technical-project` are one mode or separate mode names
- define a minimal mode manifest with active skills, disabled skills, templates, gates, and default artifacts
- make the current workflow easier to install, inspect, and synchronize locally
- preserve local `AGENTS.md` authority for project-specific behavior

V2 should not require:

- full public packaging
- PyPI distribution
- a broad catalog of mature modes
- generated skill systems
- formal mode test infrastructure

### V3: Mode Refinement And Expansion

V3 should build on the local PPW mode once it is useful in real work.

V3 may include:

- fine-tuning mode-specific skill behavior
- adding reading, article-analysis, book-analysis, research, or maintenance modes
- mode tests or evaluation checks
- generated skills or base-plus-overlay tooling if duplication becomes painful
- public packaging after the local version stabilizes

## Mode-Specific Skill Identity

Mode-specific installed skill instances are the clearest early option when behavior differs.

Example installed skills:

```text
ppw-project-planning-clarify-intent
ppw-project-planning-note-manager
ppw-project-planning-planner
ppw-project-planning-implementer
ppw-project-planning-review-sync

ppw-reading-clarify-intent
ppw-reading-note-manager
ppw-reading-note-search
```

This avoids dynamically rewriting skills every time a mode is used.

## Skill Behavior By Mode

### Project Planning / Technical Project

`note-manager` can behave more like a product or technical documentation manager.

It should care about:

- operational project state
- planning notes
- task packets
- implementation reports
- decision traceability
- stale documentation
- implementation review and sync

### Reading / Article / Book Mode

`note-manager` can behave more conceptually.

It should care about:

- reading notes
- concepts
- claims
- questions
- tensions between sources
- links between ideas
- recurring themes

It should not force implementation packets, technical task structure, or project-planning gates when those are irrelevant.

## Implementation Options

### Option 1: Mode-Specific Skill Names

Install separate skill instances per mode.

This is the clearest option and probably best for early v3 work.

Tradeoff: some duplication across `SKILL.md` files.

### Option 2: Shared Base Skill Plus Mode Overlay

Keep a shared base skill and apply a mode-specific overlay.

This reduces duplication but depends on the agent reliably combining base and overlay instructions.

Tradeoff: more conceptual complexity and weaker isolation.

### Option 3: Generate Installed Skills From Base Plus Mode Patch

Maintain base skills and mode patches in source, then generate concrete installed skills.

This keeps installed skills explicit while reducing source duplication.

Tradeoff: requires more tooling and version-management discipline.

## Current Preference

Start with Option 1.

Use explicit mode-specific skill names and accept some duplication while the mode boundaries are still forming.

Move toward Option 3 later if duplication becomes painful and mode behavior is stable enough to generate safely.

## Governance Rule

Global workflow rules define phase safety.

Modes define which phases and skills exist for a workflow.

Local `AGENTS.md` defines repo-specific or vault-specific behavior.

Mode-specific skills should respect both the selected mode and the local project contract.

## Open Questions

- Should the first mode be named `ppw`, `project-planning`, or `technical-project`?
- Are `project-planning` and `technical-project` separate modes, or is technical-project tuning part of the initial PPW mode?
- Which mode should be developed first after the PPW technical-project mode: reading, research, or maintenance-review?
- Should `clarify-intent` stay mostly shared or become mode-specific immediately?
- Should `note-search` be shared across modes or tuned for reading versus project retrieval?
- How much duplicated skill text is acceptable before generation tooling is worth building?
- Should a mode have a manifest that declares active skills, disabled skills, templates, gates, and default artifacts?
- How should a user see which mode is active in a directory?

## Next Possible Step

Define the first minimal local PPW mode manifest and decide which skills, templates, tools, gates, and default artifacts belong to the technical-project tuned version.
