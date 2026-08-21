# The August 17 outage, and the work ahead

- Score: 261 | [HN](https://news.ycombinator.com/item?id=49378957) | Link: https://github.blog/news-insights/company-news/the-august-17-outage-and-the-work-ahead/

- TL;DR
    - GitHub’s CTO explains the 7h47m August 17 outage as a capacity failure triggered by record traffic, not a bad deploy, which cascaded into auth, Actions, APIs, and Copilot. A VS Code Copilot retry bug amplified load roughly 10x, slowing recovery. GitHub is adding large amounts of Azure capacity, re‑architecting for linearly scalable reads, tightening retry policies, and isolating critical systems. HN debates retry design and testing, AI‑driven commit explosions, and Microsoft’s incentives around Copilot usage and reliability.

- Comment pulse
    - Client-side retries blamed for 10x traffic spike → critics say this reflects poor test coverage; defenders note complex, imperfect real‑world retry behavior.
    - Auto-retries → many argue they hide failures and worsen outages unless paired with circuit breakers and server-directed backoff—counterpoint: essential on flaky networks like mobile.
    - Exploding monthly commits → readers suspect AI tools and auto-commit bots, worry capacity planning lags demand, and question using commits (not pushes) as scaling metric.

- LLM perspective
    - View: GitHub is shifting from firefighting incidents toward systemic resilience, but massive AI-driven load makes stability a moving target.
    - Impact: Outages at scale incentivize better client behavior standards—retries, backoff, circuit breakers—across IDEs, bots, and CI systems, not just GitHub.
    - Watch next: Concrete SLOs, public incident postmortems, and Azure migration milestones will reveal whether reliability actually improves under accelerating usage.
