# Ironclad – formally verified, real-time capable, Unix-like OS kernel

- Score: 151 | [HN](https://news.ycombinator.com/item?id=45860843) | Link: https://ironclad-os.org/

### TL;DR

Ironclad presents itself as a free, Unix-like kernel for general-purpose and embedded systems, written in SPARK and Ada. The project advertises POSIX compatibility, preemptive multitasking, mandatory access control, hard real-time scheduling, blob-free operation, multiple architectures, and formal verification across cryptography, security controls, and user-facing facilities. Discussion focused less on the feature list than on maturity: commenters questioned the current verification level, worst-case execution-time guarantees, production readiness, performance, and the absence of capability-based security, while welcoming the project’s ambition.

### Comment pulse

- Skeptics said the site lacks enough evidence to assess hard real-time suitability without inspecting code and verification artifacts.
- Supporters saw formal isolation proofs as valuable, but noted that unverified firmware can undermine a trustworthy operating-system stack.

### LLM perspective

- View: “Formally verified” needs a precise map of proven properties, assumptions, coverage, and remaining runtime risks.
- Impact: Clear assurance boundaries determine whether Ironclad is experimental infrastructure or credible for safety-critical deployment.
- Watch next: Stronger proof levels, WCET evidence, certification plans, benchmarks, and documented production use.
