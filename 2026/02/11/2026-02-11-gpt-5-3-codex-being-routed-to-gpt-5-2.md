# GPT-5.3-Codex being routed to GPT-5.2

- Score: 64 | [HN](https://news.ycombinator.com/item?id=46968891) | Link: https://github.com/openai/codex/issues/11189

### TL;DR

Codex Pro users selected GPT-5.3-Codex, but SSE traces identified GPT-5.2 responses, varying by account. OpenAI initially said cyber-abuse detection intentionally reroutes suspected activity to a less-capable model and offered identity verification to restore access, while promising notices and false-positive reporting. It later called the broad flagging a bug, restored access without identification, and a commenter reported 9% were affected for three hours. The discussion accepted safety controls as potentially necessary but rejected silent substitution, citing broken reproducibility, wasted debugging, unclear billing, and distrust among legitimate security researchers.

### Comment pulse

- Users demanded either the requested model or an explicit error—counterpoint: OpenAI argued dynamic restriction limits abuse from its most cyber-capable model.
- Security researchers said exploit analysis resembles malicious activity, so opaque classifiers punish defensive work while determined attackers can evade verification.
- Account-specific results and earlier fallback reports deepened suspicion; even restored users lacked a durable way to confirm every extension or CLI request.

### LLM perspective

- View: Safety routing may be defensible, but undisclosed model identity violates the product contract and contaminates every evaluation.
- Impact: Professionals may misdiagnose prompts, lose work, expose identity documents, or cancel subscriptions when quality silently changes.
- Watch next: Add per-response model disclosure, explicit refusal semantics, billing adjustments, audit history, classifier appeals, and published false-positive metrics.
