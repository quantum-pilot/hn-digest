# Show HN: I built a real-time OSINT dashboard pulling 15 live global feeds

- Score: 147 | [HN](https://news.ycombinator.com/item?id=47300102) | Link: https://github.com/BigBodyCobain/Shadowbroker

### TL;DR

ShadowBroker is a self-hostable Next.js, MapLibre, and FastAPI dashboard unifying 15 public feeds for aircraft, vessels, satellites, earthquakes, conflict events, Ukraine's frontline, traffic cameras, GPS interference, markets, and regional dossiers. It offers Docker and packaged setup, requires several API keys, and labels carrier positions as estimates rather than operational intelligence. HN readers like the dense real-time map but note many similar dashboards, question whether AI-assisted projects will be maintained, and flag that an early release archive exposed frontend and backend environment files.

### Comment pulse

- Raw GeoJSON suits moving targets; vector tiles help historical scale, but constant cache invalidation complicates live entities.
- Aggregation creates usefulness and liability: upstream freshness, rate limits, attribution, and false precision matter more than a polished military aesthetic.
- Leaked environment files damage trust; release convenience needs automated secret scanning and key rotation.

### LLM perspective

- **View:** The value is cross-feed correlation; credibility depends on provenance, uncertainty, and operational hygiene.
- **Impact:** Researchers gain a rapid overview; maintainers inherit 15 upstream contracts, schemas, outages, and restrictions.
- **Watch next:** Secret revocation, source-health indicators, historical storage, uncertainty labels, contributors, and licensing.
