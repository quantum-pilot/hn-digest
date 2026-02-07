# GitHub Actions is slowly killing engineering teams

- Score: 354 | [HN](https://news.ycombinator.com/item?id=46908491) | Link: https://www.iankduncan.com/engineering/2026-02-05-github-actions-killing-your-team/

### TL;DR
The author, a veteran of many CI systems, argues GitHub Actions wins by default but delivers a punishing developer experience: a crash-prone log viewer, a half-language bolted onto YAML, opaque caching and permissions, and a risky third‑party actions marketplace. You rent slow, generic runners or pay dearly for better ones, yet still fight the same UX. By contrast, Buildkite keeps YAML as pure pipeline description, pushes real logic into scripts you can run locally, lets you own fast, cached agents, supports dynamically generated pipelines, and has a more thoughtful, humane UI. HN discussion is split: some see Actions as “good enough” general orchestration, others stress thin CI plus real build tools, and many agree the deeper issue is slow feedback and “programming in config.”

---

### Comment pulse
- Pro‑Actions: as a general workflow engine, Actions is flexible, widely integrated, and “pretty good” where it counts; Buildkite looks nice but not essential.
- Domain‑specific view: in game dev and similar domains, generic CI orchestration is too slow; build systems must understand dependency graphs deeply to be viable.
- “Keep CI thin” camp: central Make/Fastlane/shell scripts make CI portable and simpler—counterpoint: real projects still accumulate nontrivial branching, permissions, and environment logic in CI.

---

### LLM perspective
- View: Treat CI as a core developer UX product; bad logs and config languages silently burn huge amounts of engineering time.
- Impact: Teams with big monorepos, long builds, or strict security needs gain most from Buildkite-style owned agents and generated pipelines.
- Watch next: Track PR-to-green times, flakiness, and CI-config churn; use metrics to justify piloting alternative CI or stronger local-repro tooling.
