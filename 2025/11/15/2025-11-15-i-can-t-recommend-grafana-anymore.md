# I can't recommend Grafana anymore

- Score: 221 | [HN](https://news.ycombinator.com/item?id=45934940) | Link: https://henrikgerdes.me/blog/2025-11-grafana-mess/

TL;DR
- The author stops recommending Grafana due to relentless churn: Grafana Agent/Flow and OnCall deprecated, Alloy introduced with a new DSL, dashboards broken by Angular→React, partial Prometheus-Operator CRD support, and Mimir 3.0 now requiring Kafka. Combined with pushes toward cloud “fleet” config and unmaintained charts, trust eroded; they want boring, stable monitoring. HN echoes fatigue and UI sprawl, while others say core Grafana+Prometheus is stable if you avoid new toys. Many suggest right-sizing or switching to simpler OTEL-native stacks.

Comment pulse
- Churn breaks dashboards/alerts → frequent deprecations, UI sprawl, Angular→React rewrite; ops don’t want to relearn in incidents.
- Stick to boring core → Grafana+Prometheus LTS can run for years without drama — counterpoint: Angular removal forced freezes or rewrites.
- Right-size the stack → Mimir+Kafka is hyperscale; most use Prometheus/VictoriaMetrics; alternatives: SigNoz, OpenObserve, GreptimeDB.

LLM perspective
- View: Prefer stable, standards-led pieces; delay adopting vendor DSLs until interfaces settle.
- Impact: Platform teams absorb migration risk; small orgs pay complexity tax for hyperscale features they don’t need.
- Watch next: OTel Collector maturity, kube-prometheus-stack roadmap, Kafka overhead benchmarks for mid-scale Mimir deployments.
