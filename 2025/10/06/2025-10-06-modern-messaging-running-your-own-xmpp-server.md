# Modern messaging: Running your own XMPP server

- Score: 208 | [HN](https://news.ycombinator.com/item?id=45490439) | Link: https://www.codedge.de/posts/modern-messaging-running-your-own-xmpp-server

- TL;DR
  - A practical guide to self-hosting XMPP with ejabberd on Debian/RPi: set up subdomains and ports, TLS via ejabberd behind nginx, OMEMO and s2s STARTTLS, SQLite, MUC/file uploads with cleanup, captcha-gated registration, and WebSocket discovery files; Ansible roles included. The setup favors privacy-first defaults amid EU “chat control” proposals. HN reaction: servers are straightforward, but iOS clients lag (notifications, reactions) while Android’s Conversations shines; Prosody wins on simplicity; Matrix feels more modern yet can be flaky; some suggest Delta Chat.

- Comment pulse
  - XMPP on iOS feels half-baked → unreliable notifications, no reactions, confusing group E2EE; Android’s Conversations is solid — counterpoint: Matrix UX is richer but flaky.
  - Prosody vs ejabberd → Prosody praised for quick setup and extensions; ejabberd robust but intimidating; notification reliability blamed on clients, especially iOS.
  - Decentralization tradeoffs → People miss Google/Facebook XMPP federation; looming EU scanning could push DIY servers or apathy; some suggest email-based Delta Chat.

- LLM perspective
  - View: Server-side is mature and cheap; the bottleneck is cohesive XEP adoption and polished iOS clients with reliable push.
  - Impact: Helps small communities, family groups, and orgs regain control; enterprise use hinges on compliance tooling and predictable mobile UX.
  - Watch next: OMEMO v2 interop tests, Monal/Siskin releases and APNS stability, EU chat-control votes, bridges to Matrix and Delta Chat.
