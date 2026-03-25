# Log File Viewer for the Terminal

- Score: 288 | [HN](https://news.ycombinator.com/item?id=47498924) | Link: https://lnav.org/

### TL;DR
lnav is a long‑lived, terminal-based log viewer that merges, tails, searches, filters, and SQL-queries logs locally without servers or setup. It auto-detects formats, handles compression on the fly, and can outperform typical shell pipelines on large files via an integrated SQLite engine. HN comments split between fans who’ve used it for years in production and newcomers who find its TUI, colors, and discoverability (exiting, help, man pages) confusing, prompting discussion of themes, onboarding, and alternatives like Grafana or custom TUIs.

---

### Comment pulse
- Mature, lightweight log navigator → Users report success monitoring many servers and lab devices since ~2009, praising low overhead and effectiveness for multi-source logs.
- Steep-ish UX for newcomers → Some can’t tell what’s happening, struggle to exit, and dislike colors; maintainer notes pager-like keys, themes, and improved recent versions — counterpoint: others say `q` works and man page exists in their distro.
- Desire for “TUI Grafana” for JSON → One wants log dashboards in-terminal; others say lnav already beats Grafana for quick searches, while pointing to treewalker and vnlog+feedgnuplot as alternatives.

---

### LLM perspective
- View: lnav nicely bridges basic CLI tools and full log platforms, especially for SSH-centric debugging and small deployments.
- Impact: Best suited for individual developers, SREs, and small ops teams who lack or distrust heavyweight logging stacks.
- Watch next: More discoverable UI cues (exit/help hints, progress during indexing) and first-class JSON workflows could broaden adoption.
