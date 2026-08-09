# GLM-5.1: Towards Long-Horizon Tasks

- Score: 392 | [HN](https://news.ycombinator.com/item?id=47677853) | Link: https://z.ai/blog/glm-5.1

### TL;DR

Z.ai released GLM-5.1 as an MIT-licensed, 754-billion-parameter model focused on long-horizon agentic engineering. Vendor tests report 58.4% on SWE-Bench Pro, 21,500 QPS after 655 vector-database iterations, and 3.6× KernelBench Level 3 speedup, behind Claude Opus 4.6’s 4.2× there. An eight-hour self-review loop also built a browser-based Linux desktop. The claim is sustained improvement over thousands of tool calls, not merely stronger first attempts. HN users praised its code output but reported slowness and instability beyond roughly 100,000 context tokens.

### Comment pulse

- Open weights impressed users as a credible fallback to frontier closed models.
- Local inference remains impractical for most: one four-bit quantization is 361 GB and SSD offload would crawl.
- Users manage long sessions with frequent compaction — counterpoint: vendor examples emphasize productive horizons exceeding 200,000 tokens.

### LLM perspective

- **View:** The standout contribution is persistence under iterative feedback, though all marquee results are self-reported.
- **Impact:** Agent developers can trade more runtime and tool calls for better optimization on measurable tasks.
- **Watch next:** Independent reproductions, long-context failure rates, inference cost, and self-evaluation quality on subjective tasks.
