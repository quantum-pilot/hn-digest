# Elevated errors on Claude.ai, API, Claude Code

- Score: 241 | [HN](https://news.ycombinator.com/item?id=47779730) | Link: https://claudestatus.com/

### TL;DR

The April 15 incident caused elevated errors across Claude.ai, the API, Platform, and Claude Code authentication. The API recovered first, at 16:01 UTC; logged-in Claude Code users could continue, while new logins remained broken until success rates stabilized and the incident was resolved. An unofficial dashboard showed roughly 91–92% 30-day uptime for the main surfaces and listed many recent failures. Commenters described recurring 500s near US West Coast mornings, criticized support and account complexity, and debated whether peak-demand pricing or automatic fallback models would improve reliability without silently degrading quality.

### Comment pulse

- Users reported a daily-looking error pattern around 14:30 UTC, attributing it to overlapping London work and the US Pacific morning.
- Reliability jokes contrasted AGI ambition with sub-two-nines uptime — counterpoint: some preferred explicit 500s to silent reductions in model thinking.
- One pricing proposal used short surge windows and cheaper-model exemptions; critics saw customers volunteering an enshittification playbook.

### LLM perspective

- **View:** The incident looks less isolated when authentication, model requests, billing, consoles, and support repeatedly fail across adjacent days.
- **Impact:** Development agents become operational dependencies; outages halt work, while opaque quality throttling can damage code more quietly than errors.
- **Watch next:** Peak-hour error rates, published incident root causes, capacity changes, login decoupling, and transparent fallback behavior.
