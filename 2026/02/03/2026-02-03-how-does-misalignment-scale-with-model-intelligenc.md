# How does misalignment scale with model intelligence and task complexity?

- Score: 235 | [HN](https://news.ycombinator.com/item?id=46864498) | Link: https://alignment.anthropic.com/2026/hot-mess-of-ai/

## TL;DR
Using repeated sampling, the authors decompose large-model failures into bias (systematic error) and variance (incoherence). On complex, long-horizon reasoning and agentic tasks, variance dominates: models “overthink” into unpredictability, even as accuracy rises. Scaling helps coherence only on easy problems; on hard ones, larger models stay or become hot messes. A synthetic optimizer experiment shows models learn objectives faster than they learn to pursue them reliably. HN discussion pivots to task decomposition, multi-agent orchestration, and the difficulty of specifying goals clearly.

## Comment pulse
- Practitioners see the bias–variance framing as immediately useful: keep sessions narrower, merge edits into initial prompts, and ensemble runs to dampen randomness.  

- System designers report better coherence from task decomposition and “team of rivals” agents than deeper single-model reasoning—counterpoint: orchestration increases system complexity and failure modes.  

- Others argue misalignment often reflects under-specified goals; writing precise specs and documentation may rival coding effort—while fundamental human values remain impossible to fully enumerate.  

## LLM perspective
- View: Treat incoherence as a monitored metric; log variance across samples in evals and key production workflows, not just accuracy.  

- Impact: Encourages designs with smaller per-step scopes, hierarchical planning, and fail-fast subagents instead of monolithic, ever-longer chains of thought.  

- Watch next: Whether new training regimes, architectures, or tools meaningfully reduce long-horizon variance on realistic agents beyond benchmark multiple-choice settings.
