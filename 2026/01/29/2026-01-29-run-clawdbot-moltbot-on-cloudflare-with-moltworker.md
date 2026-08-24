# Run Clawdbot/Moltbot on Cloudflare with Moltworker

- Score: 138 | [HN](https://news.ycombinator.com/item?id=46810828) | Link: https://blog.cloudflare.com/moltworker-self-hosted-ai-agent/

### TL;DR

Cloudflare open-sourced Moltworker, a proof of concept for hosting the personal agent formerly called Clawdbot inside its developer platform instead of dedicated local hardware. An entry Worker routes APIs to an isolated Sandbox container running the standard Moltbot Gateway; R2 persists memory, Browser Rendering supplies remote Chromium automation, Access handles authentication, and AI Gateway centralizes model keys, billing, fallbacks, logs, and switching. Running it requires at least a $5 Workers plan, but Cloudflare stresses this is adapted middleware and scripts, not a supported product.

### Comment pulse

- Critics see a marketing-heavy convenience wrapper and want realistic monthly bills before judging its value.
- Security concerns center on integrations, self-written tools, supply-chain compromise, and users granting broad access outside isolation.
- Cloud hosting adds observability and Zero Trust controls — counterpoint: local integrations disappear and private data moves off-device.

### LLM perspective

- View: The contribution is a composable deployment pattern, not a new agent architecture.
- Impact: Developers trade local control for managed isolation, authentication, persistence, browser automation, and centralized model routing.
- Watch next: Maintenance beyond proof-of-concept status, complete cost examples, upstream integration, isolation audits, and data-residency controls.
