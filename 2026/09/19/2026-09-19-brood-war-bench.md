# Brood War Bench

- Score: 288 | [HN](https://news.ycombinator.com/item?id=49766966) | Link: https://bw.swerdlow.dev/report

### TL;DR

Brood War Bench ran 19 agent configurations in a round robin. Codex Astra xhigh finished 18–0, ahead of its medium setting and Claude Fable, yet no model played beyond beginner level. Agents discovered harassment and cheese more readily than macro play, often pausing too long while the real-time game continued. Specialized subagents communicated poorly, producing disjointed trickle attacks; human direction improved coordination. HN discussion largely recalled earlier StarCraft bot tournaments and wanted better replay reconstruction and viewing tools.

### Comment pulse

- Real-time latency is strategically costly → prolonged reasoning leaves agents inactive while opponents continue gathering, building, and attacking.
- Older bot research remains relevant → commenters recalled genetic programming and dedicated Brood War competitions predating general-purpose model agents.
- Better presentation would help evaluation → reconstructed replays or spectator tooling could make tactical failures easier to inspect.

### LLM perspective

- View: This benchmark measures coordination under time pressure as much as game knowledge or planning quality.
- Impact: Agent builders need tighter action loops and shared state, not merely longer reasoning budgets.
- Watch next: Compare fixed-latency agents and instrument production, idleness, resource use, and communication failures.
