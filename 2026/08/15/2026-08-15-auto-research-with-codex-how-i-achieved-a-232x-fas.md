# Auto-research with codex: How I achieved a 232x Faster Kernel

- Score: 391 | [HN](https://news.ycombinator.com/item?id=49309549) | Link: https://sankalp.bearblog.dev/autoresearch/

### TL;DR

Using Codex in a two-week GPU Mode contest, the author made more than 1,500 submissions and cut a batched Householder QR benchmark from roughly 419,000 to 1,805 microseconds, placing 12th of 183. The workflow combined blocked WY QR, profiling, quantitative goals, persistent experiment logs, candidate beams, and periodic human steering. Comments broadly endorsed self-correcting benchmark loops for kernels and codecs, but warned leaderboard-specific specialization often breaks on unseen shapes, making expert oversight, broad tests, and appropriate abstractions decisive for production use.

### Comment pulse

- Tight correctness and performance feedback enables autonomous optimization → similar loops reportedly improved codecs, SIMD kernels, protobuf, ROM decompilation, and expression evaluation.
- Benchmark success can conceal overfitting → counterpoint: contest rules reward specialization, while libraries require out-of-distribution correctness and maintainability.
- GPU work suits agents → rich profiling counters and constrained primitives make changes unusually measurable, though high-leverage abstractions still matter.

### LLM perspective

- View: Auto-research excels where goals are numeric, verifiers are reliable, and experiments are cheap enough to repeat.
- Impact: Performance engineers shift toward harness design, profiling interpretation, candidate management, and defining acceptable generalization.
- Watch next: Test winning kernels on unseen shapes, compare maintenance costs, and quantify how much human steering each gain required.
