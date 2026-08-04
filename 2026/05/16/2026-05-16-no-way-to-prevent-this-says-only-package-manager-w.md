# 'No way to prevent this,' says only package manager where this regularly happens

- Score: 414 | [HN](https://news.ycombinator.com/item?id=48155690) | Link: https://kevinpatel.xyz/posts/no-way-to-prevent-this/

### TL;DR

A satire blames npm’s sprawling dependency graphs, weak registry guardrails, and default install-script execution for recurring supply-chain compromises, contrasting JavaScript with ecosystems that rely more on standard libraries and verification. HN agreed safer defaults are overdue but rejected simple comparisons: Cargo can run unsandboxed build code and may lack stronger publishing protections, while malicious library code eventually executes even without postinstall hooks. Practical defenses included company-controlled registries, immutable namespaces, delayed adoption, dependency reduction, and explicit overrides for urgent security releases.

### Comment pulse

- Cooldowns catch attacks removed within hours → counterpoint: universal delays merely postpone discovery unless some users still test fresh releases.
- Registry governance matters: Maven verifies namespaces and makes releases immutable, while npm’s ownership and publication rules historically permit broader attack paths.
- Postinstall is not the whole threat → dependency code runs during builds, tests, or production; meaningful trust requires review, isolation, or fewer packages.

### LLM perspective

- **View:** Package security is an ecosystem-design problem spanning authority, mutability, execution, dependency depth, and adoption timing.
- **Impact:** Teams need layered controls; maintainers face pressure to ship safer defaults without breaking native tooling.
- **Watch next:** Measure cooldown efficacy, malicious-version dwell time, install-script usage, namespace takeovers, sandbox adoption, and dependency-graph shrinkage.
