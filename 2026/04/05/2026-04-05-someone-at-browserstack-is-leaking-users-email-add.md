# Someone at BrowserStack is leaking users' email addresses

- Score: 360 | [HN](https://news.ycombinator.com/item?id=47649117) | Link: https://shkspr.mobi/blog/2026/04/someone-at-browserstack-is-leaking-users-email-address/

### TL;DR

Terence Eden gave BrowserStack a unique email address while applying to its open-source program; days later, an outsider contacted it. Apollo initially claimed it inferred the address from public data and corporate patterns, then acknowledged BrowserStack supplied it through Apollo’s customer contributor network on February 25. BrowserStack did not answer repeated inquiries. Eden considers deliberate sharing, a third-party integration, employee exfiltration, or compromise possible. HN’s dominant explanation was less clandestine: Apollo customers automatically contribute contact data unless they opt out, exchanging privacy for enrichment and prospecting value.

### Comment pulse

- Apollo enriches uploaded contacts, then exposes contributed details to other customers; inbox-scraping plugins can also exchange address-book access for lookup credits.
- Custom-domain or randomly generated aliases preserve attribution and phishing detection, whereas providers can normalize predictable `+service` suffixes.
- Some suspected a compromised database — counterpoint: others considered voluntary CRM synchronization simpler and consistent with Apollo’s documented contributor model.

### LLM perspective

- **View:** Calling routine CRM enrichment a breach can obscure the deeper issue: normalized sharing may operate exactly as configured.
- **Impact:** Business-product signups can become shared sales intelligence, exposing users to spam, phishing, profiling, and regulatory risk.
- **Watch next:** BrowserStack’s response, Apollo consent records, opt-out defaults, processor contracts, privacy notices, retention, deletion requests, and regulator action.
