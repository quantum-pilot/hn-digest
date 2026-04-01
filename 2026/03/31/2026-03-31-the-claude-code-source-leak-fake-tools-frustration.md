# The Claude Code Source Leak: fake tools, frustration regexes, undercover mode

- Score: 652 | [HN](https://news.ycombinator.com/item?id=47586778) | Link: https://alex000kim.com/posts/2026-03-31-claude-code-source-leak/

### TL;DR

- Anthropic accidentally shipped Claude Code’s full CLI source via a source map, exposing internal mechanisms: anti‑distillation “fake tools”, Bun-level API attestation, regex frustration detection, heavy prompt‑cache engineering, and an unreleased KAIROS autonomous agent mode. The most contentious discovery is “undercover mode”, which strips AI attribution and bans mentioning Claude in public commits, raising accountability concerns. HN discussion focuses on hidden AI authorship, aggressive DMCA takedowns, and whether repeated leaks are starting to undermine trust in Anthropic.

### Comment pulse

- Undercover mode hides AI authorship → prompt forbids “Claude Code” and Co‑Authored‑By in public commits; critics call it deceptive, defenders say it just reduces noise.  
- Pattern of mishaps hurts trust → back-to-back Mythos and Claude Code leaks plus usage-limit issues make some wary of giving Anthropic access to proprietary repos.  
- Anthropic’s DMCA response rankles → GitHub forks without leaked code reportedly removed, seen as futile attempt to “unring the bell” and punish contributors.

### LLM perspective

- View: LLM developer tools now blend IP protection, behavior obfuscation, and nudges about how users disclose or conceal AI-generated contributions.  
- Impact: Competitors gain roadmap insight; enterprises may reevaluate security posture; open-source projects will push harder on explicit AI-attribution norms.  
- Watch next: How Anthropic revises attribution policies, enforces DMCA, and whether KAIROS-like autonomous agents ship in mainstream developer tooling.
