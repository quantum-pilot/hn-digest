# How I use every Claude Code feature

- Score: 461 | [HN](https://news.ycombinator.com/item?id=45786738) | Link: https://blog.sshh.io/p/how-i-use-every-claude-code-feature

TL;DR
Engineer details a practical Claude Code playbook: keep CLAUDE.md as concise guardrails, audit context with /context, avoid /compact in favor of /clear + /catchup and “document & clear,” prefer general-agent Task clones over custom subagents, enforce pre-commit tests via Hooks, plan before coding, favor Skills/CLIs with MCP as a minimal secure gateway, leverage SDK for batch refactors and GHA for auditable PRs, and tune settings. HN discussion flags CLAUDE.md compliance variability, support for MCP-as-gateway, and frustration with compaction latency/failures.

Comment pulse
- Claude often ignores CLAUDE.md rules → users report better compliance by simplifying and emphasizing instructions; others still see inconsistent adherence.
- MCP should be a minimal auth/data gateway → expose few high‑level tools, let Skills/CLIs handle scripting; some build MCP “proxies” or code interpreters.
- /compact criticized → slow, failure‑prone, with hidden reserved context; /clear plus a custom /catchup is faster and more reliable — counterpoint: compaction may improve soon.

LLM perspective
- View: Treat coding agents as CI-grade coworkers: small guardrails, commit-stage checks, self-orchestrated delegation, and externalized memory beat tool proliferation.
- Impact: Dev productivity, platform teams, and security benefit; standardized manifests, logs, and GHAs make agent work auditable and improvable.
- Watch next: Reliable compaction, signed Skills with policy, MCP auth/hardware sandboxes, metrics for instruction adherence, and benchmarks for agent-led PR quality.
