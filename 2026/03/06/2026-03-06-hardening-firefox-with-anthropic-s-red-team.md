# Hardening Firefox with Anthropic's Red Team

- Score: 446 | [HN](https://news.ycombinator.com/item?id=47273854) | Link: https://www.anthropic.com/news/mozilla-firefox-security

### TL;DR

In two weeks, Claude Opus 4.6 scanned 6,000 Firefox C++ files and submitted 112 reports; Mozilla recognized 22 vulnerabilities, including 14 high-severity flaws, and fixed most in Firefox 148. Exploitation proved harder: several hundred attempts costing about $4,000 yielded only two crude demonstrations in an environment stripped of Firefox’s sandbox. Anthropic says defenders currently retain an advantage and recommends task verifiers, minimal tests, proofs of concept, regression suites, and candidate patches. HN welcomed the scale but warned about false positives, unclear impact, and models confidently missing nonlocal security boundaries.

### Comment pulse

- Cheap audits now feel mandatory because attackers can run them too — counterpoint: unverified findings can bury maintainers in automated noise.
- Models excel at local unsafe patterns; cross-feature business logic and imperfect security boundaries remain harder to assemble and judge.
- Reproducible crashes and proofs of concept make triage tractable; static prose alone repeats traditional analysis’s false-positive burden.

### LLM perspective

- **View:** Tool-backed verification, not raw model eloquence, converted mass crash discovery into maintainable security work.
- **Impact:** Open-source teams gain scalable fuzzing help but must budget scarce human triage and patch-review capacity.
- **Watch next:** Sandbox-escape performance, exploit costs, nonlocal bug discovery, disclosure throughput, patch regressions, and access safeguards.
