# V8 Garbage Collector

- Score: 116 | [HN](https://news.ycombinator.com/item?id=45925431) | Link: https://wingolog.org/archives/2025/11/13/the-last-couple-years-in-v8s-garbage-collector

- TL;DR
  - Survey of V8 GC work since 2023: security-focused sandboxing (32/40‑bit offsets, external pointer tables, now hardware-enforced bounds), Oilpan integration via pinning to support conservative stack scanning while keeping a copying nursery, and groundwork for shared-memory threads, e.g., 64‑bit alignment in shared Wasm objects. Side quests: heuristics tuning, lock changes, third‑party heap removal. HN discusses signed vs unsigned length fields surfacing sandbox edge cases, how hard GC tuning is for game workloads, and practical debugging tools (rr, watchpoints).

- Comment pulse
  - Signed length fields enable sandbox edge cases → negative lengths can sign-extend; boundary code may escalate in-sandbox corruption — counterpoint: pre-sandbox required existing OOB write.
  - V8 GC tuning for games is hard → developers seek lower pauses; suggestions include QuickJS or JavaScriptCore; V8 knobs may trade memory for latency.
  - Debugging heap corruption is painful → rr and memory watchpoints help reproduce and isolate issues in moving collectors.

- LLM perspective
  - View: Security hardening and multithreading add state duplication, alignment constraints, and heuristics bloat; automated, per-platform tuning becomes essential.
  - Impact: Browsers, Node, and edge runtimes may see higher memory footprints but better isolation; game engines will watch pause percentiles closely.
  - Watch next: Finch results and benchmarks for conservative-stack generational GC, rollout of direct handles, and Wasm shared-everything threading shipped-by-default.
