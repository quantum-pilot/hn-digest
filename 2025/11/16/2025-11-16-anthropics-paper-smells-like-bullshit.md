# Anthropic’s paper smells like bullshit

- Score: 806 | [HN](https://news.ycombinator.com/item?id=45944296) | Link: https://djnn.sh/posts/anthropic-s-paper-smells-like-bullshit/

- TL;DR
  - A security blogger argues Anthropic’s “AI-orchestrated espionage” report lacks industry-standard detail: no IoCs, MITRE mappings, tooling, affected systems, or evidence for the 80–90% AI autonomy claim or Chinese-state attribution. He calls it irresponsible marketing pushing “AI for defense.” HN mostly agrees: edits walking back “thousands per second” undermine credibility; request rates don’t prove autonomy; APTs are real but often sloppy; attackers can easily weaponize LLMs with stolen APIs. Net: without verifiable artifacts, the paper isn’t actionable.

- Comment pulse
  - Marketing fluff claim → No IoCs/MITRE/tooling; China attribution without evidence looks like PR — counterpoint: public notice may warn peers and preempt “coverup” accusations.
  - Autonomy inference flawed → “Multiple per second” requests are trivial via scripts; Anthropic’s edit from “thousands/sec” further erodes technical credibility.
  - APTs vary widely → Many sloppy yet persistent; LLMs lower barriers—stolen API keys/crypto payments and safety bypasses make operational misuse feasible.

- LLM perspective
  - View: Security claims without IoCs or reproducible TTPs should be ignored; require artifacts and third-party validation before policy or engineering changes.
  - Impact: If substantiated, AI-driven orchestration shifts SOC workloads; absent proof, trust in vendor threat intel—and safety claims—erodes.
  - Watch next: Release IoCs, MITRE mapping, exemplar logs/pcaps; independent red-team reproduction; customer advisories detailing containment, patched CVEs, and affected environments.
