# Assessing Claude Mythos Preview's cybersecurity capabilities

- Score: 238 | [HN](https://news.ycombinator.com/item?id=47679155) | Link: https://red.anthropic.com/2026/mythos-preview/

### TL;DR

Anthropic says Claude Mythos Preview marks a step-change in autonomous vulnerability research: during isolated testing it found zero-days across major operating systems and browsers, built multi-bug exploit chains, and converted patched Linux flaws into working privilege-escalation exploits. Public examples include a 27-year-old OpenBSD crash, a 16-year-old FFmpeg bug, and unauthenticated root access through FreeBSD NFS. Most findings remain unpatched and therefore unverifiable; Anthropic is limiting access through Project Glasswing while urging faster patching, automated triage, and model-assisted defense.

### Comment pulse

- Readers worried most about unpatchable embedded devices and the legal danger of remotely “inoculating” them.
- Security practitioners called the scale impressive — counterpoint: old C/C++ targets, weak KASLR, and familiar techniques make some claims less novel.
- Clear reward signals may explain rapid exploit progress: breaking a target is easier to score than designing maintainable software.

### LLM perspective

- **View:** Cheap, scalable exploit development compresses disclosure-to-attack windows even if headline claims remain partly opaque.
- **Impact:** Maintainers, distributors, and defenders face more findings, triage, emergency releases, and legacy-system risk.
- **Watch next:** Patched disclosures behind Anthropic’s hash commitments, independent reproductions, false-positive rates, and results on hardened memory-safe targets.
