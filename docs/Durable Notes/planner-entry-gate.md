# Planner Entry Gate

Status: [[Tags/status-draft]]
Type: [[design-note]]
Parent: [[planner-agent]]
Related: [[planner-agent]]
Created: 2026-05-15
Last Reviewed: 2026-05-15
Source: modes/dev-workflow/skills/project-planner/SKILL.md
Decisions:
Dependencies:
Tasks:

---

The planner entry gate is a four-question test that determines whether a request needs planning before implementation, or whether implementation can begin directly.

A request is ready for direct implementation only when all four answers are yes:

- **Clear objective** — the intended outcome is explicit
- **Bounded scope** — the area to change is known and narrow
- **Known files** — the exact files to edit are identifiable without discovery
- **Concrete acceptance** — success criteria are testable without interpretation

If any answer is no, the request needs planning before implementation begins. If all four pass, the planner surfaces this to the user and lets them decide whether to plan or proceed directly — it does not unilaterally skip planning.

The test is intentionally binary across all four dimensions. A partial pass — where three of four questions can be answered — still leaves an implementation gap. The gate forces that gap into the open rather than letting it reach the implementer as an unresolved assumption.

The tradeoff is explicit: a gate that is too strict over-plans trivial tasks; one that is too permissive means implementers receive packets that require guesswork to execute. The gate is calibrated at the point where any unanswered question materially affects what the implementer needs to do.
