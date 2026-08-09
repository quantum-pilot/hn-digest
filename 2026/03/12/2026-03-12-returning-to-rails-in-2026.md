# Returning to Rails in 2026

- Score: 327 | [HN](https://news.ycombinator.com/item?id=47347064) | Link: https://www.markround.com/blog/2026/03/05/returning-to-rails-in-2026/

### TL;DR

After 13–14 years away, the author built a band setlist app with Rails 8 and found its convention-driven productivity intact but its operational story transformed. Hotwire, Stimulus, Turbo, and import maps enabled interactive server-rendered pages with little JavaScript tooling; Solid Cache, Queue, and Cable plus production-tuned SQLite removed several service dependencies; Kamal made container deployment nearly one command. Commenters celebrate Rails’ coherent, stable, batteries-included workflow and long upgrade horizon, while critics cite weak typing, runtime magic, slower Ruby, aging gems, and difficult hiring at scale.

### Comment pulse

- Rails minimizes web-development yak shaving → integrated conventions let small teams move from models and routes to polished features quickly.
- Longevity can beat fashion → documented deprecations make upgrades less disruptive than framework migrations that replace fundamental application models.
- Large dynamic codebases divide teams → counterpoint: disciplined architecture yields durable Rails systems, but RBS and Sorbet still disappoint typing advocates.

### LLM perspective

- **View:** Rails 8’s strongest pitch is fewer independently operated parts, not nostalgia or raw benchmark leadership.
- **Impact:** Side projects and small teams gain leverage; organizations needing abundant typed-language hires face a sharper tradeoff.
- **Watch next:** SQLite write contention, Solid component reliability, Kamal operations, gem maintenance, and native typing progress.
