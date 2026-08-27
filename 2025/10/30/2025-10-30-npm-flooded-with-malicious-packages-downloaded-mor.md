# NPM flooded with malicious packages downloaded more than 86k times

- Score: 127 | [HN](https://news.ycombinator.com/item?id=45755027) | Link: https://arstechnica.com/security/2025/10/npm-flooded-with-malicious-packages-downloaded-more-than-86000-times/

### TL;DR

Security firm Koi reports that PhantomRaven placed 126 credential-stealing packages on NPM, collectively downloaded more than 86,000 times, with 80 reportedly still available when checked. The campaign hides remote dynamic dependencies that can be fetched fresh over HTTP, evade static dependency displays, change payloads by target, and steal environment, GitHub, Jenkins, NPM, and CI/CD data. HN commenters debate legitimate install scripts for native compilation, while recommending disabled-by-default lifecycle hooks, version pinning, checksums, delayed adoption, and isolated development environments.

### Comment pulse

- Install hooks have legitimate uses → native modules may need compilation, though automatic arbitrary execution creates a broad compromise path.
- Dynamic remote code defeats review → an unchanged package can later serve targeted or newly malicious payloads.
- Sandboxing limits credential theft → containers, VMs, and ephemeral secrets reduce exposure but do not make dependencies trustworthy.

### LLM perspective

- View: Package identity is meaningless when installation can retrieve mutable, undeclared code from unrelated infrastructure.
- Impact: Registries, scanners, and developers need controls that cover execution-time downloads, not only published archives.
- Watch next: Track package removals, NPM policy changes, lifecycle-hook defaults, and indicators of follow-on credential abuse.
