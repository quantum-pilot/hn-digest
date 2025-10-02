# No more "check mail from other accounts" in Gmail web

- Score: 146 | [HN](https://news.ycombinator.com/item?id=45439670) | Link: https://support.google.com/mail/answer/16604719?hl=en

- TL;DR
  - Google will retire Gmailify and Gmail web’s POP-based “Check mail from other accounts” in Jan 2026. Previously fetched mail stays, but Gmail won’t pull external mail or apply Gmail features to third‑party inboxes. Alternatives: access other accounts via IMAP in the Gmail mobile app, push mail by forwarding from the other provider, or use a desktop client/paid Workspace. HN: users lament losing one-inbox consolidation, warn of silent breakage, and see revenue/security motives; others note forwarding/IMAP clients work.

- Comment pulse
  - Monetization push → POP/Gmailify gave cheap branded emails Gmail features; removing them nudges upgrades to Workspace — counterpoint: IMAP hosting is cheap, savings marginal.
  - It’s POP pull in web that dies → Gmail app can IMAP to other accounts, but won’t import; solution: forward (push) from source.
  - Operational risk → Many consolidate via POP; fear silent mail loss. Some Workspace admins got deprecation notices; personal accounts report none yet.

- LLM perspective
  - View: Deprecating server-side aggregation reduces abuse surface, operational complexity, and support costs.
  - Impact: Solo/SMB domains using Gmail as POP hub; IT help desks; migration/forwarding tooling vendors.
  - Watch next: Forwarding deliverability (SPF/DMARC/ARC), notice cadence for free users, any IMAP aggregation in web or client migration trends.
