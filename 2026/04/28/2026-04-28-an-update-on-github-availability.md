# An update on GitHub availability

- Score: 302 | [HN](https://news.ycombinator.com/item?id=47932422) | Link: https://github.blog/news-insights/company-news/an-update-on-github-availability/

### TL;DR
GitHub’s CTO explains two recent high‑profile outages and outlines a push to design for 30× today’s scale, driven largely by automated/agentic workloads. Short term, they’ve removed bottlenecks, reduced database load, isolated critical services (git, Actions), and leaned on Azure for more compute; longer term they’re moving more code out of the Ruby monolith, optimizing monorepos/merge queues, and pursuing multi‑cloud. HN readers remain skeptical, citing ongoing instability, Azure concerns, vague graphs, and visible bugs in PR lists and search.

---

### Comment pulse
- Priorities don’t match experience → GitHub claims “availability first,” but users see frequent outages and constant feature churn; some blame management incentives—counterpoint: big orgs can pursue multiple tracks.

- Azure and multi‑cloud → Multi‑cloud read as quiet admission Azure isn’t reliable enough; others say it’s standard redundancy and enterprise-retention strategy, not just Azure shade.

- Real-world symptoms → Missing PRs, broken search, and a “green” status page make reliability/transparency promises ring hollow; some suspect approximate queries as load-shedding hacks.

---

### LLM perspective
- View: Root causes and mitigation themes are plausible, but details on concrete targets, SLAs, and rollback safeguards are thin.

- Impact: Any GitHub outage now fractures global CI/CD, agent workflows, and release pipelines; platform risk becomes a board-level topic.

- Watch next: Monitor uptime metrics, multi-cloud announcements, and the promised RCAs/merge-queue API changes; verify if PR/search inconsistencies actually disappear.
