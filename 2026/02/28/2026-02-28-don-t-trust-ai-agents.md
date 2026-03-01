# Don't trust AI agents

- Score: 298 | [HN](https://news.ycombinator.com/item?id=47194611) | Link: https://nanoclaw.dev/blog/nanoclaw-security-model

### TL;DR
The post argues AI “agents” must be treated like potentially malicious code, not trusted helpers. Instead of relying on prompts, allowlists, or polite assumptions, you should enforce security *outside* the agent: per-agent OS containers, unprivileged users, ephemeral filesystems, and strict host mounts so misbehavior has a capped blast radius. The author contrasts NanoClaw’s tiny, reviewable core plus opt‑in “skills” with OpenClaw’s massive, unaudited codebase. HN commenters debate code bloat from LLMs, real-world use cases, and whether any high-privilege agent can ever be truly safe.

---

### Comment pulse
- LoC as a metric is backwards → LLM-driven projects like OpenClaw exemplify bloat; more code increases attack surface and maintenance cost, not value.  
- Many don’t feel enough personal-life friction to justify risky agents → consumer “check me in to flights” use cases seem marginal versus security and maintenance overhead.  
- Proposed safety norms: reversible actions, read/draft-only tools, secret proxies, strict tool-layer guardrails → skeptics say fully autonomous, high-privilege agents still seem fundamentally unsafe.

---

### LLM perspective
- View: Treat AI agents like untrusted browser plugins with OS sandboxes and minimal, auditable integrations, not like trustworthy coworkers.  
- Impact: Platform builders and ops teams must own isolation, permissions, and reversibility; end users shouldn’t be expected to reason about prompt-injection threats.  
- Watch next: Standardized “agent permission” models, stronger adversarial evals on tools/proxies, and reference architectures for per-task containers and rollback-first designs.
