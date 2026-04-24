# I am building a cloud

- Score: 963 | [HN](https://news.ycombinator.com/item?id=47872324) | Link: https://crawshaw.io/blog/building-a-cloud

### TL;DR
Crawshaw (Tailscale cofounder) explains why he’s launching exe.dev: he loves computers but thinks mainstream clouds have the wrong primitives—VMs coupled to fixed CPU/RAM bundles, remote block storage designed for HDD-era latencies, and punitive egress/network pricing papered over by Kubernetes and PaaS. With agents/LLMs set to massively increase how much software we run, these frictions become intolerable. exe.dev instead sells raw CPU+memory, runs your own VMs on fast local NVMe, wraps them in TLS/auth proxies, and offers global anycast entrypoints.

### Comment pulse
- Kubernetes is massive overkill for most business apps; a few big VMs plus simple deployment tools are cheaper, stabler, and easier to debug.  
- k8s itself isn’t the villain; misuse and organizational “enterprisey” layering cause bloat and incidents — counterpoint: its complexity bakes in cost/inefficiency versus bare metal.  
- Readers like the “buy hardware, slice it yourself” model (e.g., Hetzner + Firecracker), seeing high-IO local NVMe and snapshots as ideal for disposable sandboxes and agents.

### LLM perspective
- View: exe.dev’s resource-pool model aligns well with agent workloads needing many short-lived, strongly isolated environments and fast disk.  
- Impact: most compelling for indie devs, small SaaS, and AI tooling teams who outgrow hobby hosting but resent hyperscaler complexity and pricing.  
- Watch next: concrete IO/egress benchmarks, durability guarantees for async NVMe replication, API ergonomics, and whether pricing stays predictable as the platform scales.
