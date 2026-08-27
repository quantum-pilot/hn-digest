# The CRDT Dictionary: A Field Guide to Conflict-Free Replicated Data Types

- Score: 150 | [HN](https://news.ycombinator.com/item?id=46087022) | Link: https://www.iankduncan.com/engineering/2025-11-27-crdt-dictionary/

### TL;DR

This field guide explains how conflict-free replicated data types make replicas converge through deterministic, associative, commutative, and idempotent merges. It compares state- and operation-based designs across counters, sets, registers, maps, sequences, trees, causal tracking, and delta transmission, emphasizing that semantics determine the right choice. Preserving concurrent work costs metadata, complexity, or lost-update compromises. Garbage collection is especially difficult because forgotten causal history can resurrect deleted data. The author ultimately cautions that conventional databases and coordination remain simpler for many applications.

### Comment pulse

- Readers stressed that systems such as Automerge are complete, formally analyzed CRDTs, not merely bundles of primitive types.
- One commenter summarized the central concern: some conflicts are displaced into application semantics rather than eliminated.

### LLM perspective

- View: CRDT selection is domain modeling disguised as distributed-systems engineering.
- Impact: Automatic convergence is valuable only when its conflict semantics match what users expect.
- Watch next: Metadata bounds, offline-replica policy, garbage collection, and tests for adversarial concurrent edits.
