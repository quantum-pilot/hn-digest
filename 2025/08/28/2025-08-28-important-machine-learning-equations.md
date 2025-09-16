# Important machine learning equations

- Score: 302 | [HN](https://news.ycombinator.com/item?id=45050931) | Link: https://chizkidd.github.io//2025/05/30/machine-learning-key-math-eqns/

- TL;DR
  - A blog catalogs “core” ML equations (entropy, KL, linear algebra, gradient descent/backprop, MSE, softmax, attention, diffusion) with Python snippets. HN appreciates the approachable sweep but criticizes treating information-theory pieces independently, notes technical mistakes (entropy implementation, cross-entropy mismatch, affine vs linear, sloppy backprop phrasing), and flags omissions (MLP forward pass, kernel methods, reverse diffusion). Some suspect LLM authorship; others find checklists useful as study maps. Verdict: decent primer, not a reference—needs corrections and deeper sources.

- Comment pulse
  - Unify information theory → cross-entropy and KL derive from entropy; teach encoding interpretation, not separate formulas — counterpoint: broad lists help orient beginners.
  - Fix correctness and numerics → entropy code bug, cross-entropy mismatch, Ax+b is affine, backprop isn’t a “supervised algorithm”; don’t use as reference.
  - Coverage gaps matter → add MLP forward equations, kernel methods, and reverse diffusion; some suspect LLM authorship from tone and boilerplate.

- LLM perspective
  - View: Curated formula sheets are useful on-ramps, but must include derivations, caveats, and numerically safe implementations.
  - Impact: Novices risk cargo-culting; instructors and blogs should prioritize conceptual threads and audited code.
  - Watch next: Author revisions, unit tests on examples, add reverse diffusion derivation, kernels, MLP; link to Shannon; fix affine terminology.
