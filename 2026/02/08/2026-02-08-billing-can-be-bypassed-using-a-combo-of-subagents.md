# Billing can be bypassed using a combo of subagents with an agent definition

- Score: 180 | [HN](https://news.ycombinator.com/item?id=46936105) | Link: https://github.com/microsoft/vscode/issues/292452

### TL;DR
A VS Code Copilot user found that by chaining “subagents” to a premium-model agent, they could run expensive models like Claude Opus almost unlimitedly while being billed only for a cheap “free” model, because billing was computed on the initial agent and subagent/tool calls weren’t metered. A second variant used looping tool calls to keep premium subagents running for hours on a single credit. Microsoft’s security response initially rejected it as out-of-scope billing abuse; the public issue was later reopened and commenters say it’s now patched.

---

### Comment pulse
- Copilot pricing seen as already a good Claude gateway → fixed monthly fee, message-based billing, agents and PRs; critics say harness is weaker and quotas small for heavy users.  
- Microsoft’s MSRC and triage process criticized → teams bounce responsibility, auto-close issues, and force reporters to chase the “right” forum—counterpoint: bug was eventually reopened and assigned.  
- Per-invocation “premium request” model called structurally broken for long-running agents → some argue pay-per-token also warps incentives; enshitification risks are baked into current business models.  
- Observation: many agentic IDEs enforce billing and guardrails client-side → local business logic becomes an obvious target for exploits like this.

---

### LLM perspective
- View: Any client-side-only metering for multi-agent systems is fundamentally fragile; determined users will chain tools/agents to bypass pricing tiers.  
- Impact: Copilot, Cursor, Replit, JetBrains AI, etc. must harden server-side billing/quotas and re-audit tool-calling/agent orchestration paths.  
- Watch next: clearer premium metering for agent sessions, server-validated “message types,” and public postmortems on how these bypasses were found and fixed.
