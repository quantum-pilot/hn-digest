# GitHub will begin charging for self-hosted action runners on March 2026

- Score: 441 | [HN](https://news.ycombinator.com/item?id=46291414) | Link: https://github.blog/changelog/2025-12-16-coming-soon-simpler-pricing-and-a-better-experience-for-github-actions/

### TL;DR

GitHub announced a $0.002-per-job-minute platform fee for self-hosted Actions runners in private repositories starting March 1, 2026, offset by up to 39% lower hosted-runner prices from January. Public-repository jobs and Enterprise Server remain free, and self-hosted usage can consume plan allowances. GitHub says 96% of customers will see no billing change; among affected users, most will pay less, while the minority facing increases sees a reported $13 median. Commenters disputed whether orchestration and logging justify charging on customer hardware.

### Comment pulse

- Critics saw proprietary platform dependence becoming lock-in and revisited GitLab, Forgejo, and other alternatives.
- Defenders noted scheduling, logs, caches, and result storage have costs even when compute is customer-owned.
- A $1,051 yearly calculation assumed continuous billable jobs, not merely an idle runner; commenters questioned that distinction.

### LLM perspective

- View: The controversy is about pricing control and switching costs more than the two-tenths-cent rate alone.
- Impact: High-volume private CI users must compare allowances, hosted discounts, migration expense, and alternative orchestration.
- Watch next: Audit actual job minutes, model both rate changes, and verify billing behavior before redesigning infrastructure.
