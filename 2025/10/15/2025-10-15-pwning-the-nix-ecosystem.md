# Pwning the Nix ecosystem

- Score: 236 | [HN](https://news.ycombinator.com/item?id=45592401) | Link: https://ptrpa.ws/nixpkgs-actions-abuse

- TL;DR
  - Two researchers showed how nixpkgs’ GitHub Actions could be hijacked via pull_request_target: an xargs argument-injection in an EditorConfig check and a CODEOWNERS validator that allowed symlinked local-file reads, leaking the runner’s write-scoped GITHUB_TOKEN—enough to push to nixpkgs. Maintainers disabled, hardened, and renamed workflows; lessons: least privilege, never mix untrusted PR inputs with privileged steps, and avoid dangerous triggers. HN debates scrapping pull_request_target versus operational needs, urges fine‑grained/single‑use capabilities and signing agents over bearer tokens, and revisits signed commits/reproducible builds amid broader supply‑chain fatigue.

- Comment pulse
  - pull_request_target is unsafe and unnecessary → write scopes and secret exposure; prefer fine-grained/single-use tokens — counterpoint: needed for non-mergeable PRs and deterministic base workflows.
  - Bearer tokens amplify CI compromise → use signing agents, mTLS, or SPIFFE-style identities to avoid exposing credentials.
  - Enforce signed commits and independent reproducible builds → reduces “last mile” attacks — counterpoint: onerous for nixpkgs scale; mobile signing/tooling and infra gaps persist.

- LLM perspective
  - View: Trust boundary collapse in CI—untrusted PR data influenced privileged jobs via pull_request_target and unsafe tooling (xargs, symlinks).
  - Impact: Maintainers must restrict permissions, drop bearer tokens, and isolate PR inputs; GitHub should provide fine-grained, single-use capabilities for automation.
  - Watch next: Audit pull_request_target workflows, enforce permissions, adopt OIDC-bound signing agents; track GitHub deprecations, zizmor findings, and NixOS reproducibility milestones.
