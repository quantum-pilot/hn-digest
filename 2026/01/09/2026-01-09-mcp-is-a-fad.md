# MCP is a fad

- Score: 138 | [HN](https://news.ycombinator.com/item?id=46552254) | Link: https://tombedor.dev/mcp-is-a-fad/

## TL;DR
- MCP, Anthropic’s Model Context Protocol, standardizes how AI agents call tools, but the article argues its costs exceed its benefits. Separate MCP processes create incoherent toolsets, operational friction, and extra attack surface, while mostly wrapping thin APIs that LLMs can now generate as scripts or clients. Existing mechanisms—command runners, first‑party integrations, and OpenAPI—cover most real needs with better security and ergonomics. HN discussion splits between seeing MCP as thin, useful glue and as a quickly obsoleting fad, with growing interest in Claude‑style skills.

## Comment pulse
- Interoperability defenders → MCP is a small, USB‑like standard: define tools once, reuse across Claude, IDEs, agents—security should be handled by servers, not protocol.  
- Critics → LLMs plus REST/OpenAPI already generate glue; MCP adds context bloat, process and supply‑chain risk, and enterprises rarely permit arbitrary third‑party MCP servers.  
- Pragmatists → With one curated server, MCP is boring plumbing; resource mounts for large datasets help — counterpoint: insecure, over‑permissive setups are common in reality.

## LLM perspective
- View → MCP is likeliest to persist as an enterprise‑only convention, bundling a few audited tools behind one controlled server.  
- Impact → If teams favor scripts, OpenAPI, and first‑party code, AI integrations will resemble engineering more than bespoke plugin ecosystems.  
- Watch next → See whether Claude Skills and OpenAI equivalents subsume MCP’s niche or a leaner OpenAPI‑centric standard emerges.
