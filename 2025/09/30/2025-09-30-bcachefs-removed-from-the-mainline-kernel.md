# Bcachefs removed from the mainline kernel

- Score: 220 | [HN](https://news.ycombinator.com/item?id=45423004) | Link: https://lwn.net/Articles/1040120/

- TL;DR
  - Linus Torvalds removed bcachefs from Linux 6.18 after it moved to DKMS; keeping stale in-tree code risked confusion. Debate centered on governance and operations: kernel won’t support out‑of‑tree ABIs, and Secure Boot + DKMS complicates deployments. Some attribute the removal to maintainer conduct rather than technical instability. Users split: bcachefs praised as more reliable than btrfs by some, while others prefer btrfs’ maturity. Many want a clear path to re‑merge once process issues are resolved.

- Comment pulse
  - DKMS complicates ops at scale → Secure Boot MOK enrollment and no stable module ABI break unattended boots — counterpoint: avoids per-project custom kernels now.
  - Removal was governance-driven → Linus can drop code after discussion; many blame maintainer guideline breaches rather than filesystem stability.
  - Need for integrated COW+RAID remains → some praise bcachefs reliability after btrfs data loss; others argue btrfs is mature enough and default in major distros.

- LLM perspective
  - View: Short term, DKMS keeps bcachefs alive; long term, lack of in-tree user risks supporting kernel changes being reverted.
  - Impact: Distros, fleet admins, and Secure Boot environments absorb maintenance; kernel maintainers regain freedom to refactor affected subsystems.
  - Watch next: Track DKMS packaging across distros, subsystem churn touching bcachefs interfaces, and any re-merge criteria or leadership changes communicated by maintainers.
