# iPhone 17 Pro Demonstrated Running a 400B LLM

- Score: 449 | [HN](https://news.ycombinator.com/item?id=47490070) | Link: https://twitter.com/anemll/status/2035901335984611412

### TL;DR

A demo shows an iPhone 17 Pro generating from a nominal 400-billion-parameter model at about 0.6 tokens per second by streaming weights from SSD storage. HN commenters stress that the model is Qwen3.5-397B-A17B, a mixture-of-experts design activating roughly 17B parameters per token, so the headline overstates the active compute. They also flag unspecified quantization, 12GB device memory, storage wear, heat, and throttling as essential context. The result is technically striking, but not evidence of practical pocket-scale 400B inference.

### Comment pulse

- Apple’s earlier “LLM in a flash” approach prompted questions about SSD-to-GPU weight streaming and storage wear.
- An M2 iPad user reports capable local inference but rapid heating and throttling, making sustained tests essential.
- Parameter-count marketing drew criticism as hype — counterpoint: the demo still establishes storage-streaming feasibility.

### LLM perspective

- **View:** Report active parameters, bit width, memory traffic, and energy per token beside total model size.
- **Impact:** Local inference expands model choice, but interactive use remains constrained by latency and thermals.
- **Watch next:** Sustained throughput, battery drain, SSD writes, output quality, and dense-17B comparisons.
