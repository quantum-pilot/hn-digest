# Microsoft Amplifier

- Score: 226 | [HN](https://news.ycombinator.com/item?id=45549848) | Link: https://github.com/microsoft/amplifier

- TL;DR
  - Microsoft Amplifier appears to be a multi-agent coding/orchestration framework that automates long tasks and parallel solution attempts. HN asks for proof: the repo reads buzzwordy, lacks metrics, and may use brittle patterns (git worktrees, ad‑hoc context export). Practitioners advocate human-in-the-loop planning, small steps, and strong observability/container isolation; multi-candidate “alloying” can help. Overall: promising packaging of familiar agentic ideas, but without benchmarks and guardrails, treat it as an experiment, not an autopilot.
  - Content unavailable; summarizing from title/comments.

- Comment pulse
  - Autonomous agents waste tokens → lack determinism and transparency; prefer plan-review loops and discrete tasks — counterpoint: some agent systems already request periodic approvals.
  - Show metrics → repo feels buzzword-heavy; community tired of A/B launches; perhaps just packaging known techniques for wider use.
  - Alternative patterns → run 2–4 parallel candidates (“alloying”), use containers and standard observability; avoid fragile git worktrees and ad‑hoc “context export.”

- LLM perspective
  - View: Treat Amplifier as an orchestrator; keep humans approving steps; enforce limits and visibility on actions, code diffs, and spending.
  - Impact: Teams may speed experiments via parallel branches if repos are isolated, auditable, and easy to compare and merge.
  - Watch next: Head-to-head tasks against Cursor/Copilot/Claude, logs and metrics shipped, containerized runners, and safe approval-loop defaults.
