# Dev Workflow Documentation Model

Status: [[Tags/status-settled]]
Type: [[design-note]]
Parent:
Related: [[note-manager]], [[clarify-intent]], [[Main Vault Note Structure and Agent Context]], [[Workflow CLI Mode System]]
Created: 2026-05-08
Last Reviewed: 2026-05-14
Source: clarified context handoff from documentation model discussion
Project Subjects:
Tasks:
Reports: `docs/In-flight/report-technical-project-documentation-governance.md`

---

## Design Scope

This note defines the core documentation creation model for `dev-workflow`.

It covers how technical project documentation should move from rough ideas into durable project knowledge, how local design choices and technical details should be preserved, and when broader design documentation is useful.

It does not define task/report lifecycle details, implementation packet structure, or low-level note metadata rules.

## Context

Technical project documentation in `dev-workflow` needs to support both AI maintenance and human understanding.

The documentation should help a future reader understand:
- what exists,
- why it exists,
- how it works,
- and how to continue safely.

This means documentation should not be only architecture notes, only task notes, or only implementation references. It should preserve the project outline, design rationale, technical shape, and execution trace in a connected form.

## Chosen Design

Documentation should follow a layered lifecycle:

```text
draft idea, plan, or question
-> active project subject
-> local design choices and technical shape
-> task and report trace when implemented
-> broader design note when a subject set needs one shared explanation
```

Ideas begin as rough backlog material. When an idea becomes active project knowledge, it should become a durable project subject rather than automatically becoming a broad design note.

Project subject documentation should preserve the local thought process for one feature, workflow behavior, implementation concept, or action area. It should include why the subject exists, current direction, design choices, technical shape, implementation notes, open questions, and related task/report history.

Broader design notes should be created when a design spans multiple project subjects, explains a coherent system area, or constrains future work. A broader design note should not replace the local design-choice trail inside related project subject notes.

## Rationale

This model keeps documentation useful without turning it into ceremony.

Backlog notes preserve early uncertainty. Project subject notes preserve the local reasoning that led to a feature or workflow behavior. Design notes explain broader system behavior only when a single-source explanation is useful.

The result should be readable for humans and maintainable by AI because the documentation gives small, traceable surfaces rather than one large generic project document.

## Alternatives Considered

One rejected alternative was treating every accepted idea as a design note. That would make design documentation too broad and would hide the local thought process that belongs with the subject itself.

Another rejected alternative was creating a separate learning-note type. The learning value should come from every note being clear about what was done, why it was done, and how it works.

Another rejected alternative was treating technical documentation as mostly architecture. Architecture and design matter, but they are not enough without technical shape, commands, file paths, lifecycle details, and implementation/report links.

## Constraints

- Do not create a separate learning-tool note type.
- Do not promote every idea directly into a broad design note.
- Do not move every discovered design choice out of the project subject where the thinking happened.
- Do not copy large source code blocks into documentation when links, commands, or small contract examples are enough.
- Keep task packets and reports as execution artifacts managed separately from durable project knowledge.
- Keep folders as readability aids; note meaning should come from content, metadata, and links.

## Technical Shape

Good technical project notes should include enough detail to reconstruct understanding later:
- important commands,
- configuration shape,
- key file paths,
- lifecycle flows,
- public entry points,
- interfaces or contracts,
- small snippets only when they clarify usage or behavior,
- and links to implementation files or reports when the code itself is the source of truth.

For example, documentation for a CLI feature should explain what the command is responsible for, what it deliberately does not own, what files implement it, what configuration it reads or writes, how to run it, and which design choices shaped those boundaries.

## Impacted Project Subjects

- Workflow note creation and update behavior
- Documentation synchronization after implementation
- Feature/project subject promotion from backlog material
- CLI and mode documentation as reusable technical examples
- Future task and report artifact lifecycle work

## Open Questions

- How much of this model should be reflected in future starter templates versus role instructions?
- Should broader design notes be indexed from a dedicated design-oriented hub later, or is linking from related subjects enough for now?

## Review Notes

This note was created from a clarified conversation handoff after the documentation model had already been discussed and narrowed.

2026-05-14: `docs/In-flight/report-technical-project-documentation-governance.md` sharpened the reusable and synced Project Subject and Design Note templates to reflect this model. No new note type was introduced, and accepted ideas still should not automatically become design notes.
