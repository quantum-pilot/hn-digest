# The GitHub Actions control plane is no longer free

- Score: 213 | [HN](https://news.ycombinator.com/item?id=46291500) | Link: https://www.blacksmith.sh/blog/actions-pricing

### TL;DR

Blacksmith interprets GitHub’s coming $0.002-per-minute fee on self-hosted and third-party Actions runs as direct monetization of the workflow control plane. From March 1, 2026, CI bills will combine runner compute with GitHub’s scheduling and orchestration charge, setting a revenue floor wherever jobs execute. The vendor argues that lower hosted-runner prices reflect a shift from lower-margin compute toward higher-margin platform revenue, while faster runners and caching can limit exposure. Commenters disputed whether the move strengthens or weakens third-party runners and reopened comparisons with competing forges.

### Comment pulse

- Third-party runner vendors said they remain cheaper and faster despite the fee — counterpoint: GitHub’s pricing now makes that value harder to explain.
- Critics read lower hosted prices plus self-hosting charges as deliberate steering toward GitHub infrastructure, not neutral ecosystem alignment.
- Some preferred per-job control-plane pricing, arguing elapsed minutes mainly reflect runner performance rather than GitHub’s orchestration cost.

### LLM perspective

- View: The fee converts GitHub’s integration advantage into recurring revenue without owning the machines doing the work.
- Impact: Runner vendors must sell enough speed or caching savings to offset both their compute bill and GitHub’s meter.
- Watch next: Third-party pricing, customer migration, hosted-runner uptake, control-plane reliability, and whether competitors retain free bring-your-own execution.
