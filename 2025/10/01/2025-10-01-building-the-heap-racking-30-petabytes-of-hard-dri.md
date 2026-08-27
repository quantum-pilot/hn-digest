# Building the heap: racking 30 petabytes of hard drives for pretraining

- Score: 232 | [HN](https://news.ycombinator.com/item?id=45438496) | Link: https://si.inc/posts/the-heap/

### TL;DR

Standard Intelligence says it built a 30-petabyte video-training store for $426,500 upfront and about $29,500 monthly including depreciation, versus quoted or public cloud estimates of $270,000 to $1.13 million monthly. Its workload tolerates data loss and needs throughput rather than enterprise durability, enabling 2,400 mostly used drives, XFS, nginx, SQLite, and roughly 200 lines of Rust instead of Ceph or MinIO. The team reports saturating a 100-Gbps link, while acknowledging labor, density, cabling, compatibility, networking, and maintenance challenges.

### Comment pulse

- Readers welcomed rebuilding on-premises skills but warned that long-lived hardware can accumulate fragile, pet-like state.
- The authors said proximity to the colocation facility justified higher costs for their five-person team.
- Commenters questioned retail-cloud comparisons; the authors said AWS egress pricing remained prohibitive even after negotiation.

### LLM perspective

- View: The savings follow from matching infrastructure to disposable training data, not proving self-hosting universally superior.
- Impact: Relaxed durability requirements can erase much of managed storage’s value while transferring operations risk in-house.
- Watch next: Long-term drive failure, staffing, refresh, and data-rebuild costs will test the three-year economics.
