# Decreasing Certificate Lifetimes to 45 Days

- Score: 148 | [HN](https://news.ycombinator.com/item?id=46117126) | Link: https://letsencrypt.org/2025/12/02/from-90-to-45.html

### TL;DR

Let’s Encrypt will shorten certificates from 90 days to 64 in February 2027 and 45 in February 2028, following industry requirements. Domain-control authorization reuse will fall from 30 days to ten days, then seven hours. Most automated users should be unaffected, but fixed 60-day schedules will fail; the issuer recommends ARI-aware clients, roughly two-thirds-lifetime renewal, and monitoring. An opt-in profile issues 45-day certificates in May 2026, while proposed DNS-PERSIST-01 validation could make automation possible with a stable DNS record.

### Comment pulse

- Shorter exposure windows pleased automation advocates → compromise duration falls — counterpoint: legacy-system operators expect brittle maintenance and little practical gain.
- Persistent DNS validation excited operators → one record could eliminate recurring edits and broadly scoped credentials.
- Public-certificate pinning drew warnings → applications would bind themselves to third-party infrastructure they do not control.

### LLM perspective

- View: Short lifetimes improve ecosystem hygiene only when renewal and failure detection are genuinely automatic.
- Impact: Hardcoded schedules, manual workflows, and fragile pinning will become operational liabilities before 2028.
- Watch next: ACME client ARI support, DNS-PERSIST-01 standardization, monitoring coverage, and staged-profile adoption.
