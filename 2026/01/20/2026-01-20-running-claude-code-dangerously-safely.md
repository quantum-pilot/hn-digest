# Running Claude Code dangerously (safely)

- Score: 268 | [HN](https://news.ycombinator.com/item?id=46690907) | Link: https://blog.emilburzo.com/2026/01/running-claude-code-dangerously-safely/

### TL;DR
Author wants to use Claude Code’s `--dangerously-skip-permissions` flag without babysitting or risking their host machine. Docker-in-Docker and Firejail feel awkward, cloud VMs are costly, so they resurrect Vagrant + VirtualBox: a small reproducible VM per project with shared folder, Claude installed inside, and even sudo enabled. Claude can freely install packages, run Docker, and mutate project files; if it wrecks the VM, you just destroy and recreate it. This mitigates accidents, not malicious escapes or shared-folder abuse.

---

### Comment pulse
- Approval fatigue is real; people build layered sandboxes (Landlock, bubblewrap, DNS controls) so they can safely leave agents in YOLO mode.
- VM isolation isn’t bulletproof: shared folders allow editing Vagrantfiles, git hooks, or repo code that later runs on the host—counterpoint: confine AI to subdirectories or snapshot-based flows.
- Others explore Docker-based sandboxes, microVM-backed Docker Sandboxes, and tools like Shannot or devcontainers with strict network/file policies for reviewed or constrained execution.

---

### LLM perspective
- View: This is a pragmatic “good-enough” safety layer aimed at human error and prompt-injected mishaps, not adversarial containment.
- Impact: Most useful for solo devs and small teams heavily relying on agentic coding against local repos and Docker workflows.
- Watch next: Standardized “agent sandboxes” combining microVMs, fine-grained network controls, and per-directory ACLs, with benchmarks for escape risk and developer friction.
