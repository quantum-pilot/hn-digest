# LinkedIn checks for 2953 browser extensions

- Score: 234 | [HN](https://news.ycombinator.com/item?id=46904361) | Link: https://github.com/mdp/linkedin-extension-fingerprinting

### TL;DR
LinkedIn’s site actively probes for thousands of specific browser extensions by attempting to load their web‑accessible resources, effectively building a per‑user “extension fingerprint.” This appears mainly aimed at detecting scrapers and automation tools that monetize LinkedIn’s data, but it also expands LinkedIn’s already substantial tracking and profiling capabilities. Firefox users are largely shielded because it randomizes per‑install extension URLs, blocking straightforward probing. HN discussion focuses on privacy risks, LinkedIn’s data‑broker role, and workarounds or mitigation techniques.

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Firefox design blocks this fingerprinting → randomized moz-extension IDs prevent mapping resources to specific extensions — counterpoint: unique per‑browser IDs might still be trackable if ever exposed.
- Probed extensions are mostly scrapers/automation tools → LinkedIn fights abuse, but critics note its own massive data brokering and likely TOS‑violating metadata collection.
- Console errors confirm probing → LinkedIn seems to log matches to CSV for later fingerprinting, with no visible user benefit or explicit disclosure.

---

### LLM perspective
- View: Extension-based probing is becoming a quiet but powerful fingerprinting vector; UX side-effects (console noise) are just collateral.
- Impact: Scraper operators will adapt; privacy-conscious users gain another reason to prefer Firefox or hardened Chromium forks.
- Watch next: Browser vendors may restrict web-accessible resources, standardize randomization, or mandate user consent for extension detection.
