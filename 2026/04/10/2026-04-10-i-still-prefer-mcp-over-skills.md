# I still prefer MCP over skills

- Score: 423 | [HN](https://news.ycombinator.com/item?id=47712718) | Link: https://david.coffee/i-still-prefer-mcp-over-skills/

## TL;DR
The author argues that Model Context Protocol (MCP) is better than “skills” for giving LLMs real capabilities. MCP acts as a networked connector: remotely hosted, auto-updating, authenticated, sandboxed, and portable across devices and clients. Skills shine as documentation and workflow hints, but become brittle when they depend on CLIs, secret juggling, and dumping large manuals into context. The proposed architecture: services expose MCP connectors; skills sit on top as concise “LLM manuals” describing how and when to use those tools.

---

## Comment pulse
- MCP for persistent, cross-session, multi-environment access; skills for higher-level behavior and docs — counterpoint: MCP is just a noisy, unnecessary wrapper around existing APIs/CLIs.  
- CLI+skills camp: local agents, custom scripts, REST+Swagger+skills are enough; MCP adds servers and complexity, though auth and secret isolation remain pain points.  
- Many see a false dichotomy: best workflows pair MCP with skills, plus auto-generated scripts; real trade-offs depend on user type (solo hacker vs. org-scale, cloud-hosted agents).

---

## LLM perspective
- View: Treat MCP as infrastructure for safe, portable capabilities; treat skills as project-specific operating manuals and workflow patterns.  
- Impact: Cloud-hosted, multi-tenant agents and non-technical end-users benefit most from MCP; power users can still lean on CLIs locally.  
- Watch next: Standardized skill formats, lighter MCP clients, permissioned tool exposure, and benchmarks comparing CLI+skills vs MCP+skills on real workflows.
