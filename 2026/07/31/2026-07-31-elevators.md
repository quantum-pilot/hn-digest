# Elevators

- Score: 814 | [HN](https://news.ycombinator.com/item?id=49124218) | Link: https://john.fun/elevators

### TL;DR

Elevator scheduling is an optimization problem shaped by traffic patterns and tail latency, not merely nearest-car distance. LOOK reverses at the furthest requested stop; multi-car RSR scores load, direction, bunching, and proximity, then reassigns calls every five seconds. Simulations show RSR can lose to LOOK under heavy flow or in small banks, while destination dispatch generally worsens pickup waits. Commenters challenge that broad result, arguing offices, hotels, and cruise ships have clustered, directional demand that random-destination models may miss.

### Comment pulse

- Workload shapes dispatch results → offices batch lunch groups and hotels have two-way breakfast traffic — counterpoint: fixed assignments prevent rebalancing.
- Metric choice may change winners → destination dispatch could reduce onboard stops, a benefit missed by pickup-wait-only comparisons.
- Scheduling makes an effective teaching problem → commenters connected SCAN to disk scheduling and described classroom simulations, breadboard circuits, and games.

### LLM perspective

- View: Benchmark schedulers against observed origin-destination clusters and passenger groups, not only independent random calls.
- Impact: Operators need separate service targets for pickup tails, onboard time, and throughput.
- Watch next: Publish sensitivity tests across rush patterns, car counts, capacity saturation, and reassignment intervals.
