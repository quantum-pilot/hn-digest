# Anthropic Outage for Opus 4.5 and Sonnet 4/4.5 across all services

- Score: 172 | [HN](https://news.ycombinator.com/item?id=46267385) | Link: https://status.claude.com/incidents/9g6qpr72ttbr

### TL;DR

Claude’s Opus 4.5 and Sonnet models suffered degraded availability across chat, API, console, and coding services from 13:25 to 14:43 Pacific time. Anthropic attributed the 78-minute incident to a network-routing misconfiguration that dropped traffic to backend infrastructure; reverting it restored service. An incident engineer said identification took about 75 minutes and normal mitigation paths underperformed. Users praised prompt status updates, but some received misleading quota messages instead of outage errors, complicating diagnosis.

### Comment pulse

- Rapid status-page updates helped users distinguish platform failure from their own code, though detection still lagged most of the incident.
- Engineers identified overlapping route advertisement and promised better synthetic monitoring and visibility into high-impact infrastructure changes.
- Users joked about dependence on centralized inference, while one veteran programmer described feeling unable to work efficiently during interruption.

### LLM perspective

- View: Transparent communication reduced confusion, but weak detection and misleading client errors reveal separate resilience gaps.
- Impact: Agent-dependent workflows increasingly inherit provider outages as direct engineering downtime and diagnostic noise.
- Watch next: The review should address route validation, synthetic probes, fallback paths, error classification, and multi-provider continuity.
