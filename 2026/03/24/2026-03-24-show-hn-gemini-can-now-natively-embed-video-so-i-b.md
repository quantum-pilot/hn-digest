# Show HN: Gemini can now natively embed video, so I built sub-second video search

- Score: 228 | [HN](https://news.ycombinator.com/item?id=47503617) | Link: https://github.com/ssrajadh/sentrysearch

### TL;DR

SentrySearch turns MP4 dashcam footage into searchable vectors using Gemini Embedding 2, which places video and text in the same 768-dimensional space without transcription or frame captions. It chunks overlapping windows, preprocesses them, skips likely-still footage, stores embeddings locally in ChromaDB, and returns a trimmed clip for natural-language queries in under a second after indexing. HN users immediately saw editing and personal-archive uses, but the dominant concern was scalable camera surveillance once cost, latency, and centralized access fall.

### Comment pulse

- A Premiere-style workflow could locate or remove scenes and produce an editable decision list rather than a final cut.
- Dashcam owners see obvious benefit in retrieving incidents without manually scrubbing recordings or removing storage media.
- Local open-weight models could keep footage private — counterpoint: cheap centralized systems enable pervasive, queryable surveillance.

### LLM perspective

- **View:** The core advance is cross-modal retrieval over moving imagery, not merely faster captions.
- **Impact:** Archivists, editors, drivers, and investigators gain search; bystanders lose practical obscurity.
- **Watch next:** Benchmark chunk-boundary recall, false still-frame skips, preview pricing, and local-model quality.
