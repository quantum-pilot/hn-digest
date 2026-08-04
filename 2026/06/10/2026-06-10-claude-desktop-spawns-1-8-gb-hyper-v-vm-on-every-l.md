# Claude Desktop spawns 1.8 GB Hyper-V VM on every launch, even for chat-only use

- Score: 432 | [HN](https://news.ycombinator.com/item?id=48479452) | Link: https://github.com/anthropics/claude-code/issues/29045

### TL;DR

A Windows 11 bug report says Claude Desktop starts a Hyper-V VM using about 1.8 GB of RAM on every launch after Cowork has been used, even for chat-only sessions. The reporter found 2,689 stale session files, recurring invalid-JSON VM errors, and idle memory rising from roughly 50% to 62%; deleting sessions did not stop respawning. Disabling VirtualMachinePlatform prevents it but removes Cowork. HN agreed sandboxing explains the VM, not eager startup, and cited broken macOS permission links on Windows as evidence of rushed cross-platform engineering.

### Comment pulse

- Product design → Commenters wanted Cowork opt-in and sandbox initialization on demand — counterpoint: eager startup may reduce latency for users who invoke agents.
- Resource control → Users also reported an approximately 10 GB VM bundle, difficult removal, and frustration that applications increasingly deny configuration or deletion.
- Platform maturity → Windows dialogs opening Apple System Preferences reinforced criticism that fast-changing AI workflows are shipping before desktop integrations receive adequate platform testing.

### LLM perspective

- **View:** Sandboxing local agents is defensible; silently reserving memory and disk before use is a lifecycle-management failure.
- **Impact:** Users on 16 GB laptops or small SSDs bear disproportionate performance and storage costs.
- **Watch next:** Verify lazy startup, idle teardown, session cleanup, bundle removal, Windows-native permission routes, and a persistent Cowork disable switch.
