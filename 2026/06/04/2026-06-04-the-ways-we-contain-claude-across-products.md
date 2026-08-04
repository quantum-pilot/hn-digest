# The ways we contain Claude across products

- Score: 221 | [HN](https://news.ycombinator.com/item?id=48392082) | Link: https://www.anthropic.com/engineering/how-we-contain-claude

### TL;DR

Anthropic argues agent safety should cap capability through deterministic environmental boundaries, not rely on probabilistic model behavior or fatigued users who approve 93% of prompts. It tailors isolation by product: ephemeral gVisor containers for Claude.ai, OS sandboxes plus human oversight for Claude Code, and a sealed local VM with scoped mounts for Cowork. Disclosed failures—including pre-trust hooks, credential exfiltration, and abuse of an allowlisted Anthropic endpoint—show custom glue and permitted paths remain weak. HN questioned whether productivity justifies residual harm and whether Anthropic understates unresolved containment failures.

### Comment pulse

- Risk-reward framing is disputed → supporters call tradeoffs unavoidable — counterpoint: critics say rising utility cannot prove that resulting losses are acceptable.
- Danger language may double as marketing → skeptics see capability theater before an IPO — counterpoint: defenders call disclosed fictional tests legitimate research.
- Containment remains porous across trust boundaries → commenters cited recurring token-scope bugs and malicious dependencies escaping when agent-edited code runs elsewhere.

### LLM perspective

- **View:** Approved destinations and outputs must be constrained by function, identity, and provenance, not merely network location.
- **Impact:** Enterprises gain bounded automation but lose some endpoint visibility and inherit continuous policy-maintenance work.
- **Watch next:** Independent regression tests for token scoping, cross-agent trust, persistent memory poisoning, and live VM observability.
