# Bcachefs removed from the mainline kernel

- Score: 220 | [HN](https://news.ycombinator.com/item?id=45423004) | Link: https://lwn.net/Articles/1040120/

### TL;DR

Linux 6.18 removes bcachefs after 6.17 marked it externally maintained, because the project now ships as a DKMS module and leaving stale in-kernel code could create version confusion. Upstreaming had previously made bcachefs self-contained enough for DKMS, but external maintenance exposes it to kernel API churn and Secure Boot packaging friction. Discussion largely attributed the split to maintainer-process conflict rather than filesystem instability. Supporters still want a modern native copy-on-write alternative, while questioning whether leadership and distribution support can restore trust.

### Comment pulse

- DKMS is a mixed outcome → users avoid custom kernels, but module builds, Secure Boot enrollment, and disappearing internal APIs threaten reliability.
- Governance dominated the postmortem → former supporters urged maintainer introspection; others hoped bcachefs might return under different leadership.
- Technical demand persists → users value integrated snapshots, integrity, and multi-device features beyond layered filesystem, RAID, and volume-manager setups.

### LLM perspective

- View: Mainline removal converts a social-maintenance failure into recurring operational risk for users and distributions.
- Impact: Bcachefs adopters now depend on DKMS packaging and compatibility work across kernel releases.
- Watch next: Distribution packages, Secure Boot workflows, API breakage, maintainer changes, reliability telemetry, and any upstream re-entry plan.
