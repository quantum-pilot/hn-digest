# Language models are injective and hence invertible

- Score: 212 | [HN](https://news.ycombinator.com/item?id=45758093) | Link: https://arxiv.org/abs/2510.15511

TL;DR
- The paper proves transformer LMs are injective from token sequences to their internal continuous representations; this losslessness holds from init through training. They report zero collisions in billions of tests across six models and introduce SipIt, a linear-time method that exactly reconstructs inputs from hidden activations. HN highlights limits: injectivity applies to hidden states/distributions, not final tokens; empirical collision tests in high dimensions are weak evidence; and the result heightens privacy risks for embeddings but less so for ordinary outputs.

Comment pulse
- Empirical “no collisions” is unconvincing → In 768-D unit spheres, random vectors are nearly orthogonal; billions of trials barely probe space — counterpoint: birthday-style sanity check still supports claim.
- Scope matters → Injective from prompts to hidden states/distributions, not emitted tokens; temperature/randomness break exact invertibility; cannot extract training data.
- Privacy risk → Embeddings can reveal original text; invertibility implies recoverability; mitigations include random rotations — counterpoint: typical systems expose only text outputs.

LLM perspective
- View: Injectivity formalizes that internal states uniquely encode prompts; inversion is feasible only with access to activations/KV caches.
- Impact: Stronger provenance/debugging and watermarking; higher liability for storing embeddings or hidden-state logs; complicates data-deletion compliance.
- Watch next: Proofs under quantization/low-precision, collision lower bounds, inversion from cached states in real serving stacks.
