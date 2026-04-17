# AI cybersecurity is not proof of work

- Score: 193 | [HN](https://news.ycombinator.com/item?id=47791236) | Link: https://antirez.com/news/163

### TL;DR
Antirez argues AI-driven bug hunting is not like proof-of-work mining: for any fixed model, more tokens eventually stop helping because the true limit is the model’s intelligence and ability to reason over code states, not brute-force search. Using the subtle OpenBSD SACK vulnerability, he claims weaker models only pattern‑match or hallucinate, while a frontier system like Anthropic’s closed Mythos can actually understand and exploit it. HN debates Mythos secrecy, experiment rigor, and how AI reshapes security economics and attacker–defender dynamics.

---

### Comment pulse
- Secrecy around Mythos and vague “better model” claims → commenters question methodology, suspect marketing, countered by safety concerns and coding-focused training accidentally yielding security skills.  
- Tokens and model quality both matter → LLMs make scalable, on‑demand bug-hunting cheaper than hiring experts, though humans plus top models still outperform either alone.  
- AI shifts attack–defense balance → attackers need one bug, defenders many; orgs buy tokens — counterpoint: formal-methods plus AI may remove whole bug classes.

---

### LLM perspective
- Bug-finding behaves like search under a model-specific ceiling; intelligence and training domain beat sheer sampling volume.  
- Security work commoditizes into tokens; small teams and states gain capabilities once limited to elite consultancies and intelligence agencies.  
- Track comparative studies: weaker models with orchestration versus frontier models; measure real exploit rates, not just static bug flags.
