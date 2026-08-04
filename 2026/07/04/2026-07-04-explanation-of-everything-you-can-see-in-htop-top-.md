# Explanation of everything you can see in htop/top on Linux (2019)

- Score: 371 | [HN](https://news.ycombinator.com/item?id=48784777) | Link: https://peteris.rocks/blog/htop/

### TL;DR

This hands-on guide decodes Linux process monitors by tracing their data through `/proc`: uptime, exponentially weighted 1/5/15-minute load averages, tasks, PIDs, parent-child trees, users, states, CPU time, priorities, and memory columns. Crucially, load counts runnable plus uninterruptible tasks, so it is not CPU utilization; VIRT includes mappings and allocations never resident in RAM, while RES still double-counts shared pages. HN readers recommended tree view and hidden user threads, debated RSS versus proportional-set size, and praised btop’s broader hardware, disk, network, and power panels.

### Comment pulse

- Process ancestry often beats flat ranking → tree view reveals launch context and compiler fan-out — counterpoint: it prevents dynamic list reordering.
- No single memory column tells allocation truth → PSS apportions shared pages, while RSS changes under pressure and includes mapped-file cache.
- btop trades density for scope → users value GPU, disk, network, wattage, and polished graphs but report missing zram, ZFS, Arc, and musl support.

### LLM perspective

- **View:** The article’s enduring lesson is epistemic: monitor fields are kernel accounting constructs, not plain-language measurements.
- **Impact:** Operators who understand provenance can avoid diagnosing CPU saturation from I/O load or memory leaks from address-space reservations.
- **Watch next:** Validate suspicious readings with `/proc`, `mpstat`, PSS-aware tools, and workload-specific I/O or scheduler metrics.
