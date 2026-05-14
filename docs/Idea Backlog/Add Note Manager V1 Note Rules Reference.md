# Defer Note Manager V1 Note Rules Reference

Status: [[Tags/status-pending]]
Type: [[idea-note]]
Related: [[note-manager]], [[Workflow Mode Skill Governance]]
Created: 2026-05-08
Priority: [[docs/Tags/priority-low|priority-low]] 

---

## Idea

Do not add a separate bundled `references/v1-note-rules.md` file for `dw-note-manager` yet.

`dw-note-manager` only owns one core job: bounded note mutation.
The rules for note splitting, grouping, note type choice, hub role selection, and folder handling are part of that core skill behavior, so they can live directly in `SKILL.md` for now.

Create a better documentation rules for tech stack so things are not that random. Setup paths like design note promotion, architecture extraction etc. So the actual documentation part evolves naturally without forgetting things. 
## Decision

The separate reference file is deferred.

The current preferred shape is:

- keep operational note-shaping rules directly in `modes/dev-workflow/skills/dw-note-manager/SKILL.md`
- keep old durable docs from acting as runtime authority
- repurpose `docs/Durable Notes/note-manager.md` into design rationale, tradeoffs, and mode-tuning thoughts
- introduce a separate `references/v1-note-rules.md` only if the rules become too large, need to be shared by multiple skills, or need schema-like versioning

## Why This Changed

The earlier reference-file idea made the skill fragile because the missing file became a packaging error.
That does not fit the current role boundary: Note Manager should already know its own note-shaping rules.

Separate bundled references are still useful for artifact schemas or shared long-form rules, but this case is currently simple enough to stay inside the skill source.

## Follow-Up

- Keep `dw-note-manager/SKILL.md` self-contained for note type, splitting, grouping, hub-role, and folder rules.
- Revisit a separate reference only if the rules become too bulky or need reuse outside `dw-note-manager`.
- When repurposing `docs/Durable Notes/note-manager.md`, preserve design reasoning without treating it as the direct runtime contract.
