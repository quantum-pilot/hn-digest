# No leap second will be introduced at the end of December 2026

- Score: 221 | [HN](https://news.ycombinator.com/item?id=48846281) | Link: https://datacenter.iers.org/data/latestVersion/bulletinC.txt

### TL;DR
No leap second will be added at the end of December 2026, meaning UTC will continue with its current offset from TAI and GPS. Leap seconds are irregular because Earth’s rotation is influenced by weather, fluid motion in the core, geology, and even human water redistribution, all hard to predict precisely. Commenters discuss how Unix time ignores leap seconds, workarounds like Google’s “time smear,” the planned global phase-out of leap seconds around 2035, and joke about sci‑fi‑sounding time agencies.

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Earth’s rotation is chaotic-ish → atmosphere, liquid core, oceans, geology, and human water movement change day length unpredictably—counterpoint: we can still model trends, just not exact seconds.
- Unix timestamps skip leap seconds → some real seconds are unaddressable and some timestamps map to no physical second; large systems smear adjustments over hours.
- Timekeeping bureaucracy is peak nerd culture → titles like “International Earth Rotation Service” and “Director of the Directorate of Time” sound like Douglas Adams; offsets (UTC–TAI, UTC–GPS) stay fixed for now.

---

### LLM perspective
- View: Ending leap seconds stabilizes civil time for computers, but gradually detaches UTC from apparent solar time, a social and legal compromise.
- Impact: Operators of distributed systems, databases, and satellites can simplify time logic; standards bodies must codify behavior for historical and future timestamps.
- Watch next: Track IERS decisions, ITU/ISO standards, GNSS handling of offsets, and whether time-smearing becomes de facto practice post-leap-second phase-out.
