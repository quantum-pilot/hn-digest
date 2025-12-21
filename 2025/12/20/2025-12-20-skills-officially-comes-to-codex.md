# Skills Officially Comes to Codex

- Score: 231 | [HN](https://news.ycombinator.com/item?id=46334424) | Link: https://developers.openai.com/codex/skills/

### TL;DR
OpenAI’s Codex now supports “Agent Skills”: small, shareable capability packages defined mostly in a `SKILL.md` file plus optional scripts and assets. Skills are loaded from well-defined directories, discovered via short YAML front-matter, and invoked explicitly (via `/skills` or `$skill-name`) or implicitly when descriptions match a task. They compose, can call local scripts in a sandbox, and can be created/installed by other skills—prompting comparisons to reusable libraries and to a lighter-weight alternative to MCP-style integrations.

---

### Comment pulse
- Skills as long-term primitive → Markdown-based, composable workflows that leverage sandboxed scripts; easier than MCP, can even describe how to use tools/CLIs and MCPs themselves.  
- Skills as “workflow cache” → Encapsulate repeatable user stories; agents can iteratively refine them from past sessions, turning good/bad runs into durable capabilities.  
- Skill index concerns → Front-matter is injected every turn, risking prompt pollution, tone drift, and token bloat—counterpoint: better agent harnesses could use RAG or smarter selection.

---

### LLM perspective
- View: Skills formalize “prompt + tools + assets” into versionable modules, bridging between ad-hoc prompts and full-blown services.  
- Impact: Teams get org-wide, repo-scoped workflows; open-source skill packs could standardize common patterns like auth, onboarding, or incident runbooks.  
- Watch next: Quality and safety standards, global searchable skill registries, and IDEs that auto-suggest or auto-install skills per codebase and task.
