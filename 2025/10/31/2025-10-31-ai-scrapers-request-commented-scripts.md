# AI scrapers request commented scripts

- Score: 175 | [HN](https://news.ycombinator.com/item?id=45773347) | Link: https://cryptography.dog/blog/AI-scrapers-request-commented-scripts/

### TL;DR

A site operator found bots requesting a JavaScript file referenced only inside an HTML comment, despite a crawler ban in `robots.txt`. The behavior suggests some scrapers search raw text for URLs rather than interpreting the DOM, although their purpose and operators were not established. The author proposes using such hidden or commented links as detection traps, then blocking offenders with fail2ban or serving adversarial payloads. Decompression bombs and training-data poisoning are discussed as riskier countermeasures, not demonstrated remedies.

### Comment pulse

- Operators agreed naive URL extraction is plausible and discussed byte limits, timeouts, and hidden bait as crawler defenses.
- Debate centered on consent: public GET access permits requests, while deceptive identities, heavy load, and ignored policies undermine implied permission.

### LLM perspective

- View: Comment-only requests are a useful bot signal, but they do not prove LLM training or malicious intent.
- Impact: Low-cost traps can improve observability; retaliatory payloads introduce operational, ethical, and collateral-damage risks.
- Watch next: Measure false positives, request rates, user-agent consistency, and whether blocking materially reduces server costs.
