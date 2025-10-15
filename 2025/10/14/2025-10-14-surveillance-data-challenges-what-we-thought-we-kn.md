# Surveillance data challenges what we thought we knew about location tracking

- Score: 275 | [HN](https://news.ycombinator.com/item?id=45584498) | Link: https://www.lighthousereports.com/investigation/surveillance-secrets/

- TL;DR
    - Lighthouse Reports uncovered First Wap’s Altamides, a global phone-tracking suite exploiting SS7 signaling. A leaked 1.5M-record archive shows targets across 160+ countries, including public figures and ordinary people, and undercover footage captured executives proposing workarounds for sanctions and non‑government buyers. HN discussion pivots to why this persists: SS7’s unfixed trust model, weak/voluntary telecom controls, opaque public–private use, and public apathy—alongside proposals for warrant-based access, transparency limits, and tighter data-handling rules.

- Comment pulse
    - Surveillance persists → leaders prize safety/power, apathy, and diffuse societal costs make pushback hard — counterpoint: warrants/notifications and narrow mandates can balance safety and privacy.
    - SS7 enables cross-border tracking → networks trust foreign partners; regulators favored voluntary filters; carriers also sold location data, compounding risk.
    - Surveillance firms leak too → “open S3 bucket”–style ops and weak cloud hygiene expose their archives, ironically enabling accountability through their own security lapses.

- LLM perspective
    - View: Legacy telecom trust is the root; commercialized exploits plus lax procurement spread nation-grade tracking to corporations and stalkers.
    - Impact: Telecoms, regulators, and law enforcement face reforms; high-risk groups need operational security beyond app-layer encryption.
    - Watch next: Mandate SS7/Diameter firewalls; measure roaming-filter efficacy; require warrant logs with delayed notice; enforce broker bans.
