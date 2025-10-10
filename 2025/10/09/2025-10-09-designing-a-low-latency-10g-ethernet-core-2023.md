# Designing a Low Latency 10G Ethernet Core (2023)

- Score: 159 | [HN](https://news.ycombinator.com/item?id=45522406) | Link: https://ttchisholm.github.io/ethernet/2023/05/01/designing-10g-eth-1.html

- TL;DR
    - An engineer opens a series on building an FPGA 10G Ethernet core optimized for latency, targeting under 60 ns loopback and verified with cocotb/pyuvm. He plans to detail low‑latency MAC/PCS techniques, measurements, and comparisons against commercial IP. HN debates the numbers: “4 ns switches” are L1 replicators, not real switching; fastest L3 devices are ~90 ns, and loopback ≠ pass‑through. End‑to‑end latency is often PCIe‑bound (~1 µs between hosts). Side‑discussion: HFT FPGA work is thrilling to some, purposeless or stressful to others.

- Comment pulse
    - 60 ns loopback is strong → 4 ns L1 parts only replicate; true L3 switching ~90 ns; pass-through ≠ loopback; some switches ~800 ns round-trip.
    - End‑to‑end host latency bound by PCIe → ~250 ns one‑way on the NIC path; inter‑host exchanges rarely beat ~1 µs even with ultra‑low‑latency network gear.
    - HFT FPGA work: exciting but stressful → outages cost millions; some call it pointless — counterpoint: others value the technical challenge and craft.

- LLM perspective
    - View: Intro frames an open, measured effort to cut MAC/PCS latency on FPGA using Python-based verification and transparent benchmarking.
    - Impact: Practitioners get reproducible tests, cocotb/pyuvm patterns, and a latency baseline (~60 ns loopback) comparable to commercial low-latency IP.
    - Watch next: Specify measurement method, PHY/MAC split, cut-through depth, clocking; publish cores/testbenches and cross‑vendor results to distinguish L1 replication from real switching.
