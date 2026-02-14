# IronClaw: a Rust-based clawd that runs tools in isolated WASM sandboxes

- Score: 137 | [HN](https://news.ycombinator.com/item?id=47004312) | Link: https://github.com/nearai/ironclaw

### TL;DR
IronClaw is a Rust reimplementation of OpenClaw that runs LLM tools and channels as WebAssembly components plus long‑running “sandbox jobs” in containers. It focuses on privacy and security: untrusted tools are isolated from the host, HTTP access is allow‑listed, secrets are brokered and never exposed to the model, and the sandbox/orchestrator are hardened against path traversal and auth bypass. It adds a full web UI, routines/scheduling, and many scoped SaaS integrations. HN discussion centers on whether such sandboxes meaningfully improve real security.

### Comment pulse
- Skepticism about “vibe-coded” agent security → unclear threat model; with webfetch+codeexec, sandboxes seem pointless. — counterpoint: fans argue WASM isolation and secret-brokering shrink blast radius.  
- Debate on sandbox granularity → some say VMs suffice; others want per-capability sandboxes (calendar vs bank vs internet) plus policy to control composed actions.  
- Broader need beyond sandboxes → commenters call for capability-gated runtimes, human review, orchestration systems, formal analysis and audits to prove security claims.  

### LLM perspective
- View: IronClaw pushes toward practical, layered defenses: WASM isolation, careful secret handling, scoped tools, hardened orchestration.  
- Impact: Most relevant for organizations wiring LLMs into real SaaS accounts; less meaningful for adversarial web code-execution scenarios.  
- Watch next: explicit threat model documentation, red-team reports, benchmarked exploit demos, and comparisons versus VM-only or broker-only architectures.
