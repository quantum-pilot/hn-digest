# Potential session/cache leakage between workspace instances or consumer accounts

- Score: 267 | [HN](https://news.ycombinator.com/item?id=48785485) | Link: https://github.com/anthropics/claude-code/issues/74066

### TL;DR
An Anthropic Claude enterprise user reports seeing inexplicable “Minecraft” code and other foreign context in fresh sessions, raising fears of session/cache leakage between workspaces or consumer accounts. Commenters debate whether this indicates serious infrastructure isolation failures—like HTTP desync or misrouted cached responses—versus an unusually pathological hallucination or cache-miss behavior. Anthropic staff reply that they currently believe it’s hallucination but are investigating. The thread highlights how hard it is to distinguish privacy‑impacting leaks from model errors, especially for regulated data.  

*Content unavailable; summarizing from title and comments only.*

---

### Comment pulse
- Infra bugs can swap client responses → past large‑vendor incidents from HTTP desync/request smuggling on multiplexed connections—counterpoint: no concrete evidence this case matches.  
- Probably bizarre hallucination or cache-miss artifact → LLMs sometimes emit unrelated conversations or languages, especially with long contexts; missing cache input can trigger foreign content.  
- Privacy concerns are acute → even transient cross‑tenant responses could break HIPAA/ZDR promises; commenters demand clear postmortems, transparency, and better control over Claude Code memory.  

---

### LLM perspective
- View: Incident shows ambiguity between hallucinations and infra leaks; safety claims need technical proofs, not assurances, especially for enterprise deployments.  
- Impact: Enterprise and regulated users may reassess reliance on closed LLM services, demanding stronger isolation guarantees and contractual remedies.  
- Watch next: Anthropic report, red‑team tests for cross‑tenant leakage, and industry standards for logging and disclosing LLM failures.
