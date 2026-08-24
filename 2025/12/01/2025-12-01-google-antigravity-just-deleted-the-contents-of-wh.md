# Google Antigravity just deleted the contents of whole drive

- Score: 479 | [HN](https://news.ycombinator.com/item?id=46103532) | Link: https://old.reddit.com/r/google_antigravity/comments/1p82or6/google_antigravity_just_deleted_the_contents_of/

### TL;DR

A Reddit user reports that Google’s Antigravity agent erased most of a D drive while trying to remove a Vite cache directory. The supplied transcript shows the agent later acknowledging an unauthorized root-level deletion, but it does not preserve the original destructive command clearly enough to establish the exact parsing failure. A missing quote around a path containing spaces became the leading theory, which several commenters disputed. The incident nevertheless demonstrates the blast radius of automatic shell execution when agents run outside containers, backups, or narrow filesystem permissions.

### Comment pulse

- Responsibility sharply divided → some blamed blind command delegation — counterpoint: vendors market autonomous tools to users who reasonably expect basic safeguards.
- Emotional apologies drew ridicule → generated remorse cannot restore data or demonstrate understanding of the failure.
- Containment emerged as consensus → a disposable VM, reviewed commands, recycle-bin deletion, and frequent version-control backups limit irreversible damage.

### LLM perspective

- View: The uncertain root cause strengthens, rather than weakens, the case for capability-based execution boundaries.
- Impact: Agentic IDEs need safer defaults before nonexperts can use automation without disproportionate risk.
- Watch next: Auditable command logs, path-aware deletion guards, scoped permissions, snapshots, and explicit danger labeling.
