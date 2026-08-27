# Kimi Linear: An Expressive, Efficient Attention Architecture

- Score: 208 | [HN](https://news.ycombinator.com/item?id=45766937) | Link: https://github.com/MoonshotAI/Kimi-Linear

### TL;DR

Moonshot AI presents Kimi Linear, a hybrid architecture mixing three Kimi Delta Attention layers with one global MLA layer. Its repository claims up to 75% smaller KV caches and roughly 6× faster decoding at one-million-token contexts, while maintaining competitive benchmark quality. It releases MIT-licensed kernels and 48B-parameter checkpoints with 3B active parameters, trained on 5.7T tokens. Commenters focus on whether efficiency reduces energy use or instead induces more demand, and recommend local execution when model-provider surveillance is a concern.

### Comment pulse

- Hybrid means selective full attention → one quarter of layers retain conventional quadratic attention while KDA handles the rest.
- Efficiency may not cut total energy → cheaper inference can unlock enough new demand to consume the savings.
- Privacy depends on deployment → commenters distrust both Chinese and American cloud providers and favor locally run models.

### LLM perspective

- View: The architecture’s strongest proposition is long-context economics; its quality claims still come from the project’s own benchmarks.
- Impact: Smaller caches could make million-token workloads practical on less memory, widening deployment options.
- Watch next: Seek independent quality, throughput, memory, and power measurements against full attention and MLA.
