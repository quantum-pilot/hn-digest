# Let's Encrypt bans certificate usage in any US sanctioned territory [pdf]

- Score: 301 | [HN](https://news.ycombinator.com/item?id=48453275) | Link: https://letsencrypt.org/documents/LE-SA-v1.7-June-04-2026-diff.pdf

### TL;DR

Let’s Encrypt’s June 2026 agreement makes certificate users affirm they are outside comprehensively U.S.-sanctioned territories and are neither sanctioned parties nor their controlled entities, while obeying applicable sanctions and export law. If that changes, subscribers must seek revocation; ISRG may refuse issuance or revoke for legal or contractual violations. HN read this as cutting encryption from vulnerable populations, but an ISRG representative said the text clarifies existing compliance, mostly targets sanctioned governments, and keeps certificates available in Iran and Russia. Discussion shifted to trust-store centralization and independent alternatives.

### Comment pulse

- The headline overstates the scope → comprehensive sanctions and listed parties are covered; ISRG says general users in Iran and Russia remain eligible.
- A mission conflict exists → U.S. incorporation binds a global public service to sanctions — counterpoint: compliance reflects legal obligations, not discretionary exclusion.
- Technical alternatives face a social bottleneck → independent CAs can issue certificates easily but must win inclusion in browser and OS trust stores.

### LLM perspective

- **View:** TLS trust is globally consumed but jurisdictionally governed, so legal constraints propagate beyond the issuer’s home country.
- **Impact:** Operators in sanctioned contexts need renewal monitoring, fallback CAs, and documented ownership screening before certificates expire or are revoked.
- **Watch next:** Track ISRG’s plain-language guidance, OFAC licensing, actual denial patterns, revocations, and trust-store acceptance of alternative nonprofit CAs.
