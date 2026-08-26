# I hate GitHub Actions with passion

- Score: 391 | [HN](https://news.ycombinator.com/item?id=46614558) | Link: https://xlii.space/eng/i-hate-github-actions-with-passion/

### TL;DR

A four-platform build failed only on Linux ARM because CUE was installed on host architectures but unavailable inside the isolated cross-build environment. Each attempted YAML fix required a push, several clicks, and a two-to-three-minute failure cycle. After 30 minutes, the author removed generation from build.rs, moved it into a GNU Makefile, committed generated files, and restored simple CI. HN largely agreed the real problem is the remote feedback loop, recommending locally runnable scripts, containers, Nix, or local Action emulators while keeping workflows thin.

### Comment pulse

- CI should orchestrate repository-owned scripts → portability and local reproduction beat embedding logic in vendor YAML.
- Containers or reproducible environments reduce drift → counterpoint: macOS builds and CI-native caching, artifacts, retries, and step visibility remain awkward.
- Better debugging changes the experience → SSH access and editable remote manifests avoid commit-push-wait loops.

### LLM perspective

- View: The decisive CI feature is observability with fast reproduction, not the breadth of marketplace actions.
- Impact: Teams separating orchestration from build logic reduce vendor lock-in and incident diagnosis time.
- Watch next: Native local execution, run URLs from dispatch, typed workflow tooling, resumable steps, and interactive failed runners.
