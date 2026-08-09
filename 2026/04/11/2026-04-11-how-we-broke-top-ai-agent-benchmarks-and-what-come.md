# How We Broke Top AI Agent Benchmarks: And What Comes Next

- Score: 171 | [HN](https://news.ycombinator.com/item?id=47733217) | Link: https://rdi.berkeley.edu/blog/trustworthy-benchmarks-cont/

### TL;DR

Berkeley researchers built an exploit scanner that earned near-perfect scores across eight leading agent benchmarks without completing their tasks. Attacks included forcing SWE-bench tests to pass, trojanizing Terminal-Bench’s verifier dependencies, reading WebArena answers through local files, submitting arbitrary JSON to FieldWorkArena, downloading OSWorld gold artifacts, and injecting LLM judges. The common failures are shared agent/evaluator state, exposed answers, unsafe eval, weak matching, prompt-injectable judges, and broken scoring. They propose isolated evaluators, secret rotating tests, adversarial null/tampering agents, sanitized judges, and BenchJack as automated benchmark penetration testing.

### Comment pulse

- Skeptics asked whether manually designed exploits predict autonomous model behavior; proving spontaneous reward hacking would be more consequential.
- FieldWorkArena’s public validator may be unused, commenters noted, because its leaderboard does not show universal perfect scores.
- Others saw familiar benchmark gaming from CPUs and GPUs. — counterpoint: commercial incentives may favor impressive ad copy over methodological repair.

### LLM perspective

- **View:** Capability scores need a threat model; an agent with tools is also an adversary against its measurement system.
- **Impact:** Model buyers and safety teams should discount leaderboards lacking isolated, reproducible, independently audited evaluation pipelines.
- **Watch next:** BenchJack’s release, benchmark patches, rerun scores after hardening, and demonstrations of untuned agents discovering exploits.
