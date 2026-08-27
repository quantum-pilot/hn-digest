# Migrating Dillo from GitHub

- Score: 249 | [HN](https://news.ycombinator.com/item?id=46096800) | Link: https://dillo-browser.org/news/migration-from-github/

### TL;DR

Dillo plans to leave GitHub for a lightweight self-hosted service mirrored on Codeberg and SourceHut. GitHub’s JavaScript-heavy frontend barely works in Dillo, consumes excessive resources, centralizes control, favors interruptive workflows, offers weak moderation, and conflicts with the project’s view of generative AI. After previously losing its original domain and some project history, Dillo now stores source and bugs in mirrored Git repositories. Its new stack uses cgit plus a custom C tool that converts Markdown bug files into static HTML, enabling offline work and replication.

### Comment pulse

- Forgejo users praise its small operational footprint versus GitLab, though solo developers may need only bare Git over SSH.
- Some readers saw the notification complaint as configurable — counterpoint: the author wants intentionally scheduled, offline-friendly project review.
- Discussion favors decentralized forge choices over replacing GitHub with another universal central platform.

### LLM perspective

- View: Dillo is optimizing its forge for resilience, low resources, and self-compatibility rather than mainstream convenience.
- Impact: Git-backed issue data lowers recovery costs but makes maintainers responsible for custom tooling and hosting.
- Watch next: Verify mirror synchronization, domain-loss recovery, contributor workflow, CI replacement, and long-term maintenance of the bug generator.
