# Why We Abandoned Matrix (2024)

- Score: 172 | [HN](https://news.ycombinator.com/item?id=46376201) | Link: https://forum.hackliberty.org/t/why-we-abandoned-matrix-the-dark-truth-about-user-security-and-safety/224

### TL;DR
Hack Liberty explains why they shut down their public Matrix and Lemmy services and migrated to SimpleX. They argue federation is structurally bad for privacy and moderation: Matrix leaks rich metadata by design, lets homeserver admins impersonate users and tamper with rooms, struggles with redaction/history, and is resource‑hungry. They further criticize Matrix.org’s data collection, Cloudflare TLS termination, weak abuse handling (especially CSAM), and removal of Tor-browser support. SimpleX is pitched as a non-federated, queue-based system with no user identifiers, mandatory E2EE, onion-style routing, and lower operational overhead.

---

### Comment pulse
- Ex‑fans: Matrix is overcomplex and resource-heavy; state resolution and room “bricking” are unacceptable, while basic UX features still lag. Some retreat to XMPP or wait on SimpleX.  
- Defenders: recent work (e.g., state-resolution fixes, MSCs for emojis/status) and private/self-hosted setups make Matrix stable in practice—counterpoint: funding pushed priorities toward gov/public-sector deployments.  
- SimpleX skeptics: “no identifiers” ignores IP metadata and centralized relay hosting; want Tor bundled and on by default—counterpoint: SimpleX designer says threat model is inter‑relay correlation, not hiding from all servers.

---

### LLM perspective
- View: The post is really an indictment of federation-for-everything, not just Matrix; it elevates metadata privacy above interoperability and convenience.  
- Impact: Highly paranoid or liability-sensitive communities may gravitate to SimpleX-like architectures, while mainstream users and orgs likely stick with Matrix/Signal/Discord.  
- Watch next: Concrete Matrix protocol fixes, abuse-handling tooling, and SimpleX’s scalability, governance, and “crypto coin” plans will determine which model gains durable trust.
