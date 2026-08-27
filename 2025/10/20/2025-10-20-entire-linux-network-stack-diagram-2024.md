# Entire Linux Network stack diagram (2024)

- Score: 544 | [HN](https://news.ycombinator.com/item?id=45639995) | Link: https://zenodo.org/records/14179366

### TL;DR

This dense reference diagram maps packet flow across Linux applications, sockets, TCP and UDP, IP, netfilter, queuing disciplines, drivers, hardware queues, bridges, virtual interfaces, namespaces, containers, virtual machines, and OpenStack networking. It also annotates inspection and tuning points such as buffer limits, congestion control, IRQ affinity, RSS, RPS, RFS, XPS, and offloads. The artifact is best treated as a navigation map: its breadth helps orient debugging, but kernel documentation remains necessary for current behavior and exact ordering.

### Comment pulse

- Commenters praised the diagram for making otherwise opaque packet paths and processing order easier to reason about.
- Readers also highlighted the author’s disk-I/O diagram and wished the accompanying Croatian book had an English translation.

### LLM perspective

- View: The diagram’s main value is exposing cross-layer dependencies that single-subsystem documentation tends to hide.
- Impact: Operators can use it to choose measurements before changing buffers, queues, affinity, or offloads.
- Watch next: Verify any debugging hypothesis against the deployed kernel version and relevant subsystem documentation.
