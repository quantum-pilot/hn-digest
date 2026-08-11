# A CPU that runs entirely on GPU

- Score: 238 | [HN](https://news.ycombinator.com/item?id=47243069) | Link: https://github.com/robertcprice/nCPU

### TL;DR

nCPU is a research runtime that keeps registers, memory, flags, program counter, decoding, and execution as GPU-resident tensors, while routing ALU operations through trained PyTorch models. It reports perfect integer results across 347 tests, about 4,975 instructions per second in neural mode, and a 2.5-fps raycaster. Its unusual architecture makes multiplication twelve times faster than addition because parallel byte-pair lookups beat sequential carry propagation. HN viewed it as a clever experiment, not a CPU replacement, and suggested differentiable execution could matter more for program synthesis than general computing.

### Comment pulse

- GPUs hide latency through parallelism; branch-heavy serial workloads still favor CPUs that minimize latency and predict control flow directly.
- Hardware-design ideas transfer → Kogge–Stone carry lookahead cut neural addition latency 3.3×, while vectorization reduced shift latency 6.5×.
- Heterogeneous systems may invert today’s hierarchy — counterpoint: consolidating CPU and GPU roles is likelier than eliminating either processor.

### LLM perspective

- **View:** The most novel artifact is a differentiable instruction pipeline, not competitive emulation performance.
- **Impact:** Researchers gain a sandbox for neural arithmetic and gradient-based program experiments; application developers gain little today.
- **Watch next:** Independent benchmarks, larger programs, numerical failures, end-to-end differentiation, and behavior around discrete branches.
