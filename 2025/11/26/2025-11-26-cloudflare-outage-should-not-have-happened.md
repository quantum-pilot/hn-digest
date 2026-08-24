# Cloudflare outage should not have happened

- Score: 124 | [HN](https://news.ycombinator.com/item?id=46059227) | Link: https://ebellani.github.io/blog/2025/cloudflare-outage-should-not-have-happened-and-they-seem-to-be-missing-the-point-on-how-to-avoid-it-in-the-future/

### TL;DR

Cloudflare's global failure began when a ClickHouse permissions change exposed an underconstrained metadata query: without a database filter, it returned duplicate column rows, inflated a Bot Management feature file, and triggered proxy crash loops. The author calls this a logical single point of failure and argues normalization, non-null schemas, and formal verification would prevent such bugs by construction. HN readers largely disputed that prescription, emphasizing operational fault containment and the speed requirements of live threat response.

### Comment pulse

- Formal rigor must match system maturity → critical proxies warrant stronger guarantees — counterpoint: verification constrains hiring, speed, and still inherits flawed specifications.
- Fault containment matters beyond correctness → replicated infrastructure still fails globally when one behavior-changing configuration reaches every proxy.
- The database diagnosis looks incomplete → the same metadata mistake exists in PostgreSQL, and normalization would not necessarily reject duplicate query results.

### LLM perspective

- View: Reliability depends on containing incorrect assumptions, not proving that every assumption is correct.
- Impact: Cloudflare customers inherit concentration risk from logically centralized control paths.
- Watch next: Staged feature-data rollout, automatic rollback, bounded parsers, kill-switch coverage, and formal methods on critical components.
