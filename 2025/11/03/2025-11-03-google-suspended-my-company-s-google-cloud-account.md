# Google suspended my company's Google cloud account for the third time

- Score: 397 | [HN](https://news.ycombinator.com/item?id=45798827) | Link: https://www.agwa.name/blog/post/google_suspended_sslmates_cloud_account_again

- TL;DR
  - SSLMate’s GCP access was suspended three times without notice, breaking customer integrations built per Google’s guidance (service‑account impersonation). Recovery involved contradictory, automated emails and no root cause; full access returned only after HN attention. The author now faces a forced trade‑off: insecure long‑lived keys, complex and fragile OIDC setup, or recurring suspension risk. HN frames this as platform‑scale liability optimization with scarce human support; some advocate smaller providers, others argue Big Tech could fund review but chooses margins.

- Comment pulse
  - Hyperscale defaults to automated bans → lowers liability/support cost; false positives tolerated — counterpoint: Giants can fund human review; choosing not to protects margins.
  - Don’t rely on Google for core ops → users cite arbitrary account losses across YouTube/Cloud; recommend smaller vendors with human support.
  - Centralized moderation risks expanding to AI APIs → a client’s misuse could nuke provider accounts; enable built‑in moderation and isolation.

- LLM perspective
  - View: Mitigate platform risk via architectural isolation: per-customer projects, least-privilege, and multi-cloud fallbacks; assume sudden revocation.
  - Impact: Complex OIDC onboarding depresses adoption; simplifying pools/providers and first-class issuer bindings would boost secure, keyless integrations.
  - Watch next: Google policy/roadmap on OIDC parity; clearer suspension appeal SLAs; tooling to auto-provision minimal OIDC with Terraform/CLI.
