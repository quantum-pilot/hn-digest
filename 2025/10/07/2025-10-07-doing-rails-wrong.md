# Doing Rails Wrong

- Score: 336 | [HN](https://news.ycombinator.com/item?id=45505692) | Link: https://www.bananacurvingmachine.com/articles/you-re-doing-rails-wrong

- TL;DR
  - A tongue‑in‑cheek dialogue skewers stacking modern JS tooling (Vite, React, Tailwind, Docker, SSR) onto Rails when a plain Rails app often ships faster with fewer moving parts. HN splits: some say complexity is inherent for “modern apps” and Rails-as-API + React is a different architecture; others note Rails 8 + Hotwire/import maps/Kamal already deliver modern UX with minimal setup. Pragmatics weigh in: Hotwire’s docs/ecosystem feel thin for complex state, hiring favors React, and Rails’ omakase churn makes true “vanilla” rare.

- Comment pulse
  - Vanilla Rails often suffices → Hotwire, import maps, Kamal trim JS tooling, builds, deploys — counterpoint: “modern” apps need React-era stacks; complexity is inherent.
  - Hotwire struggles at scale → docs are thin; stateful UIs feel hacky; teams report replacing with Inertia+React for maintainability.
  - Org reality dominates → few greenfields; hiring favors React/Vue; consistency with existing FE platforms outweighs Rails-omakase purity amid churn.

- LLM perspective
  - View: Default to Rails 8 defaults; prove the need for SPAs before importing React/Vite.
  - Impact: Small teams ship faster; larger orgs prioritize frontend uniformity and hiring pipelines over Rails-native interactivity.
  - Watch next: Quality of Hotwire/Stimulus docs, Inertia Rails adapters, Kamal adoption, and benchmarks comparing Hotwire vs SPA for typical CRUD flows.
