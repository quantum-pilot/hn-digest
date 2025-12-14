# Poor Johnny still won't encrypt

- Score: 73 | [HN](https://news.ycombinator.com/item?id=46251952) | Link: https://bfswa.substack.com/p/poor-johnny-still-wont-encrypt

## TL;DR
Email encryption usability has barely improved since the 1990s. PGP is still clunky and poorly integrated with dominant webmail; S/MIME works better in enterprises but is painful to deploy, especially on Microsoft stacks. Auditors obsess over disk/TLS encryption but largely ignore end-to-end protection, and most SMTP links don’t enforce strong transport security like MTA-STS. Meanwhile, secure messengers (Signal, WhatsApp) and corporate chat (Slack, Teams) have displaced email for most sensitive communication, so incentives to fix email encryption keep shrinking.

---

## Comment pulse
- Key management is the real blocker → users want idiot-proof, multi-device key backup; Signal’s “history loss is a feature” clashes with most people’s expectations.  
- S/MIME can work at scale → governments and some companies encrypt everything by default with smart cards and managed certs, but lose searchability and webmail convenience.  
- Hosted “private” email is distrusted → Proton is criticized for lock-in and jurisdictional risk—counterpoint: APIs for public keys exist and PGP interop technically works.

---

## LLM perspective
- View: Email will stay mostly unencrypted end-to-end; serious secrecy continues moving to session-based messengers and specialized systems.  
- Impact: Enterprises and regulators mainly care about compliance checkboxes, so disk/TLS encryption win budget over harder UX problems like key management.  
- Watch next: Adoption of MTA-STS/DANE, better automatic key discovery, and whether big providers ever make default S/MIME actually painless.
