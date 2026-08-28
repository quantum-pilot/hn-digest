# Serverless Horrors

- Score: 614 | [HN](https://news.ycombinator.com/item?id=45157110) | Link: https://serverlesshorrors.com/

### TL;DR

A collection of serverless “horror stories” centers largely on surprise cloud bills, including claimed five-figure charges attributed to public-query access, spam signups, and runaway audit logging. Commenters add similar anecdotes while debating whether providers should offer hard spending caps. Some argue automatic shutdown is essential protection; others note it could cause abrupt outages or data loss. The discussion also broadens beyond one-off shocks to opaque debugging, deployment mismatches, origin configuration, and the quieter danger of steadily rising monthly costs.

### Comment pulse

- Several commenters wanted circuit breakers, while others warned that automatic shutdown can itself damage production systems.
- Some readers found the collection too narrowly focused on bills rather than broader serverless failures.

### LLM perspective

- View: Billing surprises expose a missing safety layer between usage-based infrastructure and ordinary developer expectations.
- Impact: Teams need explicit budgets, alerts, abuse controls, and tested shutdown behavior before scaling serverless workloads.
- Watch next: Whether providers make enforceable cost ceilings practical without turning budget breaches into destructive outages.
