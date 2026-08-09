# GitHub appears to be struggling with measly three nines availability

- Score: 430 | [HN](https://news.ycombinator.com/item?id=47487584) | Link: https://www.theregister.com/2026/02/10/github_outages/

### TL;DR

GitHub’s February 9 incident affected Actions, pull requests, notifications, and Copilot; notification delays approached 50 minutes, with recovery confirmed after about three and a half hours. A separate Copilot policy-propagation problem lasted overnight. The Register says GitHub’s redesigned status page obscures 90-day availability; an unofficial reconstruction once showed platform uptime below 90% in 2025, while Enterprise Cloud promises 99.9% for applicable services. HN says aggregate numbers can mislead across components, yet commenters report no individual service reaching three nines and worry the Azure migration and AI-generated load are worsening reliability.

### Comment pulse

- Platform-wide uptime conflates independent features → teams care most about Git, API, website, pull requests, and Actions.
- Component precision does not excuse misses — counterpoint: unofficial data counts degraded performance, and SLA math uses applicable quarterly service minutes.
- Azure migration and agent-generated traffic may raise failure pressure → neither explanation is established as the cause of reported incidents.

### LLM perspective

- **View:** Availability claims require a named service, measurement window, and definition of degraded versus unavailable.
- **Impact:** Centralized development workflows stall when core GitHub services fail; peripheral Copilot incidents affect a different user slice.
- **Watch next:** Official component metrics, quarterly SLA credits, Azure milestones, incident root causes, Actions security, and continuity plans.
