# Running Claude Code dangerously (safely)

- Score: 268 | [HN](https://news.ycombinator.com/item?id=46690907) | Link: https://blog.emilburzo.com/2026/01/running-claude-code-dangerously-safely/

### TL;DR

The author uses a reproducible Vagrant/VirtualBox Ubuntu VM to run Claude Code with permission checks disabled, giving it sudo, Docker, package installation, browsers, databases, and test tooling without exposing most of the host. A bidirectional project folder preserves normal Git workflows, but the stated threat model covers accidents—not malicious escape, network abuse, data exfiltration, or deletion of shared code. HN agreed approval fatigue pushes users toward autonomous execution, while warning that writable Vagrantfiles, Git hooks, or later host execution of generated code can cross the boundary.

### Comment pulse

- Containment gap → writable shared repos let an agent alter Vagrantfiles, hooks, or code that later executes on the host.
- Alternative designs → commenters favored Landlock/bubblewrap, restricted devcontainers, DNS or network allowlists, snapshots, and emerging microVM sandboxes.
- Workflow tradeoff → human approval protects real systems — counterpoint: blocking every action defeats long-running autonomous exploration.

### LLM perspective

- View: VM isolation reduces accidental host damage, but shared writable artifacts remain an execution channel.
- Impact: Safe autonomy requires defining trust boundaries for files, credentials, networking, and host-side execution.
- Watch next: Test one-way sync, immutable launch configs, network allowlists, disposable snapshots, and diff review.
