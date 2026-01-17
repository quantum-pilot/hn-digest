# Interactive eBPF

- Score: 211 | [HN](https://news.ycombinator.com/item?id=46644181) | Link: https://ebpf.party/

### TL;DR
An in-browser tutorial platform, eBPF.party lets you write, compile, and run eBPF programs without local setup. Structured chapters cover process context, reading syscalls, stateful maps, cross-syscall tracking, network connections, and kernel probes, all via guided exercises. Hacker News readers welcome the low-friction, hands-on learning model, ask for deployment-focused lessons and a book of examples, and briefly debate eBPF’s security risks versus protections like the evolving verifier and stricter capabilities such as cap_bpf.

---

### Comment pulse
- Hands-on browser exercises remove eBPF’s steep setup cost → people can finally “just try it” without configuring kernels, toolchains, or permissions.  
- Learners want next-stage material → requests for deployment lessons (libbcc vs CO-RE) and even a paid PDF/book with full source examples.  
- eBPF expands kernel attack surface → rootkits can hide in hooks—counterpoint: verifier improvements and cap_bpf aim to restrict malicious or side-channel programs.

---

### LLM perspective
- View: Browser-based labs demystify kernel tech, similar to how REPLs transformed language learning and sandboxes simplified web development.  
- Impact: Easier eBPF experimentation could broaden its use beyond observability into security monitoring, anomaly detection, and fine-grained performance tuning.  
- Watch next: Advanced chapters on production deployment, safety patterns, and comparisons with alternatives like kprobes, perf, or traditional modules.
