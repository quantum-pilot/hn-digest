# Making Democracy Work: Fixing and Simplifying Egalitarian Paxos

- Score: 160 | [HN](https://news.ycombinator.com/item?id=45854862) | Link: https://arxiv.org/abs/2511.02743

### TL;DR

EPaxos* is presented as a simpler, corrected version of Egalitarian Paxos, a leaderless state-machine replication protocol designed to avoid leader bottlenecks and keep processing through failures. It replaces the original protocol’s complex, reportedly buggy recovery procedure with one the authors rigorously prove correct, while generalizing supported failure thresholds under an optimal replica-count bound. Discussion welcomed the repair, proposed machine-checked TLA+ or implementation verification, clarified Paxos naming, and explained how replicas order conflicting commands while freely reordering commuting ones.

### Comment pulse

- An original EPaxos author praised the work and suggested formalizing protocol plus implementation, possibly as a thesis.
- Readers unpacked leader terminology and explained that dependency graphs preserve order for conflicting operations across recovery.

### LLM perspective

- View: Recovery correctness, not leaderlessness alone, is the paper’s decisive contribution.
- Impact: EPaxos-derived systems gain a clearer protocol foundation, though production implementations still require separate verification.
- Watch next: A machine-checked specification and verified implementation would test whether the simplification survives engineering details.
