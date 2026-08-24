# Hachi: An Image Search Engine

- Score: 117 | [HN](https://news.ycombinator.com/item?id=46087549) | Link: https://eagledot.xyz/hachi.md.html

### TL;DR

Hachi is designed as a self-hosted image search system that indexes metadata and machine-learning embeddings without copying original files, even when data spans devices or remote storage. Its Python backend pairs a custom Nim metadata engine with disk-sharded vector search, face clustering, and a browser interface for recursively refining mixed semantic and deterministic attributes. The developer reports tests on 180 GB of Pexels images and 500,000 Flickr images. Constraints include a placeholder CLIP model, x64-only testing, unfinished ARM support, and a closed-source inference framework.

### Comment pulse

- Local embeddings remain replaceable → the author treats CLIP as a placeholder and prioritizes fusing semantic results with user-controlled metadata.
- Minimal dependencies improve hackability → custom databases and inference code also create maintenance debt and narrower hardware support — counterpoint: measured prototypes already scale.
- Personal search remains underserved → commenters want one private index spanning photos, browsing, notes, recordings, and repositories.

### LLM perspective

- View: A private search index becomes valuable when users can refine partial memories across semantic and factual attributes.
- Impact: Avoiding source duplication reduces storage churn, while exposed attributes give users more control over ambiguous retrieval.
- Watch next: Open sourcing the inference layer and publishing million-image latency benchmarks would test portability and scalability claims.
