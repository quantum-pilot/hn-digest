# MiMo-v2.5-Pro-UltraSpeed: 1T model with 1000 tokens per second

- Score: 474 | [HN](https://news.ycombinator.com/item?id=48446639) | Link: https://mimo.xiaomi.com/blog/mimo-tilert-1000tps

### TL;DR

Xiaomi and TileRT report over 1,000 decoded tokens/second from 1-trillion-parameter MiMo V2.5 Pro on one eight-GPU commodity node. The design selectively quantizes MoE experts to FP4, uses DFlash masked-block speculative decoding, and runs custom persistent kernels with warp specialization; coding accepts 6.3 of eight drafted tokens on average. UltraSpeed costs three times the regular API for roughly tenfold generation speed, but access is application-only from June 9–23. FP4/DFlash weights are open. HN saw near-instant agent loops as transformative but worried faster output could outrun human judgment.

### Comment pulse

- Latency changes interaction quality → instant responses eliminate task-switching and enable many small validation passes instead of long, parallel agent runs.
- Fast mistakes compound faster → agents can make massive edits before intervention — counterpoint: small commits, narrow privileges, and immediate tests constrain damage.
- Decode speed moves the bottleneck → compilation, testing, human review, and output verification must keep pace with generation.

### LLM perspective

- **View:** Throughput is useful only when accepted speculative tokens preserve quality and the workflow can validate them at matching speed.
- **Impact:** Agent builders can trade threefold API cost for tenfold decode speed, favoring interactive coding, search, and multi-path verification.
- **Watch next:** Reproduce throughput across contexts, concurrency, hardware, and tasks; report first-token latency, quality, energy, cost, and post-trial availability.
