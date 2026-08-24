# Pricing Changes for GitHub Actions

- Score: 439 | [HN](https://news.ycombinator.com/item?id=46291156) | Link: https://resources.github.com/actions/2026-pricing-changes-for-github-actions/

### TL;DR

GitHub will cut hosted-runner rates by roughly 40%, yielding up to 39% net savings after a new $0.002-per-minute platform fee is included from January 1, 2026. From March 1, the same fee applies to self-hosted runs in private repositories and consumes plan quotas; public repositories and Enterprise Server remain exempt. GitHub says 96% of customers will pay the same and most affected users will save. HN operators objected to paying for their own compute and questioned whether Actions’ control plane merits another meter.

### Comment pulse

- Self-hosters saw the fee as rent on customer hardware, especially when third-party runners already undercut GitHub-hosted compute.
- Operators catalogued fragile orchestration, awkward registration, weak Kubernetes support, cancellation failures, and poor logging — counterpoint: artifacts and control-plane services still cost GitHub.
- Some planned Forgejo, Woodpecker, or Jenkins migrations, arguing predictable self-managed maintenance now compares favorably with per-minute charges.

### LLM perspective

- View: The controversy concerns leverage and trust more than the nominal two-tenths-of-a-cent rate.
- Impact: High-volume private CI users must model costs or decouple execution triggers from GitHub’s control plane.
- Watch next: Pricing estimates, Scale Set Client delivery, multi-label restoration, uptime commitments, and migration rates after March.
