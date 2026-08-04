# Real-time LLM Inference on Standard GPUs: 3k tokens/s per request

- Score: 194 | [HN](https://news.ycombinator.com/item?id=48321076) | Link: https://blog.kog.ai/real-time-llm-inference-on-standard-gpus-3-000-tokens-s-per-request/

### TL;DR

Kog’s tech preview reaches 3,000 output tokens/s per request on eight AMD MI300X GPUs and 2,100 on eight Nvidia H200s, using a 2B FP16 model at batch size one without speculative decoding. A persistent monokernel, GPU-resident control, custom collectives, and Laneformer architecture attack memory-bandwidth limits and microsecond overheads, aiming to shorten sequential agent loops. Kog projects the approach onto large third-party MoEs. HN praised the systems work but questioned comparisons with frontier models, the “standard GPU” label, and whether architectural optimizations require retraining.

### Comment pulse

- The benchmark is not representative yet → a custom 2B model cannot establish comparable speed on useful 30B-plus or frontier models.
- DTP limits portability → its architectural changes appear to require retraining — counterpoint: Kog says monokernels and custom collectives can accelerate third-party MoEs.
- “Standard GPUs” implies broader accessibility → eight H200s or MI300Xs are conventional datacenter hardware, not consumer-grade equipment.

### LLM perspective

- **View:** Evaluating speed requires latency, cost, and quality together; tokens per second alone rewards small models and full-node allocation.
- **Impact:** Latency-sensitive agents could iterate faster, but dedicating eight GPUs to batch-one decoding may sacrifice fleet utilization.
- **Watch next:** Independent third-party-MoE benchmarks should report prompt length, output length, quality, batching, power, and total cost.
