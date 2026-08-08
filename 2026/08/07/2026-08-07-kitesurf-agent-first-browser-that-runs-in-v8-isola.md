# Kitesurf: Agent-first browser that runs in V8 isolates

- Score: 157 | [HN](https://news.ycombinator.com/item?id=49208393) | Link: https://blog.cloudflare.com/kitesurf/

### TL;DR
Kitesurf is Cloudflare’s new “agent-first” browser engine that runs entirely inside Workers’ V8 isolates, using Rust/WASM and the open‑source Blitz rendering stack instead of Chromium. It strips human UI, focuses on HTML/CSS/JS, CDP automation, isolation, and stateless components to make browsing for AI agents cheaper and more scalable. Cloudflare claims 215k+ Web Platform Tests passing and ships it via Browser Run. HN debates open-sourcing, scraping ethics, Cloudflare’s dual role as CDN and bot provider, and shows real agent workflows already in use.

---

### Comment pulse
- Blitz engine & standards → Kitesurf builds on open‑source Blitz; commenters push for WebDriver BiDi support and standards-based automation over Chrome‑specific CDP.  
- Scraping vs trust → Some fear Cloudflare will run privileged crawlers on protected sites—counterpoint: staff say Browser Run traffic is flagged as bots, no bypass.  
- Real agent usage → Multiple examples: agents driving grocery orders, navigating awful admin UIs, fetching receipts, customizing pages, or bulk-filling carts while humans confirm results.

---

### LLM perspective
- View: Treating browsers as disposable, stateless microservices for agents feels like the right architecture for large-scale automation.  
- Impact: Cheaper headless browsing could broaden access to agentic workflows beyond companies that can afford huge Chromium fleets.  
- Watch next: Open-sourcing Kitesurf patches, WebDriver BiDi support, eval performance, and concrete guarantees about separation from Cloudflare’s CDN security controls.
