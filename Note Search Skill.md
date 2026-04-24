# Note Search Skill

Status: [[status-settled]]
Parent: [[Agent Roles Hub]]
Related: [[Local Note Search Script]]
Created: 18-04-2026
Last Reviewed:
Source:
Decisions:
Dependencies:
Tasks:

---

## Summary

Note Search Skill` is the shared note-retrieval interface intended for reuse across other Codex skills.

Its current role is narrow:
- provide one stable skill entry point for note retrieval
- call the global local search script
- keep retrieval access centralized so future search changes do not require every caller skill to change independently

## Details

The current version of this skill does not implement retrieval logic itself.

Instead, it wraps the global script at:

`~/.codex/tools/local_note_search.py`

Current expectations:
- accept the retrieval need from another skill
- call the shared script with the appropriate seed note input
- return candidate note paths from the script result
- keep the calling surface stable even if the underlying search behavior evolves later

This note should treat the skill as the interface layer, while the script remains the current retrieval engine.

That separation supports:
- easier maintenance
- one controlled integration point for other skills
- easier future upgrades to search behavior without rewriting every caller

## Boundaries

The current version of `Local Note Search Skill` should not:
- own ranking or graph traversal logic directly
- introduce free-text retrieval behavior
- add semantic or embedding-based search
- broaden into a general autonomous context-selection system
- modify notes automatically

## Current Dependency

The current skill depends on the global script:

- `~/.codex/tools/local_note_search.py`

If the script interface changes later, the skill should absorb that change so other skills can continue using one stable search entry point.

## Open Questions

- What exact trigger wording should be used for this skill?
- Should the skill expose only path-based seed input at first, or also allow title-based resolution through the script?
- When the retrieval system evolves later, which behaviors should remain hidden behind the same skill interface?
