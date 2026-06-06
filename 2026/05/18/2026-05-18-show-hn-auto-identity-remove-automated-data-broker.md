# Show HN: Auto-identity-remove – Automated data broker opt-out runner for macOS

- Score: 314 | [HN](https://news.ycombinator.com/item?id=48178184) | Link: https://github.com/stephenlthorn/auto-identity-remove

### TL;DR
auto-identity-remove is a Node/Playwright tool that automatically submits privacy/opt‑out forms to 500+ data brokers on a monthly schedule. It tracks state, retries removals, supports macOS/Linux/Windows, and can outsource CAPTCHAs via CapSolver. About 30+ brokers have hand‑coded flows; ~470 use generic heuristics that may silently fail, so verification and dead‑URL pruning are built in. HN discussion praises the idea but flags rough edges: US‑centric assumptions, many manual steps/404s, and broader questions about data brokers, GDPR, and CAPTCHA arms races.

---

### Comment pulse
- Promising automation → Author asks for help improving generic heuristics, adding broker-specific flows, cross‑platform scheduling, and handling email confirmation flows.
- Rough edges for non‑US users → Canadian tester hits sign‑up prompts, Mail.app dependency, many 404s, and manual flows; likely US‑centric form and ZIP assumptions.
- Bigger picture → Data brokers seen as socially harmful; GDPR cited as partial counterweight; CAPTCHA‑solving services highlight that CAPTCHAs mostly burden legitimate users.

---

### LLM perspective
- View: Strong DIY alternative or complement to paid “data removal” services, but reliability hinges on community-maintained selectors and rigorous verification.
- Impact: Helps privacy-conscious users and activists systematically suppress people-search listings without subscriptions or trusting third-party processors.
- Watch next: More robust non-US handling, shared success/failure statistics per broker, and integrations with official registries like California’s Delete Registry.
