# Debian's Git Transition

- Score: 186 | [HN](https://news.ycombinator.com/item?id=46352231) | Link: https://diziet.dreamwidth.org/20436.html

### TL;DR

Debian's transition plan aims to let everyone obtain, inspect, modify, and release package sources entirely through Git while legacy source packages remain supported. Its core invariant is lossless, bidirectional conversion between a source package and the canonical tree produced by dpkg-source, implemented through dgit. Canonical branches keep Debian patches applied for outsider clarity, while tag2upload enables releases from signed tags. Remaining work includes importing legacy uploads, supporting security releases, moving internal consumers, updating documentation, and persuading maintainers to adopt the workflow.

### Comment pulse

- The goal enables Git-only work rather than banning existing tools; current maintainer workflows can continue during migration.
- Readers dislike patch queues, though defenders say gbp-pq already turns them into editable Git commits and preserves rebasing workflows.

### LLM perspective

- View: The difficult part is preserving archival equivalence while changing Debian's social default.
- Impact: A canonical Git history could lower barriers for downstreams, audits, security work, and occasional contributors.
- Watch next: Measure tag2upload adoption, legacy-import coverage, security-archive support, and documentation conversion.
