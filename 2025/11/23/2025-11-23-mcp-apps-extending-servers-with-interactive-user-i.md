# MCP Apps: Extending servers with interactive user interfaces

- Score: 157 | [HN](https://news.ycombinator.com/item?id=46020502) | Link: http://blog.modelcontextprotocol.io/posts/2025-11-21-mcp-apps/

### TL;DR

The proposed MCP Apps Extension lets servers declare `ui://` HTML templates, associate them with tools, and exchange bidirectional JSON-RPC messages with hosts. Sandboxed iframes, predeclared resources, auditable communication, consent for UI-initiated calls, caching, and text fallbacks aim to make rich interfaces interoperable without breaking existing MCP implementations. OpenAI, Anthropic, and MCP-UI maintainers jointly authored the proposal and early SDK. Commenters disputed whether static embedded interfaces help ordinary users or enlarge an already fragmented protocol when generated interfaces, CLIs, or conventional APIs may be simpler.

### Comment pulse

- Accessibility case → embedded charts and forms can expose MCP workflows to users who should never need to understand the protocol.
- Flexibility objection → server-defined interfaces may constrain task-specific interaction — counterpoint: the extension is optional and preserves text fallbacks.
- Standardization trade-off → one convention limits proprietary fragmentation but adds implementation and security surface to uneven clients.

### LLM perspective

- View: MCP Apps standardizes an existing demand; its success depends more on host adoption than schema elegance.
- Impact: Server authors can own presentation while clients inherit sandboxing, consent, compatibility, and lifecycle responsibilities.
- Watch next: Test cross-host portability, permission prompts, template updates, accessibility, fallback quality, and extension versioning.
