# How Claude Code works in large codebases

- Score: 229 | [HN](https://news.ycombinator.com/item?id=48144494) | Link: https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start

### TL;DR

Anthropic argues Claude Code scales by searching the live filesystem rather than relying on potentially stale code embeddings, provided teams build a strong harness: lean layered CLAUDE.md files, hooks, on-demand skills, plugins, LSP, MCP, and separate exploration agents. It recommends starting inside relevant subdirectories, scoping tests, excluding generated code, mapping unconventional trees, reviewing configuration every three to six months, and assigning an organizational owner. HN challenged the anti-index framing: engineers use memory and IDE indexes, grep can explode at scale, instruction-triggering is unreliable, and harness upkeep adds substantial cost.

### Comment pulse

- “Like an engineer” was disputed → humans combine memory, symbol indexes, and deliberate narrowing; brute-force grep wastes context and can invent missing abstractions.
- Live search avoids stale embeddings → counterpoint: local branch indexes remain current, work at IDE scale, and can be exposed through integrations.
- Harness configuration carries maintenance cost: rules can be ignored, tokens burned, and compensations become obsolete as models and tooling change.

### LLM perspective

- **View:** Search methods are complementary; live inspection ensures freshness while symbol indexes and curated maps reduce exploration entropy.
- **Impact:** Enterprises need platform ownership and governance, turning coding-agent adoption into ongoing developer-infrastructure work.
- **Watch next:** Benchmark task accuracy, navigation tokens, index staleness, rule compliance, setup labor, and regressions across model upgrades.
