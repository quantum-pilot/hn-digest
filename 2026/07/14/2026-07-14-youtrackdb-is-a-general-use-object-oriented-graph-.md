# YouTrackDB is a general-use object-oriented graph database

- Score: 166 | [HN](https://news.ycombinator.com/item?id=48902026) | Link: https://github.com/JetBrains/youtrackdb

- TL;DR  
  YouTrackDB is JetBrains’ open-source, general-purpose, object‑oriented graph database that backs YouTrack in production. It stores relations natively, claims O(1) link traversal, ACID with default snapshot isolation, and supports Gremlin/TinkerPop plus its own SQL‑like YQL for graph pattern matching. It can run embedded or as a Dockerized server, with schema‑less to schema‑full modes, role‑based security, and optional encryption. HN discussion focuses on why JetBrains built this instead of using Neo4j, the Java‑over‑Kotlin choice, and whether graph DBs are worth their trade‑offs.

- Comment pulse  
  - Java implementation and Xodus lineage → YouTrackDB evolves JetBrains’ earlier Xodus engine; code stays mostly Java since YouTrack predates Kotlin and bulk ports aren’t prioritized.  
  - Costs push away from Neo4j → Neo4j’s enterprise pricing and move away from simple embedded use are seen as reasons to build an in‑house alternative.  
  - Graph DB value debated → Pros: ergonomic deep traversal; cons: tuning, index bloat, immature tooling—counterpoint: niche domains like fraud, security, investigations still see clear wins.

- LLM perspective  
  - View: Combining object‑oriented modeling with graph storage and SQL‑style YQL narrows the conceptual gap for Java developers considering graphs.  
  - Impact: Teams needing an embeddable, OSS, JVM‑native graph engine with Gremlin compatibility gain another option beyond Neo4j and JanusGraph.  
  - Watch next: workload benchmarks versus Postgres+PGQ, clarity on GQL integration, and whether JetBrains commits to long‑term governance and releases.
