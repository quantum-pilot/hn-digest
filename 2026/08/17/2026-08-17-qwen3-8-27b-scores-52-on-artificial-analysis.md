# Qwen3.8 27B scores 52 on Artificial Analysis

- Score: 375 | [HN](https://news.ycombinator.com/item?id=49334544) | Link: https://artificialanalysis.ai/models/qwen3-8-27b

### TL;DR

Artificial Analysis scored Alibaba’s Apache-2 Qwen3.8 27B at 52 on its nine-evaluation Intelligence Index, first among 135 comparable small open-weight models and far above the class median of 9. The reasoning model accepts text, images, and video with roughly 256K context. API pricing was $0.425/M input and $3.10/M output, while the full evaluation cost $666.92. It generated 160 million tokens versus a 45-million median. Commenters found the local capability remarkable but disputed benchmark equivalence, citing extreme reasoning time, verbosity, quantization, harness, and setup sensitivity.

### Comment pulse

- Test-time scaling raises small-model scores → long traces trade scarce VRAM for latency and can make benchmark comparisons misleading.
- Real users reported persistent, creative agent behavior → counterpoint: multi-hour turns sometimes ignored interruptions or failed to converge.
- Quantization changes workflow behavior → Q4 reportedly needed more reasoning and recovery than Q8 despite similar final quality.

### LLM perspective

- View: The score demonstrates attainable capability, not parity across experience; efficiency and controllability remain separate dimensions.
- Impact: Consumer hardware can host strong agents, but operators must budget inference time and tune reasoning, quantization, and harnesses.
- Watch next: Compare fixed-token scores, Q4/Q8 artifacts, output speed, convergence rate, and independent workflow benchmarks.
