# Orchestrate teams of Claude Code sessions

- Score: 289 | [HN](https://news.ycombinator.com/item?id=46902368) | Link: https://code.claude.com/docs/en/agent-teams

### TL;DR
Anthropic’s new feature lets you run “teams” of Claude Code agents that coordinate on a shared task list, with a primary agent delegating and reviewing work across others. HN commenters see this as the obvious evolution of multi-agent coding: akin to “Kubernetes for agents” or actor frameworks, and something many already hacked together with tmux, shell scripts, or local tools. Debate centers on whether the productivity boost justifies potentially heavy token costs, especially for individuals versus well-funded startups and larger companies.  
*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Cost anxiety for individuals → heavy coding sessions can exhaust $20–$30 subscriptions quickly; worthwhile mainly for VC-backed startups or companies, not hobbyists.  
- Orchestrators feel inevitable → many already built DIY agent teams; some say Yegge’s Gas Town was visionary, others call it an obvious next step — counterpoint: research/OSS multi-agents existed since 2023.  
- Workflow impact → people already juggle multiple Claude/tmux panes; native coordination and shared tasks should streamline this, but some still doubt practical output quality and reliability.

---

### LLM perspective
- View: Native multi-agent orchestration will become a standard IDE capability, replacing many bespoke tmux/shell agent setups.  
- Impact: Best suited to teams with large, modular codebases; solo devs must closely monitor token burn versus real productivity gains.  
- Watch next: Hard numbers on speedups, bug rates, and cost; comparisons to local/OSS orchestrators and to traditional actor or workflow systems.
