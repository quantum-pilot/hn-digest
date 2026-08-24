# GitHub will begin charging for self-hosted action runners on March 2026

- Score: 441 | [HN](https://news.ycombinator.com/item?id=46291414) | Link: https://github.blog/changelog/2025-12-16-coming-soon-simpler-pricing-and-a-better-experience-for-github-actions/

### TL;DR

GitHub will change Actions pricing in 2026: standard hosted-runner rates fall by as much as 39% on January 1, while self-hosted runners used for private repositories incur a $0.002-per-minute cloud-platform charge from March 1. That usage consumes included plan minutes; public repositories and GitHub Enterprise Server are exempt, and free quotas stay unchanged. GitHub projects no bill change for 96% of customers and decreases for most affected accounts, but some self-hosted users will newly pay GitHub for orchestration running on their own hardware.

### Comment pulse

- Many called charging for customer-owned compute lock-in rent — counterpoint: GitHub still supplies orchestration, logs, caches, and result storage.
- Readers considered Forgejo and GitLab, though discussion noted migration costs and competing platforms’ own pricing constraints.
- Several cost estimates incorrectly treated idle machines as billable; the announcement describes per-minute runner usage for private-repository jobs.

### LLM perspective

- View: The change redistributes Actions revenue: cheaper hosted compute, newly metered private self-hosted orchestration.
- Impact: Most bills stay flat or fall, but principle-sensitive self-hosters gain a migration incentive.
- Watch next: Billing definitions, included-minute treatment, enterprise discounts, and whether GitHub revises the policy.
