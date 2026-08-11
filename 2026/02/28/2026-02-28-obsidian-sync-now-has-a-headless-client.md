# Obsidian Sync now has a headless client

- Score: 354 | [HN](https://news.ycombinator.com/item?id=47197267) | Link: https://help.obsidian.md/sync/headless

### TL;DR

Obsidian Sync’s open-beta headless client brings paid vault synchronization to scripts, servers, CI pipelines, agents, and publishing workflows without the desktop app. The npm-installed `ob` tool can list or create remote vaults, configure local mappings, run once or continuously, inspect status, and unlink. It retains Sync’s encryption protections, including end-to-end encryption. Obsidian advises backing up first and never running desktop and headless Sync on the same device. HN welcomed automation and RAG possibilities while asking about conflicts, team use, and narrower token permissions.

### Comment pulse

- Plain Markdown keeps integrations simple → AI CLIs can work directly on vault trees without special plugins.
- Official headless Sync removes publishing friction → server workflows no longer need Git-inside-Obsidian workarounds.
- Permission scope remains a concern → automations may need one folder or note, not an entire vault.

### LLM perspective

- **View:** The valuable primitive is reliable file synchronization, not an Obsidian-specific agent layer.
- **Impact:** Teams can automate indexing, publishing, backups, and retrieval on remote machines.
- **Watch next:** Conflict semantics, scoped credentials, Linux metadata behavior, and beta stability.
