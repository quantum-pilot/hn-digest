# Show HN: Offline tiles and routing and geocoding in one Docker Compose stack

- Score: 71 | [HN](https://news.ycombinator.com/item?id=46478061) | Link: https://www.corviont.com/

### TL;DR
Corviont is a Docker Compose stack that bundles MapLibre, vector tiles (PMTiles), Valhalla routing, and a SQLite geocoder so maps, routing, and search run entirely offline. Instead of building tiles and indexes on each device, it ships prebuilt regional “packs” optimized for edge hardware and fleet deployment. HN discussion focuses on hardware needs, custom region generation, missing house-number search, the ability to run geocoder-only setups, routing hierarchies, and comparisons with similar self-hosted map stacks like Headway.

---

### Comment pulse
- Prebuilt regional packs → avoid painful OSRM/Nominatim builds on-device; main constraints become SSD space and RAM, with Valhalla chosen for lower memory use.  
- Custom data packs → requests for bbox-based builders and house-number lookup; author prefers shipping “known-good” packs but is open to bbox/admin-boundary workflows.  
- Modularity and ecosystem → interest in geocoder-only deployments and tile-based routing hierarchies; author notes Valhalla’s hierarchical tiles and differentiates from Headway via signed, automated regional updates.

---

### LLM perspective
- View: Productize the full offline stack so users skip GIS toolchains, focusing on integration rather than map data plumbing.  
- Impact: Most useful for fleets, industrial edge, remote sites, and privacy-sensitive orgs needing predictable, offline navigation and search.  
- Watch next: Concrete benchmarks by region size, updater reliability in the field, and whether world-scale geocoder-only packs become a supported option.
