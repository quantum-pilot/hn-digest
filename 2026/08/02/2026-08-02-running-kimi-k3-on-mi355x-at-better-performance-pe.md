# Running Kimi K3 on MI355X at Better Performance per Dollar Than B300

- Score: 202 | [HN](https://news.ycombinator.com/item?id=49141073) | Link: https://www.wafer.ai/blog/kimi-k3-mi355x

### TL;DR

Wafer reports Kimi K3 at 952 aggregate tokens/s and 118 single-stream tokens/s on one eight-GPU MI355X node. B300 is faster—1,568 aggregate and 172 single-stream—but quoted rental rates make MI355X lead performance per dollar at 48 versus 33 aggregate tokens/s per dollar. Fixing ROCm speculative decoding and padding 12 attention heads to 16 for AITER improved decode and 172k-token prefill. HN challenged the comparison’s selected prices, missing power and ownership costs, reproducibility, and correctness after optimization; Wafer said hosted deployment passed accuracy, reasoning, coherence, and tool-use checks.

### Comment pulse

- The benchmark demonstrates one model/configuration’s economics — counterpoint: critics called current cloud rental prices an unstable substitute for reproducible total cost of ownership.
- MI355X’s 288GB memory lets K3 fit one node, avoiding B200’s cross-node all-reduce and turning capacity into a measurable deployment advantage.
- Readers questioned whether padding and AI-assisted optimization preserved model quality; Wafer cited platform-required task and behavior evaluations.

### LLM perspective

- View: Memory capacity can outweigh peak compute when model weights and long-context caches force competing hardware across node boundaries.
- Impact: Inference providers gain pricing leverage from AMD, but software maturity and validation effort remain part of hardware cost.
- Watch next: Publish code, exact versions, energy use, owned-hardware TCO, accuracy deltas, TTFT distributions, concurrency curves, and repeatable third-party runs.
