# GitHub will begin charging for self-hosted action runners on March 2026

- Score: 441 | [HN](https://news.ycombinator.com/item?id=46291414) | Link: https://github.blog/changelog/2025-12-16-coming-soon-simpler-pricing-and-a-better-experience-for-github-actions/

TL;DR
- GitHub is overhauling Actions pricing: hosted runners get up to 39% cheaper in 2026, while self‑hosted runners in private repos incur a new $0.002‑per‑minute “platform” fee, charged against plan minutes. Public repos and Enterprise Server remain free for self‑hosting. GitHub frames this as funding orchestration, logging, and autoscaling improvements, claiming ~96% of customers see no increase. Hacker News splits between viewing this as predictable SaaS lock‑in and price creep versus a reasonable cost rebalancing that may push teams toward alternatives.

Comment pulse
- Vendor lock‑in warning → proprietary GitHub inevitably monetizes control; critics urge migration to Forgejo/Gitea‑style libre forges and contributing features instead of funding future “user‑hostile” changes.
- Pricing outrage → $0.002/minute feels like paying for idle hardware; defenders note it’s for job time plus orchestration, storage, and that free self‑hosting was unsustainable.
- Alternatives debated → many praise GitLab CI or DIY runners on cheap VPSs, but argue GitLab pricing and AI bundling limit it as an escape.

LLM perspective
- View: This is a classic SaaS ratchet—initially underpriced component becomes billable once dependency and workflow lock‑in are strong.
- Impact: Heavy private‑repo CI users on self‑hosted hardware must reassess minutes consumed versus simply moving workloads to GitHub‑hosted runners.
- Watch next: Expect more interest in Forgejo, Gitea, WoodpeckerCI, Tekton, plus third‑party orchestration layers that sit atop GitHub webhooks.
