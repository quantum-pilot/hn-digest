# Cloudflare OS: an open platform for agents, apps, and work

- Score: 649 | [HN](https://news.ycombinator.com/item?id=49182996) | Link: https://blog.cloudflare.com/cloudflare-os/

### TL;DR

Cloudflare OS is an open-source workplace agent platform combining browser workspaces, curated organizational skills, isolated code execution, connected apps, and deterministic workflows. Its Gatekeepers replace broad API keys with typed, resource-specific capabilities, mediate side effects, log what agents observe, and carry those access constraints into shared outputs. Each generated app runs as a sandboxed Dynamic Worker with separate SQLite state and can be shared live or copied as a data-free blueprint. Organizations can choose models through AI Gateway, attribute spending, and self-deploy a customized instance on Cloudflare’s stack.

### Comment pulse

- Supporters said the real novelty is Sandstorm-like per-document app instances whose code users can safely modify with agents.
- Skeptics questioned sandbox absolutes, schema evolution, regulated data, long-term maintenance, and individual customization.
- Open sourcing eased some lock-in concerns — counterpoint: the architecture still leans heavily on Cloudflare-specific services.

### LLM perspective

- View: Capability tracking and observation-aware sharing address gaps left by tool-level MCP permissions.
- Impact: Nondevelopers could build connected internal software without receiving raw credentials.
- Watch next: Security audits, self-hosting portability, and governance for customized apps after their creators leave.
