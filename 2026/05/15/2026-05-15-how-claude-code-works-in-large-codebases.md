# How Claude Code works in large codebases

- Score: 229 | [HN](https://news.ycombinator.com/item?id=48144494) | Link: https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start

### TL;DR
Anthropic describes Claude Code’s approach to huge, messy repositories as “agentic search”: it runs locally, walks the filesystem, uses grep and LSP rather than maintaining global vector indexes. Performance depends heavily on a configurable “harness” (CLAUDE.md hierarchy, hooks, skills, plugins, MCP integrations, subagents) and organizational ownership. Recommended patterns: make the repo navigable for the agent, keep CLAUDE.md lean and updated as models evolve, and assign an “agent manager” to standardize setups. HN commenters question the dismissal of indexing and report harness friction and token costs.

### Comment pulse
- “Like a software engineer” claim disputed → real engineers lean on IDE indexes, LSP, and memory, not naive grep-based traversal of huge repos.  
- Agentic search feels brute-force → grep on massive trees times out, burns tokens, and can re-explore static code instead of building durable shared understanding.  
- Harness configuration seen as brittle → CLAUDE.md, skills, plugins often ignored; commenters note JetBrains/Copilot indexing works at scale—counterpoint: Claude can call IDE indexes via MCP.  

### LLM perspective
- View: Agentic search plus IDE/LSP integration is complementary; neither raw grep nor global embedding alone fits all enterprise codebases.  
- Impact: Success hinges on someone owning “AI dev tooling” to prune CLAUDE.md, maintain skills, and standardize plugins across teams.  
- Watch next: Better auto-harness generation, tool-usage reliability metrics, and sidecar agents that build durable semantic maps of codebases over time.
