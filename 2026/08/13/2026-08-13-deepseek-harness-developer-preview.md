# DeepSeek Harness developer preview

- Score: 544 | [HN](https://news.ycombinator.com/item?id=49285244) | Link: https://deepseek.com/harness/en/

### TL;DR

DeepSeek released a source-included, MIT-licensed developer preview of its agent harness. Built on Cordis, it makes models, tools, skills, sandboxes, storage, loops, scheduling, sessions, and UI swappable plugins. An append-only event stream records prompts, reasoning, tool results, subagent scheduling, and context injections, powering inspection, resume, fork, search, and replay. Standard, code, minimal, and creator modes target different workflows. An author warns of rough edges and breaking changes; commenters praised traceability but debated novelty, dependency complexity, and overlap with earlier plugin systems.

### Comment pulse

- Trace enthusiasts value inspecting the complete model-visible trajectory for debugging and tool improvement.
- Framework veterans liked hot reload and cleanup—counterpoint: cross-plugin dependency resolution may add footguns with little benefit for independent plugins.

### LLM perspective

- View: Composability is useful only if stable contracts let plugins move between configurations without recreating hidden assumptions.
- Impact: Harness developers gain an inspectable experimentation platform, while sensitive reasoning and tool logs create new data-governance obligations.
- Watch next: API stability, plugin adoption, replay fidelity, MCP support, lifecycle cleanup, and trace redaction will reveal production readiness.
