# Every layer of review makes you 10x slower

- Score: 493 | [HN](https://news.ycombinator.com/item?id=47408205) | Link: https://apenwarr.ca/log/20260316

### TL;DR

Approval layers multiply wall-clock latency: the author’s rule of thumb turns a 30-minute fix into five hours with peer review, 50 hours with architecture approval, and 500 hours across teams. Faster AI coding only floods that unchanged queue; simply deleting review produces unowned defects. Drawing on Deming, the proposed alternative is to eliminate whole classes of review through better systems, root-cause fixes, automation, modular interfaces, small trusted teams, and genuine stop-the-line authority. HN agreed queues and incentives matter, but disputed whether design sessions can replace discoveries made during implementation.

### Comment pulse

- Shift review left → pairing, design sessions, and linters prevent most late comments — counterpoint: architecture often changes only after implementation exposes constraints.
- Review is under-rewarded → authorship earns credit while reviewers absorb blocking work, production risk, and learning responsibilities.
- Fast approval has tradeoffs → some teams achieve minutes through priority and SLAs; others associate speed with mounting technical debt.

### LLM perspective

- **View:** Review should generate durable controls that prevent recurrence, not repeatedly catch identical mistakes.
- **Impact:** AI-heavy teams need WIP limits and quality ownership before increasing code-generation capacity.
- **Watch next:** End-to-end cycle time, escaped defects, review-queue age, modularity experiments, and whether trust survives agent-generated PRs.
