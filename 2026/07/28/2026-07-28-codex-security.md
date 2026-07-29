# Codex Security

- Score: 288 | [HN](https://news.ycombinator.com/item?id=49089755) | Link: https://github.com/openai/codex-security

### TL;DR
Codex Security is an open-source CLI and TypeScript SDK from OpenAI that scans repositories for security vulnerabilities, validates and tracks findings, and plugs into CI pipelines. It relies on the hosted Codex Security service, with authentication via ChatGPT sign-in or API keys, and keeps local scan state. HN discussion highlights powerful capabilities but early rough edges: high token cost, rate limiting, fragile long scans, questions about guardrails and local-LLM support, plus interest in its reusable English “skill” prompts and concerns about AI-created insecurities.

---

### Comment pulse
- Newly open-sourced CLI/SDK extends the existing Codex plugin to repos and CI; maintainer is active, invites feedback; users ask about guardrails and when to prefer plugin vs CLI.  
- Early testers report long, expensive scans that can fail on rate limits or HEAD changes with only partial output; maintainer apologizes, suggests `--max-cost`, promises better partial-result handling.  
- Some focus on the English “Skill” definitions as the real IP and reusable pattern; others question AI vendors selling security for problems AI code generation worsens.

---

### LLM perspective
- View: This is essentially an LLM-orchestrated security scanner; real value is in workflows, prompts, and CI integration, not the raw model.  
- Impact: Most useful for teams already on OpenAI stacks who want automated vuln triage and historical tracking, not as a replacement for traditional SAST yet.  
- Watch next: Independent benchmarks, clearer cost envelopes, resilience to repo changes, optional alternative backends, and transparency around guardrails that redact vulnerability details.
