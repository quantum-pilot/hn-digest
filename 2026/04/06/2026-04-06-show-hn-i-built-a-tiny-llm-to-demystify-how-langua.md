# Show HN: I built a tiny LLM to demystify how language models work

- Score: 837 | [HN](https://news.ycombinator.com/item?id=47655408) | Link: https://github.com/arman-bd/guppylm

### TL;DR

GuppyLM is an intentionally tiny, 8.7-million-parameter transformer designed to make language-model training inspectable. A single Colab notebook covers synthetic data, a 4,096-token BPE vocabulary, six-layer vanilla architecture, training, and inference in about five minutes on a T4 GPU. Its 60,000 template-composed examples teach a cheerful fish persona across 60 topics; a quantized 10 MB ONNX build runs locally in browsers. Simplicity drives explicit tradeoffs: 128-token context, single-turn chats, baked-in personality, learned positions, ReLU feed-forward layers, and no modern architectural embellishments.

### Comment pulse

- Readers liked its educational potential but wanted documentation explaining attention, feed-forward networks, normalization, and positional embeddings for newcomers.
- Comparisons with microgpt, minGPT, and an interactive layer visualizer surfaced — counterpoint: some felt benchmarking misses the project’s playful purpose.
- Uppercase prompts expose a tokenizer gap caused by lowercase-only training, although Guppy’s personality still appears in the response.

### LLM perspective

- **View:** Its constrained character makes the training-data-to-behavior relationship unusually visible without pretending to model general intelligence.
- **Impact:** Students can modify a complete pipeline cheaply, learning which architectural choices matter before confronting production-scale complexity.
- **Watch next:** Explanatory annotations, tokenizer casing support, controlled architecture experiments, evaluation metrics, and contributions extending the browser interface.
