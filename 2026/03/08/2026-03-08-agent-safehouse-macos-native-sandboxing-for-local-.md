# Agent Safehouse – macOS-native sandboxing for local agents

- Score: 230 | [HN](https://news.ycombinator.com/item?id=47301085) | Link: https://agent-safehouse.dev/

### TL;DR

A dependency-free Bash wrapper generates deny-first macOS `sandbox-exec` policies for coding agents. It grants read/write access to the selected project, read-only access to required toolchains, and kernel-enforced denial for SSH keys, cloud credentials, unrelated repositories, and most of the home directory. Presets cover several popular assistants, and shell functions can make confinement the default while retaining an explicit bypass. Commenters valued the hard-won permission details, but noted missing copy-on-write filesystems, debugger friction, and unresolved network, credential-use, and cloud-spend risks.

### Comment pulse

- The wrapper looks simple, but discovering minimal permissions for updates, keychains, and clipboard workflows was recognized as the real work.
- Home-level Git configuration and debugger or process access can break under strict policies, turning safety into daily friction.
- Filesystem isolation is only table stakes; stolen credentials and unrestricted network calls can still trigger remote damage or spending.

### LLM perspective

- **View:** Kernel-level default denial meaningfully limits accidental local damage without requiring containers or virtualization.
- **Impact:** Developers trade some tool compatibility for safer autonomous runs on valuable workstations.
- **Watch next:** Overlay storage, network allowlists, and credential brokers would close the largest remaining gaps.
