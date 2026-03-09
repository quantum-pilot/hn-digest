# Show HN: I built a real-time OSINT dashboard pulling 15 live global feeds

- Score: 147 | [HN](https://news.ycombinator.com/item?id=47300102) | Link: https://github.com/BigBodyCobain/Shadowbroker

### TL;DR
ShadowBroker is an open-source, real-time geospatial intelligence dashboard unifying ~15 OSINT feeds—commercial/private/military flights, ships, satellites, earthquakes, conflicts, GPS jamming, CCTV, markets—on a MapLibre/Next.js UI with a FastAPI backend. It streams compressed GeoJSON every 60s for smooth “radar” animations and supports Docker, binaries, and developer setups. HN finds the capabilities and performance tuning impressive, but debates whether it’s another short-lived, AI-assisted “slop” project, discusses vector-tile scaling trade-offs, and highlights an accidentally bundled .env as an ironic OSINT slip.

### Comment pulse
- Suspicion of AI-slop and new accounts → polished README and trendiness make some doubt longevity — counterpoint: others note it matches older human-built intel tools.  
- Rendering raw GeoJSON every 60s → author prioritizes smooth “blinking blip” animation; vector-tile backends like Martin reserved for future historical archives.  
- Dashboard glut observation → commenters compare OSINT maps to 2020 Covid trackers and joke that real OSINT is leaked .env files and comment threads.  

### LLM perspective
- View: Technically solid mashup of existing feeds; value is integration, ergonomics, and performance rather than novel data sources.  
- Impact: Useful for journalists, hobbyists, and educators; could also seed startups or internal tools in security and insurance.  
- Watch next: Hardening auth, rate-limiting, and secrets handling, plus adding vector tiles and historical replay to differentiate from lookalike dashboards.
