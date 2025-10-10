# Two things LLM coding agents are still bad at

- Score: 305 | [HN](https://news.ycombinator.com/item?id=45523537) | Link: https://kix.dev/two-things-llm-coding-agents-are-still-bad-at/

- TL;DR
  - The author flags two gaps in LLM coding agents: they don’t truly cut/copy‑paste (they rewrite from memory, causing drift) and they rarely ask clarifying questions, preferring assumption‑driven brute force. HN adds concrete failures: hallucinated URLs, silent regex/date edits, and citation loops to users’ own comments. Agents often lack full‑repo context and stumble in monorepos, yielding bloat and fragile workflows. Suggested mitigations: deterministic IDE refactors, explicit “AI‑use” PR notes, larger-context/tools, and test-first gating. Some report wins with strict scaffolding; most warn against unsupervised refactors.

- Comment pulse
  - LLM citations are circular or fabricated → ask for sources, force research/sorting prompts. — counterpoint: even curated, grounded runs still confabulate confidently.
  - Rewrite-not-paste causes silent drift → hallucinated URLs, regex tweaks; code review must change; add “AI-use” notes in PRs to focus scrutiny.
  - Limited repo awareness derails agents → misnavigated monorepos, reinvented helpers; workarounds: strict CLAUDE.md, helper commands, deny-lists; otherwise bloat passes review under time pressure.

- LLM perspective
  - View: Weak tool primitives and poor clarification behavior, not just model quality, drive most failure modes.
  - Impact: Higher review burden, fragile refactors, and duplicated code offset perceived productivity gains.
  - Watch next: Native copy/move tools, repo-scale retrieval/planning, and policies requiring AI-use disclosure and test-gated changes.
