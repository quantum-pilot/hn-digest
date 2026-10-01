# 5x faster Edge Functions: V8 isolates to Firecracker MicroVMs

- Score: 219 | [HN](https://news.ycombinator.com/item?id=49912444) | Link: https://www.netlify.com/blog/edge-functions-firecracker-microvms/

### TL;DR

Netlify says it moved Edge Functions from an external hosted V8-isolate service to Firecracker MicroVMs inside its own edge network, cutting median warm overhead from 25–40ms to about 5–6ms. Its architecture hashes per-deploy specifications, uses rendezvous routing for cache warmth, spreads hot services across nodes, snapshots stripped-down Linux VMs and scales them to zero. Netlify also reports 47.4% faster p99 execution and 99.998% availability. Commenters questioned whether removing network hops, rather than MicroVM execution itself, explains the headline gain.

### Comment pulse

- Skeptics challenged the isolate-to-MicroVM framing → The old isolates ran outside Netlify’s network, so locality may explain most of the improvement.
- MicroVM advocates valued stronger isolation and flexibility → Others argued isolates remain lighter and easier to analyze for many edge workloads.
- Library authors requested Fetchable compatibility → Runtime portability still matters despite the invisible infrastructure migration.

### LLM perspective

- View: Architecture placement matters more here than the runtime-label comparison suggests.
- Impact: Netlify gains control over security boundaries, capacity and future runtime limits.
- Watch next: Independent benchmarks should separate network, routing, cold-start and execution-time contributions.
