# My approach to building large technical projects (2023)

- Score: 322 | [HN](https://news.ycombinator.com/item?id=45535202) | Link: https://mitchellh.com/writing/building-large-technical-projects

### TL;DR

Mitchell Hashimoto describes a personal method for finishing large technical projects: split work into independently testable pieces, implement only enough to reach frequent demos, and prioritize the shortest path to using the software yourself. His terminal-emulator example began with a tested VT parser, then disposable command-line visualizations, and eventually the features needed for his own shell and editor. The method deliberately postpones perfection and speculative requirements, using visible progress and tight feedback loops to preserve motivation and expose product mistakes early.

### Comment pulse

- Readers strongly endorsed fast setup and feedback loops as predictors of project health and sustained motivation.
- Some framed demos as durable tests of the product thesis, sitting between programming and explanatory writing.

### LLM perspective

- View: Frequent demos turn motivation into a design constraint and surface wrong product assumptions before polish accumulates.
- Impact: Disposable scaffolding can reduce risk when it buys faster feedback on the system's essential behavior.
- Watch next: Teams should define which quality compromises are temporary and when demo-driven shortcuts must be repaid.
