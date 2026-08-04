# Codex Security

- Score: 288 | [HN](https://news.ycombinator.com/item?id=49089755) | Link: https://github.com/openai/codex-security

### TL;DR

OpenAI open-sourced a CLI and TypeScript SDK for scanning repositories, validating and fixing vulnerabilities, tracking findings, reviewing changes, and running checks in CI. It supports ChatGPT or API-key authentication, stores scan history locally, and requires Node 22 plus Python 3.10. The HN discussion quickly exposed rough edges: rate limits, unclear resumption, high token cost, authentication confusion, and a 50-minute scan invalidated because repository HEAD changed. Contributors acknowledged these failures and said changing checkouts and partial-result recovery need substantial improvement.

### Comment pulse

- Reliability can erase value → one scan consumed half a Pro weekly allowance before failing on a changed HEAD and requiring restart.
- Product boundaries are unclear → users asked when to choose the CLI over the plugin and whether local OpenAI-compatible endpoints work.
- Open-source skills expose reusable value → commenters see optimized English task definitions as useful beyond security scanning.

### LLM perspective

- View: Security agents must preserve evidence incrementally; final-state validation should not invalidate an hour of completed analysis.
- Impact: Teams need stable checkouts, explicit budgets, and CI authentication before trusting autonomous scans in development workflows.
- Watch next: Add resumable scans, rate-limit backoff, local-provider support, checkout-change handling, and transparent vulnerability disclosure behavior.
