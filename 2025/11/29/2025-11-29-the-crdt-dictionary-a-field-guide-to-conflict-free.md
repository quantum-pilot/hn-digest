# The CRDT Dictionary: A Field Guide to Conflict-Free Replicated Data Types

- Score: 150 | [HN](https://news.ycombinator.com/item?id=46087022) | Link: https://www.iankduncan.com/engineering/2025-11-27-crdt-dictionary/

### TL;DR

The guide explains how replicated data structures converge without consensus when merges are associative, commutative, and idempotent. It compares state and operation distribution, then maps application semantics to counters, sets, registers, maps, sequences, trees, version vectors, and delta updates. Each choice moves complexity: last-write-wins discards concurrent work, observed-remove designs preserve it with tags, and sequences accumulate identifiers or tombstones. Garbage collection can require expiry, causal tracking, checkpoints, bounds, or coordination. The author ultimately recommends choosing by required operations and admits a conventional database often remains simpler.

### Comment pulse

- High-level libraries are complete CRDTs → Automerge and similar systems expose proven collaborative document semantics without manual composition of primitive types.
- Coordination is displaced, not eliminated → applications still choose conflict semantics, causal delivery, compaction, and acceptable anomaly boundaries.
- Metadata is the availability bill → offline replicas force systems to retain history or risk resurrecting deleted data.

### LLM perspective

- View: CRDT correctness solves convergence, while product correctness still depends on whether the chosen merge behavior matches user intent.
- Impact: Offline collaboration becomes resilient, but storage growth, surprising conflict outcomes, and debugging complexity move into application design.
- Watch next: Teams should benchmark merge latency, tombstone growth, resynchronization costs, and user-visible outcomes under realistic partitions.
