# Writing a good Claude.md

- Score: 251 | [HN](https://news.ycombinator.com/item?id=46098838) | Link: https://www.humanlayer.dev/blog/writing-a-good-claude-md

### TL;DR

A useful `CLAUDE.md` or `AGENTS.md` should briefly onboard a stateless coding agent to a project’s what, why, and how: architecture, purpose, workflows, and verification. Because the file enters every session, the author recommends universally applicable instructions, progressive disclosure through pointers to task-specific documents, and deterministic linters rather than prose style rules. Auto-generated files risk persistent mistakes. Commenters agreed that excess context dilutes attention, but disputed how much special agent documentation is needed versus focused prompts, ordinary READMEs, code comments, or direct file selection.

### Comment pulse

- Context-minimalists → hard tasks benefit from high information density and little irrelevant commentary.
- Table-of-contents approach → a short root file can route agents to specialized documentation only when relevant.
- Setup skepticism → some prefer conversational file selection — counterpoint: recurring constraints otherwise require repeated onboarding.

### LLM perspective

- View: The best agent file is an index of durable constraints, not an encyclopedia or behavior patch log.
- Impact: Teams can reduce repeated guidance without consuming every session’s attention budget.
- Watch next: Evaluate task success, ignored instructions, token use, and stale pointers across different models and repositories.
