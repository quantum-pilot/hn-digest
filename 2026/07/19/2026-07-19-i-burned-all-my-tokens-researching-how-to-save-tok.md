# I burned all my tokens researching how to save tokens

- Score: 89 | [HN](https://news.ycombinator.com/item?id=48967355) | Link: https://quesma.com/blog/custom-deep-research-pipeline/

### TL;DR
The author tried Claude’s `/deep-research` to map “tokenomics” and instantly maxed out a Claude Max 5× plan with 111 agents and no final report. They rebuilt the workflow as a multi-model, multi-vendor pipeline: cheap models search, stronger ones verify, the most expensive only plan and arbitrate, and external CLIs (OpenAI Codex, Gemini) act as headless subagents, all sharing a local memory. Verification rules plus human review gate every claim. Deep-research now runs last over pre-verified facts, extending useful research time ~10× with no extra spend and yielding a curated Obsidian “LLM wiki.”  

---

### Comment pulse
- Cloud AI is seen as self-referential hype → some complain it mostly powers blogs about AI; others say they quietly ship real products and see clear ROI.  
- Hallucinations are fundamental → commenters argue you can’t “rule them away”; prompts and cross-checking only reduce, never eliminate them.  
- Local vs cloud cost tradeoff → many say decent local research models need multi‑$k hardware; cheap cloud models and smart routing are usually more economical.  

---

### LLM perspective
- View: The real optimization lever is orchestration—role-based model routing, memory, and verification—rather than obsessing over a single “best” model.  
- Impact: Teams running agents or eval-heavy workflows can slash surprise bills and improve reliability by formalizing these stages and anti-hallucination gates.  
- Watch next: Tools that auto-tune harnesses, cache use, and model mixes per task budget, plus better spend observability beyond naive token counters.
