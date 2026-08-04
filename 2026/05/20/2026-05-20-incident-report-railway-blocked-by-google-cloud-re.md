# Incident Report: Railway Blocked by Google Cloud [resolved]

- Score: 547 | [HN](https://news.ycombinator.com/item?id=48201484) | Link: https://status.railway.com/incident/I23M92U0

### TL;DR

Railway suffered a major outage after Google Cloud blocked its account, disrupting the dashboard, API, control plane, builds, networking, logins, and hosted workloads beginning 19 May at 22:29 UTC. Access returned in stages, but networking problems persisted; Railway throttled non-enterprise builds, recovered metal capacity, and declared resolution at 07:57 UTC, advising redeploys for unhealthy services. HN users disputed blame: many criticized GCP’s account enforcement and weak human support, while others cited Railway’s operational history and argued customers ultimately experience Railway’s resilience, not its vendor relationship.

### Comment pulse

- Some called account suspension uniquely damaging to GCP’s reputation — counterpoint: AWS, Azure, Hetzner, and OVH also throttle, suspend, or suffer major outages.
- Railway skepticism focused on prior reliability and support experiences; an unnamed informed commenter insisted this incident was entirely Google’s fault.
- A user remained down for over 11 hours until manually redeploying, challenging the resolved label despite Railway’s promised automatic recovery.

### LLM perspective

- View: Provider account state is a control-plane dependency; regional redundancy cannot mitigate a single administrative suspension.
- Impact: Railway customers inherit both Railway’s architecture and Google’s enforcement/support processes, even when their own workloads are healthy.
- Watch next: Verify the postmortem’s suspension trigger, escalation latency, cross-provider failover gaps, redeploy completion, and safeguards against recurrence.
