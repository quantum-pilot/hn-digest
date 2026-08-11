# Show HN: Mcp2cli – One CLI for every API, 96-99% fewer tokens than native MCP

- Score: 138 | [HN](https://news.ycombinator.com/item?id=47305149) | Link: https://github.com/knowsuchagency/mcp2cli

### TL;DR

mcp2cli turns an MCP server or OpenAPI specification into a CLI, avoiding code generation and exposing commands only when an agent requests `--list` or `--help`. It supports HTTP/SSE and stdio MCP, OAuth, secret-file or environment credentials, caching, structured output, and provider-agnostic agent skills. Its tests claim 96–99 percent context savings for large, multi-turn tool sets, though small OpenAPI cases save less. HN readers agree lazy discovery attacks schema bloat, but note dozens of similar wrappers exist and stress that fewer tokens do nothing to constrain authorization or prompt-injection blast radius.

### Comment pulse

- Lazy discovery solves context efficiency → large schemas stop recurring every turn, while agents pay help-text costs only for used tools.
- Authorization is unchanged → an efficient agent still retains every server-granted capability, so prompt injection preserves the same blast radius.
- Ecosystem duplication is conspicuous → many MCP-to-CLI projects exist; this implementation differentiates through runtime generation, OpenAPI support, and an agent skill.

### LLM perspective

- **View:** The benchmark demonstrates an architectural win under eager-schema clients, but savings depend on conversation length and tool usage.
- **Impact:** Multi-provider agent builders can trade extra shell discovery calls for dramatically smaller prompts.
- **Watch next:** Permission scoping, standardized deferred discovery, comparative latency, malformed-schema handling, and benchmarks against native tool-search implementations.
