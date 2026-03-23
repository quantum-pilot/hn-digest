# OpenClaw is a security nightmare dressed up as a daydream

- Score: 276 | [HN](https://news.ycombinator.com/item?id=47479962) | Link: https://composio.dev/content/openclaw-security-and-vulnerabilities

## TL;DR

OpenClaw is a popular open‑source “do‑everything” AI agent that can read your email, chats, files and then act on your behalf. The article argues it’s also a near-perfect security anti-pattern: unvetted third‑party “skills” already delivered malware, prompt injection is unavoidable given its access and connectivity, tokens and plaintext memory are easy to abuse, and tens of thousands of instances shipped misconfigured and exposed. The author recommends heavy sandboxing, least‑privilege, managed integrations—and pitches TrustClaw as a more constrained alternative. HN debates whether such agents are ever safely usable and laments how mundane today’s “futuristic” use‑cases are.

---

## Comment pulse

- Examples are boring (flight booking, meeting scheduling) → users already do these fine; more interesting: cross-account morning briefings, research pipelines, multi-app context summarization.

- “No safe OpenClaw; lethal trifecta is inherent” → any useful access implies exfil risk — counterpoint: narrow-scope agents, per-tool permissions and separate identities are already practical and useful.

- Giving LLMs system access seems reckless → prompt injection via hidden email text is trivial; others note Google-style data access already exists and accept the tradeoff.

---

## LLM perspective

- View: General-purpose, fully trusted agents are structurally unsafe; useful systems will be narrow, heavily sandboxed, and auditable by design.

- Impact: Agent platforms must look more like identity/security products: managed OAuth, scoped tools, logging, anomaly detection, and revocation workflows.

- Watch next: OS-level agent sandboxes, standardized “agent permissions” UX, real incident postmortems, and benchmarks that include security, not just task completion.
