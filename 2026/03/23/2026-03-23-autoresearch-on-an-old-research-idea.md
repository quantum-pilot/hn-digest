# Autoresearch on an old research idea

- Score: 244 | [HN](https://news.ycombinator.com/item?id=47493460) | Link: https://ykumar.me/blog/eclip-autoresearch/

### TL;DR
An ML researcher wired Karpathy’s Autoresearch loop into an old eCLIP-style vision–language model, letting Claude Code autonomously edit `train.py`, run 5‑minute experiments, and accept/revert changes. Under tight sandboxing and a new Ukiyo-e dataset, the agent mostly did bug fixing and hyperparameter tuning, cutting mean rank by 54% and achieving strong Recall@5, but architectural “moonshots” largely failed. HN sees this as an emerging pattern: LLMs as automated, semi-smart hyperparameter/experimentation engines—useful, but far from fully autonomous research.

---

### Comment pulse
- LLMs help surface prior art and ideas but most suggestions are noisy; automation only pays off when experiments are cheap and fast.  
- Autoresearch is essentially a loop around a single prompt file (program.md) directing iterative edits, training, eval, and revert/commit.  
- Debate: classic AutoML/HPO exists, but LLMs can read code, papers, and curves to make more informed trial choices—counterpoint: still unclear if this beats tuned grid/random search.

---

### LLM perspective
- View: Treat agents as tireless junior researchers for bug-hunting and HPO, not as creative theorists or architecture designers.  
- Impact: Small ML teams with spare GPU cycles gain leverage by automating low-level experimentation and sanity-checking old codebases.  
- Watch next: Standardized Autoresearch benchmarks, comparisons vs Optuna/BO, and better safety/sandbox patterns for long-running autonomous loops.
