# Small models also found the vulnerabilities that Mythos found

- Score: 749 | [HN](https://news.ycombinator.com/item?id=47732020) | Link: https://aisle.com/blog/ai-cybersecurity-after-mythos-the-jagged-frontier

### TL;DR
AISLE tests Anthropic’s Mythos claims by feeding the showcased vulnerable functions (FreeBSD NFS, OpenBSD SACK, an OWASP snippet) to small, cheap, largely open models. Once the relevant code is isolated, these models often match or rival frontier models on detection and exploitability reasoning, and sometimes beat them on false-positive avoidance. AISLE argues AI security power is “jagged”: no single best model, and the real moat is the surrounding system (scaffold, validation, triage, maintainer trust), not exclusive access to one frontier model.

---

### Comment pulse
- AISLE’s test is cherry-picked → isolating known-bad functions with hints isn’t comparable to Mythos exhaustively scanning huge codebases. — counterpoint: Anthropic’s own harness also narrows to per-file prompts.  
- System > model → many agree the harness (file ranking, ASan, triage) is the core value; cheap models can be run broadly, then escalated to stronger ones.  
- Risk and economics → Mythos runs reportedly cost ~$20k per large search; critics say that’s hype plus trophy-bug hunting, defenders say capability still matters even if expensive.

---

### LLM perspective
- View: AISLE’s data convincingly shows security capability is uneven across tasks and model sizes; “frontier-only” stories are overstated.  
- Impact: Organizations can start AI-assisted security using smaller/open models plus good pipelines, instead of waiting for restricted mythic systems.  
- Watch next: Independent, repo-scale benchmarks comparing open vs frontier models under identical harnesses, with false-positive rates and full cost accounting.
