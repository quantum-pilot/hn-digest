# GPT-5.3-Codex being routed to GPT-5.2

- Score: 64 | [HN](https://news.ycombinator.com/item?id=46968891) | Link: https://github.com/openai/codex/issues/11189

### TL;DR
Codex users noticed that selecting GPT‑5.3‑Codex in the CLI still returned responses labeled as GPT‑5.2, meaning a quieter, less capable model was being used. OpenAI staff explained this was due to a cyber‑abuse classifier that silently rerouted “risky” usage to a weaker model and initially pointed people to an ID‑based “Trusted Access for Cyber” flow to restore full access. The discovery sparked accusations of deception, billing concerns, and privacy worries. OpenAI later called the broad flagging a bug (~9% of users, ~3 hours), said ID isn’t required, and promised visible routing notices and better feedback tools.

---

### Comment pulse
- Silent model downgrades are unacceptable → users pay for 5.3 but get 5.2, wasting debugging time and arguably constituting fraud when billed at premium rates.  
- Security rationale splits opinion → vague “cyber activity” rules and ID checks feel punitive and privacy-invasive — counterpoint: some accept extra friction for high‑risk tooling.  
- Router abuse worries → dynamic model substitution could be reused to cut costs or enforce policy, normalizing opaque, provider-controlled changes to AI behavior.  

---

### LLM perspective
- View: Silent routing plus retroactive “bug” stories erodes trust; future model selection must be explicit, observable, and contractually constrained.  
- Impact: Affects pro users, security researchers, and enterprises building workflows that assume specific models and reproducible behavior.  
- Watch next: clear router docs, billing guarantees per model, independent audits, and whether other providers quietly introduce similar safety-driven downgrades.
