# Can Intel finally beat ARM on performance per Watt?

- Score: 146 | [HN](https://news.ycombinator.com/item?id=49223079) | Link: https://hackaday.com/2026/08/08/want-energy-efficiency-dude-youre-getting-a-dell/

### TL;DR
Jeff Geerling’s tests of a Dell XPS 13 with Intel’s new Core 5 320 show it *slightly* beating Apple’s MacBook Neo in Linpack performance-per-watt (6.21 vs 5.38 GFLOPS/W), and even topping some M3/M4 desktop Macs—suggesting x86’s historic efficiency gap versus ARM is closing. Hacker News commenters like the rigor but stress that this is one matrix-math benchmark with non-Apple BLAS, so it may understate Apple’s potential, and that real-world experience still hinges on GPU, thermals, OS power management, and UX details.

### Comment pulse
- Linpack ≠ everything → Benchmark measures matrix math using BLIS/OpenBLAS; a re-run using Apple’s Accelerate on M1 Max nearly doubled GFLOPS/W — counterpoint: still a useful apples-to-apples CPU test.
- System vs chip → Apple optimizes silicon, OS, and libraries together; Intel’s Wildcat Lake on 18A looks strong, but Neo still leads in GPU and single-core burst.
- UX over micro-watts → Fans, missing headphone jack, and whether the OS actually sleeps often matter more to buyers than small benchmark efficiency deltas.

### LLM perspective
- View: Intel’s new mobile parts show ISA isn’t destiny; process node and microarchitecture now dominate efficiency comparisons.
- Impact: Competitive x86 perf/W slows ARM’s inevitability narrative in laptops, especially for Linux-first users and corporate fleets.
- Watch next: Independent suites mixing web, compile, video, and idle tests across 18A laptops vs M-series and Snapdragon X, with wall-plug measurements.
