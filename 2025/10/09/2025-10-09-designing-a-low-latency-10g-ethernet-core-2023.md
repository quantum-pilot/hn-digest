# Designing a Low Latency 10G Ethernet Core (2023)

- Score: 159 | [HN](https://news.ycombinator.com/item?id=45522406) | Link: https://ttchisholm.github.io/ethernet/2023/05/01/designing-10g-eth-1.html

### TL;DR

This brief introduction opens a five-part account of a personal FPGA project implementing a low-latency 10-gigabit Ethernet core. The author reports under 60-nanosecond loopback latency, which he describes as comparable with commercial offerings. Subsequent installments are promised to cover architecture and verification using cocotb and pyuvm, packet-processing latency reductions, comparisons with commercial low- and ultra-low-latency cores, measured performance, and unimplemented improvements. The frozen entry contains no design details, test setup, resource utilization, or measurement results beyond that headline figure.

### Comment pulse

- Readers warned against comparing full receive-and-return loopback with nanosecond Layer-1 signal replication in crosspoint devices.
- Discussion placed the work near low-latency trading applications while noting the operational pressure such systems can create.

### LLM perspective

- View: The latency claim is intriguing, but its meaning depends on boundaries, buffering, packet size, and measurement method.
- Impact: An open design series can make specialized FPGA networking techniques more reproducible and teachable.
- Watch next: Verification coverage, timing closure, resource costs, complete latency distributions, and like-for-like comparisons.
