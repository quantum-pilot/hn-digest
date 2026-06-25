# OpenAI unveils its first custom chip, built by Broadcom

- Score: 464 | [HN](https://news.ycombinator.com/item?id=48663324) | Link: https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/

- TL;DR  
  OpenAI’s first custom AI chip, co-designed with Broadcom and fabbed at TSMC, targets high-efficiency inference, echoing Google’s long-running TPU strategy. Marketing touts a nine‑month design cycle and “AI‑accelerated” workflow plus better performance per watt than GPUs, but technical details, benchmarks, and exact milestones are missing. Commenters debate how much LLMs can really speed RTL and verification, whether Broadcom’s IP and TSMC capacity are the real story, and if specialized silicon is premature amid rapid model churn.  

  *Content unavailable; summarizing from title/comments.*

- Comment pulse  
  - Widely skeptical of “AI-designed in 9 months” → LLMs can help HDL coding and verification, but timeline bragging without clear design/tapeout milestones feels marketing-driven.  
  - Broadcom seen as key partner → preexisting AI-SoC IP and, crucially, TSMC and HBM allocation, not just design talent, likely enabled OpenAI’s fast path.  
  - Custom inference ASICs promise efficiency gains → attractive since inference dominates cost, but fixed-function chips may age quickly as architectures evolve—counterpoint: fine once models stabilize.

- LLM perspective  
  - View: Vertical co-design of models, compilers, and silicon will matter more than raw TOPS; OpenAI now joins Google, Amazon, Meta here.  
  - Impact: If Jalapeño-like chips deliver perf-per-dollar, they strengthen OpenAI’s bargaining power with Nvidia and cloud vendors, pressuring GPU pricing and availability.  
  - Watch next: Watch for real benchmarks, software-stack maturity, and economics versus H100/B100 and post-Blackwell parts before calling this a win.
