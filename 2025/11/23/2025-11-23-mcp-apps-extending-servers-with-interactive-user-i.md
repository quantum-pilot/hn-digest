# MCP Apps: Extending servers with interactive user interfaces

- Score: 157 | [HN](https://news.ycombinator.com/item?id=46020502) | Link: http://blog.modelcontextprotocol.io/posts/2025-11-21-mcp-apps/

- TL;DR  
  - MCP Apps proposes an MCP extension letting servers ship sandboxed HTML UIs (via `ui://` resources) tied to tools, communicating over existing JSON‑RPC for auditability and security. It targets standardized “agentic apps” across hosts (e.g., ChatGPT) while staying optional and backward‑compatible. HN discussion is divided: some like the shared runtime for richer workflows; others worry about complexity, ecosystem fragmentation, and a return to static, assistant-style UIs instead of LLM-generated interfaces or direct API/CLI use.

- Comment pulse  
  - Static MCP UIs feel backwards → LLMs should generate UIs or call CLIs; fixed layouts constrain tasks — counterpoint: models can't build complex UIs.  
  - Spec surface already large → adding HTML apps risks splintering MCP; few implement simpler elicitation today — counterpoint: shared extension beats many proprietary UI hacks.  
  - Some see MCP Apps as assistant-platform redux and monopolist lock-in; others at Anthropic argue it’s optional infrastructure bringing MCP closer to real user flows.

- LLM perspective  
  - View – This makes MCP more like a mini web platform; success depends on staying lean and genuinely interoperable.  
  - Impact – Most benefit goes to rich chat clients; terminal-style agents can ignore it, but risk missing emerging ecosystem conventions.  
  - Watch next – Real-world SDK adoption, security incidents, and whether dynamic LLM-generated UIs start to outperform handcrafted MCP apps.
