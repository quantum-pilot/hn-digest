# Apple Silicon costs more than OpenRouter

- Score: 290 | [HN](https://news.ycombinator.com/item?id=48168198) | Link: https://www.williamangel.net/blog/2026/05/17/offline-llm-energy-use.html

- TL;DR  
  - The post computes the cost of running Gemma 4 31B on an M5 Max MacBook versus renting it via OpenRouter. Assuming a $4.3k laptop, 50–100 W power draw, and 10–40 tokens/s, local inference comes out around $0.40–$4.80 per million tokens—often slower and several times more expensive than hosted APIs, where the same model is ~$0.4/M tokens. HN discussion challenges the assumptions, emphasizes incremental device cost, privacy/control benefits of local models, and argues for hybrid local–cloud setups.

- Comment pulse  
  - Analysis overstates cost → assumes $4.3k laptop dedicated 24/7 to inference; real users own Macs and run models sporadically — counterpoint: lower utilization raises cost/token.  
  - Local models add value → you also get a general‑purpose laptop, offline use, privacy, censorship resistance, model stability and resale value absent from SaaS APIs.  
  - Cloud inference often wins on cost/speed → shared GPUs, high utilization, and newer hardware lower prices; local Qwen/DeepSeek favored more for privacy, control, and uptime.

- LLM perspective  
  - View: Cost‑per‑token math matters only if the laptop is primarily an inference box; otherwise incremental cost is what you should model.  
  - Impact: Hosted AI likely remains default for most devs; local shines for regulated data, offline workflows, and power users who tinker.  
  - Watch next: Track benchmarks of new Apple Silicon, GPUs, and open‑weights; compare lifetime TCO under realistic mixed‑use workloads instead of 24/7 scenarios.
