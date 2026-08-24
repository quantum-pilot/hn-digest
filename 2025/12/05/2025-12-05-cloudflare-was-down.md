# Cloudflare was down

- Score: 811 | [HN](https://news.ycombinator.com/item?id=46158191) | Link: https://www.cloudflare.com/

### TL;DR

The supplied page is Cloudflare’s normal product homepage, while commenters reported a fresh outage producing plain HTTP 500 responses across several unrelated services. Cloudflare’s incident text, reproduced in discussion, blamed a Web Application Firewall request-parsing change deployed to mitigate a React Server Components vulnerability and said it was not an attack. Reports suggested only certain configurations were affected. Debate centered on repeated incidents, missing or delayed status-page warnings, inadequate staged rollout, Cloudflare as a shared failure domain, and customers lacking practical contingency plans.

### Comment pulse

- Repetition threatens trust → commenters distinguish exceptional bad luck from process or architecture problems that turn routine changes into recurring broad failures.
- Status visibility lagged reality → users saw customer-site errors while Cloudflare’s page showed little or only planned maintenance.
- Exposure varied by configuration → WAF-enabled locations reportedly failed while some CDN, tunnel, and proxied services remained available.

### LLM perspective

- View: Live reports exposed provider failure and customers’ inability to bypass a third-party dependency they do not control.
- Impact: Teams relying on Cloudflare inherit its blast radius unless they maintain tested DNS, WAF, and origin fallbacks.
- Watch next: Postmortem scope, affected products, canary policies, status accuracy, and customer adoption of temporary bypass procedures.
