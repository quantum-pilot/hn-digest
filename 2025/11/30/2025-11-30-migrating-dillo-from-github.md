# Migrating Dillo from GitHub

- Score: 249 | [HN](https://news.ycombinator.com/item?id=46096800) | Link: https://dillo-browser.org/news/migration-from-github/

### TL;DR

Dillo is leaving GitHub because the forge's JavaScript-heavy interface no longer works in the lightweight browser, while centralized control and notification-driven workflows conflict with the project's resilience and offline goals. The maintainer now self-hosts cgit and a lightweight issue system on a VPS. Repositories, bug data, and signed pages can be mirrored through Codeberg and SourceHut, reducing data-loss risk following the original domain loss. GitHub copies remain updated until migration stabilizes, preserving downstream URLs and releases.

### Comment pulse

- Lightweight self-hosting can be operationally simple → Forgejo users reported low memory, easy upgrades, local availability, and greater integration control than GitLab or GitHub.
- The custom tracker embodies resilience → plain files, Git history, and static output ease replication — counterpoint: skeptics expect bespoke maintenance costs.
- Forge fragmentation may be durable → some expect consolidation, while others prefer federation and niche platforms over another dominant centralized replacement.

### LLM perspective

- View: Portability comes from ordinary, replicable files; signatures preserve authority across hosts.
- Impact: Dillo contributors gain browser-native access but face a transition across several independent services.
- Watch next: Mirror synchronization, DNS recovery plans, tracker stability, GitHub archival timing, and contributor participation.
