# Incident with Issues and Webhooks – Resolved

- Score: 418 | [HN](https://news.ycombinator.com/item?id=48010301) | Link: https://www.githubstatus.com/incidents/72q3n8yxthcy

## TL;DR
GitHub reported and resolved a roughly hour-long incident where Issues, Webhooks, Git operations, PRs, Actions, Packages, Pages, and Codespaces experienced latency and degraded performance. Services were gradually restored and a root-cause analysis is promised but not yet published. Hacker News discussion treats this as part of a continuing reliability decline, connecting it to GitHub’s explosive usage growth and AI/agent-driven load, questioning architectural choices and business incentives, and debating whether developers will actually migrate to alternatives despite mounting frustration.

---

## Comment pulse
- Scaling crisis narrative → Explosive commit and Actions growth plus always-on AI/agent traffic are stressing architecture; some argue better endpoint design could cut backend load 5x.  
- Reliability expectations → External tracking shows sub-90% uptime; even if overstated, commenters say GitHub is far from “three nines” and well past “unacceptable.”  
- Lock‑in and priorities → People eye Codeberg/alternatives yet stay due to inertia and network effects; Copilot’s separate, unaffected infra fuels jokes about where investment is going.

---

## LLM perspective
- View: Agentic tooling is reshaping traffic patterns; platforms must distinguish human vs automated usage and engineer around worst‑case bot behaviors.  
- Impact: Dev teams increasingly need contingency plans—mirrors, local workflows, and CI/CD fallbacks—assuming the forge is periodically unavailable.  
- Watch next: Concrete SLOs from GitHub, pricing/rate‑limit changes for bots/Actions, and whether serious projects start standardizing on multi‑forge setups.
