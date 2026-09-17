# Training a 4B model to produce 81% faster query plans than Postgres

- Score: 573 | [HN](https://news.ycombinator.com/item?id=49731285) | Link: https://rohanbansal.com/qorl

### TL;DR

An experiment trained a 4B model to steer PostgreSQL plans with pg_hint_plan for repeated analytical queries. After supervised distillation from roughly 400 GPT-6 Astra trajectories and 1,200 reinforcement-learning updates, the author reports a 1.81× geometric-mean and workload speedup across 113 join-heavy IMDb queries, selecting the best of up to 15 candidates; summed latency fell 44.7%. HN praised the engineering but questioned generalization from a warmed 8.5 GB read-only dataset, production drift, inference cost, and whether specialized search or adaptive planning fits better.

### Comment pulse

- Benchmark scope limits the headline → in-memory, warmed analytical SELECTs do not establish gains for larger, changing OLTP workloads.
- Offline optimization can be validated safely → repeated costly queries permit cloned-data testing and amortization — counterpoint: plans can regress as statistics and workloads drift.
- LLMs may be an indirect fit → commenters favored specialized heuristics or adaptive execution, though conventional optimizers also suffer unstable plan choices.

### LLM perspective

- View: The result demonstrates profile-guided plan search under controlled conditions, not a general replacement for PostgreSQL's online optimizer.
- Impact: Teams with stable, repetitive analytics could train small models to propose hints, provided every candidate is benchmarked before deployment.
- Watch next: Test unseen schemas, disk-bound workloads, changing distributions, planning overhead, and deterministic alternatives against identical candidate budgets.
