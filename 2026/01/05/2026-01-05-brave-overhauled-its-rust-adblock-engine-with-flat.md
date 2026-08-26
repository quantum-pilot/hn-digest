# Brave overhauled its Rust adblock engine with FlatBuffers, cutting memory 75%

- Score: 320 | [HN](https://news.ycombinator.com/item?id=46501894) | Link: https://brave.com/privacy-updates/36-adblock-memory-reduction/

### TL;DR

Brave moved roughly 100,000 default ad-blocking filters from heap-allocated Rust structures into FlatBuffers, enabling compact zero-copy access and reducing the engine’s memory consumption by 75%. Brave says the change saves about 45 MB across desktop and mobile in version 1.85, with more optimizations planned for 1.86, including fewer allocations, faster builds and matching, and shared resources. Commenters praised Rust ecosystem reuse, clarified that the 75% figure applies to the ad-block engine rather than the whole browser, and revisited demand for a stripped-down Brave distribution.

### Comment pulse

- Publishing the engine as a reusable Rust crate showcases open-source composition—counterpoint: static linking and dependency supply chains introduce separate tradeoffs.
- A screenshot’s smaller overall reduction caused confusion until readers separated browser-process memory from the engine-specific 75% claim.
- Users value native blocking but want commercial extras removed; others noted features can be disabled and forks already target that niche.

### LLM perspective

- View: Serialization delivers meaningful baseline savings because filter data is read-heavy, shared, and structurally repetitive.
- Impact: Mobile devices and filter-heavy configurations benefit most through lower memory pressure, smoother multitasking, and potentially better battery life.
- Watch next: Independent benchmarks should test matching latency, startup, battery use, and memory across platforms and expanded filter lists.
