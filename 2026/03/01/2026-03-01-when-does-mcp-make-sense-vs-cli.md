# When does MCP make sense vs CLI?

- Score: 220 | [HN](https://news.ycombinator.com/item?id=47208398) | Link: https://ejholmes.github.io/2026/02/28/mcp-is-dead-long-live-the-cli.html

### TL;DR

The author argues that command-line tools are usually the better agent interface: models understand help text, humans can reproduce commands, pipelines filter large data before it consumes context, existing authentication carries over, and binaries avoid server initialization. MCP remains useful where no CLI exists. Hacker News broadly endorsed CLI composition and lower token use, but supplied an important boundary: remote MCP can offer zero-install OAuth, telemetry and guarded enterprise access for nontechnical chat users without shells. The choice therefore depends on environment and trust model.

### Comment pulse

- CLI composition is decisive → agents can probe structured data before context, reducing tokens while leaving reproducible commands.
- Remote MCP centralizes OAuth, telemetry and deployment → useful when users cannot install binaries or access a shell.
- Guardrails favor typed tools — counterpoint: equivalent least-privilege authorization can protect CLI or API access too.

### LLM perspective

- **View:** Choose interfaces by execution environment and trust boundary, not AI branding.
- **Impact:** Product teams should ship robust APIs, then expose CLI and remote integrations as their audiences require.
- **Watch next:** Parameter-level permissions, composable MCP execution and measured latency and context costs.
