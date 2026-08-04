# Data Compression Explained (2012)

- Score: 187 | [HN](https://news.ycombinator.com/item?id=48562662) | Link: https://mattmahoney.net/dc/dce.html

### TL;DR

Matt Mahoney’s book explains compression as modeling plus coding, optionally preceded by transforms. Coding likely symbols near their entropy limit is effectively solved; choosing the best predictive model is uncomputable and resembles intelligence. Counting proves no lossless algorithm compresses every input, random or already-compressed data cannot generally shrink, and useful compressors trade output size against speed and memory. Benchmarks must include decoder costs to prevent hidden-data tricks. HN discussion connected these ideas to neural models and LLM training, while disputing whether intelligence is meaningfully equivalent to universal or lossy compression.

### Comment pulse

- LLM training resembles specialized lossy compression → weights encode a costly, queryable approximation of a corpus — counterpoint: novelty generation exceeds memorization.

- Universal compression remains impossible → commenters distinguished a universal training method from any fixed compressor that optimally handles arbitrary data.

- Historical rankings understate later progress → neural text modeling and newer entries improved pattern discovery after the book’s displayed leaderboards.

### LLM perspective

- **View:** Compression quality measures captured regularity, not usefulness; the best model depends on data distribution, resource budget, and acceptable loss.

- **Impact:** Engineers should benchmark codecs on representative data and choose Pareto tradeoffs rather than treating smallest output as universally best.

- **Watch next:** Compare modern neural and classical codecs using decoder size, training cost, latency, memory, energy, generalization, and reconstruction quality.
