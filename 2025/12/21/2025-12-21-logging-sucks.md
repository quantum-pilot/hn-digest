# Logging sucks

- Score: 500 | [HN](https://news.ycombinator.com/item?id=46346796) | Link: https://loggingsucks.com/

### TL;DR

The article argues that scattered, message-oriented logs make distributed debugging an exercise in reconstructing context. It recommends one “wide event” or canonical log line per request and service hop, progressively enriched with technical and business fields such as user tier, feature flags, timing, payment outcome, and errors. Structured high-cardinality events enable production questions to become queries rather than text searches. OpenTelemetry transports data but does not supply domain context; tail sampling can retain errors and unusual latency while reducing routine-event storage costs.

### Comment pulse

- Readers liked richer request context but warned that emitting only at completion can lose evidence from crashes, timeouts, or bypassed error paths.
- Others saw wide events as established structured logging and preferred retaining chronological logs or traces as complementary evidence.

### LLM perspective

- View: Wide events are a valuable request summary, but replacing all intermediate logs creates a new visibility blind spot.
- Impact: Teams gain queryable business context only if schemas, identifiers, instrumentation, and developer awareness stay consistent.
- Watch next: Hybrid designs combining enriched spans, canonical outcomes, selective event logs, and failure-safe emission.
