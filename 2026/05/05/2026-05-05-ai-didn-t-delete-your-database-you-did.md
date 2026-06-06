# AI didn't delete your database, you did

- Score: 485 | [HN](https://news.ycombinator.com/item?id=48022742) | Link: https://idiallo.com/blog/ai-didnt-delete-your-database-you-did

### TL;DR
The article pushes back on blaming an AI coding agent for wiping a production database, arguing the real failure was human: unsafe architecture, over-privileged access, and “vibe-coded” systems nobody truly understands. The author contrasts AI with real automation: CI/CD removes whole classes of human error, whereas stochastic LLMs add new ones and cannot explain themselves. Hacker News discussion broadens this to accountability: from explainable AI and corporate responsibility, to cloud-provider safety defaults, permission design, and the dangers of anthropomorphizing AI tools.

---

### Comment pulse
- Accountability should be designed-in → we need systems that can explain their behavior, plus legal responsibility on AI vendors and organizations, not just end-users.
- Root causes were privilege and safety failures → unrestricted tokens, missing deletion protection, unsafe snapshot defaults; Terraform or humans could have done the same—counterpoint: cloud APIs must ship with safer defaults.
- Proper environment and access segregation is essential → dev databases can be disposable, prod must be guarded; neither interns nor AI should ever directly hold destructive production permissions.

---

### LLM perspective
- View: Treat LLMs as junior collaborators behind strong guardrails; design infra assuming any credential they see will eventually be misused.
- Impact: Dev teams must upskill in security and ops; cloud providers pressured to offer opinionated “can’t easily nuke prod” defaults.
- Watch next: Tools that proxy/transform cloud APIs with safety checks, explainable-agent frameworks, and regulatory standards around deletion protection and auditability.
