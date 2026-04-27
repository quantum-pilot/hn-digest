# GnuPG – post-quantum crypto landing in mainline

- Score: 160 | [HN](https://news.ycombinator.com/item?id=47907018) | Link: https://lists.gnupg.org/pipermail/gnupg-announce/2026q2/000504.html

- TL;DR  
  GnuPG 2.5.19 rolls post‑quantum encryption (Kyber/ML‑KEM, FIPS‑203) into the mainline, plus routine fixes and 64‑bit Windows improvements. The 2.4 branch hits end‑of‑life soon, so users with multi‑year confidentiality needs (archival email, backups, regulated data) are nudged to upgrade, while short‑lived data gains little. HN discussion centers on “harvest‑now‑decrypt‑later” risk, challenges for long‑lived smartcard/HSM keys, ecosystem‑scale migration complexity, and annoyance that GnuPG still foregrounds SHA‑1 fingerprints.

- Comment pulse  
  - Risk‑based view → PQC matters for messages with multi‑year value; rotating backups with short retention gain little from immediate migration.  
  - Deployment view → Hybrid PQC+classical key exchange eases adoption; hardware with FPGAs can offload PQC, but larger keys and slower operations remain unavoidable overhead.  
  - Fingerprint debate → Some want SHA‑256/Blake2/3 key fingerprints; others argue SHA‑1 collisions don’t practically threaten this usage — counterpoint: optics and future‑proofing still matter.

- LLM perspective  
  - View → Mainline PQC in GnuPG normalizes quantum‑safe crypto for email, backups, and software signing rather than niche research deployments.  
  - Impact → Organizations with long retention policies and smartcard/HSM vendors now face timelines to deliver PQC or hybrid key‑management support.  
  - Watch next → Track OpenPGP PQC standards, hardware-token roadmaps, and benchmarks of hybrid schemes’ latency and storage penalties on traffic.
