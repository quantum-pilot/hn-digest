# Beliefs that are true for regular software but false when applied to AI

- Score: 187 | [HN](https://news.ycombinator.com/item?id=45583180) | Link: https://boydkane.com/essays/boss

### TL;DR

The essay argues that public intuition about conventional software misleads discussions of frontier language models. Unlike a localized coding defect, undesirable model behavior can emerge from vast training datasets and opaque learned interactions, resist precise causal diagnosis, reappear under untested prompts, and vary with tiny input changes. Model builders can test narrow properties but cannot guarantee global behavior or fully specify capabilities before training. The author’s claims are deliberately broad and acknowledge exceptions, but the central warning is that model failures cannot simply be patched like ordinary bugs.

### Comment pulse

- Commenters cited Apple’s constrained AI rollout as evidence that polished, controllable LLM products remain difficult.
- Others argued that concentrated power and information pollution deserve more attention than speculative autonomous-model risks.

### LLM perspective

- View: “Not patchable like code” is useful intuition, provided it does not excuse conventional engineering failures around models.
- Impact: Deployment needs behavioral evaluations, containment, and monitoring alongside normal code review and regression tests.
- Watch next: Whether interpretability and targeted model editing produce durable fixes across prompts, contexts, and model updates.
