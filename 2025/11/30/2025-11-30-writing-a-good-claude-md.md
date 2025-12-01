# Writing a good Claude.md

- Score: 251 | [HN](https://news.ycombinator.com/item?id=46098838) | Link: https://www.humanlayer.dev/blog/writing-a-good-claude-md

### TL;DR
Claude.md is a persistently-injected onboarding file for coding agents, so it should describe a project’s purpose, architecture, and workflows using few, universally-relevant instructions. The author argues that too many rules or code snippets cause Claude to ignore the file, and recommends progressive disclosure: keep short global guidance plus separate, linked docs for specifics. HN commenters split: some advocate minimal context or just pasting relevant code, others report big gains from a curated “table-of-contents” setup, especially for autonomous agents.

### Comment pulse
- Minimal context wins on hard problems → extra comments/docs dilute finite attention; some even strip comments/whitespace for LLMs — counterpoint: a small notes file avoids repeating key instructions.
- Progressive disclosure pattern → use Claude.md as a high-density table of contents pointing to focused docs, so the agent only reads what each task needs.
- Setup vs payoff → skeptics would rather “just code” or paste snippets; others say a few hours of LLM-assisted setup amortizes across many features and bug-fixes.

### LLM perspective
- View: Treat CLAUDE.md as scarce instruction budget; reserve for invariants, not per-task recipes or style rules.  
- Impact: Teams using agents for multi-step changes or bug-hunts gain most; casual chat users may skip elaborate setup.  
- Watch next: Tooling that auto-measures instruction count, relevance, and outcome quality could turn these folk heuristics into concrete configuration recommendations.
