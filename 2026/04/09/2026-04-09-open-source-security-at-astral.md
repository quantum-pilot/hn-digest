# Open source security at Astral

- Score: 350 | [HN](https://news.ycombinator.com/item?id=47699181) | Link: https://astral.sh/blog/open-source-security-at-astral

## TL;DR
Astral details a defense-in-depth approach to securing its popular Python tools (Ruff, uv, ty) across CI/CD, organization, releases, and dependencies. They harden GitHub Actions by banning risky triggers, pinning all actions to commit SHAs, minimizing permissions, and isolating secrets via environments. Org-wide rules lock down branches/tags and require strong 2FA. Releases use Trusted Publishing, Sigstore attestations, immutable releases, no caches, and multi-person approvals. Dependencies are tightly managed with cooldowns, social coordination, and targeted de-risking. HN debates whether GitHub Actions can ever be truly safe and whether the market actually values maximal supply-chain assurance.

## Comment pulse
- GitHub Actions cannot be made truly secure → safe use needs fragile, expert-only patterns, suggesting poor defaults and weak isolation — counterpoint: others see complexity as inherent to CI security.  
- Volunteer projects claim stronger provenance than Astral → reproducible, multi-signed builds; frustration that users prefer convenience over assurance — counterpoint: Astral questions value when signers differ from upstream.  
- Supply-chain risk is systemic → mutable registries, GitHub as critical dependency, and ad‑hoc tools (e.g., multi‑sig file auth) show need for broader ecosystem fixes.

## LLM perspective
- View: This post is a practical checklist for any serious OSS project relying on GitHub; most aren’t close to this bar.  
- Impact: If adopted widely, expectations on CI providers and registries will shift toward immutable artifacts, OIDC, and attestations by default.  
- Watch next: Standardized policies for dangerous triggers, ecosystem tooling for immutability gaps, and easier hosted GitHub App platforms for small projects.
