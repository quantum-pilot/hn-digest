# First public macOS kernel memory corruption exploit on Apple M5

- Score: 211 | [HN](https://news.ycombinator.com/item?id=48139219) | Link: https://blog.calif.io/p/first-public-kernel-memory-corruption

### TL;DR

Calif says it built the first public macOS kernel memory-corruption exploit for M5 hardware with Memory Integrity Enforcement enabled. The two-vulnerability, data-only local privilege-escalation chain starts as an unprivileged user on macOS 26.4.1, uses ordinary system calls, and produces a root shell. Researchers found the bugs April 25 and completed the exploit by May 1, with Mythos Preview helping identify known bug classes while humans handled the novel mitigation bypass. Details remain withheld pending Apple’s fix, leaving commenters unable to assess how the chain evades MIE.

### Comment pulse

- Readers warned AI may accelerate offensive security — counterpoint: defenders and engineers can use the same capability rather than remain static.
- Speculation centered on data-only attacks, bounds checking, and unprotected GPU paths, but the unpublished report prevents confirmation.
- Bounty discussion distinguished this local privilege escalation from remote or zero-click chains eligible for Apple’s largest awards.

### LLM perspective

- View: The rapid result shows expert-model compression of development time, not autonomous defeat of hardware security.
- Impact: Advanced mitigations still raise attacker cost, but their useful lifetime may shorten as vulnerability discovery scales.
- Watch next: Apple’s patch, the promised report, reproducibility, Mythos’s exact contribution, and bounty classification.
