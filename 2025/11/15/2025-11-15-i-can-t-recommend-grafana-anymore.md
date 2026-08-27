# I can't recommend Grafana anymore

- Score: 221 | [HN](https://news.ycombinator.com/item?id=45934940) | Link: https://henrikgerdes.me/blog/2025-11-grafana-mess/

### TL;DR

A longtime user says Grafana Labs’ broader observability stack has become too volatile to recommend for teams seeking dependable infrastructure. The essay cites Agent’s evolution into Flow and Alloy, OnCall’s deprecation, unmaintained charts, dashboard breakage from Angular removal, and Mimir 3.0’s Kafka-based ingestion redesign. The author still considers the technology capable, but argues repeated migrations impose unacceptable operational cost. Comments complicate that verdict: basic Grafana and Prometheus deployments can remain stable, while Mimir targets scales many teams do not need.

### Comment pulse

- Several operators corroborated recurring dashboard, alerting, and interface churn.
- Others reported years of stability by keeping a simple stack and avoiding components designed for massive scale.

### LLM perspective

- View: The real dividing line is core visualization versus adopting an entire fast-changing vendor ecosystem.
- Impact: Misaligned scale choices can convert powerful observability components into recurring migration work.
- Watch next: OpenTelemetry may reduce coupling, but only if collection interfaces remain stable across backend changes.
