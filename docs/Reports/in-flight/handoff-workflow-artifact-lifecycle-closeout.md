# Workflow Artifact Lifecycle And Closeout Handoff

- Type: clarified-context-handoff
- Status: ready_for_note_manager
- Related to: idea note for workflow decision-making, artifact lifecycle, in-flight state, and review closeout
- Created: 2026-05-11

## Clarified Subject / Subjects

### Subject 1: Handoff As Mandatory Intake For Important Work

The workflow idea is that important work should start with a durable handoff artifact before moving into Note Manager, planner, or implementer roles.

The handoff preserves the user's intent, uncertainty, boundaries, and reasoning before downstream work begins. This avoids raw chat becoming the hidden source of truth for important decisions.

The proposed rule is:

- Handoff required when the task changes durable notes, workflow rules, architecture, implementation direction, project structure, or future agent behavior.
- Handoff optional for tiny mechanical edits and simple inspection.

### Subject 2: Review As The In-Flight Closeout Gate

The workflow idea gives review/sync a stronger operational role: it should own closeout of active workflow artifacts, not only inspect and summarize completed work.

Review/sync should:

- inspect `docs/Reports/in-flight/`
- decide what is still active
- check whether downstream docs need sync
- archive or distill completed artifacts
- leave `in-flight/` clean

In this model, `docs/Reports/in-flight/` becomes a hard workflow signal. If it is non-empty, agents should not start unrelated important work until the current work is continued or reviewed and closed out.

### Subject 3: Distilled Archive Instead Of Raw Artifact Accumulation

The workflow idea is that completed handoffs, packets, and reports should not automatically remain forever as separate raw files.

Instead, review closeout should usually create one distilled archive summary per task, such as:

`docs/Reports/archive/2026-05/context-map-active-context-simplification.md`

The archive summary should preserve the useful learning and traceability:

- original intent
- work done
- important decisions
- final files
- verification
- reusable pattern

Raw in-flight artifacts should be deleted or moved to raw archive only when they contain important evidence.

### Subject 4: Project-Over Learning Extraction

The workflow idea treats distilled archive summaries as the better source for project-end learning extraction.

At project end, concise closeout summaries can support extracting:

- step-by-step build guides
- decision patterns
- failure modes
- workflow improvements
- reusable implementation sequences

Raw handoffs, packets, and reports are likely too verbose and duplicated for this purpose.

### Subject 5: Replacing Manually Maintained Active Context With In-Flight State

The workflow idea proposes that `docs/Reports/in-flight/` should become the current state mechanism.

The best current model is:

- `docs/context-map.md`: stable project structure
- `docs/Reports/in-flight/`: current active workflow state
- `docs/Reports/archive/`: distilled task history and reusable learning

Under this model, `active-context.md` becomes unnecessary or generated from `in-flight/`, rather than maintained by hand as a separate state file.

## Interpretation Basis

Origin type: direct user prompt / workflow design idea.

Original user input preserved:

```text
The core shift is:

  handoff opens work
  review closes work
  in-flight shows whether work is still open
  archive stores distilled learning, not raw clutter

  1. Handoff As Mandatory Intake

  This makes sense for important work.

  A handoff becomes the first durable artifact for any meaningful decision path:

  idea / request
    -> handoff
    -> note-manager OR planner OR implementer

  Examples:

  create/update notes:
  request -> clarified handoff -> note-manager draft/write

  implement feature:
  request -> clarified handoff -> planner packet -> implementation

  workflow/governance change:
  request -> clarified handoff -> note-manager/planner depending on action

  The benefit is that every important task starts with preserved intent, uncertainty, and boundaries. You avoid raw chat becoming the hidden source of truth.

  But I would not require handoffs for tiny mechanical tasks. Otherwise it becomes heavy. A good rule:

  Handoff required when the task changes durable notes, workflow rules, architecture, implementation direction, project structure, or future agent behavior.
  Handoff optional for tiny mechanical edits and simple inspection.

  2. Review As The In-Flight Closeout Gate

  This is the missing useful job for review.

  Review should not just “inspect and summarize.” It should own closeout:

  review-sync:
  - inspect in-flight/
  - decide what is still active
  - check whether downstream docs need sync
  - archive or distill completed artifacts
  - leave in-flight clean

  Then in-flight/ becomes a hard workflow signal:

  if docs/Reports/in-flight/ is non-empty:
    do not start unrelated important work
    first continue or review/close out current work

  That gives review a real reason to exist. It becomes the cleanup and continuity mechanism.

  3. Raw Artifacts Vs Distilled Archive

  I agree that saving every handoff, packet, and report forever as separate files may become noisy.

  A better closeout product is a single distilled archive record per task:

  docs/Reports/archive/2026-05/context-map-active-context-simplification.md

  Shape:

  # Context Map And Active Context Simplification

  Date: 2026-05-11
  Status: closed

  ## Original Intent
  Short summary of the handoff intent.

  ## Work Done
  - Created/updated X
  - Changed Y
  - Deferred Z

  ## Important Decisions
  - Handoff is mandatory for important workflow changes.
  - In-flight folder is current workflow state.
  - Review owns closeout.

  ## Final Files
  - `docs/context-map.md`
  - `modes/dev-workflow/docs/context-map.md`

  ## Verification
  - Files read back
  - Diff reviewed
  - Remaining risk

  ## Reusable Pattern
  How to do similar work in another project.

  Then during review closeout:

  handoff + packet + report -> distilled archive summary
  raw in-flight files -> deleted or moved to raw archive only if needed
  in-flight/ -> cleaned

  You could even have two archive levels:

  docs/Reports/archive/summaries/
  docs/Reports/archive/raw/

  But I’d start with just the distilled summary. Keep raw files only when they contain important evidence.

  4. Project-Over Learning Extraction

  This is a strong reason to archive summaries instead of raw artifacts.

  At project end, you can extract:

  step-by-step build guide
  decision patterns
  failure modes
  workflow improvements
  reusable implementation sequence

  from concise closeout summaries. Raw handoffs and reports are too verbose and duplicated for that.

  Recommended Lifecycle

  1. Important request arrives
  2. Create handoff in `docs/Reports/in-flight/`
  3. Route handoff to note-manager / planner / implementer
  4. Create packet/report in `in-flight/` as needed
  5. Work completes
  6. Review-sync runs closeout
  7. Review creates one distilled archive summary
  8. Review deletes or moves consumed in-flight artifacts
  9. `in-flight/` is empty

  Best Current Model

  I’d define the workflow around these three operational pieces:

  docs/context-map.md
    stable project structure

  docs/Reports/in-flight/
    current active workflow state

  docs/Reports/archive/
    distilled task history and reusable learning

  Then active-context.md becomes unnecessary or generated from in-flight/.

  My recommendation: make in-flight/ the state mechanism, make handoffs the intake gate, and make review the closeout/archive gate. That gives every artifact a clear lifecycle and avoids
  maintaining a separate state file by hand.
 I need you to preserve all the content here and create a handoff for an idea note.
```

Relevant context used:

- The local `AGENTS.md` bridge treats markdown workflow artifacts as operational state.
- The local `AGENTS.md` bridge requires hard-gate artifacts to be persisted under `docs/Reports/in-flight/`.
- Existing related in-flight handoff: `docs/Reports/in-flight/handoff-context-map-active-context-templates.md`.
- Existing related idea note: `docs/Idea Backlog/Task and Report Artifact Lifecycle.md`.
- Existing local context map already lists `docs/Reports/in-flight/` as active workflow artifacts, not durable project knowledge.
- Atlas skill sync was checked before this workflow work and reported no changes needed.

Intent to preserve:

- The idea is about a workflow model and artifact lifecycle, not just a small wording tweak.
- The idea should become an idea note candidate before any direct governance or reusable mode changes.
- The note should explain workflow decision-making, artifact lifecycle, in-flight state management, review closeout, archive distillation, and active-context simplification.
- The idea should preserve the pragmatic exception for tiny mechanical tasks.

User intent versus agent inference:

- User intent: create a handoff for an idea note explaining this new workflow idea.
- User intent: preserve the supplied content.
- User intent: the idea concerns workflow, decision-making, artifact lifecycle, and management.
- Agent inference: `docs/Idea Backlog/Task and Report Artifact Lifecycle.md` is likely related context, but Note Manager should decide whether to update it or create a separate idea note.
- Agent inference: the idea may affect `AGENTS.md`, `modes/dev-workflow/agents-bridge.md`, `project-review-sync`, and starter docs later, but this handoff does not authorize those edits.

Open ambiguity and downstream cautions:

- Whether this should update an existing idea note or become a new idea note is for Note Manager.
- Whether `active-context.md` should be removed, generated, or retained as a thin pointer is not finally decided.
- Whether raw artifacts should ever be retained by default is not finally decided beyond the current preference to keep raw files only when they contain important evidence.
- Whether `docs/Reports/archive/` should have only summaries or separate `summaries/` and `raw/` subfolders is proposed, with a current preference to start with distilled summaries only.

Validation target:

- Downstream Note Manager should preserve the lifecycle model: handoff opens work, review closes work, in-flight shows open state, archive stores distilled learning.
- It should not convert this into immediate implementation work or silently rewrite workflow governance files.
- It should keep the tiny-mechanical-task exception visible.
- It should keep the distinction between distilled archive summaries and raw artifact retention.

## User Goal

Create durable idea-note input that explains a new workflow model for decision-making, artifact lifecycle management, in-flight state, review closeout, and archive-based learning extraction.

The goal is to preserve the idea clearly enough that future note management or planning can decide whether and how to revise the dev-workflow rules, review/sync role, artifact folders, and `active-context.md` behavior.

## Decided

- The handoff should target an idea note, not immediate implementation.
- The supplied content should be preserved.
- Important work should begin with a durable handoff intake artifact.
- Review should become the closeout/archive gate for completed workflow artifacts.
- `docs/Reports/in-flight/` should act as the visible signal for open workflow work.
- Archive should preserve distilled learning rather than raw clutter by default.
- Raw handoffs, packets, and reports should only be retained when they contain important evidence.
- Handoffs should not be required for tiny mechanical edits or simple inspection.
- Project-end learning extraction is a major reason to prefer concise archive summaries.

## Proposed

- Create or update an idea note explaining the lifecycle model:
  `request -> handoff -> note-manager/planner/implementer -> report -> review closeout -> distilled archive -> clean in-flight`.
- Treat non-empty `docs/Reports/in-flight/` as a blocker for unrelated important work until review or continuation resolves it.
- Add `docs/Reports/archive/` as the place for distilled task history and reusable learning.
- Consider making `active-context.md` unnecessary or generated from `in-flight/`.
- Start with one distilled archive level before adding separate `archive/summaries/` and `archive/raw/`.
- Later evaluate changes to `AGENTS.md`, `modes/dev-workflow/agents-bridge.md`, project-review-sync behavior, and starter docs.

## Unclear / Blocked

- Note Manager must decide whether this belongs in the existing `Task and Report Artifact Lifecycle` idea note or a new idea note.
- The exact durable note title is not fixed.
- The exact archive folder structure is not fixed.
- The exact implementation mechanism for generating or replacing `active-context.md` is not fixed.
- The cutoff between "important work" and "tiny mechanical task" may need examples or vocabulary later.

## Boundaries / Non-goals

- Do not implement workflow rule changes from this handoff alone.
- Do not edit `AGENTS.md`, `modes/dev-workflow/agents-bridge.md`, skills, templates, or starter docs from this handoff alone.
- Do not delete existing in-flight artifacts as part of this handoff.
- Do not decide the final note target or note type beyond "idea note candidate"; subject-to-note mapping belongs to Note Manager.
- Do not make handoffs mandatory for tiny mechanical tasks.
- Do not make raw artifact deletion automatic without an approved workflow decision.

## Relevant Context Already Known

- `docs/Idea Backlog/Task and Report Artifact Lifecycle.md` already discusses whether completed task packets and reports should be archived or treated as transient working artifacts.
- `docs/Reports/in-flight/handoff-context-map-active-context-templates.md` already captures related simplification thinking around `context-map.md` and `active-context.md`.
- `docs/context-map.md` currently describes `docs/Reports/in-flight/` as active workflow artifacts, not durable project knowledge.
- The local workflow contract requires persisted hard-gate artifacts under `docs/Reports/in-flight/`.

## Readiness For Note Manager

Ready for Note Manager.

This handoff preserves the user's idea, the important distinctions, the original input, likely related context, and unresolved decisions. Note Manager can now decide whether to draft a new idea note or update an existing idea note without guessing the user's intent.
