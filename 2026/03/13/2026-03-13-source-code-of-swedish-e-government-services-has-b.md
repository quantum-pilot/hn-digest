# Source code of Swedish e-government services has been leaked

- Score: 192 | [HN](https://news.ycombinator.com/item?id=47362350) | Link: https://darkwebinformer.com/full-source-code-of-swedens-e-government-platform-leaked-from-compromised-cgi-sverige-infrastructure/

### TL;DR
Dark Web Informer reports that threat actor “ByteToBreach” leaked what they say is the full source code for Sweden’s e‑government platform from CGI Sverige’s infrastructure, plus staff data, document‑signing APIs, Jenkins credentials, and exploit details. They also claim to have exfiltrated citizen PII databases and electronic signing documents, selling those separately. Swedish authorities and CGI, however, say only test systems and an e‑signature service were affected, with no real citizen data leaked and no single “e‑government platform” existing, leaving impact and scope contested.  

---

### Comment pulse
- Swedish personal ID numbers are quasi‑public via SPAR and sites like mrkoll.se, so a “citizen database” sounds less shocking → but unauthorized, full‑copy access is still different.

- Several Swedes question the “e‑government platform” label and cite officials saying only a signing service’s test servers were hit → counterpoint: others distrust these reassurances and fear lateral movement.

- Commenters note source code leaks mainly help find bugs; the truly serious risk would be stolen PII, encryption/signing keys, and long‑term compromise of trust systems.

---

### LLM perspective
- View: The incident underlines how CI/CD (Jenkins, Docker) misconfigurations can cascade into full vendor and multi‑tenant government compromise.

- Impact: Governments relying on CGI‑style integrators will likely revisit data segregation, key management, and what ever leaves core agency networks.

- Watch next: Look for key rotations, e‑ID or signing‑certificate reissuance, and any independent forensic summary contradicting or confirming official “no real data” claims.
