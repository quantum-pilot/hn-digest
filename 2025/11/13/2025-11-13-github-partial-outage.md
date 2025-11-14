# GitHub Partial Outage

- Score: 176 | [HN](https://news.ycombinator.com/item?id=45915731) | Link: https://www.githubstatus.com/incidents/1jw8ltnr1qrj

- TL;DR
    - GitHub experienced a brief partial outage impacting git push/pull; investigated at 15:00 UTC and resolved by 15:13. Only Git Operations were degraded; an RCA is promised. HN commenters first blamed their SSH keys before noticing the status page, then broadened to reliability gripes and months-long regressions (e.g., Insights Traffic stats). Alternatives came up: mixed field reports on GitLab—some note improved stability with webhook flakiness, others report outages or prefer GitHub. Overall: annoyance, but ongoing dependence on hosted Git.

- Comment pulse
    - Outage prompted local blame → devs rotated SSH keys and configs; status page clarified server-side failure.
    - Reliability frustration → minor outages and long-standing UI issues (Insights Traffic banner). — counterpoint: GitHub engineer says the ancient stats service is being replaced soon.
    - GitLab as foil → several report better stability with occasional webhook flakiness; others cite outages or prefer GitHub’s UX.

- LLM perspective
    - View: Short infra blips trigger wasted troubleshooting; publish fast status updates and client-facing error messages to reduce churn.
    - Impact: Push/pull failures stall CI/CD, releases, and chatops that rely on webhooks; distributed teams pause merges and deployments.
    - Watch next: RCA specifics, committed SLOs, and the Insights fix timeline; consider repo mirrors, read-only fallbacks, and queued pushes for resilience.
