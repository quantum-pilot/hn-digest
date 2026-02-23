# Show HN: Local-First Linux MicroVMs for macOS

- Score: 96 | [HN](https://news.ycombinator.com/item?id=47113567) | Link: https://shuru.run

- TL;DR  
Shuru is a Rust-based CLI that spins up ephemeral Linux microVMs on Apple Silicon macs using Virtualization.framework, aimed at safely running AI agent workloads and disposable dev environments. Each run starts clean; you can create named checkpoints that act like git commits for environments, with configurable CPU/RAM/disk, opt‑in networking, and vsock-based port forwarding. HN discussion compares it to Apple’s container project, debates “local‑first” as a buzzword, and asks about network allowlists and Windows equivalents.

- Comment pulse  
  - MicroVM + checkpoints vs Apple container → simpler scope than OCI-style containers; appealing for unified environments where only performance differs.  
  - “Local-first” meaning → everything runs on-device instead of cloud sandboxes—counterpoint: some see the term as empty marketing jargon.  
  - Security and portability questions → users want outbound-traffic allowlists when networking is enabled and ask for analogous Windows solutions beyond WSL.

- LLM perspective  
  - View: A clean CLI over Virtualization.framework lowers friction for safely shipping agent-powered desktop apps without bundling Docker or complex setup.  
  - Impact: Mac developers building code-executing agents, eval harnesses, and education tools gain reproducible, destroyable environments with minimal UX overhead.  
  - Watch next: benchmarks vs Docker/Apple container, network policy features (allowlists, logging), and cross-platform analogues using Windows Hyper-V or Linux KVM.
