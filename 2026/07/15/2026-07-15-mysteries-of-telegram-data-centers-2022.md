# Mysteries of Telegram Data Centers (2022)

- Score: 238 | [HN](https://news.ycombinator.com/item?id=48920475) | Link: https://dev.moe/en/3025

### TL;DR

A 2022 reverse-engineering investigation explains Telegram’s five logical data centers and why public lookup bots appeared to find no users on DC2 or DC3. Accounts were assigned by registration phone-country code; CDN-based bots confused DC2 with colocated DC4 and DC3 with DC1 because they shared web domains. Login migration errors and uploaded-file locations showed DC2 was active, while tests across 10,000 numbers suggested DC3 stopped registrations and moved users to DC1. HN added reports of DC2 outages, debated the scheme’s simplicity, and raised unverified infrastructure-security concerns.

### Comment pulse

- Regional pain differed → Chinese communities complain about DC5 downtime, while Russian- and Ukrainian-speaking technical groups reportedly say the same about DC2.
- Architecture split opinion → critics saw custom routing and debt — counterpoint: defenders called a country map simpler than per-user master election.
- Trust concerns overshadowed topology → one commenter alleged links to an FSB-associated infrastructure operator, without supporting evidence reproduced in the discussion.

### LLM perspective

- **View:** Opaque infrastructure rewards triangulation; one protocol surface may reflect storage, routing, or presentation rather than account placement.
- **Impact:** Bot operators need protocol-grounded tests; users cannot infer residency or availability from CDN hostnames alone.
- **Watch next:** Repeat country-code probing and migration checks, since the documented behavior dates to 2022 and Telegram remains opaque.
