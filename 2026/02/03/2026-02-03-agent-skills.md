# Agent Skills

- Score: 348 | [HN](https://news.ycombinator.com/item?id=46871173) | Link: https://agentskills.io/home

### TL;DR

Agent Skills defines an open folder format bundling instructions, scripts, and resources that compatible agents discover and load on demand. The goal is portable, version-controlled domain knowledge, repeatable workflows, and capabilities reusable across products without filling every prompt’s context. Commenters split over whether this is valuable standardization or merely README files with branding. Practitioners reported the strongest results from explicit, self-contained workflows with precise triggers and deterministic scripts; skeptics expect larger contexts and smarter base models to reduce the need, and asked for controlled productivity and consistency evaluations.

### Comment pulse

- Discovery is the differentiator → a compact index lets agents load relevant procedures only when needed instead of front-loading every instruction.
- Workflow skills outperform vague guidance → checklists, scripts, explicit triggers, and verification behave like reusable subroutines; generic best practices are often ignored.
- Standardization aids portability → counterpoint: competing hidden folders, commands, READMEs, and rapid model progress make early formalization look premature.

### LLM perspective

- View: Skills formalize procedural documentation plus discovery; their lasting value depends more on reliable activation and execution than folder syntax.
- Impact: Teams can version organizational practice across agents, but must maintain, test, secure, and de-duplicate another automation layer.
- Watch next: Cross-product paths, permission semantics, skill evaluations, regression tests, provenance, script sandboxing, automatic activation, and compatibility guarantees.
