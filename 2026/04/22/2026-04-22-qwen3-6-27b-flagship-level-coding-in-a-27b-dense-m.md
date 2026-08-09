# Qwen3.6-27B: Flagship-Level Coding in a 27B Dense Model

- Score: 629 | [HN](https://news.ycombinator.com/item?id=47863217) | Link: https://qwen.ai/blog?id=qwen3.6-27b

### TL;DR

Qwen released Qwen3.6-27B, an open-weight, dense, multimodal model with thinking and non-thinking modes. Qwen reports 77.2 on SWE-bench Verified, 53.5 on SWE-bench Pro, and 59.3 on Terminal-Bench 2.0, beating its 397B-total/17B-active predecessor while avoiding Mixture-of-Experts routing. Hacker News welcomed a capable local coding option, with quantized deployments fitting roughly 17–32 GB and reported generation from 5 to 30 tokens per second. Commenters cautioned that dense models activate all parameters, quantization changes quality, official benchmarks use different setups, and closed frontier models still feel more reliable.

### Comment pulse

- A 16.8 GB quant produced a strong visual test at 25.6 tokens per second — counterpoint: possible training contamination made that anecdote uncertain.
- Dense 27B can be smarter than 35B-A3B yet much slower on Macs because every parameter computes; dedicated GPUs fare better.
- Open weights improve freedom and price competition, but marginal coding reliability, provider trust, and support still justify frontier premiums for some teams.

### LLM perspective

- **View:** The headline is parameter efficiency, not consumer efficiency; dense simplicity trades routing for higher per-token compute than sparse MoE.
- **Impact:** Developers with 24–32 GB accelerators gain local agency but must benchmark their exact quantization, context, and agent scaffold.
- **Watch next:** Independent quantized evaluations, long-context stability, Model Studio availability, tool-call reliability, and reproducible hardware throughput.
