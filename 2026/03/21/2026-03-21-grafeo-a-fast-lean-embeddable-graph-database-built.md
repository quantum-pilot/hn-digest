# Grafeo – A fast, lean, embeddable graph database built in Rust

- Score: 177 | [HN](https://news.ycombinator.com/item?id=47467567) | Link: https://grafeo.dev/

- TL;DR  
    - Grafeo is a new Rust-based, embeddable graph database claiming top LDBC benchmark performance, dual LPG/RDF storage, multi-language querying (GQL, Cypher, SPARQL, GraphQL, SQL/PGQ), vector search, ACID transactions, and bindings from Python to WebAssembly. HN discussion is intrigued but wary: users note a glut of me-too graph/AI projects, question benchmark framing, and strongly suspect heavy LLM code generation given massive single-author commits, raising concerns about robustness versus mature graph databases and even plain PostgreSQL for many workloads.

- Comment pulse  
    - Graph DB glut → commenters see many me-too Rust/AI-era projects; LadybugDB author argues for narrower scope and one typed Cypher dialect instead of feature set.  
    - Benchmark skepticism → praise for using LDBC-based tool but urge clearly stating it’s author-maintained to avoid “we built it and we win” concerns.  
    - LLM-coded smell → huge LOC bursts suggest AI generation; many avoid for prod, prefer mature graph DBs or Postgres — counterpoint: some defend v0 iteration.

- LLM perspective  
    - View: Ambitious “everything graph” stack (LPG/RDF, many languages, vectors, bindings) risks complexity and thinly tested edges, especially if AI-generated.  
    - Impact: Best fit as an embedded analytics/experimentation engine on bounded datasets, not yet as a primary OLTP system of record.  
    - Watch next: independent LDBC runs, fuzzing/chaos tests, and real-user case studies will matter more than feature matrices or language-count marketing.
