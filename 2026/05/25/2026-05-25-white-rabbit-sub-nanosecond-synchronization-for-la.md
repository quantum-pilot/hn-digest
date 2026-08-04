# White Rabbit – sub-nanosecond synchronization for large distributed systems

- Score: 187 | [HN](https://news.ycombinator.com/item?id=48245916) | Link: https://ohwr.org/projects/white-rabbit/

### TL;DR

White Rabbit is an open hardware, firmware, and software network that synchronizes thousands of distributed nodes with sub-nanosecond accuracy while carrying deterministic gigabit Ethernet data, typically across 10-kilometer links. Unlike ordinary Ethernet NICs with independent clocks, its physical layers share timing, combining enhanced PTP and SyncE techniques with two-way delay measurement and active compensation. HN commenters explained that propagation time does not bound synchronization accuracy, cited roughly 10-picosecond lab jitter over 50 kilometers, and distinguished precise clock transfer from distributed consensus.

### Comment pulse

- Two-way transfer estimates round-trip delay; assuming similar paths, clients correct phase drift rather than waiting for signals to arrive simultaneously.
- Fiber-temperature changes were reportedly compensated across 50-kilometer lab links, showing the system tracks changing path length, not merely fixed delay.
- Readers pointed to European 10-Gbps implementations and CERN documentation as better technical entry points beyond the sparse project page.

### LLM perspective

- View: White Rabbit relocates time synchronization into network hardware, turning clock distribution and data transport into one engineered system.
- Impact: Laboratories can correlate measurements and trigger equipment across large installations without separate timing cabling.
- Watch next: Verify asymmetry tolerance, holdover behavior, topology scaling, interoperability, and end-to-end accuracy under temperature and link failures.
