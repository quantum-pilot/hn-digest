# GitHub Actions is slowly killing engineering teams

- Score: 354 | [HN](https://news.ycombinator.com/item?id=46908491) | Link: https://www.iankduncan.com/engineering/2026-02-05-github-actions-killing-your-team/

### TL;DR

Former CircleCI employee Ian Duncan argues GitHub Actions’ convenience hides compounding costs: slow, crash-prone logs; awkward YAML expressions; risky marketplace dependencies; constrained runners; opaque caches; and difficult permissions, reuse, concurrency, and secrets. He prefers Buildkite’s readable logs, user-controlled agents, dynamic pipelines, and separation of orchestration from code, while conceding self-hosting overhead and GitHub’s value for small or public projects. Commenters found the critique hyperbolic or promotional, but agreed local reproducibility and portable build commands matter; they split on whether complex CI logic is avoidable and whether Actions is broadly adequate.

### Comment pulse

- Keep builds portable → local Makefiles, scripts, or build tools ease debugging and migration — counterpoint: complex triggers inevitably leave provider-specific orchestration.
- Buildkite’s differentiation is control → commenters praised dynamic pipelines, ergonomic logs, and owned agents, while noting major CI systems also support self-hosted compute.
- Convenience remains decisive → GitHub integration and free public-repository use make Actions adequate for many teams despite real interface and feedback-loop flaws.

### LLM perspective

- View: CI choice depends on pipeline complexity and engineering-time costs; neither default convenience nor maximum control wins universally.
- Impact: Large monorepos and long builds can justify migration; small projects may spend more operating alternative infrastructure than they recover.
- Watch next: Queue time, debugging time, failure retries, cache performance, dependency risk, agent costs, and migration effort measured per team.
