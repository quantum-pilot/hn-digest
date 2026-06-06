# First public macOS kernel memory corruption exploit on Apple M5

- Score: 211 | [HN](https://news.ycombinator.com/item?id=48139219) | Link: https://blog.calif.io/p/first-public-kernel-memory-corruption

### TL;DR
Calif reports the first public macOS kernel memory‑corruption exploit on Apple’s M5 chips with Memory Integrity Enforcement (MIE) enabled. Using their AI system Mythos Preview plus human experts, they found two kernel bugs and built a local, data‑only privilege‑escalation chain in about five days, going from unprivileged user to root on macOS 26.4.1 via normal syscalls. The work shows MIE/MTE significantly raise the bar but don’t prevent all exploits, and previews an AI‑driven “bugmageddon” where small teams can rival big vendors.

---

### Comment pulse
- LLMs will radically change security → Calif’s AI‑assisted exploit against Apple’s flagship mitigation shows offense can move very fast — counterpoint: defenders are also adopting similar automation.

- Readers probe the MTE bypass → explanation centers on data‑only attacks that avoid invalid memory accesses and on domains like GPU memory not fully covered by MTE/PAC.

- Risk perception splits → some downplay a local privilege escalation versus remote zero‑click RCE; others stress MIE still blocks many bugs and bigger threats are supply‑chain malware.

---

### LLM perspective
- View: AI now materially reduces the skill and time needed to turn complex kernel bugs into reliable exploits against modern mitigations.

- Impact: OS and silicon vendors must assume adversaries wield comparable AI tooling and prioritize systematic memory safety over incremental mitigations.

- Watch next: Independent replication, Apple’s technical writeup of the fix, and extension of MTE‑like protections to GPUs and other accelerators.
