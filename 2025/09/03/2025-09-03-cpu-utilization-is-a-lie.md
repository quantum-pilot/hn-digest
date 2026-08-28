# %CPU utilization is a lie

- Score: 436 | [HN](https://news.ycombinator.com/item?id=45110688) | Link: https://www.brendanlong.com/cpu-utilization-is-a-lie.html

### TL;DR

Reported CPU percentage is busy time, not a linear measure of remaining throughput. On a 12-core, 24-thread Ryzen 5900X, the author's stress tests found 50% reported utilization could already represent 60–65% of general compute, 65–85% of integer capacity, and 80–100% of matrix or Nginx throughput. SMT adds shared threads rather than full cores, while turbo frequency falls as more cores activate. The recommendation is workload-specific load testing and comparing actual current work with the point where latency or errors become unacceptable.

### Comment pulse

- Readers add caches, memory bandwidth, locks, interconnects, burst windows, request mix, and queueing effects as further nonlinearities.
- Several defend utilization as useful when modeled empirically, while objecting to calling a clearly defined metric a “lie.”

### LLM perspective

- View: The dangerous mistake is treating an accounting percentage as a universal capacity gauge across hardware and workloads.
- Impact: Linear forecasts can underprovision services long before dashboards approach 100%, especially for SMT-saturated or memory-bound work.
- Watch next: Throughput, tail latency, queue depth, IPC, clock rate, burst duration, and per-workload saturation curves.
