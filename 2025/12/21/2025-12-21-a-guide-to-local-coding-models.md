# A guide to local coding models

- Score: 139 | [HN](https://news.ycombinator.com/item?id=46348329) | Link: https://www.aiforswes.com/p/you-dont-need-to-spend-100mo-on-claude

### TL;DR
The author tests whether a $4.7k, 128 GB MacBook running local coding models can replace a $100+/month cloud subscription like Claude Code. After weeks with Qwen-based setups via MLX/Ollama and Qwen Code, they conclude local models are surprisingly strong (covering ~90% of typical dev tasks) and great for privacy, offline use, and cost control—but they still fall short on the hardest 10%, where frontier cloud models shine. The article pivots from “ditch subscriptions” to “use locals as a supplemental, cost-saving tool.”

---

### Comment pulse
- Subscription economics → Many hobbyists jump straight to $100–200/month; several argue $20 plans or pay-per-token usually suffice—counterpoint: heavy users hit low limits quickly.  
- Tooling landscape → Readers note LM Studio and ramalama as important omissions; some distrust LM Studio’s closed source given the privacy rationale for local models.  
- Hardware vs progress → Skepticism that a $5k laptop can stay competitive for 5 years; hardware ages while cloud SOTA advances faster than local efficiency gains.

---

### LLM perspective
- View: Local models are best treated as “good enough most of the time,” not primary engines for mission‑critical coding.  
- Impact: Hobbyists and privacy‑sensitive users gain options; companies still lean on managed frontier models plus occasional on‑prem.  
- Watch next: Benchmarks of 7–30B coders vs Gemini/Claude, better open-source coding UIs, and realistic TCO comparisons including electricity, maintenance, and opportunity cost.
