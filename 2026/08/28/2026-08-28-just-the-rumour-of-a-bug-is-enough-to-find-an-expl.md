# Just the rumour of a bug is enough to find an exploit these days

- Score: 303 | [HN](https://news.ycombinator.com/item?id=49480466) | Link: https://anil.recoil.org/notes/rumour-is-the-exploit

### TL;DR

An OCaml maintainer says probes matching a cohttp path-traversal bug appeared within ten minutes of a public fix PR; agents could independently find and exploit the issue from only a rough description. He argues automated discovery has shifted the bottleneck from finding bugs to human validation, remediation, and release. Proposed responses combine private trusted coordination, continuous shipping, stronger cross-ecosystem packaging and CI, and rapidly distributed protocol-level mitigations. Commenters confirmed surging disclosures but stressed that safe deployment still cannot match automated exploitation speed.

### Comment pulse

- Maintainers face an AI-amplified disclosure flood → rclone reportedly received over 40 reports in one month, with substantial triage value.
- Patch analysis predates LLMs → automation now scales it to low-value targets within minutes or hours.
- Immediate updates reduce exposure → counterpoint: CI latency and supply-chain compromise make automatic deployment risky.

### LLM perspective

- View: Faster bug discovery helps only when defender validation and distribution capacity rise with it.
- Impact: Small maintainers become the scarce security resource while attackers cheaply monitor every public signal.
- Watch next: Measure exploit latency, disclosure volume, patch uptake, virtual-mitigation accuracy, and trusted coordination tools.
