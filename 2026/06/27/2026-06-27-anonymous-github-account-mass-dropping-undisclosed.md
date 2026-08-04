# Anonymous GitHub account mass-dropping undisclosed 0-days

- Score: 618 | [HN](https://news.ycombinator.com/item?id=48698617) | Link: https://github.com/bikini/exploitarium

### TL;DR

An anonymous researcher consolidated 23 proof-of-concept folders spanning projects such as c-ares, FFmpeg, libssh2, Ghidra, Docker, Nmap, and VLC. They say GPT-5.5-3-Codex-Spark automated fuzzing inside a strict, human-supervised harness; most PoCs were handwritten, while AI generated README formatting and assisted RustDesk work. The author admits the initial repository was incomplete and some findings weak, promising future focus on serious flaws. HN’s spot checks were mixed: several current upstream crashes or memory bugs reproduced, but many claimed zero-days were ordinary behavior, low-impact crashes, duplicates, or impractical exploit paths.

### Comment pulse

- Severity labels were inflated → Ghidra examples included overwriting already-executable tools, reachable native parsing, and RMI behavior without demonstrating a new security boundary crossing.
- Some findings deserve triage → c-ares, libssh2, and FFmpeg PoCs reportedly reproduced upstream; Nmap parser behavior could matter if exploitation is demonstrated.
- AI optimizes finding counts → verbose reports can elevate crashes and trivial weaknesses into alarming exploits — counterpoint: reviewers said some AI-assisted vulnerabilities were real.

### LLM perspective

- **View:** The bottleneck has shifted from generating candidate bugs to validating exploitability, defining threat models, and coordinating disclosure responsibly.
- **Impact:** Maintainers face higher triage volume, while credible researchers risk reputational dilution when weak findings share labels with serious vulnerabilities.
- **Watch next:** Require affected-version matrices, minimal preconditions, reproducible builds, root-cause analysis, exploitability evidence, duplicate checks, vendor timelines, and CVE status.
