# Running My Own XMPP Server

- Score: 206 | [HN](https://news.ycombinator.com/item?id=47034801) | Link: https://blog.dmcc.io/journal/xmpp-turn-stun-coturn-prosody/

### TL;DR
Author describes moving beyond dependence on centralized messengers like Signal by running a full-featured XMPP server with Prosody in Docker. They detail DNS and TLS setup, essential modules for mobile reliability (carbons, stream management, push), message archiving, HTTP file uploads behind a reverse proxy, and voice/video via a coturn TURN/STUN server. Clients like Monal, Conversations, and Gajim provide OMEMO end-to-end encryption and good UX. HN discussion compares XMPP to Matrix and Telegram, and debates server choices, OMEMO security, and self‑hosting tradeoffs.

---

### Comment pulse
- XMPP vs Matrix/Telegram → XMPP viewed as lighter, more reliable than Matrix; Telegram liked for UX but slammed for spam and weak privacy.  
- Self-hosting options → Some recommend Snikket or ejabberd over raw Prosody; others mistrust Snikket’s invites and note hosting off‑device weakens some E2EE assumptions.  
- Practical XMPP ops → Veterans report decades of low-maintenance ejabberd; discuss certificates for hosted domains and debate OMEMO critiques and self-signed CAs.

---

### LLM perspective
- View: XMPP self-hosting is viable for power users, but mainstream adoption still blocked by client UX and network effects.  
- Impact: Improved Docker images, auto-DNS/TLS setups, and better mobile clients could expand the audience beyond hobbyists and privacy diehards.  
- Watch next: Robust Signal/WhatsApp bridges, audited OMEMO revisions, and turnkey Snikket-style bundles will determine how attractive XMPP becomes.
