# Keyhive – Local-first access control

- Score: 158 | [HN](https://news.ycombinator.com/item?id=45445114) | Link: https://www.inkandswitch.com/keyhive/notebook/

- TL;DR
  - Keyhive proposes local-first access control via decentralized group keys (BeeKEM, a TreeKEM/MLS offshoot). Some are testing it for distributed chat. Others argue OAuth2/SSH already allow offline validation, so “central hot path” claims are overstated; the real shift is moving trust/issuance away from an IdP. Ink & Switch’s local-first ethos drew praise; minor naming/UI nitpicks surfaced.
  - Content unavailable; summarizing from title/comments.

- Comment pulse
  - BeeKEM explainer → details mechanics and how it diverges from TreeKEM/MLS for decentralized group management.
  - OAuth2/SSH enable offline verification → not all requests hit central auth — counterpoint: issuance/trust still centralized in IdP, unlike local-first goals.
  - Minor distractions → name confused with Windows registry; tilted callout/underlining irked readers.

- LLM perspective
  - View: Shifts from server-issued tokens to group state; revocation, churn, and auditing become first-class design problems.
  - Impact: Best for peer-to-peer or offline-friendly apps; lowers ops reliance but increases client-side crypto and rotation duties.
  - Watch next: Churn benchmarks, BeeKEM security proofs, MLS interop plans, and migration guides from OAuth2/SSH to group models.
