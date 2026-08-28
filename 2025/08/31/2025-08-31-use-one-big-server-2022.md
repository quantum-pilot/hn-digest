# Use One Big Server (2022)

- Score: 350 | [HN](https://news.ycombinator.com/item?id=45085029) | Link: https://specbranch.com/posts/one-big-server/

### TL;DR

This 2022 essay argues that modern hardware makes vertical scaling the default for most services: one capable server, plus a differently configured backup in another datacenter, can handle workloads that teams prematurely distribute. Larger nodes avoid coordination and network overhead, while dedicated rentals were dramatically cheaper than equivalent AWS capacity in the article’s examples. Cloud services still earn their premium through convenience, fast replacement, managed operations, and burst capacity; the recommendation is fewer large machines unless measured demand proves otherwise.

### Comment pulse

- Dedicated-server advocates emphasized raw capacity, predictable latency, simpler databases, and lower cost than major-cloud instances.
- Cloud supporters valued durable managed services and engineering focus when hosting expense is small relative to business revenue.
- HN reportedly follows the primary-plus-backup pattern, with differing hardware to reduce correlated failure risk.

### LLM perspective

- View: Architecture should follow measured workload shape, not inherited assumptions that distribution is automatically modern or resilient.
- Impact: Small teams can defer microservices and spend scarce engineering time on product work.
- Watch next: Updated price comparisons, recovery drills, utilization data, and the first bottleneck that actually forces horizontal scaling.
