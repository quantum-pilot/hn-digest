# AI Slop vs. OSS Security

- Score: 176 | [HN](https://news.ycombinator.com/item?id=45834303) | Link: https://devansh.bearblog.dev/ai-slop/

- TL;DR
  - A veteran bug-bounty triager argues AI-generated “slop” is flooding OSS security with plausible-but-fabricated reports, consuming scarce maintainer time and degrading trust—amid CVE/NVD backlogs and rising burnout. Suggested mitigations: mandatory AI-use disclosure, higher PoC bars (tests/screencasts/docker), public slop logs, reputation/fee-based friction, and AI-assisted triage—plus real funding for maintainers. HN largely agrees LLMs mimic the form of research without substance; debate focuses on incentive fixes and referral/gatekeeping versus preserving openness.

- Comment pulse
  - LLMs create form without substance → plausible reports without proof mislead; grifters need plausibility, not truth.
  - Broken incentives drive volume → zero-cost accounts, CVE clout, and bounty fishing flood inboxes — counterpoint: stricter PoC requirements/fees could add necessary friction.
  - Referral/reputation gating can filter noise → staked trust improves triage; risks gatekeeping newcomers and enabling plagiarism or tribalism.

- LLM perspective
  - View: Proof-first workflows beat prose: require runnable PoCs, reproducible tests, and environment scripts before triage.
  - Impact: Expect invite-only programs, refundable submission fees, and AI pre-filters; maintainers’ time shifts from debunking to validating.
  - Watch next: Measure false-positive rates of AI triage, CVE backlog recovery, and concrete funding models that pay maintainers, not just platforms.
