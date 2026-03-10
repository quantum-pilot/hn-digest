# Show HN: Mcp2cli – One CLI for every API, 96-99% fewer tokens than native MCP

- Score: 138 | [HN](https://news.ycombinator.com/item?id=47305149) | Link: https://github.com/knowsuchagency/mcp2cli

## TL;DR
mcp2cli is a Python tool that turns any MCP server or OpenAPI spec into a dynamically generated CLI, letting LLM agents discover and call tools on demand instead of loading huge JSON schemas every turn. By reducing tool discovery to short `--list` and `--help` calls, it claims 96–99% context savings in multi-tool scenarios, while adding OAuth, caching, and a compact TOON output format. HN discussion applauds the token wins, notes many similar CLIs, and questions MCP’s overall design and missing authorization model.

## Comment pulse
- Ecosystem sprawl: commenters list ~10 similar MCP CLIs; author differentiates mcp2cli via OpenAPI support, runtime generation, and an installable agent skill.  
- Security stance: token savings praised, but MCP still lacks authorization; suggestion for CLI-level `--allowed-tools` so orchestrators can hide disallowed tools from agents.  
- Value of MCP debated: critics prefer raw HTTP/ssh; defenders cite validation, schemas, granular access control, local/binary handling—MCP vs CLI likened to DLL vs process.

## LLM perspective
- View: Practical bridge that converts schema-heavy APIs into cheap, discoverable CLIs for any model, avoiding provider-specific features.  
- Impact: Multi-tool agent setups can grow far beyond current limits before hitting context ceilings or untenable per-turn costs.  
- Watch next: Standardized auth scoping on top, automated `--allowed-tools` orchestration, and head-to-head latency benchmarks against native MCP and Tool Search.
