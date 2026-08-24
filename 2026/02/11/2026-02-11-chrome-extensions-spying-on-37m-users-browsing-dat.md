# Chrome extensions spying on 37M users' browsing data

- Score: 227 | [HN](https://news.ycombinator.com/item?id=46973083) | Link: https://qcontinuum.substack.com/p/spying-chrome-extensions-287-extensions-495

### TL;DR

Researchers say an automated Chrome-in-Docker pipeline flagged 287 extensions with 37.4 million combined installations for transmitting browsed URLs. Their MITM proxy varied synthetic URL lengths and correlated them with outbound bytes, then manually reviewed candidates; honeypot visits and decoded payloads linked several extension families and data brokers. The report cautions that some collection may support legitimate features or carry consent, so not every extension is malicious. Commenters focused on post-acquisition supply-chain attacks, privileged auto-updates, school devices, and the limits of open-source availability without reproducible store builds.

### Comment pulse

- Extension ownership changes are a supply-chain boundary → developers report persistent buyout offers followed by opaque monetization.
- Open source is only a signal → store packages may differ from published code, leaving users unable to verify installed builds.
- Institutional review must scale → individuals cannot continuously audit updates, network access, permissions, sessions, and children’s school-installed tools.

### LLM perspective

- View: The study’s strongest result is behavioral detection at scale; its actor attribution and malicious-intent judgments require separate scrutiny.
- Impact: Full browsing URLs can expose searches, internal systems, identities, and sessions across consumers, companies, and schools.
- Watch next: Chrome Store removals, ownership-transfer alerts, reproducible builds, extension network controls, independent replication, consent audits, and false-positive disclosures.
