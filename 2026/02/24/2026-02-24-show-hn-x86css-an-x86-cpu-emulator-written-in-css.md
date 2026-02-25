# Show HN: X86CSS – An x86 CPU emulator written in CSS

- Score: 255 | [HN](https://news.ycombinator.com/item?id=47132102) | Link: https://lyra.horse/x86css/

### TL;DR
x86CSS is a fully working 16‑bit x86 CPU emulator implemented purely in modern CSS, executing GCC‑compiled 8086 binaries in the browser without JavaScript. It abuses container/style queries, animations, if() and @function constructs to create memory, a clock and an instruction decoder, exposing simple I/O so users can compile and run their own C or assembly. HN is impressed but split: some celebrate it as creative systems art, others see it as evidence CSS is over‑engineered and a growing security surface.

### Comment pulse
- CSS has long had Turing‑complete demos; this one removes hovering/clicking as the “clock,” strengthening claims that CSS alone can run autonomous programs.  
- Some argue CSS is now “JavaScript 2” and needlessly complex; others note Turing‑completeness often emerges accidentally in rule systems. — counterpoint: enlarges browser attack surface.  
- Security‑minded readers link prior CSS‑related CVEs, warning that ever‑richer CSS features plus JS‑less computation could enable stealthy abuse like cryptominers or tracking.  

### LLM perspective
- View: This is best seen as demoscene‑style systems art, stress‑testing CSS’s design rather than a practical programming approach.  
- Impact: Browser vendors may treat such experiments as fuzzers, revealing edge‑case bugs in CSS parsing, layout, and animation engines.  
- Watch next: Benchmarks of instruction throughput, portability to Firefox/WebKit, and constrained sandboxes mitigating CSS‑driven side channels or resource exhaustion.
