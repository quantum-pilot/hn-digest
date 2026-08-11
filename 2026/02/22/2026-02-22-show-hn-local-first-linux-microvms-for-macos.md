# Show HN: Local-First Linux MicroVMs for macOS

- Score: 96 | [HN](https://news.ycombinator.com/item?id=47113567) | Link: https://shuru.run

### TL;DR

Shuru is a local macOS sandbox for AI agents that runs lightweight ARM64 Linux virtual machines through Apple’s Virtualization.framework, without Docker. Runs start from a clean Alpine root filesystem, remain offline unless networking is explicitly enabled, and discard changes by default. Users can set CPU, memory, and disk limits, forward ports over vsock, or create named checkpoints to restore and branch environments. Commenters distinguished its simple microVM-and-snapshot scope from Apple’s OCI-oriented containers, while asking about outbound allowlists, Windows equivalents, and the local-first label.

### Comment pulse

- The author says local-first means everything stays on the Mac — counterpoint: one reader considered the term unnecessary marketing for local execution.
- Offline-by-default networking drew interest, but readers wanted domain or endpoint allowlists when external access is enabled.
- Checkpoints promise reproducible agent and evaluation environments without adopting registries or a full container workflow.
