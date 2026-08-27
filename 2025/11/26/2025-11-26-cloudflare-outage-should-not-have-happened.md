# Cloudflare outage should not have happened

- Score: 124 | [HN](https://news.ycombinator.com/item?id=46059227) | Link: https://ebellani.github.io/blog/2025/cloudflare-outage-should-not-have-happened-and-they-seem-to-be-missing-the-point-on-how-to-avoid-it-in-the-future/

### TL;DR

A critique traces Cloudflare’s November 18 outage to a ClickHouse metadata query that omitted a database qualifier; a permissions change exposed duplicate column rows, doubled a Bot Management feature file, and triggered crash loops across core systems. Cloudflare proposed configuration hardening, kill switches, resource limits, and failure reviews. The author instead argues for relational normalization and formal verification. Commenters strongly contest that diagnosis, saying the query bug was database-agnostic and safer staged rollout, rollback, and fault isolation were the more direct defenses.

### Comment pulse

- Database rigor would prevent malformed states → counterpoint: the cited metadata table was already normalized, and PostgreSQL permits analogous mistakes.
- Critical infrastructure merits exceptional assurance → formal methods still depend on correct specifications and impose substantial costs.

### LLM perspective

- View: The strongest lesson is containment of configuration surprises, not a universal database prescription.
- Impact: Global edge operators need deployment controls that bound both bad code and unexpected data.
- Watch next: Whether Cloudflare adds gradual rollout, schema-qualified checks, and automatic rollback for generated configurations.
