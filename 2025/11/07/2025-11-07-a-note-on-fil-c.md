# A Note on Fil-C

- Score: 227 | [HN](https://news.ycombinator.com/item?id=45842494) | Link: https://graydon2.dreamwidth.org/320265.html

TL;DR
Fil‑C adds a Clang instrumentation pass that enforces spatial safety with bounds checks and temporal safety with a concurrent GC. Graydon Hoare applauds its unusually high compatibility—potentially Linux‑userspace‑wide—with costs: roughly 1–4× CPU and notable memory growth, plus only dynamic guarantees; data races remain and it’s easy to disable. Discussion centers on “why now” (InvisiCaps, clearer C provenance), applicability (apps vs libraries), misconceptions about GC being the main slowdown, and whether crash frequency is acceptable—calls for real data persist.

Comment pulse
- Mature C apps rarely crash → Fil‑C surfaces latent UAFs as crashes, swapping stealthy exploits for outages; need CVE/incident data — counterpoint: assertion lacks metrics.
- Why now? → New InvisiCaps technique and clearer C pointer provenance enable high compatibility; prior tools did bounds checking but with poorer performance/coverage.
- Where it fits → Great for C apps tolerating 2–4× CPU; libraries need ABI marshaling; Python/JS are much slower, so Fil‑C still fills a gap.

LLM perspective
- View: Fil‑C pragmatically raises C’s floor; complements Rust by protecting legacy code without rewrites.
- Impact: Security teams, distro maintainers, and critical utilities could adopt per‑target builds; less silent memory corruption, more detectable failures.
- Watch next: Distro‑wide build, stable library interop, P95/P99 latency and memory profiles, and policies to keep safety switch on.
