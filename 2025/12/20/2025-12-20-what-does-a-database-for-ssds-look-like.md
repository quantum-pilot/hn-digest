# What Does a Database for SSDs Look Like?

- Score: 130 | [HN](https://news.ycombinator.com/item?id=46334990) | Link: https://brooker.co.za/blog/2025/12/15/database-for-ssd.html

### TL;DR

Marc Brooker estimates that a modern transactional database should cache roughly 30 seconds of likely reuse, target average local-SSD transfers near 32kB, and perform synchronous cross-zone coordination only at commit. Because local persistence cannot survive machine failure, he favors a distributed multi-AZ log for durability and replay, multiversioning to avoid coordinated reads, and high-quality clocks for strongly consistent scale-out reads. He would retain SQL, relational semantics, atomicity, and isolation while treating durability, availability, and scale as distributed concerns rather than preserving single-system recovery machinery.

### Comment pulse

- Critics said the AWS-centered design adds cost, complexity, latency, and vendor dependence unnecessary for many applications satisfied by local durability and replicas.
- Others argued buffering and access locality still matter on SSDs, while modern database research already explores persistent memory and SSD-aware engines.

### LLM perspective

- View: SSDs change quantitative thresholds, but cloud availability requirements reshape the architecture more radically than storage media alone.
- Impact: Global, high-availability systems benefit most; smaller workloads may rationally keep simpler local commits and recovery.
- Watch next: Workload-specific cost comparisons across local WAL, dual-site flushing, and managed distributed logs under failures.
