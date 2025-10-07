# Mise: Monorepo Tasks

- Score: 285 | [HN](https://news.ycombinator.com/item?id=45491621) | Link: https://github.com/jdx/mise/discussions/6564

- TL;DR
  - Mise adds Monorepo Tasks: a unified //path:task namespace with wildcard selection (//...:test), per-project tool/env inheritance, and consistent execution from anywhere. It’s language-agnostic, non‑hermetic, and deliberately omits heavy features like remote caching; task dependencies are supported via “depends.” Positioned between Just/Task (simple) and Nx/Turborepo/Bazel (complex), it targets polyglot teams. HN reactions praise onboarding and tool management; critiques ask for DAG/watch modes and caching, plus concerns about PATH manipulation and scope creep—defenders note local “sources/outputs” skipping and shims.

- Comment pulse
  - One config for tools+tasks → smoother onboarding than Make/Just/Nix; postinstall hooks auto-provision envs.
  - Missing caching/DAG/watch limits scalability → repeated work in monorepos — counterpoint: local skip via sources/outputs; remote caching is an anti‑goal.
  - PATH meddling anxiety → users report shims/explicit control; handles CLI tools; asdf-to-mise migrations have been painless.

- LLM perspective
  - View: A pragmatic middle layer: task runner + tool manager for polyglot repos without Bazel-level ceremony.
  - Impact: Mid-size teams standardize workflows; faster onboarding; JS-only shops may still favor Nx/Turborepo.
  - Watch next: Document cross-package depends, add watch/persistent tasks, clarify caching limits, publish perf baselines on large repos.
