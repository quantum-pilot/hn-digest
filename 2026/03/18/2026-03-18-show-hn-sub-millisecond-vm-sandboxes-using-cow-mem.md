# Show HN: Sub-millisecond VM sandboxes using CoW memory forking

- Score: 293 | [HN](https://news.ycombinator.com/item?id=47412569) | Link: https://github.com/adammiribyan/zeroboot

## TL;DR
Zeroboot is a Rust-based engine that forks Firecracker VM snapshots with mmap copy‑on‑write, giving ~0.8 ms spawn latency and ~265 KB per sandbox. Each fork is a real KVM VM with hardware isolation, exposed via HTTP plus Python/TypeScript SDKs, aimed at AI agents that need fast, untrusted code execution and speculative parallel runs. HN discussion praises the performance but flags RNG/ASLR and image‑update pitfalls, and notes Windows still lacks comparable sandbox tooling.

## Comment pulse
- Fast CoW VM forking raises entropy/ASLR issues → snapshot duplicates RNG state, needing RNDRESEEDCRNG and userspace PRNG reseeds to avoid security problems.  
- Windows sandboxing feels crude → lack of granular networking and GPU bugs push developers toward Linux tools or third‑party systems like Daytona offering Windows/macOS isolation.  
- CoW VMs suit tiny, trusted runtimes → but updating base images and wiring full agent stacks becomes complex—counterpoint: still a strong fit for many workloads.

## LLM perspective
- View: This pattern makes “VM per tool call” plausible, collapsing infra decisions into simple function‑style abstractions for agents.  
- Impact: Beneficial for any short‑lived, untrusted code execution—CI checks, education sandboxes, plugin ecosystems, multi‑tenant notebooks.  
- Watch next: Security audits on RNG, ASLR, side‑channels; transparent image‑update mechanisms; comparison benchmarks versus Wasm and lightweight containers.
