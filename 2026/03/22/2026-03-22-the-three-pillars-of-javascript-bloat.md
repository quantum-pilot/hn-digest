# The three pillars of JavaScript bloat

- Score: 441 | [HN](https://news.ycombinator.com/item?id=47473718) | Link: https://43081j.com/2026/03/three-pillars-of-javascript-bloat

### TL;DR
Article argues modern JS projects are bloated mainly by: legacy-compat helpers (for ancient runtimes/realms), “atomic” micro-packages, and ponyfills still used long after features are universally supported. These once-reasonable patterns now inflate dependency graphs, downloads, maintenance, and supply‑chain risk for the majority on evergreen runtimes. Author recommends aggressively replacing such deps with native APIs or slimmer libs using tools like e18e, knip, and npmgraph. HN discussion adds cultural bloat, tech‑debt inertia, and maintainer incentives as root causes.

### Comment pulse
- Many devs report success with dependency‑light or dependency‑free apps using modern browser features, but say tutorials and culture strongly steer newcomers toward frameworks and tooling.  
- Others argue the deeper problem is organizational: teams are rewarded for shipping features quickly via `npm i`, not for deleting code or simplifying architectures.  
- Several see bloat as tech debt and incentives: outdated targets, micro-packages inflating download stats, expanded attack surface—counterpoint: some still need weird or very old browsers.

### LLM perspective
- View: Make “no unnecessary runtime deps” an explicit design goal; treat compatibility helpers as separate opt‑in layers or builds.  
- Impact: Library maintainers, bundler authors, and security teams gain smaller graphs, fewer updates, and clearer responsibility for truly legacy support.  
- Watch next: Static analyzers that detect obsolete polyfills, single‑use helpers, and over‑broad browserslist targets could automate most of this cleanup.
