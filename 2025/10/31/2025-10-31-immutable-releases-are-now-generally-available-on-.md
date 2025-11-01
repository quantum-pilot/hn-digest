# Immutable releases are now generally available on GitHub

- Score: 135 | [HN](https://news.ycombinator.com/item?id=45772064) | Link: https://github.blog/changelog/2025-10-28-immutable-releases-are-now-generally-available/

- TL;DR
    - GitHub GA’d immutable releases: enable at repo/org to lock release assets and protect tags, with Sigstore attestations for external verification. Existing releases stay mutable unless republished. HN welcomes stronger supply-chain guarantees, but wants explicit retraction/“do not use” states instead of deletions to prevent rollback/switcheroo attacks. Some note mutability previously supported nightlies and quick asset fixes. Others advise zero-trust: use keys GitHub can’t access or pin hashes; consider this helpful, not sufficient.

- Comment pulse
    - Immutability overdue → many are shocked releases were mutable; — counterpoint: mutability enabled nightlies and quick post-publish asset fixes in complex pipelines.
    - Support retraction, not deletion → deletion creates “holes” enabling rollback/switcheroo attacks; immutable, auditable deprecation markers and deny-by-default access are preferred.
    - Zero-trust stance → only trust releases signed with keys GitHub can’t access or by pinning hashes; assume host compromise is possible.

- LLM perspective
    - View: Locks curb tag/asset drift; attestations can gate deployments via policy engines without maintaining key infrastructure.
    - Impact: OSS maintainers, enterprise CI consumers, and distros reduce tampering risk; tag stability prevents “latest” regressions.
    - Watch next: Explicit revocation API/state; UI signals for runner provenance; first-class hardware-backed keys and org-wide signing policies.
