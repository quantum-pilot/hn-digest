# No, it doesn't cost Anthropic $5k per Claude Code user

- Score: 438 | [HN](https://news.ycombinator.com/item?id=47317132) | Link: https://martinalderson.com/posts/no-it-doesnt-cost-anthropic-5k-per-claude-code-user/

### TL;DR
Anthropic’s $200/month Claude Code Max plan is being misread: the oft-quoted “$5,000 in compute” per power user reflects *retail API value*, not Anthropic’s internal GPU cost. Using OpenRouter prices for similarly large open-weight MoE models (e.g., Qwen 3.5, Kimi K2.5) as a proxy, the author estimates actual inference cost at roughly 10% of Anthropic’s list price. That implies maybe ~$500/month in compute for extreme users and break-even or profit for typical ones, while training and R&D remain the real cost sink.

---

### Comment pulse
- Qwen/Kimi vs Opus comparison is flawed → Chinese/open models may be smaller, distilled, MoE, quantized; efficiency gap might be architecture, not margin—counterpoint: Bedrock t/s suggests similar active params.  
- Profitability hinges on training depreciation → even if inference is profitable per token, frequent billion‑dollar retrains can keep labs GAAP‑unprofitable for years.  
- “Selling tokens at a loss” is overgeneralized → inference-only cost likely covered, but full cost per token must include training, R&D, infra and loss-leader usage.

---

### LLM perspective
- View: Inference for frontier models is probably high-margin; public confusion stems from conflating API price, internal cost, and total-company burn.  
- Impact: Middlemen like Cursor face squeezed economics if they buy at retail; open-weight hosts set a de‑facto floor on perceived serving costs.  
- Watch next: Detailed cost disclosures, price cuts as competition intensifies, and whether labs slow training cadence to amortize model generations longer.
