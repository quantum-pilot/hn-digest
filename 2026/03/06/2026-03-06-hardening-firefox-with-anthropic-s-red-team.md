# Hardening Firefox with Anthropic's Red Team

- Score: 446 | [HN](https://news.ycombinator.com/item?id=47273854) | Link: https://www.anthropic.com/news/mozilla-firefox-security

### TL;DR
Anthropic used Claude Opus 4.6 to scan Firefox, collaborating with Mozilla’s security team. In two weeks, Claude found 22 new vulnerabilities, 14 rated high-severity—around 20% of Firefox’s 2025 high-severity bugs—by analyzing ~6,000 C++ files and submitting 112 reports with testcases and candidate patches. Claude is currently much better at finding and helping fix bugs than exploiting them: after hundreds of attempts and $4k in runs, it produced only two crude, non-sandbox-bypassing exploits. HN discussion focuses on practical AI-audit workflows, reliability limits, and marketing vs. substance.

---

### Comment pulse
- AI audits are now table stakes for open source → maintainers should assume attackers already ran LLM scans; use models plus self-review to cut false positives and document intent.  
- Some see the post as vague marketing → lack of bug detail feels hand-wavy — counterpoint: Mozilla advisories and Anthropic exploit writeup show several genuinely serious issues.  
- Mixed practitioner experience → LLMs excel at “local” pattern bugs and tooling setup, but miss complex feature interactions and can be confidently wrong, so PoCs and skepticism are essential.

---

### LLM perspective
- View: AI has flipped vuln discovery from artisanal to semi-automated; the bottleneck moves to triage, validation, and coordinated disclosure.  
- Impact: Browser vendors and OSS maintainers must integrate AI-assisted security and harden review pipelines, not just code.  
- Watch next: Standard prompts/tooling for AI audits, CI-integrated patch verifiers, and policies limiting direct exploit generation while enabling defensive research.
