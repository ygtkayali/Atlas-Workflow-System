# Note Manager Note-Type Selection and Promotion Lifecycle

Status: [[Tags/status-draft]]
Type: [[design-note]]
Parent: [[note-manager]]
Related: [[note-manager]], [[Note Manager Escalation Routing]], [[Tags/idea-note]], [[Tags/feature-subject-note]], [[Tags/design-note]]
Created: 2026-05-15
Last Reviewed: 2026-05-15
Source: modes/dev-workflow/skills/dw-note-manager/SKILL.md
Project Subjects:
Tasks:
Reports:

---

## Design Scope

The three-way note-type model used by the dev-workflow system (idea-note / feature-subject-note / design-note), the role boundaries between them, and the rule that promotion is a three-way lifecycle transition — not a status-only flip.

## Context

Note Manager's note-type selection is not free-form. The dev-workflow vault uses a local tag model that assigns distinct roles to each type. Misassigning types creates a structural problem: a note's metadata claims one role while its content and folder reflect another, which silently distorts future retrieval and review.

Promotion is the most common point where type drift occurs. A note starts as an idea-note, the subject gets worked through, and the user wants to advance its status. The temptation is to flip the status field and call it done. The problem is that the type and folder still reflect the pre-promotion state, so the note sits in the wrong place with the wrong identity.

## Chosen Design

**Three note types with bounded roles:**

- `[[idea-note]]` — draft, exploratory, or not-yet-promoted. Owns live thinking: questions, tensions, unresolved options, and branching thoughts are first-class content. Note Manager must not smooth them into recommendations unless the handoff explicitly marks those points as decided. The question-based nature of an idea-note is preserved even when the subject is partially clarified.

- `[[feature-subject-note]]` — one promoted active or settled project subject. Owns that subject's design choices, technical details, open questions, implementation notes, and related tasks. This is the default promotion target for an idea. The key constraint: it covers one subject, not a cross-cutting area.

- `[[design-note]]` — spans multiple feature subjects or constrains future work from one place. Use only after the relevant feature set is active. It does not replace the design-choice trail inside individual feature-subject-notes; it sits above them when one explanation is genuinely needed to cover the whole area.

**Promotion as a three-way transition:**

Promotion requires one of two conditions:
1. Explicit user direction — the user says to promote, settle, or advance the note.
2. Implementation evidence — an archived task, completed implementation, or confirmed review output shows the subject is fully worked through.

When promotion is confirmed, all three must be evaluated and updated together:
1. **Status** — transition to the appropriate target (usually `[[status-active]]` or `[[status-settled]]`).
2. **Type** — re-evaluate whether the current type still fits the note's new role.
3. **Folder placement** — if the note's folder reflects its pre-promotion state, move it using `git mv` to preserve history.

Note Manager must not promote speculatively. If neither condition is met, the note stays at `[[status-draft]]` or moves to `[[status-pending]]`.

## Rationale

Feature-subject-note is the default promotion target because most promoted ideas are about one bounded subject. Design-note earns its complexity only when the subject genuinely spans multiple feature areas or needs to constrain future work from one place. Defaulting to design-note for high-level ideas inflates its scope and makes the cross-cutting signal meaningless.

The three-way promotion rule exists because status, type, and folder reflect the same lifecycle state from three angles. Updating only status creates a note that says one thing (active/settled) while its type tag and folder say another (idea/backlog). That inconsistency is invisible at the moment of promotion but accumulates across the vault and is hard to audit later.

## Alternatives Considered

**Status-only promotion**: simpler, one field to change. Rejected because it leaves type and folder reflecting the pre-promotion state, creating silent drift that compounds across notes over time.

**Automatic type inference from status**: derive type from status transition rules. Rejected because type is a semantic judgment about the note's role, not a mechanical consequence of status. Two notes with the same status may have different types depending on their subject scope.

**Single note type (no local tag model)**: use generic notes with status only. Rejected because the local tag model provides meaningful role distinctions that support routing, retrieval, and maintenance review. Collapsing them loses that signal.

## Constraints

- Promotion without explicit user direction or implementation evidence is not allowed.
- A status flip alone is not a valid promotion.
- Note Manager must flag the three-part evaluation requirement explicitly in its promotion proposal rather than handling it silently.
- idea-note content must preserve unresolved questions as questions — not converted to settled direction — unless the handoff explicitly marks those points as decided.

## Technical Shape

Folder placement follows the local `atlas.yaml` or manifest folder configuration when such folder policy is present. If placement changes during promotion, moves use `git mv` to preserve history. Type and status changes are part of the same bounded note action as the folder move.

## Impacted Project Subjects

- [[note-manager]] — primary subject

## Open Questions

## Review Notes
