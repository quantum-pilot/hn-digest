# I moved my digital stack to Europe

- Score: 869 | [HN](https://news.ycombinator.com/item?id=48120629) | Link: https://monokai.com/articles/how-i-moved-my-digital-stack-to-europe/

### TL;DR
The author rebuilt their personal/business tech stack to run mostly on European or self-hosted services, prioritizing “digital sovereignty”: knowing where data lives, which laws apply, and avoiding ad-based business models and capricious US policy risk. They swapped Google Analytics→Matomo, Workspace→Proton Mail/Pass, DigitalOcean/AWS→Scaleway/OVH, S3/Backblaze→EU object storage, SendGrid→Lettermint, OpenAI API→Mistral, and Sentry→self‑hosted Bugsink, while keeping Cloudflare, Stripe, GitHub, and Claude Code for pragmatic reasons. Migration took some effort but proved an EU‑centric stack is viable and stable.

---

### Comment pulse
- Demand for EU/local hosting is surging → EU governments, corporates, and even Canadian orgs now routinely require data residency in the EU or home country.  
- Practitioners report similar migrations → replacing AWS with Hetzner/OVH, Cloudflare with Bunny, GitHub with Forgejo/UpCloud etc., often cutting costs and gaining control.  
- EU isn’t a perfect refuge → Europe also pushes VPN limits, logging, and age verification; main benefit is slower, more predictable lawmaking—counterpoint: US instability and extraterritorial reach feel worse.

---

### LLM perspective
- View: Data-sovereign stacks are becoming a competitive requirement in regulated sectors, not just a personal or ideological preference.  
- Impact: Benefits EU clouds, self‑hosting tools, and open‑weight AI; pressures US hyperscalers and SaaS to offer credible regional isolation.  
- Watch next: Concrete EU data‑localization rules, Schrems-style court cases, Mistral/other EU AI benchmarks, and serious Cloudflare/WAF competitors based in Europe.
