# Ecommerce Session Value Review Sync to Main Vault

Status: [[status-draft]]
Parent: [[Idea Hub]]
Related: [[Workflow Hub]], [[Note Manager]]
Created: 05-05-2026

---

## Idea

Use `project-review-sync` on the Ecommerce Session Value project to extract learned information that should become durable knowledge in the main vault.

This is a separate task from aligning the main vault's general note structure and agent operating policy.

## Questions

- What implementation reports, feature findings, experiment summaries, or task packets should be reviewed as the source evidence?
- Which learned information belongs in the main vault rather than only in the Ecommerce project vault?
- Should review/sync produce one context handoff per proposed main-vault note change?
- Does the main vault need alignment first before this review/sync task can run cleanly?
- Should extracted learnings become new full notes, updates to existing full notes, or pending idea notes?

## Current Thinking

- The review/sync task should remain evidence-backed and bounded to the Ecommerce Session Value project.
- The output should not directly mutate the main vault. It should identify candidate durable knowledge and route that through clarification and `Note Manager`.
- Main vault alignment may be a prerequisite, but it should stay a separate concern.

## Open Decisions

- The exact source artifacts for the Ecommerce review/sync pass.
- Whether to run this before or after creating main-vault local agent instructions.
- Whether the output should be a review report, clarified context handoff, or both.

