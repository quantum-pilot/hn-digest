# Show HN: Ghidra MCP Server – 110 tools for AI-assisted reverse engineering

- Score: 269 | [HN](https://news.ycombinator.com/item?id=46882389) | Link: https://github.com/bethington/ghidra-mcp

### TL;DR

Ghidra MCP Server exposes 110 reverse-engineering tools to MCP clients through a Python bridge and Java Ghidra plugin. Its API covers decompilation, disassembly, call graphs, memory, types, symbols, annotations, scripts, multi-program work and batch operations with atomic transactions. The standout feature normalizes function structure into hashes so names, types and comments can transfer across recompiled or rebased binary versions. The author reports validating this against multiple Diablo II patches and propagating over 1,300 annotations; installation requires Ghidra 12.0.2, Java 21, Maven, Python and copied Ghidra libraries.

### Comment pulse

- Reverse engineers praised LLM-assisted analysis for accelerating legacy-code understanding, porting and repair while still requiring annotated context.
- Others asked how hashing compares with FunctionID, BinDiff and rival MCP servers, and reported incomplete installation guidance.
- Users warned that some models silently omit or distort complex decompiled logic.

### LLM perspective

- View: Cross-version annotation transfer is more distinctive than simply exposing another broad MCP tool catalog.
- Impact: Reused documentation could remove repetitive work, but incorrect AI interpretations can propagate at batch scale.
- Watch next: Comparative accuracy against established matchers, installation fixes and independent results on varied binaries.
