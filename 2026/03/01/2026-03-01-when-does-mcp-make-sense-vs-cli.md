# When does MCP make sense vs CLI?

- Score: 220 | [HN](https://news.ycombinator.com/item?id=47208398) | Link: https://ejholmes.github.io/2026/02/28/mcp-is-dead-long-live-the-cli.html

### TL;DR
The post argues that Model Context Protocol (MCP) mostly duplicates what LLMs can already do with ordinary command‑line tools, while adding complexity, flakiness, and auth headaches. CLIs are composable (pipes, jq, grep), easy to debug, reuse existing auth, and work identically for humans and agents. MCP is framed as useful only when there’s no CLI. HN discussion largely agrees, but notes real niches: remote, guard‑railed enterprise integrations and non‑developer chat UX where CLIs aren’t available or safe.

---

### Comment pulse
- CLIs beat MCP for agents → composability, low context use, reuse of `--help`, and stability; many MCP servers feel like fragile, marketing‑driven wrappers.
- MCP’s niche → remote HTTP endpoints with OAuth, centralized auth/telemetry, guard‑railed access to services (e.g., Gmail, Sentry) from chat UIs—counterpoint: overkill for dev workflows.
- Developer reports → better reliability and far fewer tokens after dropping MCP, giving LLMs clear instructions plus shell tools (jq, duckdb, dockerized CLIs) instead.

---

### LLM perspective
- View: Treat MCP as a specialized integration layer, not the default; prioritize APIs + CLIs that both humans and agents can drive.
- Impact: Dev tooling and infra teams can simplify stacks, focusing on robust shells and permissioned command surfaces instead of fleets of MCP servers.
- Watch next: Benchmarks comparing CLI‑driven vs MCP workflows, SaaS vendors’ MCP/CLI offerings, and finer‑grained policy for what commands agents may run.
