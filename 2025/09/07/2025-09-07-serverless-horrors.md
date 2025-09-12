# Serverless Horrors

- Score: 614 | [HN](https://news.ycombinator.com/item?id=45157110) | Link: https://serverlesshorrors.com/

- TL;DR
    - ServerlessHorrors is a roundup of cloud/serverless “gotcha” bills (e.g., $22k BigQuery query, $23k Vercel bandwidth). HN discussion pivots to why surprise costs happen: misconfigurations, bot traffic, weak defaults, and limited spend controls. Some say AWS refunds are routine; others want hard budget caps to avoid existential risk. Security angles surface (S3 “cost bombs,” CDN-bypass origin hits) alongside complaints about Lambda opacity and a quieter threat: monthly cost creep. Responsibility between user and provider remains contested.

- Comment pulse
    - Surprise bills are terrifying → refunds exist, but people want hard spend caps/circuit breakers to avoid bankruptcy — counterpoint: auto-shutdown risks data loss/outages.
    - Misconfigurations amplify costs → S3 “cost bombs” and CDN-bypass origin hits exploit public buckets; fix with private buckets, origin access, caching, rate limits.
    - Not just spikes → serverless opacity complicates debugging; real pain is monthly creep from forgotten resources, though on‑prem sees similar zombie costs.

- LLM perspective
    - View: Cloud pay‑as‑you‑go is an unbounded credit line; defaults hide blast radius and operational blind spots.
    - Impact: Teams need cost SRE: budgets, alerts, quotas, WAF/rate limits, private origins, CI linting for IaC, and postmortems on spend.
    - Watch next: Provider-level hard caps/budget-kill switches, origin access controls by default, targeted credits, better anomaly detection and preemptive throttling.
