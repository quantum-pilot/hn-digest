# Assessing Claude Mythos Preview's cybersecurity capabilities

- Score: 238 | [HN](https://news.ycombinator.com/item?id=47679155) | Link: https://red.anthropic.com/2026/mythos-preview/

### TL;DR
Anthropic’s Claude Mythos Preview can autonomously find and exploit serious zero-day vulnerabilities across every major OS and browser, including 27-year-old OpenBSD and 17-year-old FreeBSD bugs, Linux kernel privilege escalations, crypto library flaws, and browser JIT chains. It reverse-engineers closed binaries, discovers both memory and logic bugs, and often builds full exploits without human help. Anthropic is limiting access via Project Glasswing and using strict coordinated disclosure, arguing LLMs will ultimately favor defenders but create a turbulent, high-risk transition period.

---

### Comment pulse
- Capability shock → People highlight unpatchable/embedded and long-tail internet-connected devices as permanently vulnerable once models make exploit chains cheap—counterpoint: best defense is decommissioning or isolating them.
- Skepticism on novelty → Critics note these are bug-dense C/C++ stacks and KASLR was already weak, so results may overstate a qualitative “new era.”
- Structural asymmetry → LLMs excel at “rewardable” destruction (exploit success is clear) but are weaker at designing robust, novel software architectures; this worsens the offense–defense imbalance.

---

### LLM perspective
- View: This demonstrates frontier LLMs as practical offensive cyber tools, not just coding aids; exploit development is moving from art to scalable search.
- Impact: Security teams, cloud providers, browser/OS vendors, and chipmakers must assume automated large-scale bug discovery and exploit generation are imminent.
- Watch next: Hard data on defender use (auto-patching, CI integration), red-team benchmarks across memory-safe stacks, and policy on gating offensive capabilities.
