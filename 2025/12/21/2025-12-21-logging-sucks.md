# Logging sucks

- Score: 500 | [HN](https://news.ycombinator.com/item?id=46346796) | Link: https://loggingsucks.com/

### TL;DR
- The author argues most logging is still optimized for “easy writes” (scattered strings) instead of “easy queries” in modern, distributed systems. The fix is to emit one rich, structured “wide event” per request per service hop, with high-cardinality business context (user, cart, feature flags, error details) so you can query production traffic analytically instead of grep-ing text. OpenTelemetry is framed as plumbing, not a model: you still must decide *what* to capture and use tail-based sampling to control cost.

### Comment pulse
- Wide events are useful, but keep classic logs/traces → single end-of-request event risks losing information when crashes/timeouts bypass the logger.
- This is Charity Majors/Honeycomb-style observability and Nick Blumhardt-style structured logging → concepts predate the post; tools already support wide events.  
- “It’s just structured tags; grep still works” → critics see complexity and lost readability, others note JSON logs remain greppable and unlock richer queries.

### LLM perspective
- View: Treat logs as queryable event data, not narrative text, and design schema first, statements second.
- Impact: Improves debugging, SRE workflows, and cost control for teams with many services and high log volume.
- Watch next: Native wide-event support in APMs, better tail-sampling controls, and opinionated frameworks that generate canonical log lines by default.
