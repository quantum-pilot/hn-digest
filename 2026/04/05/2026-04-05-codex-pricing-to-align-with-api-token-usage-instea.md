# Codex pricing to align with API token usage, instead of per-message

- Score: 194 | [HN](https://news.ycombinator.com/item?id=47650726) | Link: https://help.openai.com/en/articles/20001106-codex-rate-card

### TL;DR
OpenAI’s Codex assistant is moving from approximate per-message pricing to precise token-based metering, starting with ChatGPT Business and new Enterprise workspaces and rolling out to Plus/Pro later. Credits remain the unit you buy, but they now map 1:1 to API-style token usage across input, cached input, and output tokens, with fast mode costing double. OpenAI says average spend is roughly $100–200 per developer monthly; impact varies by workload mix, drawing HN debate about pricing opacity, “credits,” and future bundling.

### Comment pulse
- Change only immediately hits Business/new Enterprise → article says Plus/Pro and existing Enterprise/Edu still on legacy per-message card, with token rates “coming in upcoming weeks”.
- Credit-based pricing hides real cost → users suspect obfuscation and price discrimination — counterpoint: also supports non-USD billing, discounts, and changing prices without rewriting contracts.
- Unbundling Codex from flat ChatGPT plans → some see preparation for IPO-era revenue maximization and predict similar usage-based shifts for Copilot, Claude, and competitors.

### LLM perspective
- Token-based Codex pricing aligns SaaS assistant billing with underlying APIs, making cost modeling easier for engineering orgs with mixed tools.
- Biggest winners are teams optimizing prompts and caching; output-heavy, fast-mode, or constant-review workflows may see notable cost increases.
- Watch whether GitHub Copilot, Claude Code, and IDE vendors expose token dashboards or adopt similar per-token enterprise pricing tiers.
