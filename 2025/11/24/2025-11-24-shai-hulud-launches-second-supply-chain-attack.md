# Shai Hulud launches second supply-chain attack

- Score: 339 | [HN](https://news.ycombinator.com/item?id=46035533) | Link: https://www.aikido.dev/blog/shai-hulud-strikes-again-hitting-zapier-ensdomains

- TL;DR
  - Shai-Hulud’s “Second Coming” is a self-replicating npm worm compromising 492 packages (132M monthly downloads) across AsyncAPI, ENS, Zapier, PostHog, and Postman. It installs Bun via setup_bun.js to run bun_environment.js, harvests secrets with TruffleHog, and publishes them to public GitHub repos titled “Sha1-Hulud: The Second Coming” (≈26.3k seen). New twists: random exfil repos, up to 100 package infections per account, and $HOME wipes on auth failures. Timed before npm revokes classic tokens. Spread blunted by packaging mistakes.

- Comment pulse
  - Sandbox npm installs with bwrap → isolates postinstall scripts, reducing damage; wrapper scripts make it usable; not a silver bullet.
  - Rapid exposure check → script scans npm/pnpm lockfiles for listed packages; helps triage affected repos quickly.
  - Not a pure duplicate → threads merged for the same event — counterpoint: this article adds technical details; also clarifies Shai vs “Sha1”.

- LLM perspective
  - View: Treat npm postinstall as untrusted; default-disable in CI and local dev; allowlist only required scripts.
  - Impact: Teams must rotate machine-user creds, adopt OIDC for CI, enforce npm trusted publishing and org-wide MFA.
  - Watch next: Npm classic token revocation uptake; removal of “Sha1-Hulud” repos; telemetry on home-directory wipes and Bun-based payloads.
