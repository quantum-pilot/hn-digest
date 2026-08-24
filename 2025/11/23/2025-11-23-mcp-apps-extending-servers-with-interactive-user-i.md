# MCP Apps: Extending servers with interactive user interfaces

- Score: 157 | [HN](https://news.ycombinator.com/item?id=46020502) | Link: http://blog.modelcontextprotocol.io/posts/2025-11-21-mcp-apps/

### TL;DR

A proposed MCP extension would let servers supply interactive interfaces alongside tools. Servers predeclare HTML templates through UI resources, hosts render them in sandboxed iframes, and components communicate over existing auditable JSON-RPC; hosts may require consent for interface-initiated tool calls. Static templates remain separate from dynamic results for review, caching, and prefetching, while text fallbacks preserve compatibility. The goal is consistent charts and complex input flows across clients. Critics question whether server-authored interfaces constrain agent flexibility and whether another optional extension will worsen an already fragmented specification.

### Comment pulse

- Static versus generated UI divided readers → bespoke agent interfaces promise flexibility. — counterpoint: current models cannot reliably generate polished specialized experiences.
- Specification growth worried implementers → few servers support existing advanced features. — counterpoint: one optional convention may prevent incompatible proprietary designs.
- Mainstream usability motivated supporters → embedded interfaces can turn tool protocols into invisible infrastructure for complete user workflows.

### LLM perspective

- View: Standardizing constrained embedded UI is useful when visualization or structured input matters more than conversational flexibility.
- Impact: Hosts gain reusable interfaces without implementing every domain, while assuming new sandbox, consent, and compatibility responsibilities.
- Watch next: Security review, host adoption, text fallback quality, cross-client interoperability, and whether the extension reduces proprietary fragmentation.
