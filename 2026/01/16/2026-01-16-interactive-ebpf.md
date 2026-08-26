# Interactive eBPF

- Score: 211 | [HN](https://news.ycombinator.com/item?id=46644181) | Link: https://ebpf.party/

### TL;DR

Interactive eBPF is a browser-based learning platform where users write, compile, and run programs through hands-on exercises. Its curriculum starts with process context and event data, then advances through syscall tracing, arrays, maps, multiple programs, cross-syscall state, network connection tracking, kernel probes, and TCP packet inspection. HN readers welcomed the approachable way to finally try eBPF and requested deployment material covering choices such as libbcc and CO-RE. A security thread flagged rootkit potential, while replies pointed to capabilities, the verifier, and runtime defenses.

### Comment pulse

- Readers praised the low-friction browser exercises as a welcoming path into a notoriously specialized kernel-programming topic.
- Requests centered on practical deployment lessons and a fuller book or PDF with complete examples.
- Security concerns focused on rootkits and attack surface → counterpoint: loading permissions, verifier work, and runtime hardening constrain abuse.

### LLM perspective

- View: Interactive execution makes eBPF concepts concrete without front-loading local toolchain setup.
- Impact: A guided path could broaden kernel observability skills beyond specialists.
- Watch next: Deployment exercises, richer examples, and explicit treatment of verifier limits and security boundaries.
