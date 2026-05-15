# Note Manager Escalation Routing

Status: [[Tags/status-draft]]
Type: [[design-note]]
Parent: [[note-manager]]
Related: [[note-manager]], [[Note Manager Write Authorization Model]], [[Note Manager Bundled Intake and Subject Mapping]], [[clarified-context-handoff]]
Created: 2026-05-15
Last Reviewed: 2026-05-15
Source: modes/dev-workflow/skills/dw-note-manager/SKILL.md
Project Subjects:
Tasks:
Reports:

---

## Design Scope

When Note Manager acts versus routes back to `clarify-intent`, what constitutes sufficient decision confidence to proceed, why certain upstream input types are not valid write triggers, and what a valid upstream artifact looks like.

## Context

Note Manager is the terminal role in the ideation-to-note path. It receives input from `clarify-intent` (clarified context handoffs), from `review-sync` (compact proposal tables), and from direct user requests. Each source arrives at Note Manager with a different confidence level. The escalation model defines the minimum bar for Note Manager to act rather than defer.

The failure mode being avoided: Note Manager proceeding on weak input and producing notes with wrong scope, wrong type, wrong target, or embedded ambiguity — problems that are hard to detect at write time and expensive to correct later across the vault.

## Chosen Design

**Decision confidence threshold:**

Note Manager must be able to safely choose all of the following before acting:
- the note action (create or update)
- the target note (for updates) or title and type (for creates)
- the note type
- the durable meaning — what this note is actually asserting, not just what was discussed

If any of these cannot be determined safely from the supplied context, Note Manager escalates to `clarify-intent` rather than improvising.

**Escalation triggers:**

- Input is raw review-sync output, implementation context, or a note-change proposal that has not been clarified
- The durable subject is still forming or weakly defined
- The supplied context is insufficient to choose a note type responsibly
- A requested update depends on notes that were not provided
- The correct note action cannot be determined without broader vault discovery
- The requested note target is ambiguous and Note Manager would be guessing

**What constitutes a valid upstream artifact:**

- A `clarified-context-handoff` from `clarify-intent` with a clear durable subject and interpretation basis
- A compact review/sync proposal-table row where target, action, evidence, proposed change, uncertainty, constraints, and route are all present
- A direct user request that is clear enough to choose action, target, type, and meaning without inference

**Raw review-sync output is not write approval.** A documentation sync analysis or review report describes what might need to change; it does not authorize Note Manager to apply those changes. The proposal table — reviewed and approved — is the authorization surface.

**When `clarify-intent` produces a `ready_for_note_manager` handoff** and the relevant note context is supplied, Note Manager proceeds without waiting for a separate phase-switch approval. The approval gate applies to the resulting draft or durable-write decision.

## Rationale

The escalation threshold is about note identity, not prose completeness. A note with missing body sections can be filled in later; a note with the wrong target, wrong type, or wrong durable meaning requires a corrective update that is harder to authorize and track.

The distinction between raw review output and an approved proposal table is load-bearing. Review output is analysis — it describes the state of the vault and what may need updating. An approved proposal table is a bounded authorization — it specifies what to change, why, and under what constraints. Treating them as equivalent would allow analysis to silently become writes.

The `clarify-intent` → Note Manager path is designed for exactly the cases where raw input is not sufficient: ambiguous intent, weak durable subject, unclear note action. Routing through `clarify-intent` first converts raw intent into a structured handoff that Note Manager can act on safely.

## Alternatives Considered

**Lower confidence threshold (act more, escalate less)**: reduces friction and round-trips. Rejected because the cost of a wrong note landing in the vault — wrong scope, wrong type, embedded ambiguity — is higher than the cost of one extra clarification round. Note Manager is not a drafting assistant; it is a bounded gate.

**Higher confidence threshold (always require a full clarified handoff)**: maximum safety, but blocks direct user requests that are already clear enough to act on. Rejected because many direct requests ("update the status on X", "add a link to Y") are unambiguously actionable without a full clarification pass.

## Constraints

- Note Manager must not run semantic search or broad vault discovery as its own escalation-avoidance strategy. If the target cannot be determined from supplied context, the correct response is to escalate, not to search.
- Escalation must state: the blocking ambiguity, why Note Manager would be guesswork here, and the minimum clarification needed next.
- Note Manager must not silently resolve ambiguity by choosing the most plausible target. Guessing is not a substitute for clarification.

## Technical Shape

Escalation returns a structured message to the upstream role, not a partial draft. It does not produce note content when decision confidence is not met. The return states the blocking ambiguity clearly so `clarify-intent` can resolve it with the minimum necessary clarification pass.

## Impacted Project Subjects

- [[note-manager]] — primary subject
- [[Note Manager Bundled Intake and Subject Mapping]] — escalation applies per-row in multi-subject bundles

## Open Questions

## Review Notes
