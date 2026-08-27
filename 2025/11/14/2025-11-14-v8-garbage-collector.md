# V8 Garbage Collector

- Score: 116 | [HN](https://news.ycombinator.com/item?id=45925431) | Link: https://wingolog.org/archives/2025/11/13/the-last-couple-years-in-v8s-garbage-collector

### TL;DR

After reviewing roughly 1,600 V8 commits, the author groups garbage-collector work around sandbox hardening, Oilpan generational experiments, shared-memory alignment, and platform heuristics. The sandbox uses constrained offsets, separated memory spaces, and external-pointer tables to tolerate arbitrary writes; Oilpan experiments explored sticky bits, copying nurseries, pinning, and quarantines. Shared JavaScript and Wasm memory required atomic-field alignment, while heuristic and mutex work varied across platforms. The author's effort percentages and shipping-status judgments are estimates, not an official V8 roadmap.

### Comment pulse

- Discussion clarified that some signed length fields predated the sandbox design.
- Readers also asked how application workloads, including games, might tune or observe collector behavior.

### LLM perspective

- View: GC engineering here is inseparable from sandbox security, concurrency, and platform-specific scheduling.
- Impact: Small metadata or alignment decisions can affect both exploit resistance and collection correctness.
- Watch next: Broader Oilpan generational rollout and evidence that new heuristics remain stable across platforms.
