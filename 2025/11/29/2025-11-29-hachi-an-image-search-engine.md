# Hachi: An Image Search Engine

- Score: 117 | [HN](https://news.ycombinator.com/item?id=46087549) | Link: https://eagledot.xyz/hachi.md.html

### TL;DR

Hachi is a self-hosted image-search project that indexes metadata and semantic embeddings without duplicating original files. Queries can iteratively combine deterministic attributes with machine-learned concepts, while a face pipeline supports detection, clustering, and editable names. The author uses Python for orchestration and Nim/C for indexing and vector operations, with disk-backed shards controlling memory use. Tests reportedly reached 500,000 images, but large-scale production performance remains unproven, and the custom Nim machine-learning framework is not yet open source.

### Comment pulse

- Readers welcomed private personal-photo search but questioned embedding speed and one result the author said reflected misunderstood query semantics.
- The author says the Python side currently has only three dependencies; the Nim framework remains closed.

### LLM perspective

- View: Separating originals from a replaceable semantic index is the project’s strongest architectural choice.
- Impact: Useful search depends as much on editable metadata and failure correction as embedding quality.
- Watch next: Public code, reproducible benchmarks, and tests beyond curated datasets would establish practical readiness.
