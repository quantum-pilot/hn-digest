# Returning to Rails in 2026

- Score: 327 | [HN](https://news.ycombinator.com/item?id=47347064) | Link: https://www.markround.com/blog/2026/03/05/returning-to-rails-in-2026/

### TL;DR
A longtime DevOps engineer rediscovered Rails by building a band-setlist app and argues Rails 8 quietly delivers a modern, joyful “old-school web” experience: server-rendered HTML with Hotwire, minimal JavaScript via importmaps, database-backed Solid* components (cache/queue/cable) that remove Redis, SQLite tuned for real production, and Kamal for Heroku‑like container deployments. He acknowledges Ruby/Rails’ declining popularity and aging ecosystem, but values the stable release cadence, strong batteries-included story, and fast idea‑to‑prototype loop—especially for small and solo projects.

---

### Comment pulse
- Rails is fun and productive, but large untyped, metaprogrammed codebases are painful to debug; many veterans defect to C#/Rust for static types and tooling — counterpoint: Sorbet/RBS still not compelling.
- Several devs praise Rails/Django for “just ship it” simplicity versus microservice/JS stack churn and TypeScript yak‑shaving; it feels closer to classic desktop IDE productivity than modern web stacks.
- Long-lived Rails shops report 15–19 years of stable production use and relatively smooth upgrades, contrasting this with Next.js’ breaking paradigm shifts and JavaScript ecosystem turbulence.

---

### LLM perspective
- View: Rails 8 plus Hotwire, Solid*, and SQLite forms a strong default for small–medium apps where infra sprawl is the real cost.
- Impact: Best fit for teams prioritizing stability and DX over résumé-driven tech churn; hiring may be harder but maintenance saner.
- Watch next: Benchmark Solid* + SQLite at scale, compare Kamal workflows to fly.io/Render, and see whether typed-Ruby efforts gain real traction.
