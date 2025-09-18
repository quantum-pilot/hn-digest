# The GitHub website is slow on Safari

- Score: 446 | [HN](https://news.ycombinator.com/item?id=45037365) | Link: https://github.com/orgs/community/discussions/170758

- TL;DR
    Safari users saw GitHub pages (especially large PRs) peg CPU and freeze. GitHub traced it to a recent CSS change using the :has() selector in a widely present component that triggered a Safari performance bug. They shipped a mitigation by moving the conditional styling to JavaScript; many report improvements after a hard reload, though very large diffs can still strain Safari. WebKit engineers say two related fixes are upstream and will ship in the next Safari release; both sides urged tighter coordination and better performance telemetry.

- Comment pulse
    - SPA/React ruined performance → SSR handled huge PRs; SPA bloat hurts UX. — counterpoint: This case was a Safari perf bug triggered by GitHub CSS.
    - Safari/WebKit at fault too → CSS and transforms cause excessive compositing; WebKit fixes landed, awaiting release.
    - Process failure in big orgs → PM pressure, weak cross-browser testing, and non-Chromium issues get low priority.

- LLM perspective
    - View: Add perf guardrails for new CSS features; progressive enhancement with feature flags and rapid rollback paths.
    - Impact: GitHub devs shift some conditional styling to JS; Safari users regain usability; WebKit improves selector/compositing performance.
    - Watch next: WebKit release cadence, GitHub’s Safari telemetry (INP alternatives), and diff rendering choices avoiding heavy transforms.
