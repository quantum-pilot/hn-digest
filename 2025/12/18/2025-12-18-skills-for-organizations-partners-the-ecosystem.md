# Skills for organizations, partners, the ecosystem

- Score: 219 | [HN](https://news.ycombinator.com/item?id=46315414) | Link: https://claude.com/blog/organization-skills-and-directory

### TL;DR
Anthropic extends Claude “Skills” from personal workflows to organization-wide infrastructure: admins can centrally provision skills, users can discover and edit them more easily, and a skills directory now ships partner-built workflows for tools like Atlassian, Figma, Canva, Cloudflare, Vercel, Sentry, and Zapier. Underneath, “Agent Skills” is launched as an open standard so the same packaged workflow (instructions + optional code/scripts) can work across AI platforms. HN discussion focuses on whether this pattern is durable, composable, and more than just fancy prompts.

---

### Comment pulse
- Skills as control plane → Let LLMs plan and choose tools; keep parsing/simulation in deterministic code with clear I/O contracts and composable “process” templates.  
- What a skill really is → Lazy-loaded, curated context plus optional executable code/scripts; cheaper and simpler than MCP, but adds to rapidly changing “standards” churn.  
- Hype vs rigor → Some see a JS-style circus and weak standards/security culture; others think skills quietly fix old expert-system problems and are practically useful now.

---

### LLM perspective
- View: Skills formalize “reusable workflows + tools” as a shareable artifact, sitting between ad‑hoc prompts and full-blown agent frameworks.  
- Impact: Enterprises, SaaS vendors, and consultants gain a portable way to encode best practices without retraining models or building heavy agent stacks.  
- Watch next: Independent security reviews, real productivity benchmarks, and convergence (or fragmentation) among Agent Skills, MCP, A2A, and similar ecosystems.
