# The cult of vibe coding is dogfooding run amok

- Score: 446 | [HN](https://news.ycombinator.com/item?id=47664912) | Link: https://bramcohen.com/p/the-cult-of-vibe-coding-is-insane

### TL;DR

Bram Cohen argues that Anthropic’s leaked Claude code exposes dogfooding taken past reason: a team committed to “vibe coding” allegedly avoided inspecting source, allowing duplicated agents and tools to accumulate. Pure automation is a myth, he says, because humans still create plans, skills, rules, and language scaffolding. His preferred workflow uses human review and discussion to surface edge cases, then lets the model plan and execute cleanup. AI can cheaply reduce technical debt; poor software quality comes from declining to supervise and refine it, not from AI assistance itself.

### Comment pulse

- Claude Code’s popularity suggests messy code need not block short-term success — counterpoint: maintainability determines whether a product can evolve over years.
- Supervision is contextual: developers favored deep understanding for novel algorithms, stronger guardrails for middleware, and looser automation for routine interfaces.
- “Vibe linting” drew enthusiasm: models cheaply hunt duplication, inconsistent serialization, complex functions, weak tests, documentation gaps, and subtle bugs under human review.

### LLM perspective

- **View:** AI shifts refactoring’s cost curve but cannot choose quality priorities without human attention and product context.
- **Impact:** Teams can ship first drafts faster while making disciplined second passes cheaper; deadlines still determine whether those passes happen.
- **Watch next:** Maintenance velocity, defect rates, review burden, codebase size, and whether agent-generated cleanup survives independent verification.
