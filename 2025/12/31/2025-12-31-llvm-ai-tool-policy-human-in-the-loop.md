# LLVM AI tool policy: human in the loop

- Score: 211 | [HN](https://news.ycombinator.com/item?id=46440833) | Link: https://discourse.llvm.org/t/rfc-llvm-ai-tool-policy-human-in-the-loop/89159

### TL;DR

LLVM’s proposed AI policy permits any development tools but requires contributors to read, understand, and accept responsibility for generated work before requesting review. Substantial tool use must be disclosed; autonomous agents and unreviewed automated comments are barred. Maintainers may label low-value, high-review-cost submissions “extractive” and disengage. HN largely supported the accountability principle, noting open-source projects cannot fire drive-by contributors, while warning that merely claiming ownership does not recover time wasted reviewing code the submitter never understood.

### Comment pulse

- Accountability must be demonstrated during review → contributors should explain decisions rather than relay maintainer feedback through an agent.
- Open-source asymmetry requires explicit policy → cheap generated submissions can consume scarce reviewer attention without creating durable contributors.
- “Stand behind your work” is insufficient alone → maintainers need permission to reject costly patches before exhaustive diagnosis.

### LLM perspective

- View: Review cost, not generation method, is the policy’s most enforceable and technology-neutral boundary.
- Impact: Contributors must invest more verification effort; maintainers gain a shared mechanism for protecting attention.
- Watch next: Measure extractive-label use, false positives, newcomer retention, disclosure compliance, and whether autonomous tooling develops approval gates.
