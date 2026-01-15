# I hate GitHub Actions with passion

- Score: 391 | [HN](https://news.ycombinator.com/item?id=46614558) | Link: https://xlii.space/eng/i-hate-github-actions-with-passion/

## TL;DR
Author adds a Rust `build.rs` step that shells out to the `cue` binary; GitHub Actions’ matrix build then fails only on Linux ARM, because the runner hides the x86_64 binary there. Fixing this requires a slow push–wait–inspect loop in a remote, opaque environment, turning tiny CI tweaks into multi‑minute iterations. The author deletes `build.rs`, moves generation into a Makefile and checked‑in files, and concludes: keep all real logic in scripts you can run locally; let Actions be a thin wrapper.

## Comment pulse
- Root problem: weak local/fast feedback → push–wait cycles. Mitigations: scripts runnable locally, `workflow_dispatch` + `gh`, nektos/act, local/containerized runners, or CI with SSH.
- Pattern advice: workflows should stay dumb; real logic in Makefiles/scripts or Nix derivations for reproducible, portable pipelines—counterpoint: too-big scripts hide structure from CI features.
- Many see all hosted CIs as necessary evils; containerizing the entire pipeline or using Nix reduces lock‑in and makes debugging and iteration far saner.

## LLM perspective
- View: Treat CI YAML as orchestration glue; encode build/deploy logic in versioned, locally executable tooling.
- Impact: Developers regain fast iteration and debuggability; organizations gain portability across CI providers and environments.
- Watch next: Better first-class “run locally” stories, attachable debuggers/SSH for cloud runners, and tools that infer CI workflows from local scripts.
