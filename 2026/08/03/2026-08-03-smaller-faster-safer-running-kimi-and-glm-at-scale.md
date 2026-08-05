# Smaller, faster, safer: running Kimi and GLM at scale

- Score: 264 | [HN](https://news.ycombinator.com/item?id=49158581) | Link: https://blog.cloudflare.com/smaller-faster-safer-models/

### TL;DR

Cloudflare describes three SGLang optimizations for serving large MoE models. FP8 KV caches double Kimi K2.6 context capacity to about 1.37 million tokens and permit 64 concurrent requests, raising peak throughput 41% despite slightly slower kernels. INT4 weights shrink GLM 5.2 from 705 GB to 421 GB and accelerate decode up to 55%, while FP8 remains faster for compute-bound prefill. Tagged cache pages abort mismatched requests with under 1% overhead. HN welcomed transparency but questioned claims of indistinguishable quality, limited model coverage, missing coding tests, privacy, and pricing visibility.

### Comment pulse

- Capacity gains are not free accuracy proof → aggregate benchmarks may miss small token shifts that compound during long coding or tool tasks.
- Phase separation avoids one compromise → BF16/FP8 favors prefill, while INT4 and FP8 cache formats favor memory-bound decode.
- Trust extends beyond kernels → readers debated zero-data-retention claims and disliked pricing hidden behind the dashboard.

### LLM perspective

- View: Disaggregated serving turns quantization into a phase-specific scheduling decision rather than one global model format.
- Impact: Providers serve more long-context sessions per GPU; users receive lower costs but need explicit quality and retention disclosures.
- Watch next: Coding-agent evaluations, cross-family sensitivity, NVFP4 on Blackwell, universal integrity checks, and public pricing.
