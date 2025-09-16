# Are OpenAI and Anthropic losing money on inference?

- Score: 515 | [HN](https://news.ycombinator.com/item?id=45050415) | Link: https://martinalderson.com/posts/are-openai-and-anthropic-really-losing-money-on-inference/

- TL;DR
    - The article claims inference is highly profitable: using a DeepSeek‑R1–style MoE on 72 H100s, input tokens are near‑free (~$0.003/M) while output costs ~$3/M, yielding big API margins and favoring input‑heavy, output‑light use cases (e.g., coding). HN pushback says the math is fundamentally wrong (prefill isn’t bandwidth‑bound; implied FLOPS exceed hardware; modern prefill/decode disaggregation ignored). Many still think inference can be profitable at high utilization, but margins hinge on training amortization. Lab leaders claim inference profitability; skeptics cite subsidies and mixed reporting.

- Comment pulse
    - Article’s math is off → prefill not bandwidth-bound; implied FLOPS exceed hardware; ignores prefill/decode disaggregation; published figures show ~$0.2/M output.
    - Inference can be profitable → lab modeling shows 50%+ margins with high utilization; leaders claim profitability—counterpoint: circular subsidies and reports suggest not yet.
    - Cheap inference exists → aggregators offer low-cost R1; self-hosting needs >20% utilization for savings; capex and idle GPUs kill economics for most.

- LLM perspective
    - View: Input/output cost asymmetry is real, but throughput depends on system design, attention compute, routing, and batching—not HBM alone.
    - Impact: Pricing will penalize long contexts and output-heavy tasks; input-heavy workflows like code-reading stay cheap and favored in product design.
    - Watch next: Hard numbers: MFU-verified per-token costs on H100/H200/B200; utilization disclosures; accounting of training amortization; provider price cuts and capacity auctions.
