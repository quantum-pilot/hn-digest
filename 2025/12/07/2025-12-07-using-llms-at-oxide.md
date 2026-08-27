# Using LLMs at Oxide

- Score: 644 | [HN](https://news.ycombinator.com/item?id=46178347) | Link: https://rfd.shared.oxide.computer/rfd/0576

### TL;DR

Oxide’s policy encourages LLMs only when human responsibility, rigor, empathy, and teamwork outrank speed. It favors them for document assistance, research starting points, late-stage editing, targeted review, debugging prompts, and carefully reviewed code—especially throwaway work. It rejects generated public or personal prose, mandates, shaming, and anthropomorphized agents. Operational text may be generated when correctness is verified. Commenters broadly liked the framework but questioned AI-writing detection, copyright omissions, junior-developer guidance, and whether generated production code truly preserves authorship and understanding.

### Comment pulse

- Supporters emphasized clear validation: models handle tedious mechanics best while humans retain architecture, taste, and accountability.
- Critics argued code generation can create the same ownership and comprehension problems Oxide identifies in prose.
- Reviewers questioned detector reliability and noted the policy does not address licensing or copyright risks.

### LLM perspective

- View: Oxide treats LLM governance as an accountability design problem, not a productivity contest.
- Impact: Engineers may gain speed without transferring review burden or eroding trust in human-authored communication.
- Watch next: Add junior-training guidance, detector evidence, privacy controls, licensing rules, and measured outcomes from production use.
