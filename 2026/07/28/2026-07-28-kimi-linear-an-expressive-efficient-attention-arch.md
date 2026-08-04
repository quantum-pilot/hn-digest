# Kimi Linear: An Expressive, Efficient Attention Architecture (2025)

- Score: 266 | [HN](https://news.ycombinator.com/item?id=49082022) | Link: https://arxiv.org/abs/2510.26692

### TL;DR

The Kimi Team presents a hybrid attention model combining Kimi Delta Attention, a finely gated finite-state linear module, with Multi-Head Latent Attention. Its 3B-active, 48B-total model reportedly beats full MLA under the same training recipe across short context, long context, and reinforcement-learning evaluations, while cutting KV-cache use by up to 75% and reaching 6× decoding throughput at one-million-token context. The team released kernels, vLLM support, and checkpoints; commenters praise the openness, debate scaling-driven intelligence and distillation, and point to newer architectural successors.

### Comment pulse

- Scaling may look emergent without being discontinuous → replies cite scaling laws, grokking, and general-purpose optimization rather than literal brute-force search.
- Architecture is already evolving → commenters say Kimi K3 builds on it, while one practitioner reports Gated DeltaNet 2 performs better internally.
- Original innovation and distillation can coexist → commenters reject a binary explanation of Kimi’s gains — counterpoint: training data may still be decisive.

### LLM perspective

- View: The strongest claim is not linear complexity alone, but superior quality under a controlled training comparison.
- Impact: Lower cache demand could make million-token inference practical on fewer accelerators, especially when many concurrent sessions share memory.
- Watch next: Independent reproductions should compare quality, latency, memory, training cost, and successor architectures across realistic hardware and workloads.
