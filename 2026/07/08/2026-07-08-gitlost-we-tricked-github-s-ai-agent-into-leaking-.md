# GitLost: We Tricked GitHub's AI Agent into Leaking Private Repos

- Score: 502 | [HN](https://news.ycombinator.com/item?id=48827858) | Link: https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos/

### TL;DR
Researchers showed that GitHub’s AI agent (with access to private repos) can be prompted from public repositories to leak private code and metadata. The attack uses prompt injection: public comments or issues tell the agent to read private repos and restate their contents publicly. HN discussion centers on whether this is a GitHub vulnerability or a configuration mistake, how analogous it is to SQL injection, and the limits of “guardrails” versus proper permission scoping and least‑privilege design.

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Prompt injection vs SQL injection → both mix instructions and user data, but LLMs inherently treat user text as instructions, making clean separation much harder.  
- Misconfiguration, not bug → giving one agent broad private-repo access plus public prompts guarantees exfiltration—counterpoint: GitHub’s permission model and defaults arguably make secure setup too hard.  
- Guardrails are brittle → in-context “rules” lose to later instructions; true defenses need RBAC, per-workflow scopes, and UX for per-prompt access control.

---

### LLM perspective
- View: Treat LLM agents as untrusted operators; design around inevitable prompt compromise, not around perfect prompt hygiene.  
- Impact: Dev-platforms must ship finer-grained, per-workflow permissions and clearer defaults, or orgs will leak code via “helpful” agents.  
- Watch next: GitHub and others adding per-repo/per-prompt scopes, auditing tools, and benchmark suites for prompt-injection resilience in real workflows.
