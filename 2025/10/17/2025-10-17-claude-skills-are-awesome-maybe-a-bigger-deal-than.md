# Claude Skills are awesome, maybe a bigger deal than MCP

- Score: 388 | [HN](https://news.ycombinator.com/item?id=45619537) | Link: https://simonwillison.net/2025/Oct/16/claude-skills/

### TL;DR

Simon Willison describes Claude Skills as folders containing concise Markdown instructions, optional references, and executable scripts that models load only when relevant. Small frontmatter descriptions keep initial context cost low, while a filesystem and command-running environment supply the real capability. He argues this progressive disclosure can be simpler and more token-efficient than exposing large MCP tool catalogs, and that skills are portable across coding agents. The tradeoff is substantial: powerful local execution demands strong sandboxing, while MCP still offers standardized remote tools, authentication, resources, and nonterminal clients.

### Comment pulse

- Teams reported independently building task-specific documentation trees because monolithic repository context files consumed too much context.
- Commenters argued Skills and MCP are complementary: instructions can orchestrate tools, while MCP standardizes remote access and authentication.
- Several saw immediate feedback from agents as a new incentive to write precise, task-oriented documentation.

### LLM perspective

- View: Skills are a lightweight packaging convention; their leverage comes from selective context plus a capable execution harness.
- Impact: Teams can encode procedures incrementally without building a protocol server for every workflow.
- Watch next: Standardize dependency declarations, provenance, permissions, and tests before sharing executable skills broadly.
