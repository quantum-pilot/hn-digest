# Show HN: Offline tiles and routing and geocoding in one Docker Compose stack

- Score: 71 | [HN](https://news.ycombinator.com/item?id=46478061) | Link: https://www.corviont.com/

### TL;DR

Corviont packages a MapLibre interface, PMTiles vector maps, Valhalla routing, and SQLite-based forward and reverse geocoding into an offline Docker stack, initially demonstrated with Monaco. It targets edge, fleet, offshore, and privacy-sensitive deployments, with regional bundles and an atomic local updater planned. HN feedback requests house-number search, self-service bounding-box builders, modular geocoder-only deployments, and hardware benchmarks. The creator says prebuilt artifacts simplify constrained devices, while storage and routing memory scale with region size and traffic.

### Comment pulse

- Prebuilt regional packs simplify edge deployment → devices serve artifacts instead of running expensive Nominatim or routing-data builds.
- Modularity matters → users want geocoder-only configurations to avoid unnecessary tile and routing storage.
- Dataset generation remains the product boundary → commenters request open builders while Corviont plans per-device regional licensing.

### LLM perspective

- View: Packaging, reproducible updates, and operational simplicity differentiate the stack more than its open-source components.
- Impact: Disconnected fleets could gain local location services without per-request APIs or leaking route queries.
- Watch next: Publish hardware benchmarks, regional build workflows, updater guarantees, house-number quality, and licensing details.
