# How GLM built its own inference infrastructure

- Score: 400 | [HN](https://news.ycombinator.com/item?id=49737922) | Link: https://z.ai/blog/glm-built-its-inference-infrastructure

### TL;DR

Z.ai says a GLM-5.3 Infra Agent helped engineers adapt GLM-5.3-Flash to more than 100,000 Chinese accelerators in under two weeks, tripling serving throughput through memory, quantization, parallelism, and disaggregated-serving changes. Its central lesson is dense feedback: local, cheap, timely, objectively verifiable tests that connect system regressions to kernels, concurrency, and code paths. Case studies cover a precision bug, a Python GIL transfer bottleneck, and kernel optimization. The company calls this early self-improvement, while retaining human objectives, boundaries, review, and risk decisions.

### Comment pulse

- Export restrictions may accelerate domestic capability → commenters argued constrained access creates demand and investment for Chinese accelerators and software.
- Scale claims impressed readers → a production cluster exceeding 100,000 domestic accelerators suggests inference chokepoints may be weakening.
- Throughput is not user latency → commenters reported slow service, while others noted providers may optimize aggregate tokens rather than individual speed.

### LLM perspective

- View: The reusable advance is an experimental feedback harness that turns agent proposals into attributable, falsifiable systems changes.
- Impact: Infrastructure engineers shift toward defining constraints, constructing measurements, and reviewing high-risk changes across layers.
- Watch next: Seek independent cost, utilization, latency, reliability, hardware-composition, and human-effort measurements against NVIDIA deployments.
