---
name: dw-note-manager
description: Use when a ready_for_note_manager handoff or clear direct note request is in hand and a bounded durable note create, update, or metadata change must be drafted or applied.
---

# Note Manager

Perform bounded note-mutation work from clear bounded input without turning into a vault-management system.

Use this skill when the note action is already clear enough to decide, draft, or apply from the user's request, a clarified context handoff, and the supplied relevant notes or note paths.
If decision confidence is not high enough to choose the note action, target, note type, or durable meaning safely, route the work through `dw-clarify-intent` before this skill acts.
Any durable note mutation must use this skill, including metadata-only fixes, status changes, schema/governance note edits, link changes, small corrections in durable notes, and archival changes.
Do not make raw direct durable note updates outside `Note Manager`.

## Responsibilities

Do:
- read the clarified context handoff,
- read the direct note-action request when it is already clear enough to act on,
- read only the specific relevant notes the user provides,
- consume supplied `note-search` context capsules as upstream context when provided,
- read the local note templates when they exist,
- decide whether the bounded action is `create` or `update`,
- decide note type, target note, title, links, and final durable note structure from the provided context,
- choose folder placement only from the provided context, local folder policy, or local `AGENTS.md`, treating folder placement as readability rather than governance,
- refresh dynamic metadata on every create or update so status and other changing header fields reflect the current note state rather than stale template or prior values,
- evaluate context drift on every update, including whether status should become `[[status-draft]]`, `[[status-active]]`, `[[status-pending]]`, `[[status-settled]]`, or `[[status-archived]]`,
- draft exact note content or exact update content,
- keep note bodies meaningful and durable,
- consume and preserve the handoff's `Interpretation Basis` when it affects intent, tone, uncertainty, or traceability,
- preserve the original input or upstream artifact especially when the clarified context handoff exists only as transient conversation state, using a link, excerpt, concise basis note, or intentional redaction as appropriate,
- preserve the question-based nature of `[[idea-note]]` content when the handoff is exploratory,
- preserve local design-choice trails inside `[[feature-subject-note]]` notes instead of moving every decision into a separate design note,
- use the minimum useful links needed for the provided context,
- prefer intentional related links over default parent placement,
- handle multiple bounded note actions in one approved batch when the upstream proposal table is clear,
- use managed hub or index files only when explicitly requested or supplied by local context,
- require action/write confirmation before turning review/sync findings or proposal-table rows into durable writes,
- and wait for confirmation before writing unless the prompt and current workflow state clearly authorize direct writes.

Do not:
- search the vault broadly for related notes,
- run semantic search as its own discovery step,
- silently choose unrelated notes to edit,
- allow raw direct durable note updates outside this role,
- rename, move, or reorganize notes,
- invent a richer metadata or linking system,
- act when decision confidence is not high enough to choose the note action, target, note type, or durable meaning safely,
- write broad note changes directly from raw review/sync output before the user has approved the proposed note action or proposal-table rows,
- create notes from weak clarification state,
- convert unresolved ideas into recommendations, policy, decisions, or settled direction unless the handoff explicitly marks those points as decided,
- default new notes into a hub or index file,
- treat hierarchy as required note structure,
- infer note meaning, ownership, or governance from folders alone,
- create domain hierarchy folders when links, tags, hubs, or backlinks are the intended structure,
- or preserve every conversational detail just because it was discussed.

## Required Inputs

Begin from:
- an explicit clear note-action request or upstream artifact such as a clarified context handoff,
- the relevant notes or note paths supplied by the user,
- and the local templates when the project uses them.

If any of these are missing, do not guess through the gap.

Escalate back to clarification when:
- decision confidence is not high enough to choose the note action, target, note type, or durable meaning safely,
- the upstream input is raw review-sync output, implementation context, or another note-change proposal that has not been clarified,
- the durable subject is still weak,
- the supplied context is insufficient to choose a note type responsibly,
- the requested update depends on notes that were not provided,
- or the correct note action cannot be determined without broader vault discovery.

## Context Selection

Load context in layers and stop when it is sufficient.

Preferred order:

1. Read the local `AGENTS.md` if it exists.
2. Read the clear direct note-action request or clarified context handoff.
3. Read the specific note files or note paths supplied by the user.
   Supplied context may include a semantic `note-search` context capsule, but `Note Manager` should not run search as its own discovery step.
4. Read the local note templates that match the chosen or strongly indicated note type.
5. Use the note-type, splitting, grouping, index-file, and folder rules defined in this skill.
   Do not substitute stale local durable notes as runtime authority for those rules.

Avoid broad repository scans. This skill should shape a bounded note action, not discover the whole vault.

When `dw-clarify-intent` produces a visible `ready_for_note_manager` handoff for a required note change and the relevant note context is supplied, proceed into this workflow by default without waiting for separate phase-switch approval. The approval gate applies to the resulting draft or durable-write decision.

Raw review/sync output or documentation-sync analysis is not the same thing as Note Manager write approval. A compact review/sync proposal table may go directly to Note Manager when each routed row has clear target, action, evidence, proposed change, uncertainty, constraints, and route. If the user approves those rows for writing, Note Manager may apply the bounded updates directly without creating a separate manifest or draft artifact.

## Workflow

Follow this sequence:

1. Identify the durable subject from the direct request or clarified context handoff.
2. Confirm that the direct request, clarified handoff, or approved proposal-table row gives high enough decision confidence to act.
3. Confirm the candidate action: `create` or `update`.
4. Choose and justify the note type, preferring local note-type tags such as `[[idea-note]]`, `[[feature-subject-note]]`, or `[[design-note]]` when they exist.
5. Read only the provided notes needed for the action.
6. Decide whether the subject belongs in one note or a small obvious set of notes.
   If the handoff contains provisional subject bundles, use them as input evidence rather than final note structure.
7. Refresh dynamic metadata fields for the current note state instead of preserving stale template or previously copied values.
8. If write approval is explicit, apply the bounded note update directly. If approval is not explicit or the user asks to review first, draft the exact note content or exact update content.
9. Make the minimum useful related links from the provided context and use parent placement only when explicitly justified.
10. When drafting, present the draft and wait for confirmation before writing.

If any step depends on unprovided context or unclear structure, stop and escalate instead of improvising.
If decision confidence is not high enough, route the input to `dw-clarify-intent` and wait for a clarified context handoff before drafting note content.

## Bundled Intake

`Note Manager` may receive a bundle of clarified durable subjects or approved review/sync proposal-table rows from upstream context.

A bundle is allowed for intake efficiency, but it must not collapse note-action approval.

For **single-subject handoffs**, the action header (note action + type + target/title) serves as the manifest. A separate manifest document is not required.

For **multi-subject handoffs or proposal tables**, do not create a separate manifest by default. Use the upstream proposal table as the reviewable decision surface when each row already includes target, action, evidence, proposed change, uncertainty, constraints, and route.

Create a separate manifest only when:
- upstream rows are mixed or ambiguous,
- one subject may map to several note actions and the mapping is not explicit,
- multiple subjects might collapse into one note action,
- or the user asks for a manifest before drafting or writing.

If the upstream artifact contains provisional subject bundles from complex-prompt intake, treat them as input evidence rather than final note structure.
Each bundle should contain one domain or area; branching ideas should remain together only when they are closely related.
If a branch can become its own durable subject, split it and preserve the connection instead of blending it into a broader note action.

When a separate manifest is needed, it should include one row per proposed note action:
- subject id or subject label,
- target note, if known,
- action: `create`, `update`, `defer`, or `return-to-clarification`,
- why this note is the right target,
- source basis from the clarified context,
- interpretation basis that must be preserved or validated,
- relevant context for this note action,
- excluded or non-applicable context when separation matters,
- status: `ready`, `needs_clarification`, or `deferred`.

The relationship between clarified subjects and note actions is not one-to-one:
- one clarified subject may produce zero, one, or many note actions,
- one note action must target exactly one durable note,
- multiple subjects may support one note action only when that relationship is explicit in the manifest.

`dw-clarify-intent` owns semantic subject separation.
`Note Manager` owns subject-to-note mapping, note action choice, target note choice, note type, metadata, links, and final draft structure.
When a handoff includes `Interpretation Basis`, use it as source basis for the note action and preserve the parts needed to validate intent later.
Do not discard original input, tone or stance, user-intent versus agent-inference boundaries, open ambiguity, or things not to imply when those fields affect the durable note's meaning.

Only proposal-table or manifest rows marked `ready` or routed to `note-manager` may become note updates.
Each row may be approved, revised, deferred, or rejected independently.
Approval for one note action does not approve any other note action in the same bundle unless the user explicitly approves the batch.

When the user explicitly approves a clear proposal-table batch for writing, Note Manager may apply all approved rows in one pass. It must still preserve row boundaries in its report and must not include rows routed to `clarify-intent`, `defer`, or `reject`.

If `Note Manager` cannot map a clarified subject or proposal row to note actions without mixing unrelated context, guessing target notes, or relying on raw implementation evidence, return that subject to clarification instead of drafting or writing.

## Dynamic Metadata Rules

Refresh dynamic metadata for every durable note mutation, including small-edit mode patches.

At minimum, evaluate:
- `Status`,
- `Type`,
- `Last Reviewed`,
- `Related`,
- `Parent`,
- `Tasks`,
- and `Decisions`.

### Status Transition Table

Status tags are defined in `vocabulary.md` (see also `docs/Durable Notes/Status Tag Registry.md`). Allowed transitions:

| From | To | Condition | Who decides |
|---|---|---|---|
| (new) | `[[status-draft]]` | Note is forming; intent not yet solidified | Note Manager |
| `[[status-draft]]` | `[[status-active]]` | Subject promoted, now active working context | User or handoff |
| `[[status-draft]]` | `[[status-pending]]` | Relevant but deferred | User or handoff |
| `[[status-active]]` | `[[status-settled]]` | Worked through; remains reliable context | User or handoff |
| `[[status-active]]` or `[[status-settled]]` | `[[status-archived]]` | Historical, deprecated, replaced, or removed from active context | User or handoff |
| any | `[[status-draft]]` | Significant context drift detected | Note Manager flags; user confirms |

Note Manager may flag a status drift but must not silently downgrade a settled or archived note.

### Header Format

Detect whether the existing note uses YAML frontmatter (`--- ... ---`) or inline-callout style (`Status: [[Tags/...]]` in the note body).
Preserve the existing format. Do not convert between YAML frontmatter and inline style.

Do not preserve stale metadata just because the body edit is small.

## Note-Type Selection

Prefer the local dev-workflow note-type tags when they exist. Full tag semantics live in `docs/Tags/`; the key role distinctions are:

- `[[idea-note]]` — draft, exploratory, or not-yet-promoted. Preserve live thinking: questions, tensions, unresolved options, and branching thoughts are first-class content. Do not smooth them into recommendations unless the handoff explicitly marks them as decided.
- `[[feature-subject-note]]` — one promoted active or settled project subject. Owns that subject's design choices, technical details, open questions, and related tasks. Prefer this over `[[design-note]]` when promoting an idea.
- `[[design-note]]` — spans multiple feature subjects or constrains future work from one place. Use after the feature set is active; it does not replace per-subject design trails inside `[[feature-subject-note]]` notes.

Use managed hub or index files only when explicitly requested or supplied by local context. Do not promote a note into a hub just because it is high-level; escalate if a new hub-like note is genuinely needed.

## Vault Folder Handling

Treat vault folders as a readability layer for the human, not as the primary governance model.

The primary governance model is note metadata, status tags, intentional links, backlinks, and explicit note relationships.
Folder placement and note type are separate concepts; a note's operational meaning comes from its role, metadata, and supplied context — not its folder.

For the authoritative folder list, read `atlas.yaml` (or the local `manifest.yaml`) `vault.folders`.
Apply this readability-vs-governance rule on top of whatever that config defines.

Do not create domain hierarchy folders (e.g., `Backend notes`) to group related subjects.
Domain grouping belongs in links, tags, hubs, and backlinks unless the user or local `AGENTS.md` explicitly approves a readability folder for that project type.

## Output Contract

Note Manager has two gate shapes: proposal approval and durable-write approval. For compact proposal tables, the user may approve both together by explicitly asking Note Manager to apply or write the approved rows.

Action confirmation approves preparing or applying specific note actions. It should be requested when the incoming request proposes note work but does not clearly authorize drafting or writing.

Action confirmation prompt:

```text
Proposed action: <create, update, defer, return to clarification, or promotion candidate review>
Reason: <why this action follows from the supplied handoff or review evidence>
Expected output: <direct writes, draft note, patch, manifest only if needed, or clarification return>
Planned behavior: <what Note Manager will apply or prepare and what it will not write without later approval>

Approve this action?
```

Durable-write confirmation approves applying a prepared note draft, patch, or approved proposal-table row.

Default output is draft-first unless write approval is explicit. A durable write requires one of these four explicit authorization signals:
1. The user message contains a direct write directive ("apply", "write", "commit", or equivalent).
2. The upstream handoff contains `direct_write: true`.
3. An approved execution packet explicitly authorizes the write.
4. The user approves a review/sync proposal table for Note Manager writing.

Anything outside these four signals -> draft-only output.

Action approval does not imply durable-write approval unless the approval explicitly says to apply or write. Durable-write approval for one note action does not approve any other note action in the same bundle unless the user explicitly approves the batch.

### Small-Edit Mode

When the change is metadata-only (e.g., a status flip) or a single isolated line, produce a patch instead of a full note output:

```
target   | <note path or title>
field    | <metadata field or line description>
old      | <current value>
new      | <proposed value>
reason   | <why this change is correct>
```

Dynamic metadata must still be evaluated and the `Last Reviewed` field updated even for small-edit mode patches.

### Full-Edit Mode

**When the action is `create`**, provide:
- note action,
- note type,
- proposed title,
- proposed related links from the provided context,
- proposed parent link only when explicitly justified,
- refreshed dynamic metadata for the new note state,
- and the full draft note body.

**When the action is `update`**, provide:
- note action,
- target note,
- why this note is the correct target,
- refreshed dynamic metadata for the updated note state,
- and the exact proposed updated content or patch-shaped replacement text.

### Direct Batch Write Mode

When a proposal table or user request clearly approves multiple bounded writes, apply only the approved rows and report:
- row or subject id,
- target note,
- action applied,
- metadata refreshed,
- evidence basis,
- skipped rows and why,
- checks run.

Do not create a manifest or draft artifact unless needed for ambiguity or requested by the user.

### Return to Clarification

If the request should return to clarification, state:
- the blocking ambiguity,
- why `Note Manager` would be guesswork here,
- and the minimum clarification needed next.

## Output Style

Keep outputs:
- bounded,
- explicit,
- conservative about structure,
- and clear about what is drafted versus what is already decided.

Do not hide uncertainty inside polished note prose.
Do not silently expand a local note edit into vault maintenance.

## Final Check

Before finishing, verify the four things the workflow does not automatically enforce:

1. **Subject durability** — Is this worth a note at all, or does it belong only in the conversation?
2. **Idea-note fidelity** — If the type is `[[idea-note]]`, are unresolved questions still questions rather than conclusions?
3. **Scope** — Should this be one note or a small obvious set? Did I resist the pull toward a hub or index file?
4. **Write authorization** — Is a durable write clearly authorized by one of the four signals in the Output Contract, or must the output remain draft-only?

For everything else (note type, metadata freshness, link minimalism, format preservation, status transitions), the workflow steps above are the check. If you reached this point following them, those are satisfied.

If any of the four answers above is no, refine the draft or return the work to clarification.
