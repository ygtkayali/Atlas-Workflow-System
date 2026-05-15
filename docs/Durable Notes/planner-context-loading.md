# Planner Context Loading Strategy

Status: [[Tags/status-draft]]
Type: [[design-note]]
Parent: [[planner-agent]]
Related: [[planner-agent]]
Created: 2026-05-15
Last Reviewed: 2026-05-15
Source: modes/dev-workflow/skills/project-planner/SKILL.md
Decisions:
Dependencies:
Tasks:

---

The planner loads context in layers and stops at a hard cap of approximately 5–8 notes. The cap is a design constraint, not a target — stopping earlier when context is sufficient is preferred.

## Note Ecosystem Model

The planner treats the project as a linked note system rather than a monolithic spec. Different notes serve different roles:

- **context-map.md** — default project-wide entry point when present; identifies authoritative files, metadata, and recommended entry rules
- **Feature subject notes** — local entry point for bounded work; own design choices, task notes, decisions, and follow-up items for a specific area
- **Hub notes** — supplement context-map.md when present; if the two appear to disagree, the mismatch must be surfaced rather than silently resolved

Note naming, folder layout, and hub structure vary by project. The planner must not assume that conventions from one repository apply to another unless local instructions say so.

## Layered Loading Sequence

1. Start from the triggering request, note-ready handoff, or seed note.
2. Use `note-search` when a known seed note or semantic query can retrieve a bounded relevant set — process `read_first` notes before `graph_expansion` notes.
3. Read `context-map.md` if project structure context is needed.
4. Follow direct links to feature subject notes or hub notes the project provides.
5. Inspect `docs/In-flight/` for current workflow state when the task may relate to an open lane.
6. Read relevant decisions, constraints, and recent implementation reports.
7. Follow backlinks or metadata only when they materially improve planning quality.
8. Stop when there is enough context to define the task, identify constraints, detect conflicts, and produce a scoped packet.

`note-search` is preferred over manual broad discovery for concept-level context — this keeps retrieval behavior observable and improvable centrally.

## Why the Cap Exists

The 5–8 note cap is not a hard limit on information value; it is a forcing function. When the cap is reached and context is still insufficient, the remaining gap routes through `dw-clarify-intent` rather than expanding note loading indefinitely.

The design tension is context completeness vs. context bloat. Unbounded loading shifts the cost of missing or unclear documentation onto the planning context window rather than surfacing it as a planning gap. The cap keeps that cost visible and keeps planning scope bounded.
