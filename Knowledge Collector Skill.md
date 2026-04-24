# Knowledge Collector Skill

Status: [[status-pending]]
Parent: [[Idea Hub]]
Related: [[clarify-intent]]
Created: 14-04-2026

## Summary

A standalone skill for bounded research and concept explanation when the main blocker is missing knowledge rather than unclear intent.

The default mode is fast conceptual understanding. Depending on the prompt, it may also include practical examples, common real-world patterns, or broader context.

## Why This Matters

Current behavior for knowledge gaps is informal: open an AI chat and ask for explanation or background research.

This idea would make that behavior more structured and project-aware by letting the skill use current notes or recent context when relevant, while still being usable as a standalone research helper.

It supports the repository's confidence-based workflow by helping the user learn before making durable note, planning, or implementation decisions.

## Core Behavior

- Return a skimmable research brief.
- Teach a concept or inform on a subject.
- Use internet research when necessary.
- Use current project notes or recent context when relevant.
- Work as a standalone skill without being coupled to `clarify-intent` in v1.

## Default Output Shape

- short topic summary
- key concepts
- common approaches or patterns
- source list
- open questions or conflicting information
- project relevance when context is provided

## Boundaries

- does not create durable notes
- does not recommend project direction
- does not act as a planner
- does not make architecture or workflow decisions
- does not get integrated into `clarify-intent` in the initial version

## Open Questions

- how strict source selection should be when official sources are limited
- whether project-context relevance should always be included when context exists
- whether a future version should allow optional handoff back into `clarify-intent`

