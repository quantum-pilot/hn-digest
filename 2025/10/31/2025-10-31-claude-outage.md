# Claude outage

- Score: 137 | [HN](https://news.ycombinator.com/item?id=45770317) | Link: https://status.claude.com/incidents/s5f75jhwjs6g

- TL;DR
  - Anthropic reported elevated errors on claude.ai Oct 31 (UTC): issue identified, fix deployed, monitored, then marked resolved the same day. HN discusses uneven reliability—some see timeouts and slow starts; others report smooth usage depending on region and product (chat vs Code). Tips: subscribe to status updates, try the official VS Code plugin, and keep cross-provider fallbacks. Bigger theme: dependence on LLMs—what’s the plan during outages, and are alternatives ready when primary tools falter?

- Comment pulse
  - Reliability is uneven → some see daily failures; others in Europe report long stability — counterpoint: some prefer Gemini’s reliability; others find Gemini worse.
  - Subscribe to status updates → model/platform-specific alerts help triage and reduce guesswork during slowdowns; but notifications can be spammy.
  - Overreliance concern → devs should keep fallbacks (other providers, prepaid tokens) or pause work; not all services fail simultaneously; one reports OAuth login still broken.

- LLM perspective
  - View: Centralized LLM UIs are a single point of failure; diversify clients and enable API-based failover with retries and circuit breakers.
  - Impact: Teams relying on Claude web or OAuth flows feel hiccups most; IDE integrations with cached context are more resilient.
  - Watch next: Ask for a postmortem with root cause and SLOs; verify OAuth fix; measure cross-provider uptime to justify multi-vendor budgets.
