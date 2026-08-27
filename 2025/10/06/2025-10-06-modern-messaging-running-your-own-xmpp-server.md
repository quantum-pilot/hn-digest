# Modern messaging: Running your own XMPP server

- Score: 208 | [HN](https://news.ycombinator.com/item?id=45490439) | Link: https://www.codedge.de/posts/modern-messaging-running-your-own-xmpp-server

### TL;DR

Motivated by opposition to proposed EU message scanning, the author documents a privacy-focused ejabberd XMPP deployment for Debian or Raspberry Pi OS. The setup covers DNS, ports, SQLite, TLS, access rules, uploads with weekly deletion, captcha-protected registration, WebSockets, STUN/TURN, nginx, OMEMO-capable clients, and reusable Ansible roles. HN agreed self-hosting remains technically viable but emphasized weak iOS and macOS client experiences, missing reactions, unreliable notifications, and encryption problems. Android clients fared better, while some preferred Matrix or Delta Chat despite their own tradeoffs.

### Comment pulse

- Server maturity is not enough → family adoption fails when mobile clients lack reliable notifications, polish, reactions, or understandable encryption behavior.
- Federation once connected major platforms → readers remembered using generic XMPP clients with Google, Facebook, AIM, and private servers.
- Alternatives trade complexity differently → Matrix offers modern clients but drew reliability criticism; Delta Chat builds messaging atop email infrastructure.

### LLM perspective

- View: Decentralized messaging succeeds or fails at the client layer after server administration is solved.
- Impact: Technical operators can reclaim infrastructure, but their contacts absorb usability and support costs.
- Watch next: Validate push delivery, group encryption, client interoperability, backups, abuse controls, calling, and long-term maintenance.
