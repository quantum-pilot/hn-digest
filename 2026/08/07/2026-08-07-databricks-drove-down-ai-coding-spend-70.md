# Databricks drove down AI coding spend 70%

- Score: 151 | [HN](https://news.ycombinator.com/item?id=49214468) | Link: https://www.databricks.com/blog/managing-ai-coding-costs-scale

### TL;DR
Databricks claims it cut internal AI coding spend by ~70% while keeping productivity gains, by optimizing *how* and *where* LLMs are used rather than throttling usage. Core playbook: chase the “efficiency frontier” (best quality per dollar) via rapid model swaps, favoring cheaper/open models; keep harnesses and a meta‑harness (Omnigent) to avoid lock‑in; add smart routing to pick the cheapest capable model per request/task; give developers live cost dashboards, soft gates, and “downshift” options instead of hard caps; and aggressively reduce token overhead, all coordinated through a central AI Gateway (Unity AI Gateway).

---

### Comment pulse
- AI-as-coworker workflow can 3–4× output but often yields overengineered, hard-to-understand systems → several devs favor targeted, “surgical” AI use for long-term maintainability.  
- Cost control is unusually hard: opaque pricing, volatile models/harnesses, sudden run-rate jumps (e.g., $1.2M→$10M in 60 days) make forecasting and governance tricky.  
- Routing and meta-harness layers commoditize models and UX → commenters question OpenAI/Anthropic moats and speculate about future crackdowns or tighter vertical integration.

---

### LLM perspective
- View: Treat coding models as interchangeable commodities behind a gateway; invest engineering effort in routing, observability, and policy, not just “better models.”  
- Impact: Infra and platform teams become cost gatekeepers; finance needs real-time usage telemetry; vendor lock-in weakens as routing stacks mature.  
- Watch next: Standardized eval harnesses, cross-vendor routing protocols, provider responses in pricing/TOS, and whether open-source coding models keep winning on efficiency.
