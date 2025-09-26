# This month in Servo: variable fonts, network tools, SVG

- Score: 149 | [HN](https://news.ycombinator.com/item?id=45373501) | Link: https://servo.org/blog/2025/09/25/this-month-in-servo/

- TL;DR
  - Servo’s biggest update yet: 447 PRs deliver inline SVG, variable fonts (gated), named CSS grid lines/areas (gated), devtools network monitor, JS breakpoints, and a major hit‑testing crash fix. Broad DOM/CSS/Canvas gains, 60 FPS throttling, smaller binaries, and WebDriver at 80% conformance. Servoshell adds favicons and stability fixes. Donations hit $5,552/month, funding CI upgrades and maintenance. HN debates whether Servo aims to rival browsers or stay an embeddable engine, funding beyond Mozilla (Igalia-led), “greenfield” momentum, and missing basics like scrollbars/WPE comparisons.

- Comment pulse
  - Browser choice vs embedding focus → Users want a Rust browser; maintainers frame Servo as an embeddable engine — counterpoint: optimism persists for a future browser.
  - Funding and stewardship → Worry about Mozilla’s exit; current momentum credited to Igalia-backed work and external grants; some wish for Brave or others to sponsor.
  - Maturity and alternatives → Feels greenfield with major rewrites underway; basics like scrollbars still missing; some compare it with WPEWebKit for embeddable use.

- LLM perspective
  - View: Servo is maturing as an embeddable engine; feature gates mean early adopters must selectively enable and test.
  - Impact: Rust app embedders get better rendering, devtools, automation; CI upgrades should accelerate regressions feedback.
  - Watch next: Ungate variable fonts/grid; WPT pass-rate climbs; macOS arm64 builds; scrollbars; IndexedDB/CookieStore ship; public microbenchmarks.
