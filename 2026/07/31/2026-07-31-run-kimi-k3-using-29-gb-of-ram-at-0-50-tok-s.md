# Run Kimi K3 using 29 GB of RAM at 0.50 tok/s

- Score: 132 | [HN](https://news.ycombinator.com/item?id=49123386) | Link: https://github.com/sqliteai/waste

## TL;DR
An open-source project claims to run Kimi K3 on a Mac with 29GB RAM at 0.5 tokens/s, likely via extreme quantization and SSD streaming. HN commenters doubt the technical plausibility, noting K3’s parameter size makes the memory and performance numbers inconsistent, and the README appears largely LLM-written and confusing. Others criticize unedited LLM-generated documentation and code, argue that energy cost and efficiency are far worse than GPU serving, and frame the project more as an entertaining proof-of-concept than a practical deployment path.

*Content unavailable; summarizing from title/comments.*

## Comment pulse
- Core claim looks impossible → K3’s known size vs 29GB; README is self-contradictory and LLM-ish — counterpoint: extreme 3‑bit quantization might partly explain.  
- LLM-written docs hurt usability → text assumes private context, uses opaque internal jargon, and authors seemingly didn’t reread or edit generated explanations.  
- Local inference is very inefficient → ~0.5 tok/s at ~40W gives ~50 tok/Wh, versus ~80k tok/Wh on GPU clusters, implying ~1000× higher energy per token.  

## LLM perspective
- View: Interesting as an exploration of consumer hardware limits, but claims need independent benchmarking, clear math, and reproducible configs.  
- Impact: If validated, could inspire lightweight sparse/quantized deployments at edge; if not, may erode trust in self-reported LLM projects.  
- Watch next: third-party tests of throughput, RAM, SSD wear; comparisons against existing K3 servers and other disk-streaming inference stacks.
