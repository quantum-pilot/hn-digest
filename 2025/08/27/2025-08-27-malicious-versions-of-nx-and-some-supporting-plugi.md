# Malicious versions of Nx and some supporting plugins were published

- Score: 443 | [HN](https://news.ycombinator.com/item?id=45034496) | Link: https://github.com/nrwl/nx/security/advisories/GHSA-cxm3-wv7p-598c

### TL;DR

Nx’s official advisory says attackers exploited shell injection in a GitHub Actions pull-request-title check running under the privileged `pull_request_target` event, then altered a publishing workflow and stole an npm token. Malicious Nx and plugin releases used a post-install script to scan files, steal credentials, publish encoded data in victims’ GitHub repositories, and modify shell startup files. Exposure could also occur when Nx Console fetched `latest`. Users are told to check audit logs and local indicators, remove affected versions, purge caches, and rotate all possibly exposed credentials.

### Comment pulse

- Disabling install scripts limits initial execution → counterpoint: malicious dependencies can still run when applications or tools invoke them later.
- Sandboxed development reduces blast radius → host-wide credentials should not share an unrestricted environment with package installation.
- Ecosystem controls failed together → commenters debated artifact signing, ephemeral tokens, mandatory MFA, and responsibility for open-source dependencies.

### LLM perspective

- View: A low-complexity workflow injection crossed trust boundaries until it became a developer-wide credential compromise.
- Impact: Nx users and organizations must treat exposed repositories, tokens, wallets, and environment secrets as public.
- Watch next: Verify trusted publishing, branch-wide workflow fixes, extension behavior, token rotation, and any secondary abuse.
