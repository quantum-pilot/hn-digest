# Cloudflare targets 2029 for full post-quantum security

- Score: 258 | [HN](https://news.ycombinator.com/item?id=47675625) | Link: https://blog.cloudflare.com/post-quantum-roadmap/

### TL;DR
- Cloudflare is accelerating its roadmap to make all its services fully post-quantum (including authentication, not just encryption) by 2029, reacting to recent advances in quantum algorithms and neutral-atom hardware that shorten credible “Q‑Day” timelines to around 2029–2030.  
- They argue the urgent risk is forged identities (certs, logins, code-signing), not only harvest-now/decrypt-later.  
- Cloudflare will roll PQ in by default, urges orgs to require PQ from vendors, and calls for coordinated government timelines.

---

### Comment pulse
- PQ rollout will mirror HTTPS: optional → soft browser warnings → strict modes → removal of legacy ciphers; Cloudflare can mask backend lag for many sites.  
- Legacy/IoT clients and static firmware are likely casualties when browsers deprecate non‑PQ ciphers; web servers and browsers look comparatively easy to upgrade.  
- Cryptography engineers report a sharp “vibe shift” toward urgency; rumors of secret government work fuel fears of a silent quantum break — counterpoint: PQ schemes themselves may still hide flaws.

---

### LLM perspective
- View: Treat PQ migration as multi‑year engineering, not a future research topic; start inventorying long‑lived keys and authentication paths now.  
- Impact: Smaller vendors and critical infrastructure with slow upgrade cycles risk becoming weakest links once browsers and CDNs flip defaults.  
- Watch next: Browser PQ auth roadmaps, PQ certificate support in major CAs, and concrete hardware milestones toward 10k‑qubit neutral‑atom systems.
