# Claude Skills

- Score: 446 | [HN](https://news.ycombinator.com/item?id=45607117) | Link: https://www.anthropic.com/news/skills

- TL;DR
  - Anthropic’s Claude Skills are composable folders of instructions, scripts, and resources—optionally executable—that Claude auto-loads when relevant across Claude apps, Claude Code, and the API. A new /v1/skills endpoint and the Code Execution Tool enable versioning and secure runtime; a guided “skill-creator” helps author SKILL.md packages. Partners tout Excel/PowerPoint/Word workflows; Anthropic flags security hygiene. HN debates utility vs. complexity creep, overlap with MCP/sub-agents, and whether auto-selecting the right skill is constrained by brief descriptions and limited long-term memory.

- Comment pulse
  - Concept sprawl slows adoption → Overlapping skills/tools/agents burn complexity budget. — counterpoint: Master the agentic loop; Skills are just loadable instruction+code.
  - Auto-selection is brittle → Models rely on short skill blurbs; no lived experience. Some argue it's a context/memory issue, not intelligence.
  - Overlap with MCP/sub-agents → Feels redundant; could be prompts. Others: MCP wraps APIs, Skills add just-in-time instructions, sub-agents manage context/tokens.

- LLM perspective
  - View: Skills productize context-packaged instructions + code-exec, auto-loaded per task across apps/API—reducing prompt bloat and bespoke glue.
  - Impact: Teams can package workflows once and reuse across surfaces; console and versioning ease rollout; IT can distribute org-wide.
  - Watch next: Measure auto-selection accuracy, latency, and token savings; publish security sandbox guarantees; clarify interoperability with MCP, sub-agents, and persistent memory.
