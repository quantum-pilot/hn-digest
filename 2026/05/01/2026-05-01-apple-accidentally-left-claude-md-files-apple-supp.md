# Apple accidentally left Claude.md files Apple Support app

- Score: 364 | [HN](https://news.ycombinator.com/item?id=47973378) | Link: https://x.com/aaronp613/status/2049986504617820551

- TL;DR  
  - Apple’s Apple Support app reportedly shipped with CLAUDE.md prompt files, unintentionally revealing internal use of Anthropic’s Claude to assist development. Commenters dissect what this says about Apple’s “rent vs build” AI strategy and the importance of running third‑party models on‑prem for secrecy. Others focus on process: whether agent instruction files belong in source control, how they should be kept out of production builds, and whether ubiquitous LLM tooling is degrading code review, software quality, and even online conversation norms.  
  *Content unavailable; summarizing from title/comments.*

- Comment pulse  
  - Apple may rely on Anthropic’s Claude, even on‑prem, instead of full in‑house LLMs → flexibility now — counterpoint: skeptics doubt leak details and Anthropic uptime.  
  - Debate on CLAUDE.md: some see it as disposable AI cruft; others treat it like README-level documentation that must be versioned yet excluded from builds.  
  - LLMs are blamed for lazier reviews, accidental leaks, and formulaic comments → calls for stricter review processes and community-level bans on AI-written discussion.

- LLM perspective  
  - View: Treat AI agent config files as first-class documentation with build exclusions and privacy reviews, rather than ad‑hoc workstation artifacts.  
  - Impact: Visible reliance on vendor LLMs normalizes hybrid “rent plus own” stacks, shifting focus to integration, governance, and contract risk.  
  - Watch next: Tooling to block AI artifacts from releases, and platform policies requiring disclosure or filtering of AI-generated conversational content.
