# Sampling at negative temperature

- Score: 98 | [HN](https://news.ycombinator.com/item?id=46579374) | Link: https://cavendishlabs.org/blog/negative-temperature/

### TL;DR
The post connects statistical-mechanics temperature to the softmax in language models, then explores “negative temperature” sampling by hacking LLaMA so logits are divided by a small negative value. This inverts the probability distribution, making the least likely tokens the most likely. The result is extremely strange, repetitive text dominated by “anomalous” tokens like Хронологија and entferne, which lie near the embedding centroid and the model barely understands. HN discussion probes links to perplexity, human “average temperature,” and where the physics analogy breaks down.

---

### Comment pulse
- Negative temperature ≈ picking least likely tokens → outputs “worse than random” and dominated by centroid tokens with no clear semantics—counterpoint: it may mostly expose numerical noise.
- People speculate about “average temperature” as a metric; author notes perplexity = exp(entropy) and estimates human text behaves like T≈1.7, not constant-temperature anyway.
- Physicists clarify: model temperature is just softmax scaling; thermodynamic negative temperatures exist in bounded systems (e.g., spin lattices), but don’t map cleanly to molecular-dynamics temperature.

---

### LLM perspective
- View: Negative-temperature sampling is a diagnostic tool, surfacing embedding-space anomalies and tokens the model systematically mishandles.
- Impact: Useful for probing safety, robustness, and tokenization bugs; not promising for better generation or training data.
- Watch next: Map anomalous/centroid tokens across architectures; test extreme-temperature decoding for failure modes and adversarial prompt design.
