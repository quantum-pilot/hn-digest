# Google Public CA is down

- Score: 274 | [HN](https://news.ycombinator.com/item?id=47055696) | Link: https://status.pki.goog/incidents/5oJEbcU3ZfMfySTSXXd3

### TL;DR
Google Trust Services’ public CA briefly halted certificate issuance on Feb 17, 2026, due to a rollout problem, blocking its ACME APIs for several hours. The status messages suggest an intentional pause to stop problematic issuance while a fix deployed. HN discussion focused less on the brief outage itself and more on systemic risk: heavy dependence on a single CA, workloads that assume instant ACME issuance, and how very short-lived or on-demand certificates magnify the blast radius of such events.

---

### Comment pulse
- Halt looked deliberate → wording matches patterns where CAs discover non‑compliant certs and must immediately stop issuing—counterpoint: details will only be clear from formal incident reports.  
- Short-lived or just-in-time certs are fragile → if systems need immediate issuance, even hours-long outages can break them, unlike setups with long overlaps or multiple CAs.  
- Real-world dependency risk → platforms like Heroku or YouTube-style ephemeral fleets may rely on a single ACME CA, so renewal failures can cascade into visible downtime.

---

### LLM perspective
- View: Treat CAs like any other critical infrastructure dependency, with redundancy, health checks, and explicit failure modes in app design.  
- Impact: Cloud platforms, CDNs, and large microservice fleets should audit how many components implicitly assume “ACME is always up.”  
- Watch next: Look for CA incident postmortems, browser-program compliance notes, and tooling to support multi-CA ACME and overlapping certificate strategies by default.
