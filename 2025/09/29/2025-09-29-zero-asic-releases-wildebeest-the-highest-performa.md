# Zero ASIC releases Wildebeest, the highest performance FPGA synthesis tool

- Score: 181 | [HN](https://news.ycombinator.com/item?id=45410155) | Link: https://www.zeroasic.com/blog/wildebeest-launch

### TL;DR

Zero ASIC released Wildebeest, an open-source Yosys plugin for FPGA synthesis that selects optimization scripts by circuit size and uses advanced ABC9 techniques for speculative synthesis and logic-depth reduction. The company says an internal suite exceeding 150 benchmarks informed development and publishes LogikBench for evaluation. On its PicoRV32 table, Wildebeest reports fewer LUTs or lower logic depth than listed Yosys and proprietary results. However, several targets differ substantially, and Zero ASIC acknowledged that comparing compilers across different FPGA architectures is intrinsically difficult.

### Comment pulse

- Readers welcomed smaller open tooling but noted synthesis is only one stage; proprietary bitstreams still obstruct complete toolchains.
- Commenters questioned whether cross-device LUT and depth comparisons support the “highest performance” claim.
- Critics called Wildebeest a Yosys plugin focused on Zero ASIC hardware, while defenders cited its permissive release and explicit upstream credit.

### LLM perspective

- View: The release is meaningful open synthesis work, but the superlative headline outruns the presented cross-architecture evidence.
- Impact: Open optimization techniques can improve Yosys ecosystems even before a fully open FPGA flow exists.
- Watch next: Independent same-device benchmarks, broader target ports, upstream collaboration, and end-to-end results will establish value.
