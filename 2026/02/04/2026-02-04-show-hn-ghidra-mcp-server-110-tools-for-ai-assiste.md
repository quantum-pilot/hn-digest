# Show HN: Ghidra MCP Server – 110 tools for AI-assisted reverse engineering

- Score: 269 | [HN](https://news.ycombinator.com/item?id=46882389) | Link: https://github.com/bethington/ghidra-mcp

### TL;DR
A new Ghidra Model Context Protocol (MCP) server exposes 110 reverse‑engineering tools over a clean API, letting LLMs and automation frameworks drive Ghidra for decompilation, xrefs, type/label management, and bulk analysis. Its standout feature is a normalized function-hashing system that survives recompiles and rebasing, so comments, names, and types can automatically migrate between binary versions. It runs headless, supports Docker and batch workflows, and significantly expands on earlier Ghidra MCP servers with far more endpoints and scripting.

---

### Comment pulse
- Cross-version function hashing seen as the key innovation → promises better doc transfer than existing FunctionID/bindiff; users ask for comparisons and clearer install instructions.  
- Practitioners report AI+Ghidra MCP makes keygens, legacy game ports, and vendor-lock circumvention dramatically easier—counterpoint: some worry about optics and IP/ethics.  
- Several note LLMs excel at turning decompilation into human-like code; model choice matters, with Claude/Qwen often outperforming Gemini on completeness.

---

### LLM perspective
- View: Treats Ghidra as a programmable backend for agents, making large-scale, AI-guided reverse engineering practical instead of one-off scripting.  
- Impact: Strong leverage for security researchers, game modders, and maintainers of abandonware or legacy systems where source is lost.  
- Watch next: Empirical comparisons with FunctionID/bindiff, expanded architecture/Android coverage, and more secure defaults for the embedded HTTP endpoint.
