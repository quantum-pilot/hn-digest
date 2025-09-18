# Important machine learning equations

- Score: 302 | [HN](https://news.ycombinator.com/item?id=45050931) | Link: https://chizkidd.github.io//2025/05/30/machine-learning-key-math-eqns/

- TL;DR
    - A wide-ranging cheat-sheet of core ML equations with Python snippets: probability (Bayes, entropy, KL, cross-entropy), linear algebra (eigen, SVD), optimization (gradient descent, backprop), losses, and modern ops (convolution, softmax, attention, diffusion). HN appreciated the breadth but flagged conceptual framing and accuracy: treat entropy/cross-entropy/KL as a unified information-theory story, fix coding/notation issues (entropy masking, cross-entropy formula, affine vs linear, backprop wording), and cover omissions (MLP forward pass, kernel methods, reverse diffusion).

- Comment pulse
    - Teach entropy, cross-entropy, KL as one framework → Cross-entropy encodes P with Q; KL = cross-entropy − entropy; start from Shannon for intuition.
    - Reference-quality requires correctness → Numpy entropy ‘where’ leaves garbage; cross-entropy code mismatched; Ax+b is affine; backprop isn’t a supervised algorithm.
    - Broad but incomplete → Missing MLP forward, kernel methods, and reverse diffusion dynamics — counterpoint: breadth helps learners self-direct and experts audit gaps.

- LLM perspective
    - View: Equation lists help orientation but must show derivations, connections, and caveats; otherwise they promote rote formulas instead of mental models.
    - Impact: Unchecked inaccuracies mislead beginners; educators and authors can use this thread to fix code, clarify affine/linear, and unify information-theory treatment.
    - Watch next: See revisions adding MLP forward, kernels, reverse diffusion; include proofs, references, and unit-tested notebooks with numerical checks and edge cases.
