# Jamesob's guide to running SOTA LLMs locally

- Score: 256 | [HN](https://news.ycombinator.com/item?id=48775921) | Link: https://github.com/jamesob/local-llm

## TL;DR
A community guide claims you can approximate frontier models like Claude Opus locally by spending from a few thousand dollars up to ~$40k+ on multi‑GPU rigs, heavy quantization, and pruned SOTA models such as GLM‑5.2, Qwen, and DeepSeek. Commenters stress that these quantized/pruned variants diverge significantly from benchmarked originals on long, complex tasks, and that economics are tricky: local wins mainly for huge token volumes or strong privacy needs, while many users are better served by cloud GPUs or smaller local models.

*Content unavailable; summarizing from title/comments.*

## Comment pulse
- Quantized/pruned ≠ full models; long-context coding degrades noticeably; users want re-benchmarked local variants — counterpoint: SSD-offload keeps full precision if you accept huge latency.  
- Economics: $40k rigs vs $200/month plans; worthwhile only for massive token use or high enterprise pricing — counterpoint: rent cloud GPUs, avoid depreciation and maintenance.  
- Middle-ground: 128GB unified-memory Macs, dual 3090s, or single 24GB cards handle Qwen-sized models; GPUs give far better speed, bandwidth, and comfort than laptops.  

## LLM perspective
- View: Local SOTA is feasible but rarely cheap or clean; guides should separate 'toy', 'serious solo', and 'multi-user lab' tiers.  
- Impact: Heavy users, privacy-sensitive orgs, and researchers gain most; casual coders should likely mix small locals with cloud frontier models.  
- Watch next: Better quantization, long-horizon benchmarks, SSD-offload frameworks, and cost calculators comparing local rigs against changing API and cloud-GPU pricing.
