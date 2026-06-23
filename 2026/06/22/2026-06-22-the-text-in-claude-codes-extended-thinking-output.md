# The text in Claude Code’s “Extended Thinking” output

- Score: 265 | [HN](https://news.ycombinator.com/item?id=48630535) | Link: https://patrickmccanna.net/the-text-in-claude-codes-extended-thinking-output-is-not-authentic/

### TL;DR
The blog post inspects Claude Code’s local “Extended Thinking” logs and discovers they contain only encrypted “signatures,” not the model’s actual chain-of-thought. Anthropic’s docs confirm that what users see is a summary of internal reasoning, and full access is gated behind enterprise agreements. The author argues this undermines audit trails and transparency for agent behavior. Hacker News discussion emphasizes security and trust implications of hidden reasoning, while others defend obfuscation as necessary IP protection and anti-distillation strategy.

---

### Comment pulse
- Hidden reasoning is a security and reliability risk → users can’t see prompt-injected objectives, secret server-side actions, or token-wasting loops—counterpoint: visible tool calls limit some exfiltration avenues.  
- Vendors hide raw CoT to protect proprietary inference methods and prevent competitors from distilling their models—postprocessed summaries are less useful training data but also less useful to end-users.  
- Some say this behavior is long-known and driven by anti-distillation, not deception; others note CoT isn’t “human reasoning” anyway and might alarm users if shown verbatim.

---

### LLM perspective
- View: Encrypted CoT is a rational business move but conflicts with claims of auditability, controllability, and “agents you can supervise.”  
- Impact: Security-sensitive, regulated, or safety-critical deployments should treat these systems as opaque services, not inspectable collaborators.  
- Watch next: Enterprise contracts, regulatory guidance, and open models offering verifiable logging will determine whether transparent reasoning becomes a competitive requirement.
