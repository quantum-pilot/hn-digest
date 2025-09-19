# Pnpm has a new setting to stave off supply chain attacks

- Score: 208 | [HN](https://news.ycombinator.com/item?id=45286526) | Link: https://pnpm.io/blog/releases/10.16

- TL;DR
  - pnpm 10.16 adds minimumReleaseAge, a configurable delay (minutes) before newly published dependency versions can be installed, with per-package exclusions, to blunt fast-moving supply‑chain attacks typically detected within hours. It also introduces finder functions for pnpm list/why to query dependencies by arbitrary manifest properties, plus several fixes (Node 24 warning, exact nodeVersion, publish .tar.gz, proper Ctrl‑C exit codes). HN debate: delay helps scanners act, but may slow fixes; naming/units nitpicks; uv and Yarn have similar features; appropriate wait windows vary given semver ranges and transitive churn.

- Comment pulse
  - Age-gating reduces exposure → scanners audit fresh uploads quickly; delaying installs buys detection time — counterpoint: also delays propagation of urgent fixes.
  - Config over flags → project-level setting protects teams without remembering CLI switches; still brittle if someone runs npm instead of pnpm.
  - How long to wait? → JS’s semver ranges and transitive dependencies auto‑update widely; weeks‑long freezes hinder security/stability more than they help.

- LLM perspective
  - View: Release-age thresholds are a simple, low-cost defense-in-depth; pair with excludes and CI to avoid blocking critical updates.
  - Impact: Adoption by pnpm, Yarn, uv normalizes age-gating; enterprises can standardize policies across JS toolchains.
  - Watch next: Registry-side quarantine windows, default recommended ages, per-version exemptions, and metrics on caught/averted incidents.
