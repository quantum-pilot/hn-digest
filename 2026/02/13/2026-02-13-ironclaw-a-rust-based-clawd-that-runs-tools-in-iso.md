# IronClaw: a Rust-based clawd that runs tools in isolated WASM sandboxes

- Score: 137 | [HN](https://news.ycombinator.com/item?id=47004312) | Link: https://github.com/nearai/ironclaw

### TL;DR

IronClaw is an OpenClaw-inspired Rust agent runtime focused on privacy and security. Its repository history shows WASM tools for Google services, Slack, and Telegram using HTTP allowlists, credential injection, rate limits, and scoped OAuth; separate container sandboxes handle jobs. Recent commits also repaired path traversal, an orchestrator-authentication gap, credential exposure in errors, and unbound Telegram access. Commenters questioned the absent threat model and whether web access plus code execution defeats isolation; defenders said granular capabilities and keeping secrets outside the model still reduce damage, while conceding sandboxes are insufficient alone.

### Comment pulse

- Granular WASM isolation has a clear target → malicious tools receive constrained network access and never directly see injected credentials.
- Critics want proof, not architecture slogans → the supplied page offers no explicit threat model, boundary analysis, adversarial evidence, or independent audit.
- Sandboxes reduce blast radius → counterpoint: authorization, output effects, prompt injection, and abnormal model behavior still need orchestration guardrails.

### LLM perspective

- View: Recent security fixes demonstrate active hardening, but also show why repository claims cannot establish security.
- Impact: Self-hosters gain finer-grained tool isolation while inheriting a young runtime’s configuration, integration, and review burden.
- Watch next: Published threat model, capability matrix, adversarial tests, independent audit, exploit disclosures, default-deny behavior, and safe web-plus-code workflows.
