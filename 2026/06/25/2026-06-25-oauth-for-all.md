# OAuth for all

- Score: 360 | [HN](https://news.ycombinator.com/item?id=48668033) | Link: https://blog.cloudflare.com/oauth-for-all/

### TL;DR
Cloudflare appears to be rolling out a managed OAuth service (“OAuth for all”), built on Ory Hydra 2.x and praised for very low CPU use at scale. A migration bug in Hydra is mentioned but seems fixable upstream. Commenters say OAuth/OIDC is operationally “solved” yet conceptually hard for juniors, and they note the ecosystem split between commercial and open-source stacks. Discussion then shifts to Cloudflare’s growing centrality, pricing, missing full IAM features, and security concerns around OAuth Dynamic Client Registration for multi-tenant and AI-agent use cases.  
*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Ory stack is battle-tested → Hydra powers high-scale OAuth with minimal resources; commenters praise Hydra, Kratos, and related OSS.  
- Cloudflare reduces auth complexity → developers can outsource OAuth instead of running IdPs themselves — counterpoint: increases dependence on a pricey, central provider.  
- Broader IAM is still missing → commenters want identity, multitenancy, SAML, and safer Dynamic Client Registration, especially to avoid redirect-URI phishing in AI/agent workflows.

---

### LLM perspective
- View: Managed OAuth will become commodity, but full IAM (users, orgs, policies) remains fragmented among vendors.  
- Impact: Startups and SaaS teams may default to Cloudflare/Ory rather than operating their own identity servers.  
- Watch next: Stronger standards or de-facto patterns for DCR, redirect validation, and multi-tenant auth in AI assistant ecosystems.
