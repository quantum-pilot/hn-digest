# GitHub Agentic Workflows

- Score: 192 | [HN](https://news.ycombinator.com/item?id=46934107) | Link: https://github.github.io/gh-aw/

- TL;DR  
  GitHub Agentic Workflows lets you describe “AI agents” for repo maintenance (triage, reports, refactors, docs, compliance) as markdown. A `gh aw` CLI compiles these into guarded GitHub Actions workflows with read‑only defaults, explicit allowlisted write operations, sandboxing, and support for multiple LLMs (Copilot, Claude, Codex). It’s explicitly early-stage and warns about security and supervision needs. HN reactions highlight brittle AI changes in real gh‑aw PRs, security distrust around Actions, and frustration that GitHub prioritizes AI over core reliability.

- Comment pulse  
  AI agents often mangle dependency and config updates → string-editing go.mod/package.json, hallucinating versions, ignoring proper tooling; reinforces view that current LLMs only pattern-match text.  
  GitHub’s focus on AI irks maintainers → long-standing GitHub Actions and free-tier issues feel neglected while resources go to “AI bullshit” and odd Copilot nags.  
  Security and UX doubts → “security-first” claims clash with Actions’ reputation; `gh aw init` auto-created tokens until recently, now patched with extra confirmations.

- LLM perspective  
  View: Useful concept if workflows are narrow, auditable, and treated as junior assistants, not autonomous maintainers.  
  Impact: Busy OSS maintainers and large orgs could offload rote triage, reporting, and refactors—if they invest in review discipline.  
  Watch next: Real-world incident reports, default permission hardening, and benchmarks comparing AI workflows vs. human scripts for correctness and maintenance cost.
