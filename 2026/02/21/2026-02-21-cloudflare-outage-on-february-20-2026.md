# Cloudflare outage on February 20, 2026

- Score: 140 | [HN](https://news.ycombinator.com/item?id=47103649) | Link: https://blog.cloudflare.com/cloudflare-outage-february-20-2026/

### TL;DR

Cloudflare’s February 20 outage began when a cleanup task requested `pending_delete` without a value; the server treated that as no filter, returned every BYOIP prefix, and the task began deleting them and their service bindings. About 1,100 of 4,306 BYOIP prefixes were withdrawn, with full recovery taking 6 hours 7 minutes; the public 1.1.1.1 website failed, but DNS resolution did not. HN blamed unsafe API semantics, missing integration coverage, unrepresentative staging data, and absent circuit breakers for large withdrawal operations.

### Comment pulse

- Missing destructive filters should fail closed → a clear client error is safer than returning everything or silently returning nothing.
- One representative prefix should have exposed the bug → counterpoint: complete enterprise-state testing faces combinatorial cost and blind spots.
- Recovery exposed coupled state → withdrawn routes were easier to restore than prefixes whose service bindings had also been deleted.

### LLM perspective

- **View:** The query bug was trivial; allowing its result to mutate global routing was the systemic failure.
- **Impact:** BYOIP customers need independent recovery paths and safer configuration propagation.
- **Watch next:** Typed schemas, operational snapshots, staged rollouts, withdrawal-rate circuit breakers, and fewer repeat incidents.
