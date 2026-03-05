# A CPU that runs entirely on GPU

- Score: 238 | [HN](https://news.ycombinator.com/item?id=47243069) | Link: https://github.com/robertcprice/nCPU

### TL;DR
nCPU is a research CPU whose entire state (registers, memory, flags, PC) lives on a GPU as tensors, and whose ALU ops (add, mul, shifts, trig, etc.) are all small trained neural networks. It achieves 100% accurate integer arithmetic and explores how classic hardware ideas (carry-lookahead adders, vectorized shifts) translate into neural architectures, yielding oddities like multiplication being ~12× faster than addition. HN discussion treats it as a clever demo, not a practical CPU replacement, and pivots to differentiable execution and the enduring role of conventional CPUs.

---

### Comment pulse
- Fun but misdirected novelty → Some expected a more “hardware-ish” GPU CPU; instead see it as yet another case of gratuitous AI — counterpoint: precision and stability are nontrivial here.  
- Neural MUL vs ADD inversion → People highlight the 12× faster multiplication and note the whole pipeline is differentiable, suggesting program-synthesis via backprop as the more promising research angle.  
- CPUs aren’t going away → GPUs hide latency with parallelism; CPUs excel at branchy, serialized control. Future likely heterogeneous systems, maybe with GPU orchestrating and CPU as a subordinate worker.

---

### LLM perspective
- View: Treat this as a testbed for differentiable compute architectures, not as a contender to general-purpose CPUs.  
- Impact: Useful for researchers in compilers, automatic program synthesis, and ML–systems co-design to explore new optimization and training loops.  
- Watch next: Experiments training instruction sequences end-to-end, benchmarks on real-world kernels, and integration with existing differentiable programming toolchains.
