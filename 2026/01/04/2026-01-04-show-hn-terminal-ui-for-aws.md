# Show HN: Terminal UI for AWS

- Score: 152 | [HN](https://news.ycombinator.com/item?id=46491749) | Link: https://github.com/huseyinbabal/taws

TL;DR
- taws is a Rust-based terminal UI for exploring and managing AWS resources, with vim-style navigation, multi-profile/region support, and about 30 covered services plus EC2 actions. It targets ad‑hoc inspection and interactive workflows. HN readers welcome a k9s-like experience for AWS and multi-account visibility, while others report early crashes and even allege idea copying from a commercial tool, alongside practical tips around credential and SSO-based profile setup.

Comment pulse
- TUI complements aws-cli → aws-cli stays best for scripting; an interactive, keyboard-driven view is better for one-off exploration and audits.
- Desire for k9s-style AWS tool → users accustomed to k9s appreciate similar resource-centric navigation for core services like EC2 and Lambda.
- Stability and originality questioned → reports of first-run crashes and claims it copies a commercial product — counterpoint: open-source implementations of popular ideas are common.

LLM perspective
- View: Strong niche for terminal-first AWS dashboards that keep engineers in the shell instead of constantly jumping to the web console.
- Impact: Ops and SRE teams gain faster situational awareness during incidents, especially across many AWS accounts and regions.
- Watch next: Hardening, SSO/assume-role workflows, and comparisons against existing tools for common debugging and inventory tasks.
