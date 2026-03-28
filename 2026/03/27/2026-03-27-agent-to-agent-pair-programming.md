# Agent-to-agent pair programming

- Score: 122 | [HN](https://news.ycombinator.com/item?id=47538190) | Link: https://axeldelafosse.com/blog/agent-to-agent-pair-programming

- TL;DR  
  The author built `loop`, a CLI that runs Claude and Codex side‑by‑side in tmux and lets them talk directly, mimicking human pair programming. Using two agents as worker and reviewer surfaces different critiques, and overlapping feedback becomes a strong “must-fix” signal while tightening the iteration loop versus traditional PR reviews. They argue multi-agent harnesses should treat agent-to-agent communication as first class, while Hacker News debates pair programming’s real-world value, evidence for multi-agent gains, and the future human role as on-demand expert.

- Comment pulse  
  Pair programming polarizes → some find it awkward to externalize thoughts; others report strong results (e.g., Pivotal Labs) when communication skills are learned.  
  Multi-agent value uncertain → commenters want systematic benchmarks and cost analysis; current evidence feels anecdotal and potentially biased by pay-per-use incentives.  
  Human-as-oracle networks → idea of agents querying humans for expert answers sparks interest for documentation and concern about accelerating human replacement—counterpoint: experts mostly trained without AI.

- LLM perspective  
  View: Multi-agent “pairing” mainly formalizes a second, differently-configured critic that strengthens confidence signals and catches systematic oversights.  
  Impact: Tool vendors and IDEs can embed dual-review modes by default, especially for safety-critical or large refactors.  
  Watch next: Empirical studies comparing single vs multi-config agents on bug rates, PR acceptance time, and token/latency costs.
