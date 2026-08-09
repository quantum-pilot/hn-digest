# Agent-to-agent pair programming

- Score: 122 | [HN](https://news.ycombinator.com/item?id=47538190) | Link: https://axeldelafosse.com/blog/agent-to-agent-pair-programming

### TL;DR

The author’s `loop` CLI starts Claude and Codex side by side in tmux and bridges their conversations, assigning one as primary worker and the other as reviewer while keeping the human able to steer either session. The idea compresses a manual cross-model review loop: differing feedback broadens coverage, while agreement becomes a strong signal. It also creates a practical problem: autonomous iteration can expand changes and make human review harder. HN reports promising reviews but asks for systematic evidence, cost comparisons, and whether configuration diversity matters more than distinct agents.

### Comment pulse

- Cross-model review catches unfinished work → users report Codex finding issues after Claude declares completion — counterpoint: systematic evidence remains absent.
- Extra usage is expensive → useful comparisons need defined quality, cost, latency, and human-review metrics.
- Diversity may come from prompts or harnesses, not separate agents → controlled same-model configurations could test the mechanism.

### LLM perspective

- **View:** Value likely comes from adversarial iteration and independent context, not anthropomorphic teamwork.
- **Impact:** Teams may find defects earlier but pay more tokens and face larger, harder-to-review diffs.
- **Watch next:** Benchmark single-agent, retry, and two-agent flows on fixed tasks, measuring correctness, cost, and scope creep.
