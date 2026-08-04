# Indexing a year of video locally on a 2021 MacBook with Gemma4-31B (50GB swap)

- Score: 271 | [HN](https://news.ycombinator.com/item?id=48222733) | Link: https://blog.simbastack.com/indexed-a-year-of-video-locally/

### TL;DR

A creator turned a year of unlabeled travel footage into an English-searchable local archive on a 2021 M1 Max. A 1,400-line Python pipeline extracts metadata, GPS, five frames, transcripts, and face embeddings, then asks quantized Gemma 4 31B to write structured Markdown sidecars beside each clip. The overnight run peaked at 50.89GB of swap. The central argument is that AI editors need an index first; HN welcomed the open-sourced tool but questioned excessive swapping and asked how its plain-text search, face clustering, and location metadata work.

### Comment pulse

- Open sourcing followed a sharing bug → the original local home-directory path was useless, prompting a quick MIT-licensed repository release.

- The 50GB swap figure suggests avoidable memory pressure → commenters blamed concurrent Electron apps and virtualization more than the 4-bit model itself.

- Deterministic tools handle identity and geography → InsightFace embeds faces and EXIF plus Nominatim resolves locations; the LLM describes scenes rather than guessing.

### LLM perspective

- **View:** Sidecars make AI enrichment durable: outputs remain portable, grep-able, inspectable, and useful after any model or indexer changes.

- **Impact:** Creators can search neglected archives privately and cheaply, reserving cloud models and human review for ambiguous clips and edits.

- **Watch next:** Benchmark retrieval quality, face-cluster accuracy, energy and SSD costs, editor integration, and whether indexed footage produces published reels.
