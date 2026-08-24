# MapLibre Tile: a modern and efficient vector tile format

- Score: 392 | [HN](https://news.ycombinator.com/item?id=46763864) | Link: https://maplibre.org/news/2026-01-23-mlt-release/

### TL;DR

MapLibre Tile is a new vector-tile format designed as an MVT successor for larger geospatial datasets and modern hardware. Its column-oriented layout and composable lightweight encodings promise up to sixfold compression on large tiles plus faster SIMD-friendly decoding. Current implementations target MVT feature parity, except columns cannot change value type per feature; future plans include elevation, GPU-oriented processing, linear referencing, and nested types. GL JS and Native already read it, but commenters’ early production-style tests showed nearer 10 percent archive savings, emphasizing workload-dependent tuning.

### Comment pulse

- Real gains depend on data and heuristics → each tile can choose encodings, trading compressed size against decoding speed and actual access patterns.
- Adoption has an initial path → Planetiler can generate the format from current main, while a development server converts existing MVT sources.
- PMTiles need not block migration → its container supports multiple tile types, and commenters cited a pending identifier update for the new format.

### LLM perspective

- View: This is an extensible performance foundation whose headline compression remains workload-specific.
- Impact: Map providers could cut latency, storage, and egress while preparing richer 2.5D data pipelines.
- Watch next: Planetiler release, production basemap benchmarks, PMTiles integration, decoder coverage, and GPU processing extensions.
