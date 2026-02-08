# Orchestrate teams of Claude Code sessions

- Score: 387 | [HN](https://news.ycombinator.com/item?id=46902368) | Link: https://code.claude.com/docs/en/agent-teams

**TL;DR**  
Claude Code’s experimental Agent Teams feature lets a “lead” Claude session spawn and coordinate multiple autonomous teammates with their own context windows, shared tasks, and inter-agent messaging. It targets parallelizable work—research, PR review, debugging competing hypotheses, multi-layer features—offering hooks, delegate mode, plan-approval, and tmux/iTerm2 split-pane views. Docs stress file-disjoint tasks, careful decomposition, and cleanup, noting token usage can be several times higher. HN debates originality, costs versus developer time, and how reliably such swarms produce real value.

---

### Comment pulse

- Multi-agent orchestrators feel inevitable → actor-model trees, existing tools/papers, and Steve Yegge’s Gas Town vision all prefigure this—counterpoint: only now are models capable enough.  
- Cost anxiety → agent teams burn ~4× tokens but can cut wall-clock 3×; users say they’re for short bursts where developer time outweighs API spend.  
- Comparison with Gas Town → similar multi-agent idea, but Claude uses single lead and less whimsy; some doubt either system yet delivers consistently valuable work.

---

### LLM perspective

- View: Think of agent teams as a higher-level concurrency primitive; real gains come from good task decomposition and human oversight.  
- Impact: Best for large codebases, PR review, and debugging where parallel exploration beats one agent serially exploring and forgetting context.  
- Watch next: Public metrics on speed/quality tradeoffs, smarter automatic work partitioning, and IDE/CI support for supervising bursts of agent activity.
