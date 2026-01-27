# MapLibre Tile: a modern and efficient vector tile format

- Score: 392 | [HN](https://news.ycombinator.com/item?id=46763864) | Link: https://maplibre.org/news/2026-01-23-mlt-release/

### TL;DR
MapLibre Tile (MLT) is a new open vector tile format, designed as a modern successor to Mapbox Vector Tile for planet-scale basemaps. It uses a column-oriented layout with custom lightweight encodings to significantly improve compression and decoding speed, and is built to map cleanly onto modern CPU/GPU pipelines and future 3D/elevation use cases. MLT already works in MapLibre GL JS/Native, with conversion tooling and generators emerging, and HN commenters report early but promising real-world savings.

---

### Comment pulse
- Compression gains are real but modest so far → demo comparisons show smaller tiles, with devs noting much larger wins likely on complex, production schemas.  
- Ecosystem fit looks good → PMTiles is tile-format agnostic, already moving to tag MLT tiles; some existing pipelines (e.g., Tilemaker) need work.  
- Tooling is arriving quickly → Planetiler can already output MLT via a flag, with measurable archive shrink and more optimizations in progress.

---

### LLM perspective
- View: MLT sensibly modernizes a widely-used format without abandoning existing styling and rendering ecosystems.  
- Impact: Hosting costs, client performance, and 3D/elevation-heavy applications benefit first; tile-tool authors face the main migration work.  
- Watch next: independent benchmarks on large real-world basemaps, GPU-centric render pipelines, and whether major providers adopt MLT as a default.
