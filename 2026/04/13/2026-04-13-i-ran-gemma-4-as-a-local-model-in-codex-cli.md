# I ran Gemma 4 as a local model in Codex CLI

- Score: 237 | [HN](https://news.ycombinator.com/item?id=47744255) | Link: https://blog.danielvaughan.com/i-ran-gemma-4-as-a-local-model-in-codex-cli-7fda754dc0d4

### TL;DR

Daniel Vaughan compared Gemma 4 local backends with GPT-5.4 on one Codex CLI coding task. A 24 GB M4 Pro’s quantized 26B MoE generated 52 tokens/second but needed 10 tool calls, five failed test writes, and left dead code; a 128 GB GB10’s 31B Dense managed 10 tokens/second yet finished cleanly in three calls. Both passed tests in 4m42s and 6m59s, versus the cloud model’s clean 65 seconds. Local coding is viable for privacy, cost, and resilience, but commenters agreed agentic reliability, context, quantization, and harness choice outweigh raw speed.

### Comment pulse

- Benchmark authors found 26B exceptional at one-shot coding but much weaker with tools, iterative refinement, large contexts, and non-coding decisions.
- Community setups varied: updated LM Studio fixed tool calls for some Macs, while smaller-memory and Xcode tests stalled or failed.
- Some disputed that local tool use was newly practical — counterpoint: aggressive Q4 quantization and harness overhead can sharply degrade reliability.

### LLM perspective

- **View:** Local agent economics depend more on successful tool cycles per task than tokens generated per second.
- **Impact:** Privacy-sensitive or high-volume iteration can move local, while complex changes still benefit from frontier-model escalation.
- **Watch next:** Repeated-task benchmarks, higher quantizations, smaller harness prompts, tool-call accuracy, energy cost, and hybrid routing that escalates stalled work.
