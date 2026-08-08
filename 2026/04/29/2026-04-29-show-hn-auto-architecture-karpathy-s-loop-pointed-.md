# Show HN: Auto-Architecture: Karpathy's Loop, pointed at a CPU

- Score: 228 | [HN](https://news.ycombinator.com/item?id=47937380) | Link: https://github.com/FeSens/auto-arch-tournament/blob/main/docs/auto-arch-tournament-blog-post.md

### TL;DR

An autonomous propose–implement–measure loop optimized a five-stage RV32IM CPU in SystemVerilog: 73 hypotheses over 9h51m yielded 10 accepted changes, raising CoreMark from 301 to 577 iterations/second while reducing LUTs 40%. Formal checks, differential cosimulation, three-seed FPGA place-and-route, CRC validation, schemas, and path sandboxes rejected 63 broken or regressive attempts, supporting the author’s thesis that the verifier—not the agent loop—is the durable asset. Hacker News admired the result but debated whether the search is hill climbing or evolutionary, disliked the AI-written style, and awaited broader benchmarks for CoreMark overfitting.

### Comment pulse

- LLM suggestions add informed direction, but without populations and crossover many classified the method as hill climbing, not genetic optimization.
- Benchmark-specific predictors may inflate CoreMark gains; Embench will test whether accepted architecture changes generalize.
- Fitness functions attract exploitation, making domain experts’ formal invariants and independent measurements more valuable than clever planners.

### LLM perspective

- **View:** A reliable rejection pipeline can extract value even when most agent proposals are wrong.
- **Impact:** Teams with explicit correctness contracts can automate optimization; tacit knowledge remains the bottleneck.
- **Watch next:** Population-based search, Embench retention, multiple FPGA targets, reproducibility, model cost, and human-designed baseline comparisons.
