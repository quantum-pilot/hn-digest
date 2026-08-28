# Are OpenAI and Anthropic losing money on inference?

- Score: 515 | [HN](https://news.ycombinator.com/item?id=45050415) | Link: https://martinalderson.com/posts/are-openai-and-anthropic-really-losing-money-on-inference/

### TL;DR

Martin Alderson uses napkin math on a hypothetical 72-H100 cluster running a DeepSeek-R1-like model to argue that inference can carry software-like margins. He estimates input processing near fractions of a cent per million tokens, output around $3, and consumer or coding subscriptions costing far less to serve than their prices. The analysis deliberately excludes training and most non-compute costs. Commenters identify a fundamental problem: its claimed prefill throughput implies roughly seven times the hardware’s peak compute, invalidating the bandwidth-bound calculation and making the resulting margins unreliable.

### Comment pulse

- Alternative models in discussion still suggested positive inference margins, heavily dependent on utilization, depreciation, architecture, and operating scale.
- Readers disputed whether training belongs in gross margin, while company leaders’ reported inference-profitability claims also drew skepticism.

### LLM perspective

- View: The article asks the right cost-structure question but cannot support its answer with physically inconsistent throughput.
- Impact: Cheap serving is plausible without proving that frontier-model businesses are profitable after training and infrastructure.
- Watch next: Auditable utilization, prefill/decode benchmarks, depreciation, training amortization, and provider financials are needed.
