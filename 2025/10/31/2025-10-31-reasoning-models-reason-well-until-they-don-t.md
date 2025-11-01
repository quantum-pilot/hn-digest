# Reasoning models reason well, until they don't

- Score: 200 | [HN](https://news.ycombinator.com/item?id=45769971) | Link: https://arxiv.org/abs/2510.22371

- TL;DR
  - The paper shows large reasoning models, despite chain-of-thought and self-checking, excel only up to modest complexity on a new scalable dataset (DeepRD) covering graph connectivity and natural-language proof planning; accuracy then falls off a cliff. Existing benchmarks understate difficulty; most real-world cases look easy, but long-tail complexity poses real failure risk. HN debates whether bigger models, RL, and tool use can push the threshold versus fundamental non-generalization and cost/data limits; others flag hallucination, nondeterminism, and murky definitions of “reasoning” and “complexity.”

- Comment pulse
  - Scale and tools extend horizon → Larger models, RL, and tool use could tackle DeepRD; — counterpoint: generalization to arbitrary size is unlikely and constrained.
  - LLMs mimic, don’t infer → Strong on seen patterns; struggle with extrapolative reasoning, often hallucinate, and stochastic outputs prevent guaranteed correctness.
  - Benchmark design matters → Other datasets (e.g., CogniLoad) also scale difficulty; definitions of “reasoning” and “complexity” remain task-bound, not universal.

- LLM perspective
  - View: Complexity-scaling exposes distribution shift; chain-of-thought helps locally but lacks algorithmic generalization for unbounded instances.
  - Impact: Expect good averages with brittle tails; safety, legal, and finance workflows need guards for rare high-complexity failures.
  - Watch next: Benchmark reports should include calibrated complexity curves; test memory-augmented planners, verifiers, and tool-use agents; study cost-accuracy tradeoffs under increased depth.
