# RTX 5080 and RTX 3090 Setup: 80 Tok/s on Qwen 3.6 27B Q8

- Score: 287 | [HN](https://news.ycombinator.com/item?id=48515454) | Link: https://imil.net/blog/posts/2026/rtx-5080-+-rtx-3090-setup-80+-tok-s-on-qwen-3.6-27b-q8/

### TL;DR

A mixed RTX 5080/3090 Linux rig combines 16 GB and 24 GB of VRAM to run a Q8 Qwen 3.6 27B model with a 230k context at roughly 80–90 tokens/s. The recipe uses an X570 board bifurcated to PCIe 4.0 x8/x8, UEFI with Above 4G and ReBAR, Nvidia’s open driver, a dual-architecture llama.cpp build, tensor splitting, quantized KV cache, and MTP/ngram speculative decoding. HN praised the result but questioned sampling and speculation settings, requested baseline and parallel benchmarks, and noted that electricity can erase savings versus cloud inference.

### Comment pulse

- Local models suit bounded work → Qwen performs well with supplied context and fails transparently — counterpoint: frontier models reach ambitious goals faster.

- Reported speed needs decomposition → reviewers requested results without MTP/ngram, across parallel slots, and with recommended Qwen sampling and speculative-decoding parameters.

- Economics depend on location → reused GPUs offer large reusable context, but California electricity may make hosted inference cheaper.

### LLM perspective

- **View:** Headline throughput reflects the inference stack: speculative acceptance, quantization, memory placement, PCIe topology, context length, and workload shape matter.

- **Impact:** Home users can repurpose mismatched GPUs into workstation-class inference without replacing both cards, provided motherboard bifurcation and cooling cooperate.

- **Watch next:** Benchmark prefill, generation, multi-slot scaling, power, thermals, MTP acceptance, drivers, and model quality on fixed tasks.
