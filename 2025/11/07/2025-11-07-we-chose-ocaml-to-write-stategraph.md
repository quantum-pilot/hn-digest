# We chose OCaml to write Stategraph

- Score: 144 | [HN](https://news.ycombinator.com/item?id=45845958) | Link: https://stategraph.dev/blog/why-we-chose-ocaml

### TL;DR

Stategraph’s developers chose OCaml for a Terraform-state system that normalizes JSON into a PostgreSQL dependency graph and permits non-overlapping resource operations to proceed concurrently. They credit typed records and SQL, immutable defaults, exhaustive variants, and PPX-generated serializers with moving field, schema, null-handling, and transformation errors toward compile time; database row locks handle shared-state coordination. Commenters agreed strong types remove validation work but viewed language selection as partly preference-driven and questioned the product need. The team says resource-level concurrency avoids serial queues and repeated root-module splitting.

### Comment pulse

- OCaml users praised its fast compiler and module system; others framed “why this language” essays as post-hoc justification.
- Prospective users asked for a FLOSS license; the team said it is still balancing openness and sustainability.

### LLM perspective

- View: OCaml reinforces explicit invariants, but database protocols and engineering discipline still determine end-to-end correctness.
- Impact: Teams could parallelize independent Terraform work without restructuring state, assuming Stategraph’s coordination model proves reliable.
- Watch next: Licensing, concurrency benchmarks, failure recovery, schema migrations, onboarding evidence, and audits of serialization claims.
