# Investigation uncovers two sophisticated telecom surveillance campaigns

- Score: 367 | [HN](https://news.ycombinator.com/item?id=47874814) | Link: https://techcrunch.com/2026/04/23/surveillance-vendors-caught-abusing-access-to-telcos-to-track-peoples-phone-locations-researchers-say/

### TL;DR

Citizen Lab identified two covert surveillance campaigns that exploited telecom signaling to locate phones. Unnamed “ghost” carriers hid behind access through 019Mobile, Tango Networks U.K., and Airtel Jersey. One vendor tried unauthenticated SS7 queries, then weakly implemented Diameter protections, across years and countries; another used invisible SIMjacker commands against a high-profile target. Researchers say these are two cases among millions of attacks. Hacker News focused on how commercial and state access invites insider abuse, stalker tracking, and black markets, contrasting effortless covert lookup with slow, affidavit-gated emergency requests.

### Comment pulse

- Pervasive surveillance will not remain professional: commenters cited intelligence and telecom employees abusing privileged access for personal snooping or stalking.
- Strong logging could expose irrelevant lookups — counterpoint: one telecom insider claimed the practice was once too widespread for easy enforcement.
- Some blamed profit-driven vendors; others argued protocol weaknesses and criminal operators, not corporate culture alone, explain the abuse.

### LLM perspective

- **View:** Telecom federation turns weak carriers into global surveillance entry points, so network trust needs continuous constraint and auditing.
- **Impact:** Victims cannot reliably escape by swapping phones or SIMs when attackers correlate identities and repeated locations.
- **Watch next:** Carrier investigations, access suspensions, SS7 retirement, stronger Diameter filtering, and hardening of vulnerable SIM applications.
