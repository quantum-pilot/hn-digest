# DeepSeek V4 Pro beats GPT-5.5 Pro on precision

- Score: 388 | [HN](https://news.ycombinator.com/item?id=48440448) | Link: https://runtimewire.com/article/deepseek-v4-pro-beats-gpt-5-5-pro-on-precision

### TL;DR

RuntimeWire scored four newly generated text tasks with Grok 4.1 Fast as judge. DeepSeek V4 Pro beat GPT-5.5 Pro 38–33, winning log-redaction, constrained-writing, and schema-matching; both tied on JSON cleanup. The claimed advantage was literal instruction following rather than broad intelligence. HN rejected the sample as too small and arbitrary for a model ranking, though users said it still signals competitive capability. The stronger practical case was economics: commenters reported DeepSeek costing tens to hundreds of times less, while frontier models remained somewhat more consistent on difficult work.

### Comment pulse

- Four prompts cannot establish superiority → one model-as-judge run lacks repetition, uncertainty estimates, task diversity, and independent human scoring.
- Harness quality may dominate small model gaps → domain exposure and verification can make cheaper models sufficient — counterpoint: difficult edge cases still reward consistency.
- Cost changes the optimal workflow → cheap inference enables repetition, cross-checking, and ensemble judging that may outperform one expensive pass.

### LLM perspective

- **View:** Precision is workload-specific: schema fidelity, regex correctness, and tendency to add extras should be measured separately.
- **Impact:** Teams should route routine constrained work to cheaper models and reserve premium inference for uncertain or high-consequence cases.
- **Watch next:** Repeat blinded trials across seeds, judges, domains, latency, and cost; publish outputs, rubrics, variance, and human adjudication.
