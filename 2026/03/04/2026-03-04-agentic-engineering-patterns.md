# Agentic Engineering Patterns

- Score: 475 | [HN](https://news.ycombinator.com/item?id=47243272) | Link: https://simonwillison.net/guides/agentic-engineering-patterns/

### TL;DR

Simon Willison’s evolving guide catalogs practical patterns for coding agents: Git discipline, subagents, test-first work, browser-driven QA, durable notes, code comprehension, and avoiding unreviewed output. Its premise is that generated code is cheap while reliable, maintainable code still costs judgment. HN agreed that executable feedback and explicit constraints are decisive, but worried code generation merely moves the bottleneck into review. Commenters also split on whether named patterns clarify an unfamiliar, low-affordance interface or invite another consulting vocabulary around familiar engineering practices.

### Comment pulse

- Deterministic test harnesses keep agent loops grounded; mutation and property-based testing expose tautological tests that coverage metrics reward.
- Record rejected approaches and reasons, not just decisions → code preserves chosen paths, while invisible constraints otherwise get rediscovered.
- Teams report a sharp task-fit divide — counterpoint: recent models and iterative reviewer agents have expanded the viable side.

### LLM perspective

- **View:** Agent throughput converts code review, architecture, and security assurance from secondary chores into the production constraint.
- **Impact:** Teams need stronger pre-commit automation and smaller changes; reviewers need authority to reject merely functional code.
- **Watch next:** Review latency, escaped defects, mutation scores, codebase growth, and evidence that documented patterns improve ownership.
