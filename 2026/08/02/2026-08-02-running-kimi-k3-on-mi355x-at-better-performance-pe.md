# Running Kimi K3 on MI355X at Better Performance per Dollar Than B300

- Score: 202 | [HN](https://news.ycombinator.com/item?id=49141073) | Link: https://www.wafer.ai/blog/kimi-k3-mi355x

- TL;DR  
  - Wafer claims AMD’s MI355X serves the Kimi K3 model at better performance-per-dollar than Nvidia B300s, largely due to cheaper cloud rental pricing. HN commenters argue the benchmark is marketing, not neutral science: B300s are faster, power/TCO and MSRP are ignored, code isn’t shared, and Wafer has a shaky reputation. Others probe whether kernel tweaks preserve model correctness and note the broader significance: if MI355X is truly cheaper and good enough, it pressures Nvidia’s dominance.

*Content unavailable; summarizing from title/comments.*

- Comment pulse  
  - Benchmark is an ad → B300 is faster; MI355X only “wins” by picking low rental prices, omitting power/TCO and reproducibility—counterpoint: even ads matter if they move billions in spend.  
  - Correctness worries → head-count padding optimization may risk incoherent outputs; AI-assisted setups have broken models before—Wafer staff say OpenRouter requires passing accuracy/coherency tests.  
  - Pricing and access skepticism → quoted ~$2.5–2.95/hr for MI355X seems unsustainably low vs capex and market; unclear subsidies, opaque TCO, and MI355X is hard to buy directly.

- LLM perspective  
  - View: Treat any vendor-led perf/$ comparison as marketing; demand open configs, repeatable scripts, and independent replication.  
  - Impact: Small teams chasing cheap GPUs risk overfitting infra choices to transient rental prices instead of long-term TCO and reliability.  
  - Watch next: Third-party MI355X vs B200/B300 benchmarks, power-per-token data, and OpenRouter latency/quality stats for Kimi K3 across different GPU backends.
