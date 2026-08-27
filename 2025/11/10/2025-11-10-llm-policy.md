# LLM policy?

- Score: 180 | [HN](https://news.ycombinator.com/item?id=45871531) | Link: https://github.com/opencontainers/runc/issues/4990

### TL;DR

Runc maintainers opened an RFC after seeing more apparently LLM-generated issues and pull requests. The proposer favors treating generated issues as spam because plausible descriptions may be fabricated, while requiring code submitters to understand and explain every change; they also raised an unresolved DCO concern. Other participants would allow translation, grammar correction, or trivial completion, and argued that quality should matter more than provenance. The core maintenance problem is asymmetric effort: generation scales cheaply, but verifying polished-looking claims and mentoring authors remains expensive.

### Comment pulse

- Ban supporters said generated submissions can conceal subtle errors and consume reviewer attention without an accountable author.
- Opponents favored source-neutral quality standards, asking whether evidence shows worse acceptance ratios for LLM-assisted contributions.
- Commenters warned integrated AI and résumé incentives could overwhelm open-source maintainers with low-cost, plausible spam.

### LLM perspective

- View: The enforceable standard is contributor accountability, though disclosure may help reviewers budget trust and effort.
- Impact: Maintainers need triage rules that protect scarce review time without rejecting genuinely understood, tested assistance.
- Watch next: The final runc policy, DCO interpretation, disclosure requirements, and measurable effects on issue and review volume.
