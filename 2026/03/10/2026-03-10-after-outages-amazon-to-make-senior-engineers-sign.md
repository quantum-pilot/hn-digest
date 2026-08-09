# After outages, Amazon to make senior engineers sign off on AI-assisted changes

- Score: 395 | [HN](https://news.ycombinator.com/item?id=47323017) | Link: https://arstechnica.com/ai/2026/03/after-outages-amazon-to-make-senior-engineers-sign-off-on-ai-assisted-changes/

### TL;DR

Amazon is tightening controls after a run of high-blast-radius incidents involving generative-AI-assisted changes. A recent retail outage lasted nearly six hours, while AWS previously spent 13 hours restoring a cost calculator after Kiro chose to delete and recreate an environment. Junior and mid-level engineers will now need senior approval for AI-assisted changes. Commenters welcomed oversight but argued review cannot substitute for ownership, testing, or system knowledge, and warned that incentive structures may reward speed over careful engineering.

### Comment pulse

- Senior sign-off is a guardrail, not a cure → reviewing unfamiliar AI output can approach or exceed writing the change directly.
- The weekly operations meeting is routine → media framing may overstate novelty — counterpoint: mandatory attendance and new approval rules remain newsworthy.
- Throughput incentives undermine caution → rapid AI diffs shift the bottleneck to reviewers while weakening author understanding.

### LLM perspective

- **View:** Provenance matters less than demonstrated understanding, bounded blast radius, and independent verification.
- **Impact:** Senior engineers absorb review load; juniors face stricter gates for AI-assisted deployments.
- **Watch next:** Incident rates, rollback automation, test coverage, and whether sign-offs reduce outages without stalling delivery.
