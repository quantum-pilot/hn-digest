# Open Code Review – An AI-powered code review CLI tool

- Score: 258 | [HN](https://news.ycombinator.com/item?id=48406358) | Link: https://github.com/alibaba/open-code-review

### TL;DR
Open Code Review is Alibaba’s battle-tested AI code review CLI, now open source. It wraps any Anthropic/OpenAI-compatible model in a deterministic pipeline that selects files, bundles related changes, applies path-based rules, and enforces precise line-level comments, then uses an LLM agent only for judgment and context lookup. It integrates with CLI, CI, and Claude Code/skills. HN tests show strong recall but low precision, sparking debate over false positives, model choice, and the need for human reviewers in the loop.

---

### Comment pulse
- Quality concerns → One benchmark reports ~74% recall, ~12% precision, F1 ≈ 0.2; some value recall most, others fear developer fatigue from false positives.  
- Workflow role → Compared to just asking a coding agent, value is rules, CI automation, multiple-model review, and standardized org-wide checks—counterpoint: may become “review theater” without humans.  
- Ecosystem / rules → Built-in rules (currently mostly Chinese) and skills/plugins are praised; commenters list competing tools and skills people already use for automated review.

---

### LLM perspective
- View: Hybrid “rules + agent” design is where serious production code review is heading, especially for large monorepos and strict org standards.  
- Impact: Teams bottlenecked on reviews, or standardizing style/security checks, gain most; solo devs may prefer lighter editor-integrated agents.  
- Watch next: Independent benchmarks across languages, English rule sets, per-project tuning, and cost/latency optimizations for large CI deployments.
