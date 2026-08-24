# OpenAI are quietly adopting skills, now available in ChatGPT and Codex CLI

- Score: 536 | [HN](https://news.ycombinator.com/item?id=46250332) | Link: https://simonwillison.net/2025/Dec/12/openai-skills/

### TL;DR

OpenAI has implemented filesystem-based skills in two places: ChatGPT’s code-execution environment contains instruction folders for documents, PDFs, and spreadsheets, while Codex CLI experimentally scans configured skill directories. Each package combines a short description with Markdown guidance and optional references or scripts, loading detailed context only when a task calls for it. The author demonstrates ChatGPT repeatedly rendering and inspecting a PDF, then uses a custom Codex skill to generate a working Datasette plugin. He argues the lightweight convention deserves formal documentation.

### Comment pulse

- Commenters largely framed skills as lazy-loaded context engineering, not a new tool protocol, with deterministic scripts supplying compact outputs.
- Skeptics called the mechanism obvious and easy to recreate — counterpoint: simple packaging plus ubiquitous code execution may make it broadly useful.
- Users valued one-off scripts over full MCP servers, while noting agents sometimes forget skills unless invoked explicitly.

### LLM perspective

- View: The innovation is disciplined packaging and selective loading, not a novel execution primitive.
- Impact: Teams can distribute task-specific guidance and scripts without permanently consuming model context or operating an RPC service.
- Watch next: A portable specification, trust boundaries for bundled code, reliable skill selection, versioning, provenance, and context-budget measurements.
