# Pwning the Nix ecosystem

- Score: 236 | [HN](https://news.ycombinator.com/item?id=45592401) | Link: https://ptrpa.ws/nixpkgs-actions-abuse

### TL;DR

Two researchers report finding Nixpkgs GitHub Actions flaws that mixed privileged `pull_request_target` workflows with untrusted pull-request data. One workflow exposed argument injection through attacker-controlled filenames; another let a submitted symlink make a validator print a runner credentials file, allegedly yielding a read-write token. Maintainers disabled and fixed the workflows the same day. HN discussion treated the trigger as a broad foot-gun, while debating legitimate uses, signed changes, reproducible builds, bearer tokens, and maintainability tradeoffs.

### Comment pulse

- Privileged pull-request automation is hard to contain → filenames, symlinks, and branch history expand the attack surface beyond executing submitted code.
- Removing the trigger is contested → labeling, comments, unmergeable requests, and private-repository OIDC policies still motivate its use.
- Stronger provenance divided participants → signatures and reproducible builds improve assurance but impose tooling, infrastructure, and contributor costs.

### LLM perspective

- View: Treat every pull-request-controlled byte as executable influence when a workflow carries secrets or write access.
- Impact: Repository maintainers need explicit permissions and strict separation between untrusted inspection and privileged actions.
- Watch next: Audit dangerous triggers, historical workflow versions, token scope, symlink handling, and argument boundaries.
