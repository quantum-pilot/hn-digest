# I regret building this $3000 Pi AI cluster

- Score: 400 | [HN](https://news.ycombinator.com/item?id=45302065) | Link: https://www.jeffgeerling.com/blog/2025/i-regret-building-3000-pi-ai-cluster

### TL;DR

After a two-year wait, the author assembled ten 16GB Raspberry Pi Compute Modules into a $3,000, 160GB cluster and found it poor for AI inference. Thermal throttling and flaky SSDs forced rebuilds. HPL reached 325 Gflops at 130W, but a Framework cluster was four times faster. A distributed 70B model produced only 0.28 tokens per second with llama.cpp RPC and 0.85 with fragile distributed-llama. The compact, quiet hardware still suits learning, CI, security-sensitive edge tasks, or many-node experiments.

### Comment pulse

- Commenters recommend one higher-core AMD machine with virtual machines for cheaper, simpler distributed-systems practice.
- Others defend Raspberry Pi’s educational roots and note that unusual builds can still pay through audience interest.

### LLM perspective

- View: The experiment usefully separates aggregate memory capacity from the bandwidth, software maturity, and interconnect performance inference actually needs.
- Impact: Buyers can avoid mistaking many inexpensive nodes for an economical substitute for fewer, faster machines in tightly coupled workloads.
- Watch next: Better Pi GPU support, reliable distributed runtimes, and benchmarks against a similarly priced single-node system.
