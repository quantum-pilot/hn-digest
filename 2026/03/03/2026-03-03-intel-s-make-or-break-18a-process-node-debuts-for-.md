# Intel's make-or-break 18A process node debuts for data center with 288-core Xeon

- Score: 225 | [HN](https://news.ycombinator.com/item?id=47236958) | Link: https://www.tomshardware.com/pc-components/cpus/intels-make-or-break-18a-process-node-debuts-for-data-center-with-288-core-xeon-6-cpu-multi-chip-monster-sports-12-channels-of-ddr5-8000-foveros-direct-3d-packaging-tech

### TL;DR

Intel’s Xeon 6+ Clearwater Forest brings its 18A process to servers with up to 288 Darkmont efficiency cores. Twelve 24-core compute chiplets sit on three Intel 3 base dies via Foveros Direct, connect to Intel 7 I/O tiles, and share about 1.15GB of cache. The socket-compatible package provides 12 DDR5-8000 channels, 96 PCIe 5.0 lanes, and 64 CXL 2.0 lanes for cloud, telecom, and edge workloads. Commenters saw the packaging as an Intel Foundry proof point, while warning about NUMA, scheduling, lower single-thread performance, and deployment economics.

### Comment pulse

- Dense servers can beat cloud pricing for stable workloads — counterpoint: staffing, disaster recovery, networking, and egress complicate comparisons.
- Hundreds of cores magnify NUMA locality and scheduler issues; applications may need explicit process placement to avoid remote-memory bottlenecks.
- Darkmont efficiency cores suit parallel hosting, but weaker single-thread performance and missing AVX-512 can distort headline core-count comparisons.

### LLM perspective

- **View:** The multi-node 3D package is a more consequential 18A demonstration than the 288-core headline alone.
- **Impact:** A reliable volume product could strengthen Intel Foundry credibility while increasing density for highly parallel infrastructure.
- **Watch next:** Independent performance-per-watt tests, yields, system pricing, NUMA behavior, CXL adoption, and announced availability later this year.
