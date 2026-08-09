# I am building a cloud

- Score: 963 | [HN](https://news.ycombinator.com/item?id=47872324) | Link: https://crawshaw.io/blog/building-a-cloud

### TL;DR

Tailscale cofounder David Crawshaw is starting exe.dev because he dislikes today’s cloud abstractions. He argues VM pricing wrongly binds CPU and memory, remote block storage squanders SSD performance, egress is punitive, PaaS limits capability, and Kubernetes cannot repair those foundations. Exe.dev instead sells pooled compute for many user-controlled VMs, with managed TLS and authentication proxies, local NVMe asynchronously replicated off-host, global regions, and anycast ingress. Agents make this urgent by generating more software while wasting context on infrastructure complexity. Readers liked the simpler shape but debated Kubernetes and local-disk durability.

### Comment pulse

- Small teams reported greater reliability and lower cost after replacing clusters with one or two vertically scaled VMs.
- Kubernetes defenders said complexity reflects scale or organizational requirements — counterpoint: critics saw it routinely deployed where simpler systems suffice.
- Commenters admired the founder’s incentives but warned successful clouds often add features and price lock-in after customers commit.

### LLM perspective

- Publish failure semantics for host loss, replication lag, recovery objectives, and migrations before local NVMe becomes trusted state.
- Benchmark end-to-end IOPS, tail latency, egress, density, and cost against comparable hyperscaler configurations.
- Watch whether omitted basics remain simple as static IPs, snapshots, compliance, and enterprise controls arrive.
