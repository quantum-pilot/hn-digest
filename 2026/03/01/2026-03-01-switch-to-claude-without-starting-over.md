# Switch to Claude without starting over

- Score: 515 | [HN](https://news.ycombinator.com/item?id=47204571) | Link: https://claude.com/import-memory

- TL;DR  
  - Anthropic’s “Import Memory” lets you migrate instructions, preferences, and project context from other AI assistants into Claude with a single copy‑paste. You run a provided prompt on the old assistant to dump everything it has “learned” about you, then paste that text into Claude’s memory settings, which become your account‑wide, editable memory with per‑project separation on paid plans. HN debates persistent memory’s usefulness vs privacy risks, vendor lock‑in, weak cross‑tool standards, and Claude’s relatively tight token/session limits.

- Comment pulse  
  - Persistent account‑wide memory feels indispensable for ongoing projects to some, but like unwanted bias to others—counterpoint: many prefer incognito-style, no-bleed sessions.  
  - The migration prompt exposes all stored “memories”; some suspect providers might degrade or throttle such requests, though others argue reputational risk makes deliberate sabotage unlikely.  
  - Lack of shared standards (AGENTS.md vs CLAUDE.md, MCP conventions) and differing token limits/performance create real switching costs despite features like Claude’s memory import.

- LLM perspective  
  - View: Cross‑assistant memory portability nudges the ecosystem toward user‑owned profiles, but still relies on clunky, prompt‑mediated scraping instead of APIs.  
  - Impact: Vendors now compete on turning long‑term context into automation, while still keeping personal, project, and organizational data properly separated.  
  - Watch next: Expect pressure for standard agent configs, true memory export/import APIs, and clearer UI to toggle scopes: session, project, account, workspace.
