# Cloudflare outage on December 5, 2025

- Score: 516 | [HN](https://news.ycombinator.com/item?id=46162656) | Link: https://blog.cloudflare.com/5-december-2025-outage/

### TL;DR

Cloudflare says a 25-minute incident affected approximately 28% of its HTTP traffic after changes intended to mitigate a React Server Components vulnerability. A gradual increase in WAF request-body buffering exposed a test-tool issue; disabling that tool through a fleet-wide configuration system triggered a years-old nil-access bug in the legacy Lua-based FL1 proxy. The company ruled out an attack, and reverting restored service. Commenters focused on instant global propagation, slow detection and rollback, inaccurate status reporting, and repeated outages before promised safeguards were deployed.

### Comment pulse

- Concentration magnifies ordinary mistakes → one change disrupts unrelated customers — counterpoint: centralized infrastructure may still outperform most self-hosted alternatives.
- Global configuration lacked staged rollout → alerts fired after full propagation, and rollback began roughly 24 minutes after deployment.
- Legacy typing mattered locally → Rust-based FL2 avoided this nil access, but commenters argued language choice cannot contain architectural blast radius.

### LLM perspective

- View: The decisive failure was an unbounded control-plane change reaching legacy behavior, not merely one Lua null dereference.
- Impact: Customers must reassess dependency concentration and fallback paths while Cloudflare pauses changes to install safeguards.
- Watch next: Gradual configuration rollouts, automated health rollback, fail-open defaults, status automation, and the promised resilience report.
