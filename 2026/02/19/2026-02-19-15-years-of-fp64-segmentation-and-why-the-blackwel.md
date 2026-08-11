# 15 years of FP64 segmentation, and why the Blackwell Ultra breaks the pattern

- Score: 196 | [HN](https://news.ycombinator.com/item?id=47068890) | Link: https://nicolasdickenmann.com/blog/the-great-fp64-divide.html

### TL;DR

Over fifteen years, Nvidia widened consumer GPUs’ FP64 deficit relative to FP32, moving from a driver cap on shared Fermi silicon toward structurally different products and a 1:64 ratio. The author argues AI has undermined that segmentation: low-precision tensor cores now dominate enterprise value, while Ozaki-style decomposition can reconstruct FP64 matrix multiplication. Blackwell Ultra’s B300 reportedly drops native FP64 from 37 to 1.2 TFLOPS, suggesting future tiering may shift to FP16 and lower precisions.

### Comment pulse

- HPC readers warned two-FP32 emulation retains FP32’s exponent range, causing overflow and underflow; three-part formats restore range but reduce speed.
- Cost and regulation complicated the segmentation thesis — counterpoint: several commenters argued shared FP32/FP64 units add far less area than assumed.
- Intel Battlemage and the older Radeon VII were cited as unusually affordable consumer FP64 options.

### LLM perspective

- **View:** AI demand is reallocating silicon from dedicated FP64 toward low-precision tensor throughput.
- **Impact:** HPC users may trade exact hardware arithmetic for workload-specific emulation, software complexity, and numerical caveats.
- **Watch next:** B300 application benchmarks, cuBLAS Ozaki accuracy controls, and future Nvidia FP64 roadmaps.
