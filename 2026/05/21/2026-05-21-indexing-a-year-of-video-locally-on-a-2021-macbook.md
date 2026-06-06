# Indexing a year of video locally on a 2021 MacBook with Gemma4-31B (50GB swap)

- Score: 271 | [HN](https://news.ycombinator.com/item?id=48222733) | Link: https://blog.simbastack.com/indexed-a-year-of-video-locally/

- TL;DR  
  - An indie engineer with a safari lodge and years of unlabeled footage built a local-first video indexer on a 2021 M1 Max MacBook using Gemma 4 31B plus open-source tools. The pipeline extracts frames, GPS, transcripts, and face embeddings, then has a vision model write rich YAML+markdown sidecars per clip, making the archive English-queryable. HN discussion probed the practicality and tradeoffs of pushing large multimodal models onto consumer laptops today.

- Comment pulse  
  - Author published framedex as MIT-licensed code → commenters appreciate a concrete pipeline for personal media indexing and plan to adapt it for photos, editing agents.  
  - Heavy swapping worries some readers → 50GB swap may age SSDs and reflects running a 31B model plus extras — counterpoint: acceptable for indexing runs.  
  - Index design questions → author clarifies search is plain-text sidecars plus a faces database; EXIF+Nominatim and insightface handle locations and faces, not the LLM.

- LLM perspective  
  - View: Local-first, schema-heavy indexing pipelines will become standard for serious creators overwhelmed by unlabeled photos and video.  
  - Impact: Drives demand for efficient 20–40B local models, better media metadata tools, and OS-level support for sidecar-rich personal archives.  
  - Watch next: Off‑the‑shelf apps wrapping pipelines like framedex, robust face/voice handling policies, and benchmarks comparing local vs cloud multimodal indexing.
