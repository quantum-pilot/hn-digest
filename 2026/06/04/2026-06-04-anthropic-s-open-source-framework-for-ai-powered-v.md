# Anthropic's open-source framework for AI-powered vulnerability discovery

- Score: 224 | [HN](https://news.ycombinator.com/item?id=48403980) | Link: https://github.com/anthropics/defending-code-reference-harness

### TL;DR

Anthropic released an unmaintained reference harness for Claude-driven vulnerability discovery and remediation, intended for teams to customize rather than adopt as a product. Its C/C++ pipeline builds with ASAN, partitions attack surfaces, runs parallel find agents, independently reproduces crashes, deduplicates findings, assesses exploitability, and generates patches that must build, pass tests, and resist renewed searching. Because agents execute target code, runs default to gVisor isolation with restricted egress. HN viewed it as a reusable shop jig, while stressing token cost, expert triage, harness quality, and false-positive fatigue.

### Comment pulse

- Purpose-built harnesses beat generic tooling → each team needs its own target model, effort controls, alerting, and techniques for domain-specific bugs.
- Economics depend on stakes → multi-agent scans consume tokens rapidly — counterpoint: even thousands of dollars can undercut a formal security engagement.
- Automation cannot establish absence → weak harnesses miss subtle vulnerabilities, while noisy triage exhausts developers and can promote harmful fixes.

### LLM perspective

- **View:** Independent reproduction and adversarial patch validation are the design’s strongest defenses against fluent but unsupported findings.
- **Impact:** Security teams become harness engineers and adjudicators, not passive recipients of model output.
- **Watch next:** Benchmarks on real CVEs, cost per verified finding, false-negative studies, and maintained community forks.
