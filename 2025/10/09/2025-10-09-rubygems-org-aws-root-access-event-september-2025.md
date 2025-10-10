# Rubygems.org AWS Root Access Event – September 2025

- Score: 228 | [HN](https://news.ycombinator.com/item?id=45530832) | Link: https://rubycentral.org/news/rubygems-org-aws-root-access-event-september-2025/

- TL;DR
  Ruby Central disclosed that an unauthorized actor used AWS root credentials for RubyGems.org from Sept 19–30, changing the root password. They regained control Sept 30, rotated credentials, tightened monitoring, and began an external audit, claiming no evidence of data or package compromise. Root causes: shared root credential copy and failure to rotate root password/MFA after a maintainer’s access change. HN debates whether integrity can be trusted without preexisting CloudTrail trails, if gems from that window are suspect, and governance/attribution issues, including a prior proposal to monetize HTTP logs.

- Comment pulse
  - All gems Sept 19–30 are suspect → root compromise and no CloudTrail trails; integrity unprovable — counterpoint: AWS 90‑day event history exists and is reviewable.
  - Arko implied as actor → blog screenshots, lingering access; RC cites proposal to monetize logs as motive — counterpoint: accusations without charges risk slander; wait.
  - Operational failures erode trust → root/MFA not rotated; recommend AWS Organizations, separate log-archive account, SCPs, and publish reproducible build attestations.

- LLM perspective
  - View: Package provenance, not access, is the core gap; attest releases so trust doesn’t hinge on logs.
  - Impact: Enterprises and SCA vendors may quarantine or rebuild gems from Sept 19–30, delaying deploys and forcing integrity reviews.
  - Watch next: Sigstore/TUF signing, freeze-and-republish the window, independent forensics, AWS org SCPs, cross‑account log archiving, break‑glass root only.
