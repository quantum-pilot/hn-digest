# Obsidian Sync now has a headless client

- Score: 354 | [HN](https://news.ycombinator.com/item?id=47197267) | Link: https://help.obsidian.md/sync/headless

- TL;DR  
Obsidian has released an open‑beta headless client for its paid Sync service, installable via npm, that lets you sync vaults from the command line without running the desktop app. The CLI can list/create remote vaults, bind them to local folders, run one‑shot or continuous sync, tweak conflict and inclusion settings, and report status, using the same end‑to‑end encryption as the GUI. HN readers are excited for CI, servers, publishing pipelines, AI/RAG agents, and fewer DIY Git/Syncthing setups.

- Comment pulse  
  - Headless sync + CLI make Obsidian a scriptable Markdown backend for AI tools, CI, servers, RAG—counterpoint: current CLI can’t actually display notes.  
  - Users weighing Obsidian Sync against iCloud/Syncthing ask about filesystem conflicts, multi‑user/team patterns, and finer‑grained auth like scoped tokens for automations.  
  - Early adopters already use headless sync to auto‑publish blogs and reduce Git/plugin glue; others still want single‑file editing without creating a full vault.

- LLM perspective  
  - View: This effectively turns Obsidian Sync into an API surface, even without a JSON/HTTP API, via a stable CLI contract.  
  - Impact: Makes Obsidian attractive as a central knowledge base for teams running automations, periodic exports, or analytics over their notes.  
  - Watch next: token scopes, richer status/conflict introspection, and maybe an SDK will determine how far third‑party tooling can safely go.
