# Kimi K2 1T model runs on 2 512GB M3 Ultras

- Score: 198 | [HN](https://news.ycombinator.com/item?id=46262734) | Link: https://twitter.com/awnihannun/status/1943723599971443134

### TL;DR

A 4-bit quantization of Moonshot’s trillion-parameter model reportedly runs across two Mac Studio systems, each configured with 512GB of M3 Ultra unified memory, using mlx-lm and mx.distributed. The supplied post calls performance usable but provides no throughput, context length, or prefill measurements. HN discussion concentrated less on inference architecture than on model character: users praised direct, non-obsequious editing and short-form communication, while questioning whether pushback reflects better reasoning or missing context. Others flagged roughly five-figure hardware cost per machine and asked about Linux or ordinary 10Gb-network alternatives.

### Comment pulse

- Writers valued the model’s blunt tone, social inference, and concise prose, calling it unusually effective for email drafting and editing.
- Skeptics asked whether confident correction is useful when missing context can make pushback wrong — counterpoint: users trusted its willingness to disagree.
- Hardware discussion contrasted $9,499 retail and lower refurbished pricing while asking whether standard Linux GPUs and 10Gb networking could reproduce distribution.

### LLM perspective

- View: The demonstration establishes memory fit and distributed execution, not interactive performance across realistic prompts and contexts.
- Impact: High-memory Macs offer local experimentation with enormous quantized models, but the two-machine capital cost narrows accessibility.
- Watch next: Tokens per second, prefill latency, context scaling, interconnect utilization, power draw, and reproducible Linux benchmarks.
