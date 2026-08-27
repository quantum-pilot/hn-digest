# In defence of swap: common misconceptions (2018)

- Score: 105 | [HN](https://news.ycombinator.com/item?id=45318798) | Link: https://chrisdown.name/2018/01/02/in-defence-of-swap.html

### TL;DR

The article reframes Linux swap as backing storage that makes anonymous memory reclaimable, not merely emergency RAM. Without swap, the kernel must preferentially evict file-backed pages, potentially increasing cache churn and contention rather than avoiding disk I/O. Modern kernels improved earlier over-eager behavior; SSDs also narrow the cost difference between anonymous and file-page reclamation. The author recommends workload testing, cgroup v2 protections such as `memory.low`, and proactive pressure handling instead of trusting the late OOM killer. Commenters nevertheless described painful post-spike recovery and slow re-faulting.

### Comment pulse

- Swap broadens reclaim choices → cold anonymous pages can yield RAM to hotter file cache or applications.
- Failure behavior remains contentious → runaway processes may displace useful pages and leave desktops sluggish after memory returns.
- Capacity is workload-specific → examples ranged from a few gigabytes on servers to terabytes of NVMe-backed computation.

### LLM perspective

- View: Swap policy should optimize normal reclaim while separate controls contain runaway workloads before global contention.
- Impact: Operators gain utilization and resilience, but poor sizing or missing limits can worsen recovery latency.
- Watch next: Test PSI signals, `memory.low`, process limits, device wear, refault rates, and time-to-recovery under spikes.
