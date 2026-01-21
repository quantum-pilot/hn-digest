# Nvidia Stock Crash Prediction

- Score: 328 | [HN](https://news.ycombinator.com/item?id=46693205) | Link: https://entropicthoughts.com/nvidia-stock-crash-prediction

## TL;DR
Using Nvidia options prices, the author infers a 3.1% daily volatility for far-out, 2026-dated $100 strike calls. They build a binomial price model, simulate paths, and (incorrectly) treat the risk‑neutral up/down parameter as a true probability, yielding a ~24% chance NVDA trades below $100 in 2026. Applying a Bank of England-style transformation from risk‑neutral to real‑world probabilities pulls this down to ~14%; eyeballing remaining uncertainties, the author settles on a ~10% crash probability.  

---

## Comment pulse
- Technical options-based forecast misses fundamentals → GPU boom tied to AI/datacenter capex, which can’t compound forever; demand cliffs or longer lifetimes could crush growth.  
- Concentrated revenues and cancellable orders → a single hyperscaler slowing purchases could sharply hit earnings—counterpoint: unmet demand from others likely backfills capacity.  
- Alternatives and bubbles → TPUs, custom ASICs, or a CUDA‑compatible Chinese GPU could erode Nvidia’s moat and puncture an AI-compute bubble that props up the stock.  

---

## LLM perspective
- View: Options markets encode consensus volatility, not a verdict on Nvidia’s business; translating that into real crash odds is model-dependent.  
- Impact: Forecasters and retail traders get a concrete framework to sanity-check “it can’t crash” narratives against what option prices imply.  
- Watch next: Track implied vol term-structure, hyperscaler capex guidance, non-Nvidia training runs (TPU/ASIC share), and any credible CUDA-compatible competitor announcements.
