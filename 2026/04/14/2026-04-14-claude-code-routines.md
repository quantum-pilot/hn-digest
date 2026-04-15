# Claude Code Routines

- Score: 363 | [HN](https://news.ycombinator.com/item?id=47768133) | Link: https://code.claude.com/docs/en/routines

### TL;DR
Claude Code Routines let you turn Claude into an always-on automation agent: you define a prompt, repos, environment, and connectors, then trigger runs via schedules, API calls, or GitHub events. It can maintain backlogs, triage alerts, review PRs, verify deploys, and update docs, all from Anthropic-managed cloud sessions under your account. Hacker News discussion is far more skeptical: people worry about lock-in, opaque and shifting ToS, overlapping features, and perceived recent model quality regressions.

---

### Comment pulse
- Lock-in concerns → Users resist building workflows on Routines, citing nerfing risk, feature sunsetting, and provider-specific memories and connectors that aren’t portable between LLM vendors.  
- ToS ambiguity → People are confused and frustrated about when subscriptions can be used with third-party tools, OAuth, bots, or IDEs; some suspect intentional vagueness to limit heavy use.  
- Quality and product churn → Several report Claude coding performance degrading recently and mock Anthropic’s rapid, overlapping “yet-another-feature” releases that may silently break earlier workflows.

---

### LLM perspective
- View: Routines resemble managed CI plus agents; powerful but create strong dependency on Anthropic’s infra, terms, and model behavior.  
- Impact: Most useful for teams already committed to Claude Code, wanting automated PR review, alert handling, and doc maintenance without building their own agent runner.  
- Watch next: Clearer licensing around “third-party harnesses,” standardization of agent runtimes, and open-source/self-hosted equivalents that can swap between models.
