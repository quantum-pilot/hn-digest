# Jiratui – A Textual UI for interacting with Atlassian Jira from your shell

- Score: 124 | [HN](https://news.ycombinator.com/item?id=45198481) | Link: https://jiratui.sh/

TL;DR (70–90 words)
JiraTUI is a terminal-based Jira client: search with saved JQL, create/update issues, manage comments and links, and customize shortcuts—aiming for speed and fewer context switches. HN welcomes an escape from Jira’s sluggish web UI; one reader shared a tiny, fast browser tool, prompting warnings about API keys and untrusted proxies. Opening Jira links in the TUI is feasible via a custom URI handler plus link rewriting. Discussion probes whether Jira’s slowness is mostly the web client or the server; a GitHub repo is available.

Comment pulse
- TUI could outperform Jira web → avoids heavy frontend; Jira’s drag-and-drop blocks UI pending network responses — counterpoint: some latency stems from server-side performance.
- Be wary of third‑party proxies → API tokens in hobby apps violate zero‑trust; self‑host or open‑source code reduces risk.
- Open Jira links in TUI → register a custom URI handler; rewrite links via userscript/extension; TUI must accept issue ID as CLI arg.

LLM perspective
- View: Terminal-first Jira helps keyboard-driven devs; success depends on auth flows, project permissions, and parity with required workflows.
- Impact: Teams escape slow web UI; IT/security must vet token handling, SSO, and auditability before wider rollout.
- Watch next: Publish timings vs jira.atlassian.com, add OAuth/SSO, offline caching, editor integrations, and installers for macOS/Linux/Windows.
