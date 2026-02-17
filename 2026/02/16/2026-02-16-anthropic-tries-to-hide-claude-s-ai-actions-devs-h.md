# Anthropic tries to hide Claude's AI actions. Devs hate it

- Score: 346 | [HN](https://news.ycombinator.com/item?id=47033622) | Link: https://www.theregister.com/2026/02/16/anthropic_claude_ai_edits/

- TL;DR  
  - Anthropic changed Claude Code’s terminal output to collapse which files it reads/edits into vague summaries, claiming reduced “noise” for longer, more agentic runs. Developers argue this hides crucial context needed to catch mistakes, control security boundaries, and stop token burn, especially while models remain unreliable. Pushback on GitHub and Hacker News forced a partial rollback via a redefined verbose mode, but many still see growing opacity, poor UX choices, and risk of driving devs to competing tools.

- Comment pulse  
  - Need full file-level logs → oversight lets devs interrupt runaway reads/writes, secure sensitive paths, and avoid wasting tokens; agent-swarm future doesn’t remove today’s error rates.  
  - Anthropic’s “verbose” repurposing → now shows paths but omits deep traces; users complain words and modes no longer match expectations, making debugging and trust harder.  
  - Strategic risk for Anthropic → dev-focused positioning clashes with opacity; users cancel subscriptions or switch to OpenCode—counterpoint: non-dev “co-work” users may still prefer simplified views.

- LLM perspective  
  - View: Transparency should be a per-role toggle: human-in-the-loop coding needs granular traces; autonomous agents can default to collapsed summaries.  
  - Impact: If dev trust erodes, Anthropic risks losing high-value power users to open competitors, despite strong underlying models.  
  - Watch next: Watch for explicit “observability” features: configurable logging levels, reversible runs, and standards for AI agent audit trails in regulated environments.
