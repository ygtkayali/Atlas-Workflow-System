# Main Vault Note Structure and Agent Context

Status: [[status-settled]]
Parent: [[Idea Hub]]
Related: [[Workflow Hub]], [[Note Manager]], [[Main Vault Fleeting Notes and Source Material Workflow]]
Created: 05-05-2026
Last Reviewed: 2026-05-05

---

## Decision

The main vault should use folders for human readability, not as the primary governance model.

The primary governance model is the note graph:
- intentional links,
- backlinks,
- note-based tags,
- and explicit one-way or two-way relationships.

Folders should make the vault easier to scan, but they should not define knowledge hierarchy, ownership, or domain boundaries.

## Base Folder Structure

The base main-vault folder structure is:

- `Fleeting notes` for Idea Notes and early capture.
- `Tags` for note-based tags, matching the current workflow repo pattern.
- `Main Hubs` for hub notes.
- `Templates` for note templates.
- `Full notes` for durable notes that are already created and do not belong to the other base folders.

## Folder Boundaries

Folder placement and note type are separate concepts.

A note's type, status, relationships, and operational meaning should come from metadata and links, not from its folder alone.

Do not create domain hierarchy folders such as `Backend notes` just to group related subjects. Domain relationships should be handled through links, tags, hubs, and backlinks.

## Project-Specific Folders

Individual projects may propose additional folders when the project type makes them useful for human readability.

Examples:
- a test-heavy project may use a `Tests` folder,
- a feature-oriented project may use a `Features` folder,
- a reporting-heavy project may use a `Reports` folder.

These folders should be proposed or constrained in the project's local `AGENTS.md` when they affect agent behavior.

Project-specific folders should remain readability aids. They should not replace graph-based governance.

## Agent Context

Agents should treat the folder structure as a navigation aid.

When deciding note meaning, scope, relationship, or update responsibility, agents should rely on:
- local `AGENTS.md`,
- note metadata,
- status tags,
- explicit links,
- backlinks when relevant,
- and supplied task context.

Agents should not infer rigid hierarchy from folder placement.
