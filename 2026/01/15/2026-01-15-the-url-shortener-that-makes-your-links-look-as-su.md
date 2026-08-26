# The URL shortener that makes your links look as suspicious as possible

- Score: 750 | [HN](https://news.ycombinator.com/item?id=46627652) | Link: https://creepylink.com/

### TL;DR

CreepyLink is a novelty URL shortener that deliberately makes links appear untrustworthy. That joke creates unintended behavior: commenters found several leading LLM agents unwilling to follow its outputs, while open models did, and Chrome or Firefox sometimes displayed phishing warnings or blocked them entirely. Readers wondered whether suspicious-looking redirects could deter agent-driven scraping, though ordinary training crawlers may ignore the signal. Others debated the project’s originality, generally defending repeated URL-shortener experiments as harmless fun, learning exercises, or a replacement for the defunct ShadyURL.

### Comment pulse

- Suspicion became an automation filter → several proprietary agents refused links, while GPT-OSS models followed them, exposing inconsistent safety heuristics.
- Browser defenses were less playful → Chrome and Firefox sometimes classified generated links as dangerous or deceptive and blocked access.
- Repetition does not negate value → commenters framed familiar shorteners as language-learning projects or simple toys needing no originality.

### LLM perspective

- View: The project demonstrates that URL presentation can influence automated trust decisions independently of destination content.
- Impact: Creators may gain a crude agent-deterrence signal, but users inherit serious deliverability and reputation failures.
- Watch next: Controlled tests across browsers, models, crawlers, redirect patterns, and changes in blocklists or agent policies.
