# Anthropic takes legal action against OpenCode

- Score: 355 | [HN](https://news.ycombinator.com/item?id=47444748) | Link: https://github.com/anomalyco/opencode/pull/18186

### TL;DR

OpenCode merged a two-commit pull request labeled anthropic legal requests, apparently changing how Anthropic access is presented or bundled. The supplied page shows no filed lawsuit; commenters describe a demand to stop plugins from using Claude Pro or Max authentication through internal Claude Code endpoints, directing third-party clients toward metered API access instead, while one reader disputed the exact diff’s scope. HN split between viewing this as ordinary enforcement of a subsidized first-party plan and seeing it as ecosystem lock-in motivated by costs, caching, telemetry, or model-switching risk.

### Comment pulse

- Subscription access may be a loss leader → unrestricted clients can turn a fixed plan into a cheap programmable API.
- Lock-in critics saw strategic control → a proprietary harness preserves telemetry and switching friction — counterpoint: metered API access remains available.
- Legal terminology mattered → the evidence shows requested changes backed by pressure, not a filed lawsuit.

### LLM perspective

- **View:** Product bundling becomes contentious when authentication works technically across clients but contract terms reserve its economics for one harness.
- **Impact:** OpenCode users must verify supported authentication paths, pricing, and whether plugins expose accounts to enforcement.
- **Watch next:** The final diff, OpenCode release notes, Anthropic’s written terms, account actions, and any actual court filing.
