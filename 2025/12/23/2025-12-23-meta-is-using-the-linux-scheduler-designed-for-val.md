# Meta is using the Linux scheduler designed for Valve's Steam Deck on its servers

- Score: 240 | [HN](https://news.ycombinator.com/item?id=46366998) | Link: https://www.phoronix.com/news/Meta-SCX-LAVD-Steam-Deck-Server

### TL;DR

Meta engineers are adapting SCX-LAVD, a latency-aware scheduler developed by Igalia for Valve's Steam Deck, as a general fleet scheduler for large servers. Built with Linux `sched_ext`, it reportedly handles varied CPU and memory configurations while balancing work effectively across cache boundaries. HN readers celebrate open-source reuse from gaming to hyperscale infrastructure, but emphasize that the ecosystem is collaborative: Meta developed `sched_ext`, multiple companies share scheduler work, and Valve funds specialized contractors rather than producing every component internally.

### Comment pulse

- Gaming investment spills outward → Valve-funded work on frame pacing, graphics, and compatibility can improve general Linux infrastructure.
- Attribution is distributed → Igalia built SCX-LAVD for Valve atop Meta-originated `sched_ext` within a multi-company repository.
- Contracting concentrates expertise → specialist organizations let sponsors fund narrow upstream improvements without building permanent internal teams.

### LLM perspective

- View: Pluggable schedulers let workload-specific innovation cross hardware categories without waiting for one universal kernel policy.
- Impact: Meta may improve fleet defaults while handheld and desktop users benefit from the same shared experimentation framework.
- Watch next: Seek fleet-scale benchmarks covering latency tails, throughput, power, cache locality, and workload regressions.
