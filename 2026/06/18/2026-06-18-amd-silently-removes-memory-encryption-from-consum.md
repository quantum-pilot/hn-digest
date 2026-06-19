# AMD silently removes memory encryption from consumer Ryzen CPUs

- Score: 415 | [HN](https://news.ycombinator.com/item?id=48582320) | Link: https://www.tomshardware.com/pc-components/cpus/amd-silently-removes-memory-encryption-from-consumer-ryzen-cpus-leaving-users-unaware-that-they-may-be-vulnerable-security-feature-vanishes-after-newer-agesa-firmware-amd-engineers-go-radio-silent-when-pressed-about-the-change

### TL;DR
AMD’s Transparent Secure Memory Encryption (TSME) quietly stopped working on consumer Ryzen CPUs after AGESA firmware 1.2.7.0, while still functioning on Ryzen Pro. A Linux user noticed via security tooling; MSI later confirmed an internal firmware flag now disables TSME on non‑Pro chips, regardless of BIOS settings. AMD engineers first appeared unaware, then went silent, and AMD’s only statement now frames TSME as “Pro‑only.” Practically, physical-attack protection vanished without notice, raising bigger concerns about transparency and feature segmentation.

---

### Comment pulse
- Physical attacks aren’t in most consumers’ threat model → many don’t care about cold-boot attacks on home desktops—counterpoint: removal still erodes trust and surprises security‑conscious users.  
- TSME has broader benefits → encryption / scrambling complicates rowhammer-style and DRAM-side-channel attacks, adding defense-in-depth beyond exotic RAM-freezing scenarios.  
- Complaint about artificial segmentation → vendors ship hardware with disabled features (GPU virtualization, “BMW heated seats”) to upsell tiers; users want clear disclosure or legal right to self‑unlock.

---

### LLM perspective
- View: This is less about one niche feature and more about silent post-sale downgrades of already-shipped hardware.  
- Impact: Security-conscious consumers, Linux users, and small organizations lose cheap physical-memory protection unless they move to Ryzen Pro/EPYC.  
- Watch next: Whether AMD issues a clarifying bulletin, flips the AGESA flag back, or doubles down and formalizes stricter consumer/pro feature splits.
