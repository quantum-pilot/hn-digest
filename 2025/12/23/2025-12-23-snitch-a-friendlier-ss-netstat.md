# Snitch – A friendlier ss/netstat

- Score: 290 | [HN](https://news.ycombinator.com/item?id=46361229) | Link: https://github.com/karol-broda/snitch

### TL;DR
Snitch is a new open-source, terminal-based replacement for ss/netstat that presents network connections in a clean TUI and styled tables. It emphasizes human-friendly defaults, flexible filters, JSON/CSV/plain output, and easy installation on Linux and macOS. Hacker News discussions focus on how it improves over historically awkward Unix networking tools, whether a nicer interface justifies installing it beyond servers, confusion with the similarly named Little Snitch, and how TUI tools fit accessibility and modern CLI UX expectations.

### Comment pulse
- Unix networking tools have opaque defaults → ss/lsof show queues, truncate names, hide listeners; text-stream APIs freeze output formats—counterpoint: newer CLIs increasingly prioritize UX.  
- Snitch suits workstations/homelabs → nicer filters, no noisy columns, TUI; admins still prefer ss on servers because it’s preinstalled everywhere.  
- Name sparks Little Snitch confusion → some call overlap misleading; others say scopes differ so it’s fine. Separate concern: TUIs may lag GUIs in accessibility.  

### LLM perspective
- View: Clear, queryable network views reduce cognitive load when debugging, especially versus memorizing ss/lsof flags and parsing columns.  
- Impact: Best for developers, SREs, security engineers on personal machines; large server fleets will likely stick with whatever ships by default.  
- Watch next: Interesting follow-up: structured, machine-readable modes as first-class APIs so future tools can safely evolve human-facing defaults.
