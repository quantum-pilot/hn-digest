# Benchmarking OpenTelemetry: Can AI trace your failed login?

- Score: 137 | [HN](https://news.ycombinator.com/item?id=46811588) | Link: https://quesma.com/blog/introducing-otel-bench/

### TL;DR

OTelBench tests whether leading LLMs can add correct OpenTelemetry distributed tracing to small, realistic microservices (23 tasks, 11 languages, terminal-based agent setup). Even the strongest models only succeed on about a quarter of tasks; many solutions compile but produce broken traces (e.g., merging distinct user journeys into one trace or mishandling context propagation). Performance varies sharply by language, and failures highlight long-horizon, polyglot, low-training-data challenges. Result: AI can assist, but you still must own your instrumentation.

---

### Comment pulse

- Editorialized title vs original → users welcomed the submitter’s apology and noted “simple SRE tasks” is misleading; multi-microservice tracing is non-trivial even for humans.

- Benchmark focus questioned → tasks are instrumentation, not debugging; instructions are fuzzy, no web tools; commenters prefer root-cause and trace/log-analysis scenarios—counterpoint: real systems are similarly underspecified.

- SRE skill is hard to teach → experience comes from years of outages; search space in large fleets is enormous, and LLM “vibes” fail when strict, end-to-end integration is required.

---

### LLM perspective

- View: This benchmark usefully shifts evaluation from toy puzzles to brittle, spec-heavy infra work where partial correctness is worthless.

- Impact: Encourages SREs and vendors to treat LLM assistance as pair-programmer-level, not autonomous operator, especially around observability.

- Watch next: Benchmarks that chain instrumentation, trace/log ingestion, and automated root-cause analysis with real tooling (query APIs, Text2SQL, dashboards).
