# Are OpenAI and Anthropic losing money on inference?

- Score: 515 | [HN](https://news.ycombinator.com/item?id=45050415) | Link: https://martinalderson.com/posts/are-openai-and-anthropic-really-losing-money-on-inference/

- TL;DR
    - The post claims inference isn’t a money sink: MoE models plus cheap H100 hours make input tokens nearly free, with output driving costs—yielding high margins for consumer/dev plans and APIs, except for long-context and video. HN pushback: the throughput math is flawed (prefill not bandwidth‑bound; MFU exceeds hardware peak), and decoding can be much cheaper than stated. Whether OpenAI/Anthropic “lose money” hinges on utilization and training amortization; leaders say inference is profitable, but accounting and subsidy loops muddy the picture.

- Comment pulse
    - Article’s math challenged → prefill isn’t bandwidth-bound; implied 13 PF/s exceeds hardware peak; modern EP/disaggregated setups matter; decoding can cost ~$0.2/M output.
    - Margins depend on utilization and training amortization → idle capacity and depreciation bite; some argue training belongs in COGS — counterpoint: labs say inference profitable.
    - Market reality check → if it’s cheap, where are low prices? Some exist via aggregators; self-hosting suffers from latency targets and low average utilization.

- LLM perspective
    - View: Input/output asymmetry matters, but the blog’s throughput math is flawed; margins hinge on utilization, scheduling, and capital structure.
    - Impact: Labs at scale can profit on inference; smaller hosts face spike-driven underutilization and higher effective costs.
    - Watch next: Transparent MFU/utilization benchmarks, long-context pricing changes, and disclosures on training capitalization vs COGS in public filings.
