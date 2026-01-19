# A free and open-source rootkit for Linux

- Score: 152 | [HN](https://news.ycombinator.com/item?id=46666288) | Link: https://lwn.net/SubscriberLink/1053099/19c2e8180aeb0438/

### TL;DR
Singularity is an open-source Linux kernel rootkit by Matheus Alves, intended as a research and red‑teaming testbed rather than a crime tool. Distributed under the MIT license, it focuses on post-compromise stealth: using ftrace hooks to avoid patching kernel code, hiding its own module, attacker processes, filesystem artifacts, and traffic on a chosen TCP port. It even fakes ftrace disablement to evade common checks. LWN highlights it as a vivid example for studying both evasion and detection. HN commenters riff on licensing, ethics, and its educational value.

---

### Comment pulse
- MIT licensing → enables unrestricted reuse; some wish for (A)GPL/AGPLv3 to force license distribution or allow users to “replace” the rootkit—counterpoint: copyleft brings support headaches.
- Tone and tagline → commenters enjoy the dark humor (“too secure?”) and joke about preferring proprietary, EULA-protected malware.
- Educational angle → security folks value a high-quality, readable rootkit as guidance for implementation, reverse‑engineering, and defensive tooling design.

---

### LLM perspective
- View: Treat Singularity as a living benchmark for Linux EDRs, kernel defenses, and forensic tooling, not just an academic curiosity.
- Impact: Blue teams, kernel developers, and incident responders gain a concrete model for realistic post-exploitation stealth techniques.
- Watch next: Independent detection playbooks, automated lab environments using Singularity, and upstream kernel hardening targeting ftrace and procfs abuse.
