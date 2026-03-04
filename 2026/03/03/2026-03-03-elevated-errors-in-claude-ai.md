# Elevated Errors in Claude.ai

- Score: 203 | [HN](https://news.ycombinator.com/item?id=47227647) | Link: https://status.claude.com/incidents/yf48hzysrvl5

### TL;DR
Anthropic reported and resolved a several-hour incident causing elevated errors across claude.ai, the platform console, and Claude Code, likely related to rapid user growth and finite GPU capacity. Hacker News discussion focuses less on the specific outage and more on how AI has normalized lower availability (“single 9s”) because over‑provisioning GPUs is prohibitively expensive. Users compare Anthropic vs OpenAI on reliability and quotas, debate whether AI coding tools erode or enhance developer skills, and note Anthropic’s scaling pains after recent influxes.

---

### Comment pulse
- AI infra normalizes lower uptime → GPU capacity is lumpy, expensive, and pre‑allocated, so providers trade extra “9s” of availability for model quality and access.
- OpenAI → Anthropic migration strains Claude → Some users hit frequent errors and tight limits; others report near‑perfect uptime, suggesting uneven impact and possible region- or workload-specific issues.
- AI tools and careers → Some fear skill atrophy; others say AI literacy is now interview material and accelerates learning if used thoughtfully.

---

### LLM perspective
- View: Centralized, GPU-heavy AI services will remain spiky; outages and rate limits are structural, not just “ops bugs.”
- Impact: Teams depending on LLMs for core workflows must design around partial failure and avoid single-vendor lock-in.
- Watch next: Providers publishing clearer reliability metrics, better degradation modes, and multi-model routing tools to smooth demand spikes.
