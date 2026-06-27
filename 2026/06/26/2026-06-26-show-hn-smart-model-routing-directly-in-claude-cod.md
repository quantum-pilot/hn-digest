# Show HN: Smart model routing directly in Claude, Codex and Cursor

- Score: 133 | [HN](https://news.ycombinator.com/item?id=48688700) | Link: https://github.com/workweave/router

### TL;DR
A new “smart router” chooses which LLM to call (cheap vs powerful; OSS vs proprietary) from within tools like Claude, Codex, and Cursor, aiming to cut costs while preserving quality. It’s cache-aware and tries to avoid switching models mid-session unless savings justify cache misses. HN discussion centers on whether proxy-level routing can coexist with agentic coding workflows, how to keep the router fresh via RL on limited data, and whether power users even want auto-routing.

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Proxy routing vs agent control → Coding agents already pick models by phase; inserting a router can break feedback loops and prompt caching—counterpoint: cache-aware thresholds reduce harmful switches.  
- Training and freshness → Router is RL-tuned on a golden dataset and per-customer rewards, but skeptics question coverage and keeping pace with weekly model releases.  
- Who benefits → Power users tailor prompts to specific models and distrust auto mode; proponents argue “average Joe” and org cost controls gain most.

---

### LLM perspective
- View: Value hinges on being session- and cache-aware, and outperforming agents’ built-in routing in real-world coding chains.  
- Impact: If successful, IDEs and orgs may centralize model selection policy, treating models as commodities under a smart broker.  
- Watch next: Public terminalbench/deepswe results, ablation on cache misses vs savings, and support for new models without retraining bottlenecks.
