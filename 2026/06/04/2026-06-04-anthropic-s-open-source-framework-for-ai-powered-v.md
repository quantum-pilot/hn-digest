# Anthropic's open-source framework for AI-powered vulnerability discovery

- Score: 224 | [HN](https://news.ycombinator.com/item?id=48403980) | Link: https://github.com/anthropics/defending-code-reference-harness

### TL;DR
Anthropic released an open-source, unmaintained *reference* harness showing how to use Claude as an autonomous vulnerability hunter and patch generator. It combines interactive “skills” for threat modeling, static scanning, triage, and patching with a gVisor-sandboxed pipeline that builds targets, fuzzes them with ASAN, verifies/dedupes crashes, writes exploitability reports, and proposes fixes. The repo is meant as scaffolding: teams are expected to customize it to their language, vuln class, and environment, then keep humans in the loop for triage and patch acceptance.

---

### Comment pulse
- Framework as “shop jig” → useful pattern library, but LLMs make it easier for teams to generate bespoke harnesses matching their own workflows and quirks.  
- Cost concerns → heavy token usage may mean hundreds–thousands per run, but still cheaper than traditional security engagements and can run episodically, not continuously.  
- Harness quality and triage are hard → custom techniques, especially for crypto, plus expert review are needed to avoid “vibe auditing” full of false positives and missed bugs.

---

### LLM perspective
- View: This normalizes LLMs as orchestrated fuzzing/analysis components rather than magical monoliths.  
- Impact: Security teams, auditors, and devtools vendors gain a concrete blueprint for multi-agent, sandboxed code-review pipelines.  
- Watch next: Independent benchmarks vs human auditors, CI integrations, and research on automated triage/prioritization to reduce expert bottlenecks.
