# Anthropic Explicitly Blocking OpenCode

- Score: 164 | [HN](https://news.ycombinator.com/item?id=46625918) | Link: https://gist.github.com/R44VC0RP/bd391f6a23185c0fed6c6b5fb2bac50e

### TL;DR

A Bun test script claims Anthropic’s Claude Code OAuth credentials reject system prompts identifying the client as OpenCode while accepting Cursor, Pi, or Droid, provided the first block impersonates the official CLI. It authenticates a Pro/Max account, sends controlled requests, and compares success. HN debate focused less on the observed filter than its meaning: ordinary paid API access remains available, while subscription-backed OAuth traffic expects Claude Code’s request format. Critics called selective enforcement lock-in; defenders saw legitimate protection against cheaper-plan arbitrage.

### Comment pulse

- Request fingerprinting appears broader than one phrase → a reported proxy succeeds by reproducing Claude Code headers, metadata, prompts, and tool schemas.
- Subscription users expected client choice → counterpoint: public API-key access remains available, while OAuth pricing was intended for the official client.
- Several developers cancelled or considered rivals → restrictions compounded frustration with regressions, data retention, and perceived model convergence.

### LLM perspective

- View: The dispute is about product bundling and pricing boundaries as much as technical access.
- Impact: Client restrictions can turn developer goodwill into rapid switching when comparable models exist.
- Watch next: Anthropic’s OAuth terms, request validation changes, official third-party support, and sustained bypass viability.
