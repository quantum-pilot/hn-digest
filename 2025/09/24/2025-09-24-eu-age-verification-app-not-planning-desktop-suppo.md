# EU age verification app not planning desktop support

- Score: 449 | [HN](https://news.ycombinator.com/item?id=45359074) | Link: https://github.com/eu-digital-identity-wallet/av-doc-technical-specification/issues/22

- TL;DR
  - An EU age‑verification prototype for the Digital Identity Wallet is prioritizing Android/iOS and explicitly not targeting desktop. A filed GitHub issue flags three usability risks: excluding people without smartphones, repeated checks degrading private/desktop browsing, and implementation costs/lock‑in for small developers. HN worries about forced smartphone dependency and app‑only creep (e.g., airlines), legal reality that desktop flows may still require a phone, and privacy/sovereignty concerns: the prototype’s linkable SD‑JWT vs promised ZKPs, plus reliance on Apple/Google attestation.

- Comment pulse
  - Mobile-only scope excludes non-smartphone users; app mandates like Ryanair illustrate rising friction; phones becoming de facto ID — counterpoint: desktops might avoid verification.
  - Law will still require age checks; desktop apps likely need phone interaction; some argue friction is a feature to suppress targeted content.
  - Spec promises ZKPs, but prototype uses linkable SD‑JWT, enabling issuer–verifier linkability; hardware attestation cements Apple/Google power, conflicting with EU digital sovereignty.

- LLM perspective
  - View: Smartphone-first verification excludes vulnerable groups and degrades web UX; privacy tech must ship, not just sit on roadmaps.
  - Impact: Publishers and regulated sites add phone gates; alternative OS/hardware and pure-desktop usage shrink; platform lock‑in strengthens.
  - Watch next: Real ZKP deployments, desktop flows or extensions, and DPAs auditing issuer unlinkability; plus airline/bank policies mandating apps.
