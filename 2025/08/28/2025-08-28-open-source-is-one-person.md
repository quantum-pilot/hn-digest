# Open Source is one person

- Score: 435 | [HN](https://news.ycombinator.com/item?id=45047460) | Link: https://opensourcesecurity.io/2025/08-oss-one-person/

- TL;DR
    - The author rebuts a Register piece implying risk because a DoD-used utility is maintained by a Russian. The real systemic risk is single-maintainer, under-resourced projects. ecosyste.ms tracks 11.8M OSS projects; ~7M are solo-maintained. In NPM, about half of packages with >1M monthly downloads have a single maintainer; only at >1B do multi-maintainer packages dominate. Focus on bus factor and support, not nationality. HN highlights governance-driven posture (e.g., wartime concerns), vendoring/mirroring, and OSS resilience via forking despite dominant contributors.

- Comment pulse
    - Supply-chain risk is governance-dependent; militaries plan for wartime coercion, so they mirror/vendor and pin dependencies — counterpoint: DoD likely audits, freezes, and self-patches anyway.
    - When a solo maintainer vanishes, projects fork, get replaced, are handed off, or stagnate; OSS’s edge is the ability to fork versus proprietary abandonment.
    - Multi-maintainer repos often have one dominant committer; some avoid such projects for core tooling, preferring mature alternatives.

- LLM perspective
    - View: Normalize single-maintainer reality; manage risk with process, funding, and redundancy—not nationality heuristics.
    - Impact: Critical users should vendor, mirror, pin versions, maintain SBOMs, and establish takeover plans; budget for bounties, contracts, or internal stewards.
    - Watch next: Quantify maintainer concentration, bus-factor events, and funding outcomes; track DoD/industry guidance, provenance standards, and automated dependency risk scoring.
