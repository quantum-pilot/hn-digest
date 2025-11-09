# Ironclad – formally verified, real-time capable, Unix-like OS kernel

- Score: 151 | [HN](https://news.ycombinator.com/item?id=45860843) | Link: https://ironclad-os.org/

- TL;DR
    - Ironclad is an open-source, GPLv3, UNIX‑like kernel written in SPARK/Ada, aiming for formal verification, POSIX compatibility, MAC, and hard real‑time scheduling across multiple boards without firmware blobs. HN welcomes the ambition—few projects attempt verified RT plus POSIX—but questions maturity: current proofs appear “stone‑level,” leaving WCET and isolation assurances unclear versus seL4/QNX. Debate centers on capability security vs MAC and the firmware attack surface. Clarifications: SPARK has an open version; current ports mention x86_64/riscv64, with ARM64 asked about.

- Comment pulse
    - Verification + RT skepticism → Site shows SPARK “stone level”; unclear WCET bounds and production readiness compared to seL4/QNX—counterpoint: certifications and deeper proofs could follow.
    - Security model debate → Capability systems (e.g., seL4) seen as faster/cleaner; POSIX and MAC considered clunky, though isolation proofs still valuable for safety-critical systems.
    - Supply chain and practicality → Firmware remains weakest link; desire for verifiable EFI and device firmware; SPARK licensing clarified as open-core; ARM64 support questioned.

- LLM perspective
    - View: Ambitious mix of verification and POSIX; credibility hinges on published proof artifacts, WCET analyses, and microbenchmarks against seL4/QNX.
    - Impact: If matured, good fit for regulated RT domains needing POSIX: industrial control, rail, avionics partitions, medical devices, high-assurance IoT.
    - Watch next: Roadmap with SAL level targets, proof coverage %, WCET tooling, ARM64 port timeline, firmware trust chain story, and reproducible builds.
