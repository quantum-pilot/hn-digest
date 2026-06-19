# Ubiquiti: Enterprise NAS, Built on ZFS

- Score: 236 | [HN](https://news.ycombinator.com/item?id=48585866) | Link: https://blog.ui.com/article/introducing-enterprise-nas

- TL;DR  
  Ubiquiti’s new Enterprise NAS (ENAS) is a ZFS-based, 16-bay appliance with 8-core ARM Neoverse, 64GB ECC, NVMe cache, dual 25Gb networking, and iSCSI for virtualization. It slots into the UniFi ecosystem for license-free management, identity-based access, and soon multi-site backup orchestration. HN discussion mixes enthusiasm for a polished, non-subscription ZFS box with deep skepticism about Ubiquiti’s product longevity, security history, inconsistent “no MRR” reality, and whether its software quality merits the “enterprise” label.

- Comment pulse  
  - Skeptics: Ubiquiti abandons products and ships test-in-prod releases → “enterprise” NAS deployment seen as high-risk — counterpoint: others cite long-lived EdgeRouters and robust Protect video.  
  - Business model debate: some celebrate no recurring fees; others note pricey Identity Enterprise subscriptions and paid support undercut the “no MRR” narrative.  
  - Security and software worries: past AWS key leak, misconfigured camera access, clunky UIs raise doubts Ubiquiti can outclass TrueNAS-level ZFS tooling.

- LLM perspective  
  - View: ENAS targets SMBs wanting unified UniFi management more than conservative enterprises needing multi-vendor, standards-heavy storage ecosystems.  
  - Impact: could pressure QNAP/Synology on price-per-terabyte ZFS appliances, especially if Ubiquiti proves reliable snapshots, replication, and iSCSI under real workloads.  
  - Watch next: independent performance/HA reviews, firmware update cadence, roadmap clarity, and whether multi-site backup and identity integration ship complete or half-baked.
