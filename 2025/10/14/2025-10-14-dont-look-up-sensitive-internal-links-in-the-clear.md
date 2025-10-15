# Don’t Look Up: Sensitive internal links in the clear on GEO satellites [pdf]

- Score: 516 | [HN](https://news.ycombinator.com/item?id=45575391) | Link: https://satcom.sysnet.ucsd.edu/docs/dontlookup_ccs25_fullpaper.pdf

- TL;DR
    - Researchers used consumer hardware and a new multi-protocol parser to scan 39 GEO satellites (411 transponders), finding about 50% of IP links broadcast in cleartext. Captured forward-link traffic included cellular backhaul with SMS/voice contents, utility SCADA, military asset tracking, retail credentials, and in‑flight Wi‑Fi. Disclosures led to some fixes and public guidance. HN highlights neglected basics over exotic threats, recalls long‑standing satellite eavesdropping, and worries about critical infrastructure exposure and widespread risks.

- Comment pulse
    - Critical data riding unencrypted GEO backhaul → Examples: SMS/voice, SCADA, retail creds, military SIP; some fixes verified (T‑Mobile, Walmart, KPU).
    - Encryption omitted due to bandwidth/power/fees/troubleshooting incentives → vendors license crypto; operators prioritize reliability — counterpoint: crypto can be done on ground; satellites needn’t decrypt.
    - This isn’t new; pre‑Snowden satellite traffic often plaintext → cultural lag; interception long practiced by intelligence and hobbyists.

- LLM perspective
    - View: Satellite backhaul is misclassified as “internal,” so link/network encryption is skipped.
    - Impact: Telcos, utilities, aviation, retail; vendors monetizing crypto options; regulators now have measurable evidence.
    - Watch next: Mandatory link-layer crypto in contracts, IPSec/TLS audits, rescans tracking adoption, LEO backhaul scrutiny.
