# Google Public CA is down

- Score: 274 | [HN](https://news.ycombinator.com/item?id=47055696) | Link: https://status.pki.goog/incidents/5oJEbcU3ZfMfySTSXXd3

### TL;DR

Google Trust Services halted TLS and SXG certificate issuance through its ACME API on February 17. The incident began at 11:18 a.m. Pacific; issuance started stopping around 12:14, a fix rolled out over roughly eight hours, and service resumed at 9:05 p.m. The status page gave no root cause, only that an ongoing incident forced the halt. HN inferred a possible compliance problem but had no confirmation, and used the outage to debate short-lived certificates, multi-CA fallback, renewal overlap, and dependence on just-in-time issuance.

### Comment pulse

- Several readers interpreted the staged halt as intentional containment rather than an accidental availability failure.
- Eight hours should fit normal renewal windows — counterpoint: ephemeral systems requesting certificates at startup can still fail immediately.
- Multi-CA fallback and persisted overlapping certificates reduce exposure, but many platforms defer that complexity until an outage.

### LLM perspective

- **View:** The incident tests architecture more than certificate lifetime: renewal headroom works only when systems preserve issued credentials.
- **Impact:** Teams relying on startup issuance need storage or provider diversity, exposing complexity short-lived certificates often hide.
- **Watch next:** Google’s root-cause disclosure, compliance filings, and evidence that halted issuance produced no misissued certificates.
