# Claude Code sends 33k tokens before reading the prompt; OpenCode sends 7k

- Score: 426 | [HN](https://news.ycombinator.com/item?id=48883275) | Link: https://systima.ai/blog/claude-code-vs-opencode-token-overhead

## TL;DR
Claude Code’s coding agent reportedly spends tens of thousands of tokens (e.g., 33k vs OpenCode’s 7k) before even engaging with a user’s prompt, largely due to aggressive use of subagents and tools, each re-reading large system prompts and code context. Commenters describe “tokenflation” where trivial actions trigger many tool calls, suspecting misaligned business incentives or just poor engineering. Others argue raw token counts are the wrong metric; what matters is cost per successful task and tooling quality.  
*Content unavailable; summarizing from title/comments.*

## Comment pulse
- Subagents multiply costs → each spawns with ~30k system prompt, re-reads code, misses cache, so parallelism explodes token use—counterpoint: exhaustive multi-agent search can be valuable for planning/exploration.  
- Incentives questioned → some see Anthropic as “token merchants”; others note flat-fee subs and call it incompetence plus organizational disinterest, not deliberate gouging.  
- Metrics and tooling → raw prompt size misleads; excessive tool calls drive “tokenflation.” Better benchmarks, smarter tools, and repo-aware techniques (hash-anchors, AST parsing) cut waste.

## LLM perspective
- View: Optimize for “successful change per dollar and minute,” not minimal tokens; allow user control over agent/tool aggressiveness.  
- Impact: Over-eager coding agents especially hurt small teams; enterprises absorb costs but may demand tighter governance and logging.  
- Watch next: Expect per-tool token breakdowns, tunable subagent limits, and head-to-head benchmarks on large, real-world repositories.
