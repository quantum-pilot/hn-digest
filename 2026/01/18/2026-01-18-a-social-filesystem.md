# A Social Filesystem

- Score: 229 | [HN](https://news.ycombinator.com/item?id=46665839) | Link: https://overreacted.io/a-social-filesystem/

### TL;DR

Dan Abramov recasts AT Protocol as a distributed social filesystem: users’ repositories hold JSON records as the source of truth, while apps validate named lexicons, subscribe to signed updates, and build disposable materialized views. DIDs and protocol URIs keep identities and record links stable across handle or hosting changes; independent apps can reuse records, joins, and feeds without platform coordination. HN readers liked the file metaphor but debated whether advertising incentives, public replication, privacy, and context-specific social behavior undermine portability’s practical value.

### Comment pulse

- Open records improve durability and competition → alternative clients can preserve identity, history, and social graphs when an operator deteriorates.
- Public replication resembles a public Git repository → deletion cannot guarantee disappearance, raising indexing, training, encryption, and regret concerns.
- Portability is selective, not universal cross-posting → app designers choose compatible lexicons, preserving distinct communities while enabling useful interoperability.

### LLM perspective

- View: The strongest abstraction is user-controlled, verifiable event logs with plural interfaces.
- Impact: New apps can start from shared data and identities, reducing cold-start and migration costs.
- Watch next: Evaluate private-data support, relay diversity, recovery keys, and whether independent products sustain compatible lexicons.
