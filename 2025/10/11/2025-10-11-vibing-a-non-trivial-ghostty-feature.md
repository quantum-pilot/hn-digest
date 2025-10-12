# Vibing a non-trivial Ghostty feature

- Score: 246 | [HN](https://news.ycombinator.com/item?id=45549434) | Link: https://mitchellh.com/writing/non-trivial-vibing

TL;DR
Mitchell Hashimoto describes “vibing” a non‑trivial Ghostty feature: using an LLM to rapidly scaffold UI, then iterating manually and discarding weak code. HN splits between fans of AI for zero‑to‑one momentum and those who value hand‑rolled starts and stack learning; several warn that LLM prototypes look production‑ready but require rewrites. Commenters note “vibe engineering” as a better label, praise his response to the OpenAI incident, and flag Ghostty’s new AI‑use disclosure rule. Ongoing friction: missing Cmd‑F search; community prototypes exist.
Content unavailable; summarizing from title/comments.

Comment pulse
- LLMs excel at zero-to-one prototyping → fast scaffolds unblock experimentation; keep/discard bits as needed — counterpoint: others prefer hand starts to preserve originality and learning.
- LLM prototypes look finished → management overestimates readiness; unlike hand prototypes, they teach less about the stack, so expect a clean-room rewrite before production.
- Ghostty gaps dominate chatter → missing Cmd-F search; a contributor prototyped search with Claude; roadmap targets built-in search in v1.3 (Mar 2026).

LLM perspective
- View: Use LLMs for scaffolding, then rewrite critical paths; manage the prototype-to-production gap explicitly with stakeholders.
- Impact: Policies like mandatory AI disclosure improve provenance, code review focus, and calibrate community expectations on AI-generated contributions.
- Watch next: Quality bars: Ghostty search release, comparative studies of LLM-prototyped vs hand prototypes, and toolchains that capture learning while vibing.
