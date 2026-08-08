# Idempotency is easy until the second request is different

- Score: 272 | [HN](https://news.ycombinator.com/item?id=48047930) | Link: https://blog.dochia.dev/blog/idempotency/

### TL;DR

Reliable idempotency requires remembering what an operation meant, not merely that a key appeared. The design scopes keys, fingerprints a normalized command, atomically claims execution, rejects mismatches, stores replayable outcomes, and models concurrent, failed, expired, or downstream-unknown states. Providers, queues, regions, and side effects each need stable identities and recovery; exactly-once delivery does not guarantee exactly-once business effect. Commenters agreed the edge cases are real but split on complexity: some always return 409 for duplicate keys, while others require replay so clients learn whether the first attempt succeeded.

### Comment pulse

- Simple-contract advocates return 409 whenever a key repeats, delegating uncertainty to clients — counterpoint: that response cannot reveal whether money moved.
- Contract purists said servers should trust the declared key; pragmatists prefer command hashes because detecting client bugs prevents users bearing weeks of harm.
- Engineers reported generic libraries failing when idempotency metadata and business effects used separate transactions, validating the need for failure-state classification.

### LLM perspective

- View: Idempotency is distributed transaction design under partial knowledge, with a client-visible contract layered over recovery machinery.
- Impact: Payment and workflow APIs need more storage, observability, retention policy, reconciliation, and tests than a response cache suggests.
- Watch next: Concurrent conflicts, provider-timeout recovery, schema-version replay, cross-region races, stale locks, queue duplicates, and sensitive-body retention.
