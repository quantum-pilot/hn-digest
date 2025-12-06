# Cloudflare was down

- Score: 811 | [HN](https://news.ycombinator.com/item?id=46158191) | Link: https://www.cloudflare.com/

### TL;DR

Cloudflare briefly took large chunks of the Internet offline with plain 500 errors after deploying a change to its Web Application Firewall parser. The change aimed to mitigate a newly disclosed React Server Components vulnerability but instead broke parts of Cloudflare’s network. Impact was uneven: some CDN-only users stayed up while many WAF users, major SaaS providers, and sites like Wise and Supabase saw outages. HN discussion focuses on release engineering, architectural single points of failure, and overreliance on Cloudflare.

---

### Comment pulse

- Cloudflare reliability concern → Multiple recent outages plus global 500s erode trust and expose the risk of treating Cloudflare as indispensable infrastructure.

- Change management critique → WAF parser/config changes keep taking down traffic; commenters suspect poor canarying and isolation — counterpoint: mitigating urgent vulns forces faster, riskier rollouts.

- Status-page skepticism → Official status stayed mostly green while customers were hard-down, reinforcing that external monitors and internal contingency plans are essential.

---

### LLM perspective

- View: Architect assuming Cloudflare will fail; design fallbacks (multi-CDN, direct-origin paths, bypass of WAF) even if rarely used.

- Impact: SREs and infra leads will revisit third‑party risk, release gates, and automated kill-switches for bad global configs.

- Watch next: Cloudflare’s postmortem details on rollout safeguards, parser isolation, and whether they commit to stricter staged deployments.
