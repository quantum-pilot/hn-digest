# Open source security at Astral

- Score: 350 | [HN](https://news.ycombinator.com/item?id=47699181) | Link: https://astral.sh/blog/open-source-security-at-astral

### TL;DR

Astral documents a defense-in-depth supply-chain program for Ruff, uv, and ty: it bans risky GitHub Actions triggers, commit-pins dependencies, minimizes permissions, isolates secrets, enforces strong 2FA and protected branches and tags, and moves privileged automation into GitHub Apps. Releases use Trusted Publishing, attestations, immutable artifacts, cache-free builds, and two-person approval; dependencies receive cooldowns and manual scrutiny. HN readers admired the effort but questioned whether GitHub Actions’ fragile configuration and GitHub itself remain irreducible single points of trust.

### Comment pulse

- Some argued secure configuration is too delicate to scale — counterpoint: others saw complexity as inherent to ecosystems that execute untrusted contributions.
- A StageX maintainer promoted reproducible, multisigned third-party builds; Astral’s author questioned which threat model identities outside the producer actually solve.
- Signatures prove provenance, commenters noted, but author trust and code behavior still require audit; automation cannot remove those judgments.

### LLM perspective

- **View:** Security comes from constraining compromise paths and blast radius, not asserting any single artifact or platform is trustworthy.
- **Impact:** Maintainers gain a concrete blueprint, but smaller projects face staffing and hosting costs for comparable controls.
- **Watch next:** PyPI attestation compatibility, the planned bot source release, platform-default improvements, code signing, and evidence from future incidents.
