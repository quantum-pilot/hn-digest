# Many Let's Encrypt renewals had errors today

- Score: 156 | [HN](https://news.ycombinator.com/item?id=48594715) | Link: https://letsencrypt.status.io/#2026

### TL;DR

Let’s Encrypt reported degraded ACME API performance after an upstream network event disrupted traffic between two data centers on June 18. Some clients received 400 or 500 responses, though most requests succeeded; traffic was rerouted by 16:35 UTC, restoring normal success rates, while operations continued with reduced redundancy into June 19. HN disputed the incident’s practical severity: Let’s Encrypt described roughly 90 minutes of elevated errors, but some users saw repeated total failure. Commenters stressed automation renews weeks early, so an issuance outage should not produce expired certificates.

### Comment pulse

- Status language obscured user impact → aggregate success remained high, yet individual clients reported more than 10 consecutive internal-server errors.

- Expiry warnings should remain strict → softer grace periods confuse users and reward broken renewal processes — counterpoint: pre-expiry alerts could prompt earlier fixes.

- Shorter certificate lifetimes increase issuance dependence → commenters questioned resilience and sought free ACME alternatives, including ZeroSSL, Google Trust Services, and SSL.com.

### LLM perspective

- **View:** The incident was limited at platform scale but severe for affected clients, making both aggregate and per-client metrics necessary.

- **Impact:** Operators with early, retried renewals absorb transient CA failures; last-minute workflows expose users to preventable TLS outages.

- **Watch next:** Seek the root-cause report, failure-rate timeline, retry behavior analysis, redundancy restoration, and guidance for resilient ACME clients.
