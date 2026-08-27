# Language models pack billions of concepts into 12k dimensions

- Score: 357 | [HN](https://news.ycombinator.com/item?id=45245948) | Link: https://nickyoder.com/johnson-lindenstrauss/

### TL;DR

A blog post uses quasi-orthogonal vector packing and the Johnson–Lindenstrauss lemma to argue that a 12,288-dimensional model space could accommodate vastly more concepts than dimensions. After discovering that an initial loss function merely duplicated basis directions, the author switched penalties and extrapolated experiments to enormous capacities. Commenters challenged the spherical-code framing, graph interpretation, extrapolation, and assumption that learned concepts behave like independently packed vectors, while noting that related geometry does appear in discussions of superposition and sparse autoencoders.

### Comment pulse

- Several commenters wanted comparisons with established spherical-code results rather than extrapolation from the author’s optimization experiments.
- Others argued that preserving useful relationships among concepts is harder than maximizing pairwise separation.

### LLM perspective

- View: This is an intuitive capacity sketch, not evidence that model representations organize themselves this way.
- Impact: The distinction matters when geometric intuition is used to justify sweeping claims about knowledge capacity.
- Watch next: Look for corrected plots, spherical-code baselines, reproducible experiments, and measurements from actual activations.
