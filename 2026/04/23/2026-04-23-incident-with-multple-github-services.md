# Incident with multple GitHub services

- Score: 194 | [HN](https://news.ycombinator.com/item?id=47877644) | Link: https://www.githubstatus.com/incidents/myrbk7jvvs6p

## TL;DR
GitHub experienced a roughly hour-long incident affecting Copilot, Webhooks, and Actions on April 23, 2026: services degraded, then were gradually mitigated before full resolution, with a root-cause analysis promised later. Hacker News discussion largely shrugs at the short outage itself but treats it as another data point in GitHub’s declining reliability, citing independent uptime stats, mocking the status page, and describing migrations to self-hosted Forgejo or smaller forges despite the operational burden.

## Comment pulse
- Self-hosting Git forges beats GitHub for many → higher uptime, faster page loads, local control; cheap hardware suffices — counterpoint: homelab maintenance drains time, energy.  
- GitHub reliability seen as collapsing → third-party stats show ~88% overall uptime; users joke about “two nines” SLAs and blame Azure migration, AI mandates.  
- Teams with simple needs now eye alternatives → outages disrupt CI enough that SourceHut, Tangled and others see traffic spikes; GitHub status page trust erodes.  

## LLM perspective
- View: Centralized developer platforms become single points of failure; repeated multi-service incidents accelerate fragmentation toward self-hosted and niche forges.  
- Impact: Small teams reconsider lock-in to GitHub Actions and Copilot, valuing reproducible CI stacks movable between providers or in-house.  
- Watch next: Compare GitHub’s root-cause report with independent uptime trackers; see if incidents correlate with Azure infrastructure or AI integrations.
