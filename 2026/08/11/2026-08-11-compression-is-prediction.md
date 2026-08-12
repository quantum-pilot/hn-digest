# Compression is prediction

- Score: 529 | [HN](https://news.ycombinator.com/item?id=49263497) | Link: https://ngrok.com/blog/compression-is-prediction

### TL;DR

Modern lossless compression separates preprocessing transforms, a probability model, and an entropy coder. Arithmetic coding assigns fewer bits to likely symbols; stronger contextual models make the next symbol more predictable and lower entropy, the theoretical bits-per-symbol floor. LLMs likewise output next-token probabilities and are trained to minimize cross-entropy, so their distributions can drive a compressor and outperform simple context models. In practice, multi-gigabyte models and heavy computation make them absurd for ordinary payloads, where gzip or Brotli trade some ratio for speed and tiny decoders.

### Comment pulse

- Many welcomed the visual explanations — counterpoint: critics said the equivalence is longstanding information theory and deserved stronger historical framing.
- Some disputed the slogan’s reverse direction because whole-input transforms can exploit future data without sequential prediction.
- A JavaScript-dependent article about compression was criticized for hiding already-delivered text instead of serving basic readable HTML.

### LLM perspective

- **View:** Compression ratio measures predictive calibration only after accounting for model, format, and compute overhead.
- **Impact:** Better predictors matter most where datasets amortize model distribution and inference costs.
- **Watch next:** End-to-end benchmarks reporting compressed size, model bytes, encode time, energy, and decoder requirements.
