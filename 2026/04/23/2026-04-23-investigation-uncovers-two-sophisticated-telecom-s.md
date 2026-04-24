# Investigation uncovers two sophisticated telecom surveillance campaigns

- Score: 367 | [HN](https://news.ycombinator.com/item?id=47874814) | Link: https://techcrunch.com/2026/04/23/surveillance-vendors-caught-abusing-access-to-telcos-to-track-peoples-phone-locations-researchers-say/

## TL;DR
Citizen Lab uncovered two long-running telecom surveillance campaigns abusing core phone-network signaling to track targets worldwide. Unnamed “ghost” companies posed as carriers and routed spying via three operators (Israeli 019Mobile, UK-based Tango Networks, Airtel Jersey/Sure), exploiting legacy SS7 and partially secured Diameter protocols. A second campaign used SIMjacker-style hidden SMS to silently convert a “high-profile” phone into a tracking beacon. HN discussion centers on how such capabilities are routinely abused by insiders, states, and vendors, with little real recourse for victims.

## Comment pulse
- Emergency services face hours-long, affidavit-driven processes for urgent location lookups → contrast with vendors’ near-unfettered access—counterpoint: root cause is protocol design, not just “greed.”
- Surveillance power is regularly misused (e.g., NSA LOVEINT) → without strict privacy limits, pervasive data + AI yields personalized, unaccountable oppression.
- Insider and state abuse at telcos is common globally → staff casually query PII; Russia-style black markets sell location data; avoiding tracking is practically impossible.

## LLM perspective
- View: Telecom signaling (SS7/Diameter/SIM toolkit) is structurally unsafe; “ghost carriers” turn backbone trust into a global tracking API.
- Impact: National regulators, carriers, and surveillance vendors face pressure for audits; high-risk groups (journalists, activists, abuse victims) are most exposed.
- Watch next: Independent SS7/Diameter filtering benchmarks, SIM toolkit hardening by major operators, and concrete legal bans on commercial location-tracking intermediaries.
