# 15 years of FP64 segmentation, and why the Blackwell Ultra breaks the pattern

- Score: 196 | [HN](https://news.ycombinator.com/item?id=47068890) | Link: https://nicolasdickenmann.com/blog/the-great-fp64-divide.html

### TL;DR
For 15 years, Nvidia deliberately separated consumer and datacenter GPUs by throttling double-precision (FP64) relative to single-precision (FP32), keeping FP64 strong only on expensive enterprise parts. AI flipped this logic: modern training loves low precision (FP16/FP8/FP4), not FP64. Nvidia is now leaning on FP64 emulation (double-single and Ozaki-style schemes on tensor cores) while slashing native FP64 in Blackwell Ultra B300. Instead of consumer catching datacenter, datacenter is becoming “consumer-like,” and the new segmentation frontier is low-precision throughput rather than FP64.

---

### Comment pulse
- Nvidia’s trajectory → repeated repurposing of graphics silicon (CUDA, crypto, ML) plus aggressive market-pursuit, not mere luck—counterpoint: some credit early high-performance-compute positioning making “success” almost inevitable.  
- FP64 emulation limits → double-single narrows exponent range and risks overflow/underflow; more robust triple-number schemes reduce speedup, making Intel Battlemage and old Radeon VII attractive FP64-per-dollar options.  
- Why weak FP64 on gaming cards? → debate between die-area/cost arguments and intentional segmentation; others add US export controls tied to FP64 throughput as an under-discussed constraint.

---

### LLM perspective
- View: Native FP64 will survive for niche HPC, but emulated FP64 on tensor cores becomes the default for most “scientific” GPU workloads.  
- Impact: Small labs and individual researchers get cheaper “good-enough” FP64, while precision-critical codes consolidate on specialized SKUs or non-Nvidia vendors.  
- Watch next: Benchmark Ozaki/cuBLAS FP64 vs real FP64, track Intel/AMD FP64 ratios, and monitor export rules creeping into low-precision AI compute.
