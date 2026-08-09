# Anatomy of the .claude/ folder

- Score: 349 | [HN](https://news.ycombinator.com/item?id=47543139) | Link: https://blog.dailydoseofds.com/p/anatomy-of-the-claude-folder

### TL;DR

The guide maps Claude Code configuration into project-shared and personal layers: `CLAUDE.md` for concise instructions, `.claude/rules/` for modular or path-scoped guidance, settings files for tool permissions, skills for reusable workflows, agents for isolated specialists, and home-directory files for global preferences and session memory. It recommends starting with `/init`, keeping core guidance short, and adding machinery only for repeated needs. HN broadly agrees targeted configuration can compound context, but warns against a productivity-system rabbit hole; a cited documentation update says legacy commands now share the skills model.

### Comment pulse

- Start empty and learn the harness first → extra skills add context and maintenance — counterpoint: recurring domain work can justify targeted configuration.
- Custom log, accounting, and large-codebase workflows avoid repeated context → users report step-change benefits beyond production code generation.
- Keep instructions experiential and short → encode observed thrashing, then separate planning from implementation and clear accumulated context.

### LLM perspective

- **View:** Treat configuration as executable team knowledge, added only after repeatable friction appears.
- **Impact:** Teams gain consistent behavior but inherit review, security, and version-drift obligations.
- **Watch next:** Commands-and-skills convergence, headless-agent permissions, secret isolation, and cross-harness standards.
