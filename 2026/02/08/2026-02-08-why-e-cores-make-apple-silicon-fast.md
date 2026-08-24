# Why E cores make Apple silicon fast

- Score: 226 | [HN](https://news.ycombinator.com/item?id=46933365) | Link: https://eclecticlight.co/2026/02/08/last-week-on-my-mac-why-e-cores-make-apple-silicon-fast/

### TL;DR

Apple silicon’s responsiveness comes partly from macOS assigning low-QoS background work—indexing, media analysis, backups, security scans—to Efficiency cores, preserving Performance cores for foreground apps. High-QoS threads may overflow onto E cores, but background threads normally are not promoted to idle P cores, protecting latency and battery life. This architecture favors many small processes for granular scheduling. Commenters accepted the isolation benefit but warned runaway services, opaque placement, noisy logs, and hundreds of cooperating processes complicate debugging.

### Comment pulse

- Splitting necessary work into small processes enables finer QoS classification—counterpoint: users questioned whether all background services are necessary or controllable.
- Runaway Spotlight, Photos, iCloud, or iMessage jobs can still consume resources; distributed daemons and high-volume logs make diagnosis harder.
- Performance comparisons were contextual: Apple excels in responsiveness and performance per watt, while filesystems, operating systems, RAM, and workloads can dominate benchmarks.

### LLM perspective

- View: Heterogeneous cores matter because scheduling policy preserves latency, not merely because a chip contains slow and fast cores.
- Impact: Users get responsive systems under background load; developers inherit QoS semantics, power tradeoffs, and harder cross-process observability.
- Watch next: Scheduler documentation, QoS instrumentation, promotion rules, runaway-daemon controls, power measurements, comparative workloads, log usability, and regression reports.
