# Scaling LLMs to Larger Codebases

- Score: 191 | [HN](https://news.ycombinator.com/item?id=46354970) | Link: https://blog.kierangill.xyz/oversight-and-guidance

### TL;DR
The article argues that scaling LLMs to large codebases isn’t about bigger models but about better **guidance** (context, architecture, prompt libraries) and **oversight** (human design skill, verification, guardrails). To maximize “one-shotting” useful code instead of rework, teams should: maintain a living prompt library tailored to their codebase; keep code clean, modular, and well-mapped for agents; and encode architectural rules as automated checks. HN comments share practical agent workflows, frustrations with ignored context, and experiments reorganizing repos for LLM-friendly modularity.

---

### Comment pulse
- Multi-step agent loops (research → plan → clear → implement → test) help on complex changes; others rely on simpler prompts, but many report brittle, inconsistent reasoning. — counterpoint: newer agents with auto-exploration may reduce elaborate planning rituals.  
- Iteratively refining CLAUDE.md-style prompt libraries yields high ROI for navigation and summaries, yet models often ignore these docs, forcing users to repeatedly re-anchor them.  
- Some restructure repos (e.g., small, isolated subprojects) to bound agent context, hypothesizing that LLM-optimized modularity will push new software organization patterns.

---

### LLM perspective
- View: Treat LLMs as code generators inside a designed environment: explicit conventions, rich local docs, and automated architectural guardrails.  
- Impact: Favors teams that invest in cleanliness, modularity, and design literacy over quick wins from raw model capability.  
- Watch next: IDEs that manage per-repo prompt libraries, enforce import/architecture rules, and measure one-shot success on large, messy monorepos.
