# Repurpose Skill Notes Into Design Notes

Status: [[Tags/status-archived]]
Type: [[idea-note]]
Related: [[Workflow Mode Skill Governance]], [[note-manager]], [[clarify-intent]], [[planner-agent]], [[implementer-agent]], [[review-agent]], [[implementation-verifier]]
Created: 2026-05-08
Last Reviewed: 2026-05-15
Priority:[[docs/Tags/priority-high|priority-high]]  

---

## Idea

The existing skill-related notes in `docs/Durable Notes/` should be reviewed and repurposed so they preserve design reasoning rather than acting as direct skill contracts.

The direct runtime contract should live in mode-owned skill sources and bundled references, especially under:

```text
modes/dev-workflow/skills/
```

The docs notes should become future-facing design notes that help think through why each skill exists, which design decisions shaped it, what tradeoffs remain open, and how the skill might be tuned differently across modes.

## Current Problem

Several durable notes still read like live role or skill instructions.
That creates drift because the same behavior can appear in both:

- `docs/Durable Notes/`
- `modes/dev-workflow/skills/<skill>/SKILL.md`
- skill-local `references/` artifacts

When those sources diverge, it becomes unclear whether the durable note or the mode skill source is authoritative.

## Desired Direction

For each skill-related durable note:

- preserve useful design rationale, historical decisions, open questions, and mode-tuning ideas
- remove or compress direct procedural instructions that belong in `SKILL.md`
- link to the current mode-owned skill source as the runtime authority
- make the note type a design-oriented note when appropriate
- keep mode-specific behavior in `modes/<mode>/`, not duplicated as root project docs

## Candidate Notes

- `docs/Durable Notes/note-manager.md`
- `docs/Durable Notes/clarify-intent.md`
- `docs/Durable Notes/planner-agent.md`
- `docs/Durable Notes/implementer-agent.md`
- `docs/Durable Notes/review-agent.md`
- `docs/Durable Notes/implementation-verifier.md`
- `docs/Durable Notes/note-search-skill.md`

## Open Questions

- Which notes should become `[[design-note]]` versus archived historical notes?
- Which parts should move into skill-local `references/` files?
- Which parts are mode-specific to `dev-workflow` versus reusable across future modes?
- Should each skill keep one design note, or should some related skills share a broader design note?

## Follow-Up

- Review one skill note at a time.
- Preserve current decisions before deleting or compressing old contract text.
- Update mode skill sources or references when the design review exposes missing runtime behavior.
- Use the normal note-management gate for each durable note rewrite.

## Resolution

Archived for the accepted batch covering `clarify-intent`, `note-manager`, `project-planner`, `project-implementer`, and `project-review-sync`. This note was a reminder/task seed, not durable design knowledge. Each reviewed skill now has a short design hub with extracted design notes linked to the authoritative runtime source. Follow-up coverage for `implementation-verifier` or `note-search` should be reopened as a separate task if needed.
