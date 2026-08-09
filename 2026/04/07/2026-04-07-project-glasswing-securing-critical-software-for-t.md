# Project Glasswing: Securing critical software for the AI era

- Score: 806 | [HN](https://news.ycombinator.com/item?id=47679121) | Link: https://www.anthropic.com/glasswing

### TL;DR

Anthropic’s Project Glasswing gives an unreleased Claude Mythos Preview to major technology firms and more than 40 critical-software organizations for defensive scanning. Anthropic says the model found thousands of severe zero-days across every major operating system and browser, including decades-old OpenBSD and FFmpeg flaws and a Linux privilege-escalation chain, largely autonomously. Partners receive $100 million in usage credits, while open-source security groups get $4 million. HN saw a potentially historic defensive leap but cautioned that vendor benchmarks, selective examples, and complementary fuzzing results do not establish universal superiority.

### Comment pulse

- Finding bugs fuzzers missed does not mean replacing fuzzing — counterpoint: models can build harnesses and steer fuzzers toward otherwise unreachable paths.
- Memory-safe languages, sandboxing, static analysis, and simpler architectures remove vulnerability classes instead of repeatedly discovering individual defects.
- Defenses may stratify: wealthy firms can fund immense token scans, while small maintainers face a pay-or-get-hacked bargain despite donated access.

### LLM perspective

- **View:** Discovery capacity is useful only when disclosure, triage, patching, and deployment can absorb its output faster than attackers.
- **Impact:** Maintainers gain elite analysis, but legacy operators inherit larger remediation queues and sharper pressure to modernize.
- **Watch next:** The 90-day report, independently reproduced findings, patch latency, false-positive rates, access equity, safeguard performance, and offensive leakage.
