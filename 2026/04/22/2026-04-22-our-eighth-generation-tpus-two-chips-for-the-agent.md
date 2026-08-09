# Our eighth generation TPUs: two chips for the agentic era

- Score: 380 | [HN](https://news.ycombinator.com/item?id=47862497) | Link: https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/

### TL;DR

Google unveiled two eighth-generation TPUs coming later in 2026: TPU 8t for training and TPU 8i for latency-sensitive inference. An 8t superpod joins 9,600 chips, two petabytes of shared high-bandwidth memory, and 121 exaflops, while targeting 97% productive compute. The 8i combines 288 GB HBM, larger SRAM, 19.2 Tb/s interconnects, and collectives acceleration; Google claims 80% better performance per dollar. Hacker News saw vertical integration as Google’s cost advantage but questioned cloud pricing, hardware lock-in, and whether Gemini’s agent software can exploit it.

### Comment pulse

- Gemini’s terse reasoning may reflect efficiency — counterpoint: users reported broken tool calls, search gaps, and loops in agentic coding.
- Whole-datacenter co-design may outperform standalone accelerators on cost, but critics cited GCP margins, constrained production, and Nvidia’s fabrication priority.
- Google’s quieter deployment and consumer reach inspire confidence, although commenters saw inconsistent apps and preview labeling as weak product execution.

### LLM perspective

- **View:** Specialization separates throughput-heavy training from memory-sensitive serving, improving economics without making either chip single-purpose.
- **Impact:** Large customers gain TPU options for JAX, PyTorch, SGLang, and vLLM; smaller researchers remain sensitive to rental prices.
- **Watch next:** General availability, independent benchmarks, capacity, sustained goodput, pricing, framework compatibility, and agent quality.
