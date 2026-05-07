# Workflow Mode Skill Governance

Status: [[status-draft]]
Parent: [[Idea Hub]]
Related: [[Workflow CLI Mode System|Workflow CLI Tooling System]], [[Workflow Hub]], [[Agent Roles Hub]]
Created: 2026-05-06
Last Reviewed: 2026-05-07

---

## Idea

The workflow system should support modes that select and tune only the skills needed for a specific kind of work.

This would let the current Project Planning Workflow become one mode while other modes can develop their own skill expectations without overloading the same skill files.

## Current Direction

- V2 should introduce the local mode system.
- Project Planning Workflow should become a mode, not the entire system.
- The first mode should be `dev-workflow`, based on the current Project Planning Workflow and tuned for technical projects.
- Modes should expose selective skills rather than requiring every user to understand every role.
- Reading mode should not need planning, implementation, implementation verification, or implementation review skills.
- `dev-workflow` should cover the whole technical workflow loop: clarification, note management, planning, implementation, verification, review, and sync.
- Skills can be tuned differently per mode when their identity or behavior meaningfully changes.
- V3 should focus on mode refinement, additional modes, and mode tests after the first local mode proves useful.

## Why This Matters

Some skills have matured through repeated use, especially `clarify-intent` and `note-manager`.

Other skills, such as planner, implementer, and implementation verifier, are less tested because they have not been exercised much on real technical projects.

Keeping all expectations inside one universal skill set makes skill tuning harder. Modes give each workflow a smaller surface area to refine.

## Candidate Modes

- `dev-workflow`
- `reading`
- `book-analysis`
- `article-analysis`
- `research-brief`
- `maintenance-review`
- `knowledge-extraction`
- `knowledge-base-maintenance`

## Version Scope

### V2: Local `dev-workflow` Mode System

V2 should bring most of the mode-system direction forward, but keep it local.

V2 should:

- define `dev-workflow` as the first concrete mode
- tune that mode for technical project planning, implementation, verification, review, and documentation sync
- define a minimal YAML mode manifest with active skills, disabled skills, required files, templates, tools, gates, default artifacts, and health checks
- make the current workflow easier to install, inspect, and synchronize locally
- preserve local `AGENTS.md` authority for project-specific behavior
- test `dev-workflow` in real projects, with special attention to planner, implementer, verifier, and review/sync behavior
- leave the setup clean enough that later modes can be added quickly

V2 should not require:

- full public packaging
- PyPI distribution
- a broad catalog of mature modes
- generated skill systems
- formal mode test infrastructure
- a separate `vault-governor` mode

### V3: Mode Refinement And Expansion

V3 should build on the local `dev-workflow` mode once it is useful in real work.

V3 may include:

- fine-tuning mode-specific skill behavior
- adding reading, article-analysis, book-analysis, research, or maintenance modes
- mode tests or evaluation checks
- generated skills or base-plus-overlay tooling if duplication becomes painful
- public packaging after the local version stabilizes
- revisiting whether `clarify-intent` and `note-manager` should become a separate vault-governor-style mode once non-dev mode boundaries are clearer

## Transition Hierarchy

V2 should make the system shape explicit before adding more modes.

The working hierarchy is:

```text
atlas
  CLI layer
    mode listing
    initialization
    skill install and sync
    health checks
  mode layer
    dev-workflow
      manifest.yaml
      skills
      templates
      tools
      gates
      default artifacts
      health checks
  future mode layer
    reading
    knowledge-extraction
    knowledge-base-maintenance
    maintenance-review
```

`atlas` is the product and CLI layer.
`dev-workflow` is the first mode.
The mode manifest defines the mode boundary.
Mode-specific skills define behavior inside that boundary.

## Mode-Specific Skill Identity

Mode-specific installed skill instances are the clearest early option when behavior differs.

Example installed skills:

```text
atlas-dev-workflow-clarify-intent
atlas-dev-workflow-note-manager
atlas-dev-workflow-planner
atlas-dev-workflow-implementer
atlas-dev-workflow-verifier
atlas-dev-workflow-review-sync

atlas-reading-clarify-intent
atlas-reading-note-manager
atlas-reading-note-search
```

This avoids dynamically rewriting skills every time a mode is used.

## Skill Behavior By Mode

### Dev Workflow

`dev-workflow` should be tuned for technical project work.

Planner, implementer, verifier, and review/sync are the main skills to test and refine during V2.

`note-manager` in this mode can behave more like a product or technical documentation manager.

It should care about:

- operational project state
- draft implementation ideas waiting to be worked, promoted, or discarded
- planning notes
- task packets
- implementation reports
- decision traceability
- stale documentation
- implementation review and sync

`dev-workflow` should probably rename the current `Fleeting notes/` idea area to `Idea Backlog/` or an equivalent mode-specific folder name, because these notes are not merely fleeting capture. In this mode, they function as draft project and workflow ideas waiting for later refinement, implementation planning, promotion to durable notes, or discard.

`clarify-intent` and `note-manager` should stay shared core skills for V2, but their `dev-workflow` variants or mode instructions should make technical note behavior explicit.
They should not be split into a separate `vault-governor` mode during V2 unless real mode testing shows that the current sequence cannot be tightened otherwise.

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

It should not force implementation packets, technical task structure, or dev-workflow gates when those are irrelevant.

### Knowledge Extraction / Knowledge Base Maintenance

Knowledge-base modes should treat notes differently from technical project modes.

These modes may need different note-management behavior around:

- claims and source material
- extraction from books, articles, and research
- maintenance of a durable knowledge base
- conceptual links rather than task, packet, report, and implementation traceability
- preserving source fidelity without forcing technical workflow artifacts

These modes are deferred until after `dev-workflow` is clean and workable.

## Mode-Specific Note Surface

Each mode may need its own note surface instead of inheriting the current Project Planning Workflow vault shape unchanged.

The mode manifest should be able to define or propose:

- note templates
- default note roles
- starter hubs
- vault folder names
- artifact folders
- required local files
- expected tools
- review gates
- default generated artifacts

This should stay mode-specific because different modes organize work differently.

Examples:

- `dev-workflow` needs implementation-facing idea backlog, planning, packet, report, verification, and sync artifacts.
- reading, article, or book modes may need source, excerpt, claim, concept, and question templates.
- knowledge-base maintenance may need provenance, stale-claim, conflict, and review-report structures.

Folders should remain readability aids rather than governance by themselves.
Mode-specific folder names should make the human-facing workflow clearer without replacing metadata, links, status tags, backlinks, or explicit gates.

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

- What exact YAML schema should `manifest.yaml` use?
- Which future mode should be developed first after `dev-workflow`: reading, knowledge-extraction, knowledge-base-maintenance, or maintenance-review?
- Should `clarify-intent` stay mostly shared or become mode-specific immediately?
- Should `note-search` be shared across modes or tuned for reading versus project retrieval?
- What should each mode call its draft or incubating idea area?
- How much duplicated skill text is acceptable before generation tooling is worth building?
- How should a user see which mode is active in a directory?
- What real-project trial should validate `dev-workflow` first?

## Next Possible Step

Define the first minimal local `dev-workflow` YAML manifest and decide which skills, templates, tools, gates, default artifacts, and health checks belong in the V2 mode.
