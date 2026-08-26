# Anthropic blocks third-party use of Claude Code subscriptions

- Score: 559 | [HN](https://news.ycombinator.com/item?id=46549823) | Link: https://github.com/anomalyco/opencode/issues/7410

### TL;DR

Anthropic’s Claude Code Pro/Max OAuth credentials began returning a 400 error when used through OpenCode, while Claude Code-shaped requests still worked. The evidence points to enforcement based on endpoint, client identity, and beta flags, not a ban on ordinary Anthropic API keys. OpenCode users therefore face metered API pricing or a different provider instead of using subscription access in their preferred client. HN split between defending subscription terms and criticizing client lock-in, especially because many consider OpenCode’s interface and architecture superior.

### Comment pulse

- Subscription restrictions are legitimate → Claude Code appears to be a subsidized, client-bound offering rather than a general-purpose API entitlement.
- Client lock-in harms competition → users value OpenCode’s interface and may redirect subscriptions to rival models.

### LLM perspective

- View: The dispute is contractual and architectural: discounted subscription economics now enforce first-party tooling.
- Impact: Alternative agent clients lose a major price advantage; developers must pay API rates or switch providers.
- Watch next: OpenCode authentication changes, Anthropic’s terms, and whether interoperable subscription access or standardized agent protocols emerge.
