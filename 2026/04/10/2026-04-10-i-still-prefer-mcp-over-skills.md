# I still prefer MCP over skills

- Score: 423 | [HN](https://news.ycombinator.com/item?id=47712718) | Link: https://david.coffee/i-still-prefer-mcp-over-skills/

### TL;DR

The author rejects claims that Skills should replace MCP. Skills work best as repository-local manuals: knowledge, workflows, jargon, and instructions for tools already installed. MCP is better for connecting agents to services because remote servers centralize OAuth, updates, sandboxed interfaces, portability across web, phone, desktop clients, and lazy tool discovery without arbitrary local CLIs. The preferred stack combines both: MCP executes through a controlled connector, while a Skill records domain context, tool relationships, formats, and discovered gotchas. Commenters largely agree the choice depends on user, persistence, environment, and risk.

### Comment pulse

- Solo developers favor familiar CLIs and APIs for tight local loops; organizations and cloud agents value managed persistence, auth, and policy boundaries.
- MCP can constrain exposed operations and hide credentials. — counterpoint: some servers grant everything users can access, creating enormous automated blast radius.
- Several argue the real target is minimal machine-friendly tooling; MCP, CLI, REST, and Skills are implementation choices, not rival religions.

### LLM perspective

- **View:** The durable distinction is capability transport versus behavioral guidance; forcing one artifact to provide both creates avoidable coupling.
- **Impact:** Cloud and multi-client workflows benefit most from connectors; local coding agents can exploit existing Unix tooling cheaply.
- **Watch next:** Fine-grained authorization, progressive disclosure, cross-client Skill portability, secret isolation, and standard tool metadata.
