# Privacy doesn't mean anything anymore, anonymity does

- Score: 358 | [HN](https://news.ycombinator.com/item?id=46334025) | Link: https://servury.com/blog/privacy-is-marketing-anonymity-is-architecture/

### TL;DR
- The post argues “privacy” is mostly marketing because services still tie accounts to emails, phones, and logs; true protection comes from architectures that never collect identifying data. Mullvad is held up as the model: no emails, only random account IDs, so even police raids yield nothing. The author’s company, Servury, claims a similar design (only a 32‑char credential, no recovery). HN readers like the principle but quickly find contradictions in Servury’s logging and certifications, and debate how practical Mullvad‑level anonymity really is.

### Comment pulse
- Servury’s privacy claims vs reality → Site previously admitted to logging IPs/user agents and advertised ISO27001/SOC2 without proof—counterpoint: some see such basic logs as harmless.
- Anonymity ideals vs engineering needs → Mullvad-style “no data” is praised, but infra engineers say logs, IDs, and resets are essential for debugging, SSO, and user expectations.
- Bigger picture → Many see ubiquitous surveillance as entrenched; others argue individuals can still meaningfully resist with tools like Mullvad VPN/browser and better OPSEC.

### LLM perspective
- View: Architectural anonymity (no emails, minimal data) is powerful, but trust hinges on verifiable practices, not blog rhetoric from a vendor.
- Impact: Realistically applies to VPNs, hosting, and niche tools; mass-market apps will keep trading identity for convenience, support, and growth metrics.
- Watch next: Independent audits, reproducible builds, and public incident handling will separate genuine “no-logs” services from privacy-washed marketing.
