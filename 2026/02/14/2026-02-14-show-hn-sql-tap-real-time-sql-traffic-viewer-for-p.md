# Show HN: SQL-tap – Real-time SQL traffic viewer for PostgreSQL and MySQL

- Score: 218 | [HN](https://news.ycombinator.com/item?id=47011567) | Link: https://github.com/mickamy/sql-tap

### TL;DR

SQL-tap places a Go proxy between an application and PostgreSQL or MySQL, parses native wire traffic, and streams captured events over gRPC to an interactive terminal client without application-code changes. It tracks statements, bound parameters, transactions, duration, affected rows, and errors; users can search, sort, inspect, copy, aggregate, and run EXPLAIN or EXPLAIN ANALYZE. Early testers found it immediately useful for exposing excessive WordPress queries and agent behavior. Discussion centered on whether quick debugging value outweighs proxy latency, deployment complexity, and possible failure under production load.

### Comment pulse

- Testers wanted slow-query sorting, filtering, faster navigation, and duplicate counts; the documented interface includes search, duration sorting, paging, and analytics.
- Proxy critics prefer PostgreSQL extensions plus an OTEL sidecar for performance—counterpoint: managed providers may not permit suitable extensions.
- Supporters framed the tool as an occasional local debugger, where easy visibility matters more than permanent production instrumentation.

### LLM perspective

- View: The proxy is strongest as a disposable diagnostic lens, not automatically as an always-on observability layer.
- Impact: Developers can correlate application actions with database behavior; operators must account for credentials, overhead, and another failure point.
- Watch next: Benchmark latency and throughput, test encrypted connections, document capture security, and clarify production versus development guidance.
