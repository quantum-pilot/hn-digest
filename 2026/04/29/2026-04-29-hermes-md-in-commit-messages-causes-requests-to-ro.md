# HERMES.md in commit messages causes requests to route to extra usage billing

- Score: 935 | [HN](https://news.ycombinator.com/item?id=47952722) | Link: https://github.com/anthropics/claude-code/issues/53262

### TL;DR  
A Claude Code bug caused any repo with the case‑sensitive string `HERMES.md` in recent git commit messages to bypass users’ Max-plan quotas and bill “extra usage” instead, silently burning money while dashboards showed plenty of capacity. The reporter lost about $200 and provided a minimal repro. Anthropic called it an overactive anti‑abuse rule and fixed it. After public backlash over a “no compensation for technical errors” response (likely AI-generated), Anthropic reversed course, promising full refunds plus extra credits and support-process changes.

---

### Comment pulse  
- Initial “no compensation for technical errors” reply shocks users → seen as unethical, possibly illegal, and almost certainly written by a refund‑averse LLM — counterpoint: policy was later reversed.  
- Multiple anecdotes of unexplained charges, failed refunds, and vanishing credits → people resort to chargebacks or abandoning accounts due to unresponsive bot‑only support.  
- Anti‑abuse that silently upcharges instead of blocking is viewed as hostile; many note you must “go viral” on HN/X to get real help.

---

### LLM perspective  
- View: Billing and abuse decisions driven by opaque classifiers plus AI-only support is a recipe for trust-eroding edge cases like this.  
- Impact: Developers and enterprises may reevaluate relying on Anthropic for mission‑critical workloads if billing feels unpredictable or adversarial.  
- Watch next: Detailed postmortem, user-facing billing traces, guarantees about quota-first routing, and clear human escalation paths for any money-related disputes.
