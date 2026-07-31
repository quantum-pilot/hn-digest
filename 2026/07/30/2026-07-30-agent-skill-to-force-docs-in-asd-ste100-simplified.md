# Agent Skill to Force Docs in ASD-STE100 Simplified Technical English

- Score: 152 | [HN](https://news.ycombinator.com/item?id=49114639) | Link: https://github.com/AminBlg/SimpleEnglish

### TL;DR
An “agent skill” was shared that forces LLM-generated documentation to follow ASD‑STE100, a controlled “Simplified Technical English” standard used in aerospace and other safety‑critical docs. Commenters debate whether such a skill is actually needed: some want constrained language because modern LLM prose is dense and hard to audit, while others argue a single prompt (“rewrite in ASD‑STE100”) already works. Related tools applying style guides (like The Economist’s) show value, but STE itself has known misapplication and adoption issues.

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Need for controlled language → LLMs now handle complex tasks, but their prose grows opaque; standards like ASD‑STE100 could keep docs reviewable and consistent.  
- “Agent skills” are cruft → a short prompt can enforce STE, so extra tooling is unnecessary overhead — counterpoint: reusable skills codify constraints and reduce human prompting error.  
- Style plugins show promise → economist‑style and similar guides improve structure; however, STE’s real‑world misapplication and limited adoption make strict enforcement a nuanced choice.

---

### LLM perspective
- View: Controlled-language skills are most useful in regulated or multi-author environments where consistent wording and terminology are mandatory.  
- Impact: Tech writers, QA, and compliance teams can integrate STE checks into CI pipelines, treating language control like linting.  
- Watch next: Objective STE adherence metrics, comprehension studies with human readers, and IDE/docs tooling that surface controlled-language violations in real time.
