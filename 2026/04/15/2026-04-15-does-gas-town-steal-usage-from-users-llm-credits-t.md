# Does Gas Town 'steal' usage from users' LLM credits to improve itself?

- Score: 193 | [HN](https://news.ycombinator.com/item?id=47785053) | Link: https://github.com/gastownhall/gastown/issues/3649

### TL;DR

The issue page supplies no description beyond asking whether Gas Town uses customers’ LLM credits to improve itself. Commenters treated the behavior as intentional, debating whether dramatic warnings or an open-source “social contract” could substitute for disclosure, opt-out controls, and spending limits. A later comment reports it was a bug: the system inadvertently activated an internal release tool. That update softened the accusation but not concerns about agents sending prompts, consuming money, or disguising malicious actions. Discussion split between seeing a sustainable contribution mechanism and calling undisclosed resource use unethical.

### Comment pulse

- Some considered mandatory token contributions acceptable if disclosed — counterpoint: others compared unexpected spending to hidden cryptocurrency mining.
- Critics said production-facing AI tools need exact data-flow, storage, training-use, and cost disclosures rather than theatrical warnings or buried terms.
- The reported release-tool bug reduced intent concerns, but highlighted how agent autonomy can turn internal capabilities into surprising external costs.

### LLM perspective

- **View:** The decisive distinction is consent: an accidental tool invocation is a bug, while deliberate shared-cost maintenance requires clear authorization.
- **Impact:** Unbounded agent spending converts a software defect into a direct billing and trust failure for users.
- **Watch next:** Root-cause details, patched release-tool permissions, cost ceilings, audit logs, and proof that user services cannot be silently invoked.
