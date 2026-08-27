# Pricing Changes for GitHub Actions

- Score: 439 | [HN](https://news.ycombinator.com/item?id=46291156) | Link: https://resources.github.com/actions/2026-pricing-changes-for-github-actions/

### TL;DR

GitHub will cut hosted-runner prices by roughly 40% on January 1, 2026, while adding a $0.002-per-minute platform charge to private-repository workflows on self-hosted runners from March 1. Public repositories and GitHub Enterprise Server are exempt. GitHub says 96% of customers will see no bill change, and most affected customers will pay less, though some self-hosted users will pay more. The company frames the fee as payment for Actions orchestration and promises further runner-management improvements.

### Comment pulse

- Critics call charging for customer-owned hardware a lock-in squeeze; others counter that orchestration, logs, and artifacts still cost GitHub money.
- Experiences diverge: some report reliable runners but fragile workflows, while others cite instability, poor Kubernetes integration, and weak debugging tools.

### LLM perspective

- View: The price cut and control-plane fee reposition Actions as a paid platform, not merely bundled hosted compute.
- Impact: Self-hosting decisions now depend more on workflow speed, operational burden, and platform dependence than raw compute cost.
- Watch next: Compare March invoices and runner reliability against Forgejo, Woodpecker, Jenkins, and third-party runner economics.
