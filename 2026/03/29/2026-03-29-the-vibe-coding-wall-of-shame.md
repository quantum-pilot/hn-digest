# The "Vibe Coding" Wall of Shame

- Score: 120 | [HN](https://news.ycombinator.com/item?id=47566491) | Link: https://crackr.dev/vibe-coding-failures

### TL;DR
A training/interview-prep site built a “Wall of Shame” cataloging 30+ incidents where AI-generated or “vibe-coded” software allegedly caused outages, RCEs, and data leaks at Amazon, Meta, Replit, IDEs, and more. The pattern: non-experts ship AI-written code they don’t fully understand, driving a spike in CVEs and systemic security gaps (CSRF, SSRF, missing auth). The author’s prescription is old-school: developers still need fundamentals and code comprehension; AI is a sharp tool, not a replacement. HN questions the rigor and motives of the list.

---

### Comment pulse
- Attribution is fuzzy → Several entries mislabel vendors or lack proof that AI/vibe coding caused the bugs—counterpoint: even imperfect, the trend of AI-related incidents is worth tracking.  
- Concept overstated → Critics say this is mostly “systems where AI was present,” not pure vibe coding, and bugs long predate LLMs.  
- Feels like marketing/slop → People note blogspam sources, dead links, and that the host site itself looks AI-generated, undermining its credibility.

---

### LLM perspective
- View: Using AI as an unreviewed code generator predictably magnifies classic security mistakes and makes supply chain attacks easier.  
- Impact: Org leaders, security teams, and junior devs are most exposed; strong code review and training become more critical, not less.  
- Watch next: Independent, reproducible studies comparing AI-assisted vs manual codebases, plus hardening of AI IDEs and stricter org policies around agent autonomy.
