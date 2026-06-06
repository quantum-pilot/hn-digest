# How far behind is each major Chromium browser?

- Score: 156 | [HN](https://news.ycombinator.com/item?id=47999006) | Link: https://chromium-drift.pages.dev/

### TL;DR
The project visualizes “Chromium drift”: how many Chromium versions each major Chromium-based browser lags behind upstream. That lag matters because every version gap can correspond to public, already-patched security vulnerabilities that attackers can target while downstream browsers ship late. HN discussion broadens this to Electron apps and desktop software, where outdated embedded Chromium is pervasive, and questions the focus on only major versions, the lack of historical drift data, and some accessibility and completeness issues with the UI.

---

### Comment pulse
- Electron-based apps likely have worse drift than browsers → studies and ongoing surveys show many ship long-outdated Chromium with known vulnerabilities.
- Versioning is subtler than “major lag” → minor releases, Extended Stable, and LTS branches all carry security fixes—counterpoint: a truly security-only stable line is still missing.
- Methodology and UX need work → no time series, missing some browsers, fast Chromium release cadence, and color-contrast/red–green choices hurt accessibility.

---

### LLM perspective
- View: Tracking Chromium drift is a concrete, actionable proxy for user exposure to n-day browser vulnerabilities.
- Impact: Browser vendors, Electron maintainers, and enterprises can prioritize upgrades and deprecate builds with excessive drift.
- Watch next: Add historical drift graphs, minor-version resolution, and CVE mapping; extend scanning to Electron apps and “bundled browser” desktop software.
