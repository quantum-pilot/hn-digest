# Bun support is now limited and deprecated

- Score: 335 | [HN](https://news.ycombinator.com/item?id=48238789) | Link: https://github.com/yt-dlp/yt-dlp/issues/16766

### TL;DR

yt-dlp will restrict Bun as an ejs-compatible JavaScript runtime to versions 1.2.11–1.3.14 and deprecate the integration, reserving full removal if maintenance becomes burdensome. Pre-1.2.0 builds ignore ejs’s lockfile, and releases before 1.2.11 cannot run its tests; the ceiling anticipates Bun’s Claude-assisted million-line Rust rewrite. HN split over whether rejecting an unproven rewrite without regression data is political or prudent dependency governance. Critics cite reusable tests and reviewability; supporters say downstream maintainers need not expose users to uncertain compatibility or security risks.

### Comment pulse

- Evidence should precede rejection → critics want observed crashes or vulnerabilities, not assumptions — counterpoint: waiting for failures defeats preventive risk management.
- Rewrite size complicates ownership → one million generated Rust lines strain review — counterpoint: existing tests and parallel reviewers can make validation tractable.
- Workarounds are lightweight → users can pin a standalone 1.3.14 binary or switch to Node or Deno — counterpoint: this adds duplicate tooling.

### LLM perspective

- **View:** Dependency policy can legitimately price governance risk before bugs appear, but permanent rejection should remain revisitable.
- **Impact:** Bun users lose automatic upgrade compatibility; yt-dlp maintainers narrow their test and support matrix.
- **Watch next:** Evaluate Bun.rs release versioning, independent audits, compatibility tests, crash rates, security reports, and any later support reversal.
