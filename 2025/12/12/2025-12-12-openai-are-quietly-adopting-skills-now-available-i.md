# OpenAI are quietly adopting skills, now available in ChatGPT and Codex CLI

- Score: 536 | [HN](https://news.ycombinator.com/item?id=46250332) | Link: https://simonwillison.net/2025/Dec/12/openai-skills/

### TL;DR

Simon Willison documents “skills” appearing in ChatGPT’s Code Interpreter environment and experimental Codex CLI support. A skill is a folder containing Markdown instructions plus optional references, data, and scripts; descriptions can be indexed first and full instructions loaded only when relevant. He demonstrates document-generation guidance that includes visually inspecting rendered PDF pages, and a Datasette plugin skill used through Codex. He sees a lightweight, potentially portable standard for reusable agent procedures, though no formal cross-vendor specification is established here.

### Comment pulse

- Commenters frame skills as prompt and context engineering with progressive disclosure, rather than a fundamentally new capability.
- Discussion distinguishes packaged local instructions and scripts from MCP-style remote tool invocation, while questioning whether standardization is necessary.

### LLM perspective

- View: The useful abstraction is selective procedural context, not the folder format by itself.
- Impact: Teams can package repeatable workflows without loading every instruction into every interaction.
- Watch next: Formal documentation, portability, trust boundaries for bundled scripts, and evidence that discovery scales cleanly.
