# The session you cannot take with you

- Score: 728 | [HN](https://news.ycombinator.com/item?id=49118781) | Link: https://earendil.com/posts/session-portability/

### TL;DR

Modern inference APIs increasingly bind conversations to provider-sealed state: response IDs, encrypted reasoning and compaction, hidden search evidence, opaque subagent messages, and remote artifacts. The author tests ownership through inspection, export, replay, audit, and deletion, then proposes canonical local logs, explicit storage, readable handoffs, full-fidelity tool records, and supported distillation. Commenters broadly recognize lock-in and inauditability but debate whether transcripts deserve preservation; alternatives include project notes, external tools, and open models, while hidden reasoning is defended against prompt injection and unauthorized distillation.

### Comment pulse

- Portability is competitive leverage → easy switching pressures providers on quality and price — counterpoint: local models still trail hosted coding performance.
- Preserve decisions, not chatter → users favor editable notes, plans, outcomes, and code because long sessions become noisy and forgetful.
- Externalize state → commenters suggest third-party tools, file-based compaction, and explicit subagent calls to keep operational context inspectable.

### LLM perspective

- View: Semantic portability matters even when exact model behavior cannot be replayed.
- Impact: Agent builders inherit evidence-retention and audit duties once providers hide orchestration details.
- Watch next: Standardize export bundles containing readable context, tool evidence, agent lineage, artifact hashes, and deletion receipts.
