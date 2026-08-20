# Incident with Github.com [resolved]

- Score: 559 | [HN](https://news.ycombinator.com/item?id=49330597) | Link: https://www.githubstatus.com/incidents/zkxwbgr0cnmx

### TL;DR

GitHub’s August 17 incident lasted 7 hours 47 minutes, degrading Issues, PRs, APIs, Actions, Copilot, authentication, and downloads; peak web/API errors reached about 20%, raw/archive downloads 50%. Central US load balancers saturated after an Istio sidecar hit concurrency limits under a misconfigured autoscaling policy, cascading into four HAProxy flow-limit failures. Optimistic gateway retries and a latent VS Code retry bug amplified Copilot token traffic roughly tenfold. Commenters debated AI-driven load and pricing, but GitHub’s report instead identifies scaling policy, retry, capacity-monitoring, and failover defects.

### Comment pulse

- Rate limits or paid capacity might tame agent traffic → counterpoint: charging free users could weaken GitHub’s network-effect advantage.
- Reliability goodwill is eroding → users are adopting Forgejo mirrors, though GitHub CLI and embedded CI workflows remain migration barriers.
- Development-stack downtime can be tolerated longer than production outages → integration inertia keeps dominant platforms sticky despite weak availability.

### LLM perspective

- View: The outage was a cascading-control failure: autoscaling ignored sidecars, retries multiplied pressure, and failover inherited pathological clients.
- Impact: Teams dependent on GitHub-hosted workflow definitions or authentication need mirrors and degraded-mode release procedures.
- Watch next: Verify sidecar-aware scaling, bounded exponential backoff, regional isolation, and VS Code retry fixes under peak-load exercises.
