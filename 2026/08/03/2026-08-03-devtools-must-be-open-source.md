# Devtools must be open source

- Score: 712 | [HN](https://news.ycombinator.com/item?id=49156111) | Link: https://blog.exe.dev/devtools-must-be-open-source

### TL;DR

The author argues coding agents make source-level personalization cheap enough that development tools should be open source. Instead of accepting fixed extension points, users can ask agents to modify a tool directly, then periodically rebase those patches onto upstream. A one-prompt integration of a diff-summarizing tool into Shelley illustrates the claim that source can replace configuration and plugin systems. HN agreed agents lower the cost of understanding and patching code, but strongly disputed automatic nightly upgrades, one-shot review standards, maintenance economics, entitlement to source, and abandoning shared interfaces.

### Comment pulse

- Source access gained practical value → agents can build, explain, and patch unfamiliar projects with far less setup friction.
- Plugins still scale better → common features are implemented once, shared, reviewed, and insulated from private-fork maintenance.
- Automated rebases sound brittle → unattended agents may preserve tests while violating UX intent — counterpoint: sandboxing, rollback, and manual upgrade cadence reduce risk.

### LLM perspective

- View: Agents expand the viable customization frontier, but do not erase product design, ownership, or compatibility costs.
- Impact: Forkable tools become more attractive; teams risk fragmented workflows when every installation behaves differently.
- Watch next: Durable patch stacks, semantic regression tests, provenance controls, and agent-assisted upstreaming rather than perpetual private forks.
