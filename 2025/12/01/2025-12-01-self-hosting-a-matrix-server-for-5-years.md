# Self-hosting a Matrix server for 5 years

- Score: 232 | [HN](https://news.ycombinator.com/item?id=46106132) | Link: https://yaky.dev/2025-11-30-self-hosting-matrix/

### TL;DR
Running a small self-hosted Matrix/Synapse server for five years works, but only with constant babysitting. The author details fragile storage and retention (append‑only state tables, orphaned rooms, undeletable media and users), awkward federation controls, and the lack of a built‑in admin UI. Element Classic feels flaky; Element X adds new dependencies (sliding sync, Element Call/ESS) and worsens onboarding for custom servers. With Matrix increasingly targeting large organizations, the author plans to switch to leaner XMPP-based setups like Snikket.

---

### Comment pulse
- Self-hosting is fine for some → modest VPS handles many users; they tolerate multi‑GB DBs, but resent undeletable media and fragile, repeatedly reworked calling stacks.  
- Media handling feels risky → older Matrix homeservers proxied any remote media without auth, raising CSAM worries; alternative servers like Conduit now add media‑retention controls.  
- Design trade-offs frustrate users → history replication and event signing complicate privacy expectations; absent first-party admin tools pushed several admins back to simpler XMPP deployments.  

---

### LLM perspective
- View: Matrix currently optimizes for complex, federated deployments; its architecture is misaligned with people wanting low-maintenance, small private chats.  
- Impact: This gap creates space for XMPP bundles, lightweight Matrix homeservers, or entirely new protocols positioned as “Discourse for chat”.  
- Watch next: Track ESS Community maturity, alternative servers like Conduit, and whether Element exposes retention/admin features in mainstream clients by default.
